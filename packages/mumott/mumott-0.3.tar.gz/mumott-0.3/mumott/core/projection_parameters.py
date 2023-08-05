"""This file contains the class ProjectionParameters.

It is used for determining parameters for the John transform.
"""

import logging
from typing import Tuple
import numpy as np
from numpy.typing import NDArray

from mumott.core.john_transform import john_transform, john_transform_adjoint
from numba import config as numba_config, get_num_threads, set_num_threads


logger = logging.getLogger(__name__)


class ProjectionParameters:
    """ Class for calculating the parameters for the John transform, including
    the probed azimuthal and polar angles of each measurement.

    Parameters
    ----------
    geometry : Geometry
        A container object which contains the geometry used for projection
        calculations. Changes to the `Geometry` are automatically tracked and the
        `ProjectionParameters` instance is dynamically updated as needed.
    integration_step_size : float
        Ratio for one-dimensional line upsampling parallel to the projected direction.
        Must be greater than ``0`` and smaller than ``1``.
    """
    def __init__(self,
                 geometry,
                 integration_step_size: float = 1.0):
        # Todo: fix type hinting once import issues are resolved
        self._geometry = geometry
        self._geometry_hash = hash(geometry)
        if not 0.0 < integration_step_size <= 1.0:
            raise ValueError('Integration step size must be less than or'
                             ' equal to 1.0, and greater than 0.0, but the'
                             f' provided value is {integration_step_size}.')

        self._integration_step_size = np.float64(integration_step_size)
        self._sampling_kernel = np.array((1.,), dtype=np.float64)
        self._kernel_offsets = np.array((0., 0.), dtype=np.float64)
        self._created_sampling_kernel = False
        self._update(force_update=True)

    def _update(self, force_update: bool = False) -> None:
        """Internal method for checking if geometry needs to be recomputed,
           and doing so if necessary."""
        if self.is_dirty or force_update:
            self._get_basis_vectors()
            self._calculate_cumulative_size()
            self._geometry_hash = hash(self._geometry)

    def _calculate_cumulative_size(self) -> None:
        """ Internal method for calculating indexing of projections. """
        total_projection_shape = np.array(
            (*self._geometry.projection_shape, self._geometry.detector_angles.size))
        list_of_shapes = np.repeat(total_projection_shape[np.newaxis], len(self._geometry), axis=0)
        self._cumulative_projection_size = np.concatenate(
            ((0,), tuple(np.cumsum(list_of_shapes.prod(1))))).astype(int)

    def _get_basis_vectors(self) -> None:
        """ Calculates the basis vectors for the John transform, one projection vector
        and two coordinate vectors. """
        n_proj = len(self._geometry)
        self._basis_vector_projection = np.zeros((n_proj, 3), dtype=np.float64)
        self._basis_vector_j = np.zeros((n_proj, 3), dtype=np.float64)
        self._basis_vector_k = np.zeros((n_proj, 3), dtype=np.float64)
        self._basis_vector_projection[...] = np.einsum('kij,i->kj', self._geometry.rotations_as_array,
                                                       self._geometry.p_direction_0)
        self._basis_vector_j[...] = np.einsum('kij,i->kj', self._geometry.rotations_as_array,
                                              self._geometry.j_direction_0)
        self._basis_vector_k[...] = np.einsum('kij,i->kj', self._geometry.rotations_as_array,
                                              self._geometry.k_direction_0)

    def create_sampling_kernel(self,
                               kernel_dimensions: Tuple[int, int] = (3, 3),
                               kernel_width: Tuple[float, float] = (1., 1.),
                               kernel_type: str = 'bessel') -> None:
        """ Creates a kernel to emulate the point spread function (PSF) of the
        beam. This improves the accuracy of the projection function.

        Parameters
        ----------
        kernel_dimensions
            A tuple of how many points should be sampled in each direciton of the kernel.
            The total number of line integrals per pixel in the data is
            ``kernel_dimensions[0] * kernel_dimensions[1]``.
        kernel_width
            Width parameter for the kernel in units of pixels. Typically the full-width-half-maximum of the
            beam used to measure the data.
        kernel_type
            The type of kernel to use. Accepted values are ``'bessel'``, ``'rectangular'``,
            and ``'gaussian'``.
            ``'bessel'`` uses a ``sinc`` function multiplied by a
            Lanczos window with the width parameter being the first Bessel zero. This
            gives a sharply peaked distribution that goes to zero at twice the full
            width half maximum, and samples are taken up to this zero.
            ``'rectangular'`` samples uniformly in a rectangle of size
            ``kernel_width``.
            ``'gaussian'`` uses a normal distribution with the FWHM given by `kernel_width`,
            sampled up to twice the FWHM.
        """
        if self._created_sampling_kernel:
            logger.warning('It appears that you have already created a sampling kernel.'
                           ' The old sampling kernel will be overwritten.')
        if kernel_type == 'bessel':
            L = 0.7478
            ji = np.linspace(-kernel_width[0], kernel_width[0], kernel_dimensions[0] * 100)
            fj = np.sinc(ji * L / kernel_width[0]) * np.sinc(ji / kernel_width[0])
            ki = np.linspace(-kernel_width[1], kernel_width[1], kernel_dimensions[1] * 100)
            fk = np.sinc(ki * L / kernel_width[1]) * np.sinc(ki / kernel_width[1])
        elif kernel_type == 'rectangular':
            ji = np.linspace(-kernel_width[0] / 2, kernel_width[0] / 2, kernel_dimensions[0] * 100)
            fj = np.ones_like(ji)
            ki = np.linspace(-kernel_width[1] / 2, kernel_width[1] / 2, kernel_dimensions[1] * 100)
            fk = np.ones_like(ki)
        elif kernel_type == 'gaussian':
            std = np.array(kernel_width) / (2 * np.sqrt(2 * np.log(2)))
            ji = np.linspace(-kernel_width[0], kernel_width[0], kernel_dimensions[0] * 100)
            fj = np.exp(-0.5 * (ji ** 2) / ((std[0]) ** 2))
            ki = np.linspace(-kernel_width[1], kernel_width[1], kernel_dimensions[1] * 100)
            fk = np.exp(-0.5 * (ki ** 2) / ((std[1]) ** 2))
        else:
            raise ValueError(f'Unknown kernel type: {kernel_type}.')
        fr = fj.reshape(-1, 1) * fk.reshape(1, -1)
        fr = fr.reshape(kernel_dimensions[0], 100, kernel_dimensions[1], 100)
        fi = fr.sum(axis=(1, 3))
        fi = (fi / fi.sum()).astype(np.float64)
        J = ji.reshape(-1, 1) * np.ones((1, ki.size))
        K = ki.reshape(1, -1) * np.ones((ji.size, 1))
        J = J.reshape(kernel_dimensions[0], 100, kernel_dimensions[1], 100)
        K = K.reshape(kernel_dimensions[0], 100, kernel_dimensions[1], 100)
        Ji = J.mean(axis=(1, 3)).flatten()
        Ki = K.mean(axis=(1, 3)).flatten()
        offset = np.concatenate((Ji, Ki)).astype(np.float64)
        self._sampling_kernel = fi
        self._kernel_offsets = offset
        self._sampling_kernel_size = np.int32(kernel_dimensions[0] * kernel_dimensions[1])
        self._created_sampling_kernel = True

    def project(self,
                input_field: NDArray[np.float64],
                index: int,
                projection: NDArray[np.float64] = None,
                number_of_threads: int = 4) -> NDArray[np.float64]:
        """ Perform a forward projection (John transform) using the geometry defined
        by this class instance. This method can be used directly without providing the
        outut ``projection``, in which case the array will be allocated automatically.
        However, for optimal use when iterating over many projection, you should
        pre-allocate space for each projection.

        Parameters
        ----------
        input_field
            The volume which is to be projected. Must have 4 dimensions,
            the last dimension can be of any size. For scalar projection,
            set the last dimension to size ``1``. Must be row-major and
            contiguous (also-called C-contiguous) and have
            ``dtype = np.float64``.
        index
            The index of the projection. Determines which direction the projection
            should occur in.
        projection
            Output variable. Optional, but if provided,
            the last index must have the same size as the last index of :attr:`input_field`.
            Projection is cumulative and in-place, so initialize with zeros if you do not
            want projection to occur additively when calling several times.
            Must be row-major and contiguous (also-called C-contiguous) and have ``dtype = np.float64``.
        number_of_threads
            The number of threads to use when running on CPUs. Often equals
            the number of physical CPU cores. Default is ``4``.

        Returns
        -------
        projection
            The projection of ``input_field``. If ``projection`` is provided at input,
            this will be the same object.
        """
        self._update()
        shape = (*self._geometry.projection_shape, self._geometry.detector_angles.size)
        if not np.allclose(input_field.shape[:-1], self._geometry.volume_shape):
            logger.warning('Input field shape differs from the recorded'
                           ' volume_shape of this ProjectionParameters instance.'
                           ' Please exercise caution.')
        if len(input_field.shape) != 4:
            raise ValueError('The input field must be 4-dimensional.'
                             ' If the last dimension is 1, please indicate'
                             ' this explicitly be reshaping it accordingly.')
        if input_field.dtype != np.float64:
            raise TypeError('Input field dtype must be np.float64,'
                            f' but it is currently {input_field.dtype}.')
        if projection is None:
            projection = np.zeros(tuple(shape[:-1]) + (input_field.shape[-1],), dtype=np.float64)
        else:
            if not np.allclose(projection.shape[:-1], shape[:-1]):
                logger.warning('Your input projection shape appears different from the'
                               ' data shape in this ProjectionParameters instance.'
                               ' Alignment may not work corrrectly.'
                               ' Please exercise caution.')
            if projection.dtype != np.float64:
                raise TypeError('Projection dtype must be np.float64,'
                                f' but it is currently {projection.dtype}.')
            if projection.shape[-1] != input_field.shape[-1]:
                raise ValueError(f'The last element of {projection.shape}'
                                 ' must be the same as the last element of'
                                 f' {input_field.shape}.')
            if projection.flags['C_CONTIGUOUS'] is False:
                raise ValueError('Input projection must be row-major and'
                                 ' contiguous (also-called C-contiguous).'
                                 ' It is currently defined with strides'
                                 f' {projection.strides}. For a C-contiguous'
                                 ' array, the strides are strictly decreasing.')
        if input_field.flags['C_CONTIGUOUS'] is False:
            raise ValueError('Input input_field must be row-major and'
                             ' contiguous (also-called C-contiguous).'
                             ' It is currently defined with strides'
                             f' {input_field.strides}. For a C-contiguous'
                             ' array, the strides are strictly decreasing.')
        vector_p = self._basis_vector_projection[index].astype(np.float64)
        vector_j = self._basis_vector_j[index].astype(np.float64)
        vector_k = self._basis_vector_k[index].astype(np.float64)
        projection_offsets = np.array((self._geometry.j_offsets[index],
                                       self._geometry.k_offsets[index]),
                                      dtype=np.float64).ravel()
        old_num_threads = get_num_threads()
        try:
            set_num_threads(number_of_threads)
        except ValueError as v:
            if 'number of threads' in str(v):
                logger.warning(f'number_of_threads {number_of_threads} exceeds'
                               f' maximum number of thread(s) {numba_config.NUMBA_DEFAULT_NUM_THREADS}.'
                               f' Computation will proceed with {old_num_threads} thread(s).')
            else:
                raise v
        john_transform(projection, input_field, vector_p,
                       vector_j, vector_k, self._integration_step_size, projection_offsets,
                       self._sampling_kernel.ravel(), self._kernel_offsets.reshape(2, -1))
        set_num_threads(old_num_threads)
        return projection

    def adjoint(self,
                projection: NDArray[np.float64],
                index: int,
                output_field: NDArray[np.float64] = None,
                number_of_threads: int = 4) -> NDArray[np.float64]:
        """ Calculates the projection adjoint (or back-projection) using the geometry defined
        by this class instance. Uses multithreading with reduction summation; if you do not wish
        to perform the reduction immediately, provide ``output_field`` as an input parameter,
        with ``output_field.shape[0] == number_of_threads``, the three middle indices
        indicating ``(x, y, z)``, and the final index indicating the channel.

        Parameters
        ----------
        projection
            The projection to be back-projected. Must have 3 dimensions,
            the last dimension can be of any size. For scalar projection,
            set the last dimension to size 1. Must be row-major and contiguous
            (also-called C-contiguous) and have ``dtype = np.float64``.
        index
            The index of the projection. Determines the direction in which the
            back-projection is applied.
        number_of_threads
            In CPU implementation, the number of threads to use. Often equals
            the number of physical CPU cores. Default is ``4``. Parallelization
            occurs through reduction, so please note that a high number of threads
            can heavily impact memory usage.
        output_field
            Output variable. Optional, but if provided,
            must have a total of five dimensions, where
            the last index has the same size as the last index of ``projection``, and
            ``output_field.shape[0]`` must equal ``number_of_threads``. Must be
            row-major and contiguous (also-called C-contiguous) and have
            ``dtype = np.float64``. If provided, reduction over each thread will not occur.

        Returns
        -------
        output_field
            The adjoint of ``projection``. If ``output_field`` is provided at input,
            this will contain the adjoint calculated by each thread, so that reduction
            must be done to obtain the total adjoint. This allows the same array
            to be re-used over several projections.
        """
        self._update()
        shape = (*self._geometry.projection_shape, self._geometry.detector_angles.size)
        if not np.allclose(projection.shape[:-1], shape[:-1]):
            logger.warning('Your input projection shape appears different from the'
                           ' data shape in this ProjectionParameters instance.'
                           ' Please exercise caution.')
        if len(projection.shape) != 3:
            raise ValueError('The input projection must be 3-dimensional.'
                             ' If the last dimension is 1, please indicate'
                             ' this explicitly by reshaping it.')
        if projection.dtype != np.float64:
            raise TypeError('Projection dtype must be np.float64,'
                            f' but it is currently {projection.dtype}.')
        if output_field is None:
            output_field = np.zeros(tuple(self._geometry.volume_shape) + (projection.shape[-1],),
                                    dtype=np.float64)
        else:
            if not np.allclose(output_field.shape[1:-1], self._geometry.volume_shape):
                logger.warning('Input field shape differs from the recorded'
                               ' volume_shape of this ProjectionParameters instance.'
                               ' Please exercise caution.')
            if projection.shape[-1] != output_field.shape[-1]:
                raise ValueError(f'The last element of {projection.shape}'
                                 ' must be the same as the last element of'
                                 f' {output_field.shape}.')
            if output_field.flags['C_CONTIGUOUS'] is False:
                raise ValueError('Input output_field must be row-major and'
                                 ' contiguous (also-called C-contiguous).'
                                 ' It is currently defined with strides'
                                 f' {output_field.strides}. For a C-contiguous'
                                 ' array, the strides are strictly decreasing.')
        if projection.flags['C_CONTIGUOUS'] is False:
            raise ValueError('Input projection must be row-major and contiguous'
                             ' (also-called C-contiguous).'
                             ' It is currently defined with strides'
                             f' {projection.strides}. For a C-contiguous'
                             ' array, the strides are strictly decreasing.')
        vector_p = self._basis_vector_projection[index].astype(np.float64)
        vector_j = self._basis_vector_j[index].astype(np.float64)
        vector_k = self._basis_vector_k[index].astype(np.float64)
        projection_offsets = np.array((self._geometry.j_offsets[index],
                                       self._geometry.k_offsets[index]),
                                      dtype=np.float64).ravel()
        old_num_threads = get_num_threads()
        try:
            set_num_threads(number_of_threads)
        except ValueError as v:
            if 'number of threads' in str(v):
                logger.warning(f'number_of_threads {number_of_threads} exceeds'
                               f' maximum number of thread(s) {numba_config.NUMBA_DEFAULT_NUM_THREADS}.'
                               f' Computation will proceed with {old_num_threads} thread(s).')
            else:
                raise v
        if output_field.ndim == 4:
            temp_output_field = np.zeros((number_of_threads,) + output_field.shape, dtype=np.float64)
            john_transform_adjoint(projection, temp_output_field, vector_p,
                                   vector_j, vector_k, self._integration_step_size, projection_offsets,
                                   self._sampling_kernel.ravel(), self._kernel_offsets.reshape(2, -1))
            np.einsum('i...->...', temp_output_field, out=output_field)
        else:
            john_transform_adjoint(projection, output_field, vector_p,
                                   vector_j, vector_k, self._integration_step_size, projection_offsets,
                                   self._sampling_kernel.ravel(), self._kernel_offsets.reshape(2, -1))
        set_num_threads(old_num_threads)
        return output_field

    @property
    def integration_step_size(self) -> np.float64:
        """
        One-dimensional upsampling ratio for the integration of each projection line.
        """
        return self._integration_step_size

    @integration_step_size.setter
    def integration_step_size(self, new_step_size: np.float64):
        self._integration_step_size = np.float64(new_step_size)

    @property
    def volume_shape(self) -> NDArray[int]:
        """Shape of the volume."""
        return self._geometry.volume_shape

    @property
    def number_of_voxels(self) -> np.int32:
        """ Number of voxels. Integer-typed shorthand for ``nx * ny * nz``. """
        return np.int32(np.prod(self._geometry.volume_shape))

    @property
    def number_of_projections(self) -> int:
        """ Number of data frames (data frames), or equivalently,
        the total number of tilts and rotations at which measurements were made.
        """
        return len(self._geometry)

    @property
    def data_shape(self) -> NDArray[int]:
        """ Data shape in a series of triplets ``(x_pixels, y_pixels, number_of_detector_segments)``. """
        return (*self._geometry.projection_shape, self._geometry.detector_angles.size)

    @property
    def cumulative_projection_size(self) -> NDArray[int]:
        """Cumulative size of projection arrays, used for indexing."""
        self._update()
        return self._cumulative_projection_size

    @property
    def basis_vector_projection(self) -> NDArray[np.float64]:
        """ Basis vector for each projection direction. """
        self._update()
        return self._basis_vector_projection

    @property
    def basis_vector_j(self) -> NDArray[np.float64]:
        """ Basis vector for each projection's slow index. """
        self._update()
        return self._basis_vector_j

    @property
    def basis_vector_k(self) -> NDArray[np.float64]:
        """ Basis vector for each projection's fast index. """
        self._update()
        return self._basis_vector_k

    @property
    def sampling_kernel(self) -> NDArray[np.float64]:
        """ Convolution kernel for the sampling profile. """
        return self._sampling_kernel

    @property
    def kernel_offsets(self) -> NDArray[np.float64]:
        """ Offsets for the sampling profile kernel. """
        return self._kernel_offsets

    @property
    def is_dirty(self) -> bool:
        """ Checks if calculation of parameters is up-to-date
        with changes in the attached DataContainer object by comparing hashes.
        Used to recalculate geometry when needed. """
        return self._geometry_hash != hash(self._geometry)
