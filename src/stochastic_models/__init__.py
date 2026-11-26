"""Reusable code for Stochastic Models with Applications.

Notebooks should import functions from this package instead of copying
implementations between notebooks. Simulation and pricing routines will be
added in the modules below; this package currently provides structure only.

Modules
-------
poisson
    Poisson process simulation and numerical checks.
brownian
    Standard Brownian motion simulation and numerical checks.
gbm
    Geometric Brownian motion.
jump_diffusion
    Jump-diffusion process simulation.
options
    Option payoffs and Monte Carlo pricing helpers.
utils
    Shared helpers such as random generators and output paths.
"""

__all__ = [
    "brownian",
    "gbm",
    "jump_diffusion",
    "options",
    "poisson",
    "utils",
]
