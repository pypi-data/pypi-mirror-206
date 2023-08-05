import pytest  # noqa

import numpy as np
from mumott import DataContainer

from mumott.methods.basis_sets import SphericalHarmonics
from mumott.methods.projectors import SAXSProjectorNumba
from mumott.methods.functionals import SIGTT
from mumott.optimization.objective_functions import SquaredLoss

default_hash = '15afa6'


def test_get_residual_norm():
    dc = DataContainer('tests/test_half_circle.h5')
    bs = SphericalHarmonics()
    pr = SAXSProjectorNumba(dc.geometry)
    meth = SIGTT(dc, bs, pr)  # noqa
    lf = SquaredLoss(meth)
    d = lf.get_residual_norm(get_gradient=False)
    assert np.isclose(d['residual_norm'], 7304.44)
    assert d['gradient'] is None
    d = lf.get_residual_norm(get_gradient=True)
    assert np.isclose(d['residual_norm'], 7304.44)
    assert np.allclose(d['gradient'][0, 0], [[-47.51], [-47.77], [-48.83], [-50.04]])
    dc.stack.weights *= 0.5
    lf = SquaredLoss(meth, use_weights=True)
    d = lf.get_residual_norm(get_gradient=False)
    assert np.isclose(d['residual_norm'], 3652.22)
    assert d['gradient'] is None
    d = lf.get_residual_norm(get_gradient=True)
    assert np.isclose(d['residual_norm'], 3652.22)
    assert np.allclose(d['gradient'][0, 0], [[-23.755], [-23.885], [-24.415], [-25.02]])
    lf.objective_function_multiplier = 10
    d = lf.get_residual_norm(get_gradient=False)
    assert np.isclose(d['residual_norm'], 36522.24)


def test_str():
    dc = DataContainer('tests/test_half_circle.h5')
    bs = SphericalHarmonics()
    pr = SAXSProjectorNumba(dc.geometry)
    meth = SIGTT(dc, bs, pr)
    lf = SquaredLoss(meth)
    s = str(lf)
    assert default_hash in s


def test_html():
    dc = DataContainer('tests/test_half_circle.h5')
    bs = SphericalHarmonics()
    pr = SAXSProjectorNumba(dc.geometry)
    meth = SIGTT(dc, bs, pr)
    lf = SquaredLoss(meth)
    h = lf._repr_html_()
    assert default_hash in h


def test_hash():
    dc = DataContainer('tests/test_half_circle.h5')
    bs = SphericalHarmonics()
    pr = SAXSProjectorNumba(dc.geometry)
    meth = SIGTT(dc, bs, pr)
    lf = SquaredLoss(meth, use_weights=True)
    assert hex(hash(lf))[2:8] == '1ec237'
    lf.use_weights = False
    assert hex(hash(lf))[2:8] == default_hash
    meth.coefficients += 1
    assert hex(hash(lf))[2:8] == 'd459d3'
