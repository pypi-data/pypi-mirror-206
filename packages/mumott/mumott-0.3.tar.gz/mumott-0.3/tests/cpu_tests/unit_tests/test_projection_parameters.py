import numpy as np
from mumott.core.projection_parameters import ProjectionParameters
from mumott.data_handling.data_container import DataContainer

data_container = DataContainer(data_path='tests/test_half_circle.h5', data_type='h5')

default_kwargs = dict(geometry=data_container.geometry,
                      integration_step_size=1.0)


def test_init():
    test_input = default_kwargs.copy()
    pp = ProjectionParameters(**test_input)
    pp.__repr__  # sanity check
    assert pp.number_of_projections == len(data_container.stack)
    assert pp.number_of_voxels == 64
    assert np.all(pp.data_shape[:-1] == data_container.geometry.projection_shape)
    assert np.all(pp.volume_shape == data_container.geometry.volume_shape)


def test_project():
    test_input = default_kwargs.copy()
    test_input['integration_step_size'] = 0.5
    pp = ProjectionParameters(**test_input)
    vol = np.ones((2, 2, 2, 2), dtype=np.float64)
    vol[:, 1, :, 0] *= 0.7
    vol[0, :, 1, :] *= 0.7
    proj = pp.project(vol, 0, None, 1)
    print(proj)
    assert np.allclose(proj[1:-1, 1:-1], np.array([[[1.35, 1.5],
                                                    [0.945, 1.05]],
                                                   [[1.35, 1.5],
                                                    [1.35, 1.5]]]))


def test_adjoint():
    test_input = default_kwargs.copy()
    pp = ProjectionParameters(**test_input)
    proj = np.ones((2, 2, 2), dtype=np.float64)
    proj[:, 0, :] += 0.4
    proj[1, :, 1] *= 1.7
    proj[0, :, :] *= 1.3
    vol = pp.adjoint(proj, 0, None, 1)
    print(vol[1:-1, 1:-1, 1:-1])
    assert np.allclose(vol[1:-1, 1:-1, 1:-1], np.array([[[[1.82, 1.82],
                                                          [1.3, 1.3]],
                                                         [[1.82, 1.82],
                                                          [1.3, 1.3]]],
                                                        [[[1.4, 2.38],
                                                          [1., 1.7]],
                                                         [[1.4, 2.38],
                                                          [1., 1.7]]]]))


def test_integration_step_size():
    test_input = default_kwargs.copy()
    pp = ProjectionParameters(**test_input)
    assert pp.integration_step_size == test_input['integration_step_size']

    for value in [2, 6, 9.4]:
        pp.integration_step_size = value
        assert pp.integration_step_size == value


def test_calculate_basis_vectors():
    test_input = default_kwargs.copy()
    pp = ProjectionParameters(**test_input)
    assert np.allclose(pp.basis_vector_projection, np.array([[-0.04758192, 0.99886734, 0.]]))
    assert np.allclose(pp.basis_vector_j, np.array([[0.99886734, 0.04758192, 0.]]))
    assert np.allclose(pp.basis_vector_k, np.array([[0., 0., 1.]]))
