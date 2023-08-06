# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

import numpy
from MPSPlots.Render2D import Scene2D, ColorBar, Axis, Mesh, Line
from MPSPlots import colormaps

from SuPyMode.tools import plot_style


class InheritFromSuperMode():
    def _set_axis_(self, ax: Axis):
        for element, value in self.plot_style.items():
            setattr(ax, element, value)

    def __getitem__(self, idx):
        return self._data[idx]

    @property
    def mode_number(self):
        return self.parent_supermode.mode_number

    @property
    def solver_number(self):
        return self.parent_supermode.solver_number

    @property
    def axes(self):
        return self.parent_supermode.axes

    @property
    def boundaries(self):
        return self.parent_supermode.boundaries

    @property
    def itr_list(self):
        return self.parent_supermode.itr_list

    @property
    def ID(self):
        return self.parent_supermode.ID

    @property
    def label(self):
        return self.parent_supermode.label

    @property
    def stylized_label(self):
        return self.parent_supermode.stylized_label

    def slice_to_itr(self, slice: list = []):
        return self.parent_supermode.parent_set.slice_to_itr(slice)

    def itr_to_slice(self, itr: list = []):
        return self.parent_supermode.parent_set.itr_to_slice(itr)

    def _interpret_itr_slice_list_(self, *args, **kwargs):
        return self.parent_supermode.parent_set._interpret_itr_slice_list_(*args, **kwargs)

    def add_symmetry_to_vector(self, *args, **kwargs):
        return self.parent_supermode.add_symmetry_to_vector(*args, **kwargs)

    def get_axis_vector(self, *args, **kwargs):
        return self.parent_supermode.get_axis_vector(*args, **kwargs)


class NameSpace():
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class Field(InheritFromSuperMode):
    def __init__(self, parent_supermode):
        self.parent_supermode = parent_supermode
        self._data = self.parent_supermode.binded_supermode.get_fields()
        self.plot_style = plot_style.field

    def get_value_from_itr(self, itr: float, add_symmetries: bool = True):
        slice_number = self.itr_to_slice(itr)
        if add_symmetries:
            _, _, mesh = self.apply_boundary_symmetries(mesh=self._data[slice_number])
        else:
            _, _, mesh = self.axes.x_mesh, self.axes.y_mesh, self._data[slice_number]

        return mesh

    def get_field_with_boundaries(self, slice: int):
        return self.apply_boundary_symmetries(mesh=self._data[slice])

    def apply_boundary_symmetries(self, mesh: numpy.ndarray) -> tuple:
        x_axis, y_axis = self.get_axis_vector(add_symmetries=True)

        mesh = self.add_boundaries_to_mesh(mesh=mesh)

        return x_axis, y_axis, mesh

    def add_boundaries_to_mesh(self, mesh: numpy.ndarray) -> numpy.ndarray:
        """
        Return mode field taking account of the boundaries of the solver

        """
        match self.boundaries.left:
            case 'symmetric': mesh = numpy.c_[mesh[:, ::-1], mesh]

            case 'anti-symmetric': mesh = numpy.c_[-mesh[:, ::-1], mesh]

        match self.boundaries.right:
            case 'symmetric': mesh = numpy.c_[mesh, mesh[:, ::-1]]

            case 'anti-symmetric': mesh = numpy.c_[mesh, -mesh[:, ::-1]]

        match self.boundaries.top:
            case 'symmetric': mesh = mesh = numpy.r_[mesh, mesh[::-1, :]]

            case 'anti-symmetric': mesh = numpy.r_[mesh, -mesh[::-1, :]]

        match self.boundaries.bottom:
            case 'symmetric': mesh = numpy.r_[mesh[::-1, :], mesh]

            case 'anti-symmetric': mesh = numpy.r_[-mesh[::-1, :], mesh]

        return mesh

    def _render_on_ax_(self, ax, slice):
        self._set_axis_(ax)

        ax.colorbar = ColorBar(symmetric=True, position='right')

        x, y, field = self.apply_boundary_symmetries(mesh=self._data[slice])

        artist = Mesh(x=x, y=y, scalar=field, colormap=colormaps.blue_black_red)

        ax.add_artist(artist)

    def plot(self, slice_list: list = [0, -1], itr_list: list = []) -> Scene2D:
        """
        Plotting method for the fields.

        :param      slice_list:  Value reprenting the slice where the mode field is evaluated.
        :type       slice_list:  list
        :param      itr_list:    Value of itr value to evaluate the mode field.
        :type       itr_list:    list

        :returns:   the figure containing all the plots.
        :rtype:     Scene2D
        """
        figure = Scene2D(unit_size=(3, 3), tight_layout=True)

        slice_list, itr_list = self._interpret_itr_slice_list_(slice_list, itr_list)

        for n, (slice, itr) in enumerate(zip(slice_list, itr_list)):
            ax = Axis(
                row=n,
                col=0,
                title=f'{self.parent_supermode.stylized_label}\n[slice: {slice}  ITR: {itr:.4f}]'
            )

            self._render_on_ax_(ax=ax, slice=slice)
            figure.add_axes(ax)

        return figure


class EigenValue(InheritFromSuperMode):
    def __init__(self, parent_supermode):
        self.parent_supermode = parent_supermode
        self._data = self.parent_supermode.binded_supermode.get_eigen_value()
        self.plot_style = plot_style.eigen_value

    def get_values(self):
        return self._data

    def _render_on_ax_(self, ax: Axis):
        self._set_axis_(ax)
        artist = Line(x=self.itr_list, y=self._data, label=self.stylized_label)
        ax.add_artist(artist)

    def plot(self, row: int = 0, col: int = 0) -> None:
        """
        Plotting method for the index.

        :param      slice_list:  Value reprenting the slice where the mode field is evaluated.
        :type       slice_list:  list
        :param      itr_list:    Value of itr value to evaluate the mode field.
        :type       itr_list:    list

        :returns:   the figure containing all the plots.
        :rtype:     Scene2D
        """
        figure = Scene2D(unit_size=(10, 4), tight_layout=True)

        ax = Axis(row=0, col=0)

        figure.add_axes(ax)

        self._render_on_ax_(ax)

        return figure


class Index(InheritFromSuperMode):
    def __init__(self, parent_supermode):
        self.parent_supermode = parent_supermode
        self._data = self.parent_supermode.binded_supermode.get_index()
        self.plot_style = plot_style.index

    def get_values(self):
        return self._data

    def _render_on_ax_(self, ax: Axis):
        self._set_axis_(ax)
        artist = Line(x=self.itr_list, y=self._data, label=self.stylized_label)
        ax.add_artist(artist)

    def plot(self, row: int = 0, col: int = 0) -> None:
        """
        Plotting method for the index.

        :param      slice_list:  Value reprenting the slice where the mode field is evaluated.
        :type       slice_list:  list
        :param      itr_list:    Value of itr value to evaluate the mode field.
        :type       itr_list:    list

        :returns:   the figure containing all the plots.
        :rtype:     Scene2D
        """
        figure = Scene2D(unit_size=(10, 4), tight_layout=True)

        ax = Axis(row=0, col=0)

        figure.add_axes(ax)

        self._render_on_ax_(ax)

        return figure


class Beta(InheritFromSuperMode):
    def __init__(self, parent_supermode):
        self.parent_supermode = parent_supermode
        self._data = self.parent_supermode.binded_supermode.get_betas()
        self.plot_style = plot_style.beta

    def get_values(self) -> numpy.ndarray:
        return self._data

    def _render_on_ax_(self, ax: Axis):
        self._set_axis_(ax)
        artist = Line(x=self.itr_list, y=self._data, label=self.stylized_label)
        ax.add_artist(artist)

    def plot(self, row: int = 0, col: int = 0) -> None:
        """
        Plotting method for the index.

        :param      slice_list:  Value reprenting the slice where the mode field is evaluated.
        :type       slice_list:  list
        :param      itr_list:    Value of itr value to evaluate the mode field.
        :type       itr_list:    list

        :returns:   the figure containing all the plots.
        :rtype:     Scene2D
        """
        figure = Scene2D(unit_size=(10, 4), tight_layout=True)

        ax = Axis(row=0, col=0)

        figure.add_axes(ax)

        self._render_on_ax_(ax)

        return figure


class BaseMultiModePlot():

    def _render_on_ax_(self, ax: Axis, other_supermode: 'SuperMode' = None):
        if other_supermode is None:
            other_supermode = self.parent_supermode.parent_set.supermodes

        self._set_axis_(ax)
        for mode in other_supermode:
            if mode.ID == self.ID or mode.solver_number != self.solver_number:
                continue

            artist = Line(
                x=self.itr_list,
                y=self.get_values(mode),
                label=f'{self.stylized_label} - {mode.stylized_label}'
            )

            ax.add_artist(artist)

    def plot(self, other_supermode: 'SuperMode' = None, row: int = 0, col: int = 0) -> None:
        """
        Plotting method for the index.

        :param      slice_list:  Value reprenting the slice where the mode field is evaluated.
        :type       slice_list:  list
        :param      itr_list:    Value of itr value to evaluate the mode field.
        :type       itr_list:    list

        :returns:   the figure containing all the plots.
        :rtype:     Scene2D
        """
        figure = Scene2D(unit_size=(10, 4), tight_layout=True)
        ax = Axis(row=row, col=col)
        figure.add_axes(ax)

        self._render_on_ax_(ax=ax, other_supermode=other_supermode)

        return figure


class Overlap(InheritFromSuperMode, BaseMultiModePlot):
    def __init__(self, parent_supermode):
        self.parent_supermode = parent_supermode
        self.plot_style = plot_style.overlap

    def get_values(self, other_supermode: 'SuperMode') -> numpy.ndarray:
        """
        Return the array of the modal coupling for the mode
        """
        return self.parent_supermode.binded_supermode.get_overlap_with_mode(other_supermode.binded_supermode)


class NormalizedCoupling(InheritFromSuperMode, BaseMultiModePlot):
    def __init__(self, parent_supermode):
        self.parent_supermode = parent_supermode
        self.plot_style = plot_style.normalized_coupling

    def get_values(self, other_supermode: 'SuperMode') -> numpy.ndarray:
        """
        Return the array of the modal coupling for the mode
        """

        output = self.parent_supermode.binded_supermode.get_normalized_coupling_with_mode(other_supermode.binded_supermode)

        if not self.parent_supermode.is_computation_compatible(other_supermode):
            output *= 0

        return output


class BeatingLength(InheritFromSuperMode, BaseMultiModePlot):
    def __init__(self, parent_supermode):
        self.parent_supermode = parent_supermode
        self.plot_style = plot_style.beating_length

    def get_values(self, other_supermode: 'SuperMode') -> numpy.ndarray:
        """
        Return the array of the modal coupling for the mode
        """
        return self.parent_supermode.binded_supermode.get_beating_length_with_mode(other_supermode.binded_supermode)


class Adiabatic(InheritFromSuperMode, BaseMultiModePlot):
    def __init__(self, parent_supermode):
        self.parent_supermode = parent_supermode
        self.plot_style = plot_style.adiabatic

    def get_values(self, other_supermode: 'SuperMode') -> numpy.ndarray:
        """
        Return the array of the modal coupling for the mode
        """
        output = self.parent_supermode.binded_supermode.get_adiabatic_with_mode(other_supermode.binded_supermode)

        if not self.parent_supermode.is_computation_compatible(other_supermode):
            output *= numpy.inf

        return output
# -
