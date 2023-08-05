# -*- coding: utf-8 -*-
"""
Main module of the mumott package.
"""

import logging
from .core.numba_setup import numba_setup
from .core.projection_parameters import ProjectionParameters
from .data_handling.geometry import Geometry
from .core.probed_coordinates import ProbedCoordinates
from .data_handling.data_container import DataContainer
from .optimization.optimization_parameters import OptimizationParameters
from .optimization.optimization_timer import OptimizationTimer
from .optimization.optimizer import Optimizer
from .optimization.regularizer import Regularizer
from .optimization.regularization_parameters import RegularizationParameters
from .optimization.regularization_curve_finder import RegularizationCurveFinder
from .output_handling.live_view_handler import LiveViewHandler
from .output_handling.output_handler import OutputHandler

__project__ = 'mumott'
__description__ = 'A module for analyzing tensor tomography experiments via Python'
__copyright__ = '2023'
__license__ = 'Mozilla Public License 2.0 (MPL 2.0)'
__version__ = '0.3'
__maintainer__ = 'The mumott developers team'
__status__ = 'Beta'
__url__ = 'https://mumott.org/'

__all__ = [
    'TransformParameters',
    'ProjectionParameters',
    'Geometry',
    'ProbedCoordinates',
    'DataContainer',
    'LiveViewHandler',
    'OutputHandler',
    'OptimizationParameters',
    'OptimizationTimer',
    'Optimizer',
    'Regularizer',
    'RegularizationParameters',
    'RegularizationCurveFinder',
]

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
numba_setup()
