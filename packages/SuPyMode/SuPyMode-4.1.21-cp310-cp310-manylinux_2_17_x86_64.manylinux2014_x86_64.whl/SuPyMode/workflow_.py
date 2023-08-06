
from dataclasses import dataclass

from FiberFusing import Geometry, BackGround
import FiberFusing
from SuPyMode.solver import SuPySolver
import FiberFusing.fiber_catalogue as fiber_catalogue

from PyFinitDiff.boundaries import Boundaries2D


@dataclass
class Workflow():
    fiber_list: list
    """ List of the fiber to add to the optical structure """
    wavelength: float
    """ Wavelenght at which evaluate the computation """
    additional_structure: list = ()
    """ Additional optical structure such as clad to add """
    resolution: int = 100
    """ Discretization of the mesh [resolution x resolution] """
    n_sorted_mode: int = 4
    """ Number of mode that are computed """
    added_computed_modes: int = 4
    """ Number of mode that are computed additionally to the sorted modes """
    fiber_radius: float = 62.5e-6
    """ Fiber radius for the clad fused structure """
    fusion_degree: float = 0.85
    """ Fusion degree for the clad fused structure """
    final_itr: float = 0.05
    """ Final ITR at which evaluate the modes """
    start_itr: float = 1.0
    """ Start ITR at which evaluate the modes """
    n_step: int = 500
    """ Discretization of the z-profile """
    core_position_scrambling: float = 0
    """ Scramblgin of the clad core position """
    plot_geometry: bool = False
    """ Plot the computed geometry mesh prior computation """
    plot_cladding: bool = False
    """ Plot the cladding structure prior computation """
    plot_field: bool = False
    """ Plot the mode field after computation """
    plot_adiabatic: bool = False
    """ Plot the adiabatic criterion after computation """
    boundaries: list = (Boundaries2D(),)
    """ List of boundaries cndition to which evaluate to modes """
    x_bounds: str = 'centering'
    """ X-boundaries """
    y_bounds: str = 'centering'
    """ Y-boundaries """

    def __post_init__(self):
        self.initialize_optical_structure()

        self.initialize_geometry()

        self.initialize_solver()

    def get_structure_class(self):
        match len(self.fiber_list):
            case 1:
                return FiberFusing.Fused1
            case 2:
                return FiberFusing.Fused2
            case 3:
                return FiberFusing.Fused3
            case 4:
                return FiberFusing.Fused4

        raise ValueError('Number of fibers do not correspond to any predefined structure.')

    def initialize_optical_structure(self):

        clad_structure_class = self.get_structure_class()

        silica_index = fiber_catalogue.get_silica_index(wavelength=self.wavelength)

        self.clad_structure = clad_structure_class(
            fiber_radius=self.fiber_radius,
            index=silica_index,
            core_position_scrambling=0
        )

        for n, fiber in enumerate(self.fiber_list):
            fiber.set_position(self.clad_structure.cores[n])

        if self.plot_cladding:
            self.clad_structure.plot().show()

    def initialize_geometry(self):
        self.geometry = Geometry(
            background=BackGround(index=1),
            structures=[self.clad_structure],
            x_bounds=self.x_bounds,
            y_bounds=self.y_bounds,
            n=self.resolution,
            index_scrambling=0,
            gaussian_filter=None,
            boundary_pad_factor=1.1
        )

        self.geometry.add_fiber(*self.fiber_list)

        if self.plot_geometry:
            self.geometry.plot().show()

    def initialize_solver(self):
        self.solver = SuPySolver(
            geometry=self.geometry,
            tolerance=1e-5,
            max_iter=1000,
            show_iteration=True,
            accuracy=2,
            show_eigenvalues=False,
            extrapolation_order=1
        )

        self.solver.init_superset(
            wavelength=self.wavelength,
            n_step=self.n_step,
            itr_i=self.start_itr,
            itr_f=self.final_itr
        )

        for boundary in self.boundaries:
            self.solver.add_modes(
                n_computed_mode=self.n_sorted_mode + self.added_computed_modes,
                n_sorted_mode=self.n_sorted_mode,
                boundaries=boundary
            )

        self.solver.superset.sorting_modes('beta')

        if self.plot_field:
            self.solver.superset.plot(
                plot_type='field',
                slice_list=[0, -1]
            ).show()

        if self.plot_adiabatic:
            self.solver.superset.plot(plot_type='adiabatic').show()

    def get_auto_name(self):
        fiber_name = "".join(fiber.__class__.__name__ for fiber in self.fiber_list)

        filename = (
            f"structure_{self.clad_structure.__name__}"
            f"{fiber_name}"
            f"resolution_{self.resolution}"
            f'wavelength_{self.wavelength}'
        )

        return filename

    def save_superset(self, filename: str = 'auto', directory: str = 'auto'):
        if filename == 'auto':
            filename = self.get_auto_name()

        self.solver.superset.save_instance(
            filename=filename,
            directory=directory
        )

    def generate_report(self, filename: str = 'auto', directory: str = 'auto'):
        if filename == 'auto':
            filename = self.get_auto_name()

        self.solver.superset.generate_report(
            filename=filename + ".pdf",
            directory=directory,
        )


# -
