from abc import ABC, abstractmethod

from numpy.typing import NDArray

from ... import Geometry


class Projector(ABC):
    """Projector for transforms of tensor fields from three-dimensional
    space to projection space.
    """

    def __init__(self,
                 geometry: Geometry):
        self._geometry = geometry
        self._geometry_hash = hash(geometry)

    @abstractmethod
    def forward(self,
                field: NDArray,
                index: NDArray[int]) -> NDArray:
        pass

    @abstractmethod
    def adjoint(self,
                projection: NDArray,
                index: NDArray[int]) -> NDArray:
        pass

    @property
    def is_dirty(self) -> bool:
        """ Returns ``True`` if the system geometry has changed without
        the projection geometry having been updated. """
        return self._geometry_hash != hash(self._geometry)

    def _update(self, force_update: bool = False) -> None:
        if not (self.is_dirty or force_update):  # If not dirty, do nothing
            return
        else:
            pass  # Else, do an update as detemined by the child class definition
