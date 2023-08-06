# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

# Built-in imports
import numpy
from dataclasses import dataclass

# Local imports
from SuPyMode import representations


class SuperModeCombination():
    def __init__(self, *supermodes):
        self.supermodes = supermodes


class InheritFromSuperSet():
    """
    Property class for inherited attribute from SuperSet.

    """
    @property
    def geometry(self) -> object:
        return self.parent_set.geometry

    @property
    def coordinate_system(self) -> object:
        return self.parent_set.coordinate_system


@dataclass
class SuperMode(InheritFromSuperSet):
    """
    .. note::
        This class is a representation of the fiber optic structures SuperModes.
        Those mode belongs to a SuperSet class and are constructed with the SuPySolver.
        It links to c++ SuperMode class.
    """
    parent_set: None
    """SuperSet to which is associated the computed this mode"""
    binded_supermode: None
    """C++ binded sueprmode"""
    solver_number: int
    """Number which bind this mode to a specific python solver"""
    mode_number: int
    """Unique number associated to this mode in a particular symmetry set"""
    wavelength: float
    """UWavelength of the simulated modes"""
    boundaries: dict
    """Boundary conditions"""
    itr_list: numpy.ndarray
    """List of itr value corresponding to the slices where fields and propagation constant are computed"""
    label: str = None
    """Name to give to the mode"""

    def __post_init__(self):
        self.ID = [self.solver_number, self.binding_number]
        self.field = representations.Field(parent_supermode=self)
        self.index = representations.Index(parent_supermode=self)
        self.beta = representations.Beta(parent_supermode=self)
        self.normalized_coupling = representations.NormalizedCoupling(parent_supermode=self)
        self.overlap = representations.Overlap(parent_supermode=self)
        self.adiabatic = representations.Adiabatic(parent_supermode=self)
        self.eigen_value = representations.EigenValue(parent_supermode=self)
        self.beating_length = representations.BeatingLength(parent_supermode=self)

    def __hash__(self):
        return hash(self.binded_supermode)

    @property
    def binding_number(self):
        """ Returns the mode number specific to one CppSolver """
        return self.binded_supermode.binding_number

    @property
    def mesh_gradient(self) -> numpy.ndarray:
        return self.binded_supermode.mesh_gradient

    @property
    def nx(self) -> int:
        return self.binded_supermode.nx

    @property
    def ny(self) -> int:
        return self.binded_supermode.ny

    @property
    def amplitudes(self) -> numpy.ndarray:
        amplitudes = numpy.zeros(len(self.parent_set.supermodes)).astype(complex)
        amplitudes[self.mode_number] = 1
        return amplitudes

    @property
    def stylized_label(self):
        if self.label is None:
            return f"Mode: {self.ID}"
        else:
            return f"${self.label}$"

    def is_computation_compatible(self, other: 'SuperMode') -> bool:
        """
        Determines whether the specified other supermode is compatible
        for computation of the modal coupling and adiabatic criterion.
        It, basically return False only if the mode is the same or if the
        boundaries symmetries differ in some way.

        :param      other:  The other SuperMode to compare with
        :type       other:  SuperMode

        :returns:   True if the specified other is computation compatible, False otherwise.
        :rtype:     bool
        """
        if self.ID != other.ID and self.is_symmetry_compatible(other):
            return True
        else:
            return False

    def is_symmetry_compatible(self, other: 'SuperMode'):
        return self.boundaries == other.boundaries

    def add_symmetry_to_vector(self, vector: numpy.ndarray, type: str) -> numpy.ndarray:
        n = len(vector)
        dx = abs(vector[0] - vector[1])
        if type == 'right':
            start = vector[0]
            return numpy.arange(0, 2 * n) * dx + start
        elif type == 'left':
            start = vector[-1]
            return -numpy.arange(0, 2 * n)[::-1] * dx + start

    def get_axis_vector(self, add_symmetries: bool = True) -> tuple:
        full_x_axis = self.coordinate_system.x_vector
        full_y_axis = self.coordinate_system.y_vector

        if not add_symmetries:
            return full_x_axis, full_y_axis

        if self.boundaries.right in ['symmetric', 'anti-symmetric']:
            full_x_axis = self.add_symmetry_to_vector(full_x_axis, type='right')

        if self.boundaries.left in ['symmetric', 'anti-symmetric']:
            full_x_axis = self.add_symmetry_to_vector(full_x_axis, type='left')

        if self.boundaries.top in ['symmetric', 'anti-symmetric']:
            full_y_axis = self.add_symmetry_to_vector(full_y_axis, type='right')

        if self.boundaries.bottom in ['symmetric', 'anti-symmetric']:
            full_y_axis = self.add_symmetry_to_vector(full_y_axis, type='left')

        return full_x_axis, full_y_axis

# -
