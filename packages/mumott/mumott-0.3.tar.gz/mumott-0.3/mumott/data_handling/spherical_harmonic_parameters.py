"""Container for the class SphericalHarmonicParameters."""

import logging
import numpy as np
from scipy.special import sph_harm
from numpy.typing import NDArray
from numpy import pi


logger = logging.getLogger(__name__)


class SphericalHarmonicParameters:
    """
    Class containing parameters pertaining to the orders and degrees of spherical harmonics used.
    Should be attached to a
    :class:`ReconstructionParameters <mumott.reconstruction_parameters.ReconstructionParameters>` instance.

    Parameters
    ----------
    geometry : Geometry
        The data container object linked to this instance.
    l_max : int
        The maximum order of spherical harmonics that should be reconstructed.
    integration_weights : NDArray[float]
        If the data is computed using a fitted distribution or similar, the weights of the distribution
        can be provided.
    integration_samples : int
        Number of samples to use for the integral around the probed point,
        in order to approximate the effect of summing up pixels in an area
        on the detector. If the probed points were found through a least-squares
        fit of the detector data, then set this to ``1``. Default is ``11``, which
        is almost certainly more than enough.
    use_kernel : bool
        Whether to use a kernel to prioritize certain orders in the gradient. Default is ``False``.
    kernel_exponent : float
        The power law exponent of the kernel used if :attr:`use_kernel` is set to ``True``.
        Order zero will have weight ``1``, other orders  will have weight
        ``ell ** kernel_exponent`` where ``ell`` is the order. Default is ``-1``,
        which prioritizes lower orders. Positive values prioritize higher orders.
    """

    def __init__(self,
                 geometry,
                 l_max: int,
                 integration_samples: int = 11,
                 integration_weights: NDArray[float] = None,
                 use_kernel: bool = False,
                 kernel_exponent: float = -1.):
        # Todo: fix type hinting once import issues are resolved
        self._geometry = geometry
        self._geometry_hash = hash(geometry)
        # Check if full circle appears covered or not.
        delta = np.abs(self._geometry.detector_angles[0] -
                       self._geometry.detector_angles[-1] % (2 * np.pi))
        if abs(delta - np.pi) < min(delta, abs(delta - 2 * np.pi)):
            self._full_circle_covered = False
        else:
            logger.warning('The detector angles appear to cover a full circle.'
                           ' Friedel symmetry will be assumed in the calculation.\n'
                           'If this is incorrect, please set the property full_circle_covered'
                           ' to False.')
            self._full_circle_covered = True
        self._l_max = np.int32(l_max)
        self._m_max = np.int32(l_max)
        self._update_coefficient_indices()
        self._number_of_coefficients = len(self._l_indices)
        self._integration_samples = integration_samples
        self._integration_weights = integration_weights
        self._use_kernel = use_kernel
        self._kernel_exponent = kernel_exponent
        self._update_geometry(force_update=True)

    def _update_geometry(self, force_update: bool = False,
                         update_probed_coordinates: bool = True,
                         update_gradient: bool = True,
                         update_factors: bool = True) -> None:
        """Internal method for checking if geometry needs to be recomputed,
           and doing so if necessary.

        Parameters
        ----------
        update_gradient
            If ``True`` (default), gradient factors are recomputed if needed.
            Used to avoid double computation.
        update_factors
            If ``False`` (default), forward factors are recomputed if needed.
            Used to avoid double computation.
        """
        is_dirty = self.is_dirty
        if is_dirty or force_update:
            if update_probed_coordinates or is_dirty:
                self._calculate_probed_coordinates()
                self._geometry_hash = hash(self._geometry)
                if update_factors:
                    self._compute_spherical_harmonic_factors()
                if update_gradient:
                    self._compute_spherical_harmonic_gradient()
            else:
                if update_factors:
                    self._compute_spherical_harmonic_factors()
                if update_gradient:
                    self._compute_spherical_harmonic_gradient()

    def _update_coefficient_indices(self):
        """
        Updates the attributes `l_indices` and `m_indices`.
        """
        mm = np.zeros((self._l_max + 1) * (self._l_max // 2 + 1))
        ll = np.zeros((self._l_max + 1) * (self._l_max // 2 + 1))
        count = 0
        for h in range(0, self._l_max + 1, 2):
            for i in range(-h, h + 1):
                ll[count] = h
                mm[count] = i
                count += 1
        self._l_indices = ll.astype(np.int32)
        self._m_indices = mm.astype(np.int32)

    def _compute_spherical_harmonic_gradient(self) -> None:
        """ Method for computing gradient factors for spherical harmonics. Must be called
        after ``compute_spherical_harmonic_factors``."""
        self._update_geometry(update_gradient=False)
        if self._use_kernel:
            kernel_weights = np.zeros(self._l_indices.size)
            kernel_weights[self._l_indices != 0] = \
                self._l_indices[self._l_indices != 0] ** float(self._kernel_exponent)
            kernel_weights[self._l_indices == 0] = 1
            kernel = kernel_weights
            kernel *= np.sqrt(1 / np.sum(kernel ** 2))
            kernel = kernel.reshape(1, -1).astype(complex)
            self._spherical_harmonic_gradient_factors = self._spherical_harmonic_factors * kernel
        else:
            self._spherical_harmonic_gradient_factors = self._spherical_harmonic_factors

    def _calculate_probed_coordinates(self) -> None:
        """
        Calculates the probed polar and azimuthal coordinates on the unit sphere at
        each angle of projection and for each detector segment in the system's geometry.
        """
        n_proj = len(self._geometry)
        n_seg = len(self._geometry.detector_angles)
        probed_directions_zero_rot = np.zeros((n_seg,
                                               self._integration_samples,
                                               3))
        # Impose symmetry if needed.
        if not self._full_circle_covered:
            shift = np.pi
        else:
            shift = 0
        det_bin_middles_extended = np.copy(self._geometry.detector_angles)
        det_bin_middles_extended = np.insert(det_bin_middles_extended, 0,
                                             det_bin_middles_extended[-1] + shift)
        det_bin_middles_extended = np.append(det_bin_middles_extended, det_bin_middles_extended[1] + shift)

        for ii in range(n_seg):

            # Check if the interval from the previous to the next bin goes over the -pi +pi discontinuity
            before = det_bin_middles_extended[ii]
            now = det_bin_middles_extended[ii + 1]
            after = det_bin_middles_extended[ii + 2]

            if abs(before - now + 2 * np.pi) < abs(before - now):
                before = before + 2 * np.pi
            elif abs(before - now - 2 * np.pi) < abs(before - now):
                before = before - 2 * np.pi

            if abs(now - after + 2 * np.pi) < abs(now - after):
                after = after - 2 * np.pi
            elif abs(now - after - 2 * np.pi) < abs(now - after):
                after = after + 2 * np.pi

            # Generate a linearly spaced set of angles covering the detector segment
            start = 0.5 * (before + now)
            end = 0.5 * (now + after)
            inc = (end - start) / self._integration_samples
            angles = np.linspace(start + inc / 2, end - inc / 2, self._integration_samples)

            # Make the zero-rotation-frame vectors corresponding to the given angles
            probed_directions_zero_rot[ii, :, :] = np.cos(angles[:, np.newaxis]) * \
                self._geometry.detector_direction_origin[np.newaxis, :]
            probed_directions_zero_rot[ii, :, :] += np.sin(angles[:, np.newaxis]) * \
                self._geometry.detector_direction_positive_90[np.newaxis, :]

        # Initialize array for vectors
        probed_direction_vectors = np.zeros((n_proj,
                                             n_seg,
                                             self._integration_samples,
                                             3), dtype=np.float64)
        # Calculate all the rotations
        probed_direction_vectors[...] = \
            np.einsum('kij,mli->kmlj', self._geometry.rotations_as_array, probed_directions_zero_rot)
        probed_direction_vectors *= \
            np.reciprocal(np.linalg.norm(probed_direction_vectors, ord=2, axis=-1))[..., None]

        # Assign the output structures
        self._probed_theta_interval = np.arccos(probed_direction_vectors[:, :, :, 2])
        self._probed_phi_interval = np.arctan2(probed_direction_vectors[:, :, :, 1],
                                               probed_direction_vectors[:, :, :, 0])

    def _compute_spherical_harmonic_factors(self) -> None:
        """ Method for computing real spherical harmonic factors. Computes the
        contribution of the basis function of each order and degree at a set of
        probed points on the unit sphere.

        Notes
        -----
            This function uses
            :func:`scipy.special.sph_harm <https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.sph_harm.html>`, # noqa
            the documentation and source code of which use the opposite naming convention
            for the polar and azimuthal angles.
        """
        self._update_geometry(update_factors=False, update_gradient=False)
        spherical_harmonic_factors = np.zeros((
            self._probed_theta_interval.shape[0],
            self._probed_theta_interval.shape[1],
            self._l_indices.size))
        if self._integration_weights is None:
            integration_weights = np.ones_like(self._probed_theta_interval) / \
                self._probed_theta_interval.shape[2]
        else:
            integration_weights = self._integration_weights
        for i, arc in enumerate(zip(self._probed_theta_interval, self._probed_phi_interval)):
            for j, angles in enumerate(zip(arc[0], arc[1])):
                theta, phi = angles
                complex_function = (integration_weights[i, j, np.newaxis, :] *
                                    sph_harm(abs(self._m_indices.reshape(-1, 1)),
                                             self._l_indices.reshape(-1, 1),
                                             phi.reshape(1, -1),
                                             theta.reshape(1, -1))).sum(axis=1)
                spherical_harmonic_factors[i, j, self._m_indices == 0] = \
                    np.sqrt((4 * pi)) * complex_function[self._m_indices == 0].real
                spherical_harmonic_factors[i, j, self._m_indices > 0] = \
                    ((-1.) ** (self._m_indices[self._m_indices > 0])) * np.sqrt((4 * pi)) * \
                    np.sqrt(2) * complex_function[self._m_indices > 0].real
                spherical_harmonic_factors[i, j, self._m_indices < 0] = \
                    ((-1.) ** (self._m_indices[self._m_indices < 0])) * np.sqrt((4 * pi)) * \
                    np.sqrt(2) * complex_function[self._m_indices < 0].imag
        self._spherical_harmonic_factors = spherical_harmonic_factors

    @property
    def use_kernel(self) -> bool:
        """Whether to use a kernel in computing the gradient. """
        return self._use_kernel

    @property
    def kernel_exponent(self) -> float:
        """The exponent used to compute the gradient if ``use_kernel`` is set to ``True``. """
        return self._kernel_exponent

    @property
    def integration_samples(self) -> int:
        """Number of samples used to compute spherical harmonic factors."""
        return self._integration_samples

    @property
    def integration_weights(self) -> NDArray[float]:
        """Weights used to compute spherical harmonic factors."""
        return self._integration_weights

    @use_kernel.setter
    def use_kernel(self, value) -> None:
        self._use_kernel = True
        self._update_geometry(force_update=True, update_probed_coordinates=False)

    @kernel_exponent.setter
    def kernel_exponent(self, val: float) -> None:
        self._kernel_exponent = float(val)
        self._update_geometry(force_update=True, update_probed_coordinates=False)

    @integration_samples.setter
    def integration_samples(self, val: int) -> None:
        self._integration_samples = int(val)
        self._update_geometry(force_update=True)

    @integration_weights.setter
    def integration_weights(self, val: NDArray[float]) -> None:
        self._integration_weights = np.array(val)
        self._update_geometry(force_update=True, update_probed_coordinates=False)

    @property
    def l_max(self) -> np.int32:
        """ Maximum spherical harmonic order. """
        return self._l_max

    @l_max.setter
    def l_max(self, new_l_max: int):
        self._l_max = np.int32(new_l_max)
        self._m_max = np.int32(new_l_max)
        self._update_coefficient_indices()
        self._update_geometry(force_update=True, update_probed_coordinates=False)

    @property
    def m_max(self) -> np.int32:
        """ Maximum spherical harmonic degree. """
        return self._m_max

    @property
    def l_indices(self) -> NDArray[np.int32]:
        """
        Array of spherical harmonic orders, indicating the order
        of the coefficient at the corresponding index.
        """
        return self._l_indices

    @property
    def m_indices(self) -> NDArray[np.int32]:
        """
        Array of spherical harmonic degrees, indicating the
        degree of the coefficient at the corresponding index.
        """
        return self._m_indices

    @property
    def number_of_coefficients(self) -> np.int32:
        """
        Number of spherical harmonic coefficients.
        """
        return len(self._l_indices)

    @property
    def spherical_harmonic_factors(self) -> NDArray[np.float64]:
        """ Matrix of factors mapping spherical harmonic coefficients
        to detector segments.
        """
        self._update_geometry()
        return self._spherical_harmonic_factors

    @property
    def spherical_harmonic_gradient_factors(self) -> NDArray[np.float64]:
        self._update_geometry()
        return self._spherical_harmonic_gradient_factors

    @property
    def probed_theta_interval(self) -> NDArray[np.float64]:
        """
        Full range of polar coordinates on the unit sphere probed during projection.
        """
        self._update_geometry()
        probed_vec = np.stack(
              (np.sin(self._probed_theta_interval) * np.cos(self._probed_phi_interval),
               np.sin(self._probed_theta_interval) * np.sin(self._probed_phi_interval),
               np.cos(self._probed_theta_interval)), axis=3).mean(2)
        return np.arccos(probed_vec[..., 2] / np.linalg.norm(probed_vec, 2, -1))

    @property
    def probed_phi_interval(self) -> NDArray[np.float64]:
        """
        Full range of azimuthal coordinates on the unit sphere probed during projection.
        """
        self._update_geometry()
        probed_vec = np.stack(
              (np.sin(self._probed_theta_interval) * np.cos(self._probed_phi_interval),
               np.sin(self._probed_theta_interval) * np.sin(self._probed_phi_interval),
               np.cos(self._probed_theta_interval)), axis=3).mean(2)
        return np.arctan2(probed_vec[..., 1], probed_vec[..., 0])

    @property
    def probed_theta(self) -> NDArray[np.float64]:
        """
        Polar coordinates of each segment probed during projection.
        """
        self._update_geometry()
        return self._probed_theta

    @property
    def probed_phi(self) -> NDArray[np.float64]:
        """
        Azimuthal coordinates probed during projection.
        """
        self._update_geometry()
        return self._probed_phi

    @property
    def is_dirty(self) -> bool:
        """ Checks if calculation of parameters is up-to-date
        with changes in the attached DataContainer object by comparing hashes.
        Used to recalculate geometry when needed. """
        return self._geometry_hash != hash(self._geometry)

    @property
    def full_circle_covered(self) -> bool:
        """``True`` if the detector angles appear to cover
        a full circle. """
        return self._full_circle_covered

    @full_circle_covered.setter
    def full_circle_covered(self, val: bool) -> None:
        self._full_circle_covered = val
        self._update_geometry(force_update=True)
