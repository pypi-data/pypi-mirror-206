from abc import ABC, abstractmethod
from typing import Dict

import numpy as np
from numpy.typing import NDArray

from ...methods.functionals.base_functional import Functional


class ObjectiveFunction(ABC):

    """This is the base class from which specific objective functions are derived.

    Parameters
    ----------
    functional
        A class derived from :class:`Functional <mumott.methods.functionals.base_functional.Functional>`
    use_weights
        Whether to multiply residuals with weights before calculating the residual norm. The calculation
        is also applied to the gradient.
    objective_function_multiplier
        A multiplier that is applied to the residual norm and gradient. Useful in cases where
        a very small or large objective function value changes the optimizer behaviour.
    """

    def __init__(self,
                 functional: Functional,
                 use_weights: bool = False,
                 objective_function_multiplier: float = 1):
        self._functional = functional
        self._use_weights = use_weights
        self._objective_function_multiplier = objective_function_multiplier

    @abstractmethod
    def get_residual_norm(self,
                          coefficients: NDArray = None,
                          get_gradient: bool = False) -> Dict:
        """Retrieves residual norm and possibly gradient based on the attached `functional`.
        If `coefficients` given, then `functional.coefficients` should be updated
        with these new values, otherwise, the residual norm and possible gradient should
        just be calculated using the pre-exiting coefficients.

        Parameters
        ----------
        coefficients
            An `NDArray` of values of the same shape as ``functional.coefficients``.
        get_gradient
            If ``True``, returns a ``'gradient'`` of the same shape as ``functional.coefficients``.
            Otherwise, the entry ``'gradient'`` will be ``None``.

        Returns
        -------
            A dictionary with at least two entries, ``residual_norm`` and ``gradient``.
        """
        pass

    @property
    def use_weights(self) -> bool:
        """ Whether to use weights or not in calculating the residual
        and gradient. """
        return self._use_weights

    @use_weights.setter
    def use_weights(self, val: bool) -> None:
        self._use_weights = val

    @property
    def objective_function_multiplier(self) -> float:
        return self._objective_function_multiplier

    @objective_function_multiplier.setter
    def objective_function_multiplier(self, val: float) -> None:
        self._objective_function_multiplier = val

    @property
    def initial_values(self) -> NDArray:
        """ Initial coefficient values for optimizer; defaults to zeros. """
        return np.zeros_like(self._functional.coefficients)

    @property
    @abstractmethod
    def _function_as_str(self) -> str:
        """ Should return a string representation of the associated loss function
        of the residual in Python idiom, e.g. 'L(r) = 0.5 * r ** 2' for squared loss. """
        pass

    @property
    @abstractmethod
    def _function_as_tex(self) -> str:
        """ Should return a string representation of the associated loss function
        of the residual in MathJax-renderable TeX, e.g. $L(r) = \frac{r^2}{2}$ for squared loss"""
        pass

    def __str__(self) -> str:
        s = []
        wdt = 74
        s += ['=' * wdt]
        s += [self.__class__.__name__.center(wdt)]
        s += ['-' * wdt]
        with np.printoptions(threshold=4, precision=5, linewidth=60, edgeitems=1):
            s += ['{:18} : {}'.format('Functional', self._functional.__class__.__name__)]
            s += ['{:18} : {}'.format('Uses weights', self.use_weights)]
            s += ['{:18} : {}'.format('objective_function_multiplier',
                                      self._objective_function_multiplier)]
            s += ['{:18} : {}'.format('Function of residual', self._function_as_str)]
            s += ['{:18} : {}'.format('hash', hex(hash(self))[2:8])]
        s += ['-' * wdt]
        return '\n'.join(s)

    def _repr_html_(self) -> str:
        s = []
        s += [f'<h3>{__class__.__name__}</h3>']
        s += ['<table border="1" class="dataframe">']
        s += ['<thead><tr><th style="text-align: left;">Field</th><th>Size</th><th>Data</th></tr></thead>']
        s += ['<tbody>']
        with np.printoptions(threshold=4, edgeitems=2, precision=2, linewidth=40):
            s += ['<tr><td style="text-align: left;">Functional</td>']
            s += [f'<td>{1}</td><td>{self._functional.__class__.__name__}</td></tr>']
            s += ['<tr><td style="text-align: left;">use_weights</td>']
            s += [f'<td>{1}</td><td>{self.use_weights}</td></tr>']
            s += ['<tr><td style="text-align: left;">objective_function_multiplier</td>']
            s += [f'<td>{1}</td><td>{self._objective_function_multiplier}</td></tr>']
            s += ['<tr><td style="text-align: left;">Function of residual r</td>']
            s += [f'<td>1</td><td>{self._function_as_tex}</td></tr>']
            s += ['<tr><td style="text-align: left;">Hash</td>']
            h = hex(hash(self))
            s += [f'<td>{len(h)}</td><td>{h[2:8]}</td></tr>']
        s += ['</tbody>']
        s += ['</table>']
        return '\n'.join(s)
