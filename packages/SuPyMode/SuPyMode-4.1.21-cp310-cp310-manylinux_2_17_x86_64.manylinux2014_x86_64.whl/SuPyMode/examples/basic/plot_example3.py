"""
2x2 Coupler
===========
"""

# %%
# Importing the package dependencies: FiberFusing, PyFinitDiff
from FiberFusing import Geometry, Fused3, BackGround
from FiberFusing.fiber_catalogue import DCF1300S_33
from PyFinitDiff.boundaries import Boundaries2D
from SuPyMode.solver import SuPySolver
from SuPyMode.profiles import AlphaProfile


# %%
# Generating the fiber structure
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Here we make use of the FiberFusing to generate a fiber structure that we use
# as the cladding. The refractive index of the strcture is defined using PyOptik.
wavelength = 1.55e-6

index = 1.4444

air = BackGround(index=1)

clad = Fused3(fiber_radius=62.5e-6, fusion_degree=0.99, index=index)

_ = clad.plot().show()

# %%
# Creating the geometry rasterization
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The cladding being defined we create the cores that are distributed at
# each (virtual) center of the cladding.
# All the components: air -- cladding -- cores, are inputed into a geometry class
# that will generate the mesh which will be used in the finit-difference matrix.
fibers = [
    DCF1300S_33(wavelength=wavelength, position=core) for core in clad.cores
]

geometry = Geometry(
    background=air,
    additional_structure_list=[clad],
    x_bounds='centering',
    y_bounds='centering',
    n=40,
    index_scrambling=1e-6,
    gaussian_filter=0.1
)

geometry.add_fiber(*fibers)

_ = geometry.plot().show()

# %%
# We here create the solver class and generate the superset which
# will contains the supermodes to be computed.
solver = SuPySolver(
    geometry=geometry,
    tolerance=1e-8,
    max_iter=10000,
    show_iteration=True  # Put this to True to see the computing progression
)

solver.init_superset(
    wavelength=wavelength,
    n_step=500,
    itr_i=1.0,
    itr_f=0.05
)


# %%
# We now add supermodes for different type of attributes such as symmetries.
# By default the solver assume no symmetries in the system.
_ = solver.add_modes(
    boundaries=Boundaries2D(),
    n_computed_mode=8,
    n_sorted_mode=4
)

# %%
# The modes are now computed [can take a few minutes], the modes are concatenated
# in a superset class that we can access with the get_set() function. This class
# can be used to analyse the data
superset = solver.get_set()

# %%
# Generating the z-profile of the coupler
profile = AlphaProfile(
    initial_radius=62.5e-6,
    label='test profile'
)

profile.add_taper_segment(
    alpha=0,
    stretching_length=315 * 0.02 * 1e-3,
    initial_heating_length=3 * 1e-3,
)

profile.add_taper_segment(
    alpha=0.2,
    stretching_length=2020 * 0.02 * 1e-3,
    initial_heating_length=10 * 1e-3
)

profile.initialize()

profile.plot().show()


# %%
# Field computation: :math:`E_{i,j}`
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
_ = superset.plot(plot_type='field', itr_list=[1.0, 0.05]).show()

# %%
# After mode visualization we can name them for an easier further analyze.
# This step is, however, not mandatory.
_ = superset.label_supermodes('LP01', 'LP11_v', 'LP21', 'LP11_h')

# %%
# Effective index: :math:`n^{eff}_{i,j}`
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
_ = superset.plot(plot_type='index').show()

# %%
# Modal normalized coupling: :math:`C_{i,j}`
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
_ = superset.plot(plot_type='normalized-coupling', mode_selection='pairs').show()

# %%
# Adiabatic criterion: :math:`\tilde{C}_{i,j}`
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
_ = superset.plot(plot_type='adiabatic', mode_selection='pairs', add_profile=profile).show()
