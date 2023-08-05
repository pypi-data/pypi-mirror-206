import pytest # noqa
from io import StringIO
import logging
import numba
import numpy as np
from mumott.data_handling import DataContainer
from mumott.optimization import OptimizationParameters, Optimizer


def test_minimal_pipeline():
    numba.config.NUMBA_NUM_THREADS = 1
    numba.set_num_threads(1)

    # check that the functionality for deleting frames works
    data_container = DataContainer(data_path='tests/test_half_circle.h5', data_type='h5')
    stack = data_container.stack
    assert len(stack) == 1
    del stack[0]
    assert len(stack) == 0

    # minimal check for append functionality
    dc1 = DataContainer(data_path='tests/test_half_circle.h5', data_type='h5')
    stack1 = dc1.stack
    dc2 = DataContainer(data_path='tests/test_half_circle.h5', data_type='h5')
    stack2 = dc2.stack
    assert len(stack1) == 1
    frame = stack2[0]
    del stack2[0]
    stack1.append(frame)
    assert len(stack1) == 2

    # minimal check for setitem functionality
    dc1 = DataContainer(data_path='tests/test_half_circle.h5', data_type='h5')
    dc2 = DataContainer(data_path='tests/test_half_circle.h5', data_type='h5')
    frame = dc2.stack[0]
    frame.j_offset = 1.243

    assert dc2.geometry.j_offsets[0] == 1.243

    dc2.geometry.k_offsets[0] = 4.214

    assert frame.k_offset == 4.214

    assert dc2.stack.geometry[0] == frame.geometry

    del dc2.stack[0]

    assert frame.j_offset == 1.243
    assert frame.k_offset == 4.214
    frame.data[0][0] = [1, 2, 3]
    dc1.stack[0] = frame

    assert np.all(dc1.stack[0].data[0][0] == [1, 2, 3])
    assert dc1.stack[0].j_offset == 1.243
    assert dc1.stack[0].k_offset == 4.214
    assert dc1.stack[0].geometry == dc1.stack.geometry[0]

    # load data container and check its basic output
    data_container = DataContainer(data_path='tests/test_half_circle.h5', data_type='h5')
    s = str(data_container)
    assert 'DataContainer' in s
    assert 'Corrected for transmission' in s
    assert 'Corrected for transmission' in s
    s = data_container._repr_html_()
    assert 'DataContainer' in s
    assert 'Corrected for transmission' in s
    assert 'Corrected for transmission' in s

    s = str(data_container.geometry)
    assert 'Geometry' in s
    s = data_container.geometry._repr_html_()
    assert 'Geometry' in s
    s = str(data_container.stack)
    assert 'Stack' in s
    s = data_container.stack._repr_html_()
    assert 'Stack' in s

    s = str(data_container.stack[0])
    assert 'Frame' in s
    assert 'diode' in s
    assert 'dcf160' in s
    s = data_container.stack[0]._repr_html_()
    assert 'Frame' in s
    assert 'diode' in s
    assert 'dcf160' in s

    # set up reconstruction parameters
    reconstruction_parameters = data_container.reconstruction_parameters
    s = str(reconstruction_parameters)
    assert 'ReconstructionParameters' in s

    # set up optimization parameters
    optimization_parameters = OptimizationParameters(
        reconstruction_parameters=reconstruction_parameters,
        integration_step_size=0.5,
        maximum_order=6,
        initial_value=0,
        optimization_bounds_isotropic=(-np.inf, np.inf),
        minimize_args=dict(method='L-BFGS-B'),
        minimize_options=dict(maxiter=15,
                              ftol=1e-2,
                              gtol=1e-5,
                              disp=1,
                              maxls=10,
                              maxcor=3))
    s = str(optimization_parameters)
    assert 'OptimizationParameters' in s

    # set up optimizer
    optimizer = Optimizer(optimization_parameters=optimization_parameters)
    s = str(optimizer)
    assert 'Optimizer' in s

    # reconfigure logging
    # - override default handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    # - send logging to stream
    f = StringIO()
    logging.basicConfig(stream=f, level=logging.INFO)
    # run optimization
    optimizer.run_optimization()
    s = f.getvalue()
    assert 'Running optimization' in s
    assert 'Calculating residual' in s
    assert 'Residual norm' in s

    # check that coefficients are correct
    coeffs = reconstruction_parameters.reconstruction_input.optimization_coefficients
    assert len(coeffs) == 1792
    reference_coeffs = [
        0.87460165, 0.08097529, -0.00714394, 0.48018855, -0.14996967,
        0.84801155, 0.13713276, -0.01481688, 0.0562904, -0.00439217,
        0.31208931, -0.09220303, 0.58949969, -0.10305367, 0.71151233,
        0.18419943, -0.01804851, 0.10037774, -0.0150384, 0.04186866,
        -0.00137076, 0.26784486, -0.02877578, 0.43846846, -0.10459437,
        0.52080918, -0.07439698, 0.62732564, 0.87957619, 0.0783882,
        -0.01002165, 0.53845212, -0.21038031, 0.82091841, 0.1294915,
        -0.02184576, 0.06315636, -0.00522345, 0.29896082, -0.10965364]
    assert np.allclose(coeffs[:40], reference_coeffs, atol=1e-4)
