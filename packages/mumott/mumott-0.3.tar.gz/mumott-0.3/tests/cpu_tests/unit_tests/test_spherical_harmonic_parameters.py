import pytest
from mumott.data_handling.data_container import DataContainer
from mumott.data_handling.spherical_harmonic_parameters import SphericalHarmonicParameters


@pytest.mark.parametrize('filename, expected_output', [('tests/test_full_circle.h5', True),
                                                       ('tests/test_half_circle.h5', False)])
def test_circle(filename, expected_output):
    data_container = DataContainer(data_path=filename, data_type='h5')
    sph = SphericalHarmonicParameters(data_container.geometry, 0)
    assert sph.full_circle_covered == expected_output
