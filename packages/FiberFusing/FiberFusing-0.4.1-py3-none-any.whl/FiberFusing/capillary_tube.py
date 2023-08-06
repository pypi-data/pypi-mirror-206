#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy

from FiberFusing.axes import Axes
from FiberFusing import utils
from FiberFusing import Circle
from FiberFusing.fiber_base_class import get_silica_index


class CapillaryTube(utils.StructureBaseClass):
    def __init__(self, delta_n: float, radius: float = 1000, position: tuple = (0, 0)):
        self.delta_n = delta_n
        self.position = position
        self.radius = radius
        self.index = self.get_silica_index() - self.delta_n

    @property
    def structure_dictionary(self):
        polygon = Circle(
            position=self.position,
            radius=self.radius,
            index=self.index
        )

        return {
            'name': {
                'index': self.index,
                'polygon': polygon
            }
        }

    def overlay_structures_on_mesh(self, mesh: numpy.ndarray, coordinate_axis: Axes) -> numpy.ndarray:
        """
        Return a mesh overlaying all the structures in the order they were defined.

        :param      coordinate_axis:  The coordinates axis
        :type       coordinate_axis:  Axis

        :returns:   The raster mesh of the structures.
        :rtype:     numpy.ndarray
        """
        return self._overlay_structure_dictionary_on_mesh_(
            structure_dictionnary=self.structure_dictionary,
            mesh=mesh,
            coordinate_axis=coordinate_axis
        )


# -
