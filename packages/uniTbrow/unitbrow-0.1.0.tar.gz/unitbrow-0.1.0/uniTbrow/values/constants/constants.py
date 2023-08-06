from uniTbrow.values.units.units import metre, second, newton, kelvin, joule, mole, ampere, gram, hertz, coulomb
from sympy import pi

c = 299792458 * metre * second**-1
"""Speed of light in vacuum"""

G = 6.6743015*10**-11 * metre**3 * (1000*gram)**-1 * second**-2
"""Newtonian gravitational constant"""

h = 6.62607015*10**-34 * joule * hertz**-1
"""Planck constant"""

h_bar = h/(2*pi)
"""Reduced Planck constant"""

mu_0 = 1.2566370621219*10**-6 * newton * ampere**-2
"""Vacuum magnetic permeability"""

epsilon_0 = 1/(mu_0*c**2)
"""Vacuum electric permittivity"""

k_e = 1/(4*pi*epsilon_0)
"""Coulomb constant"""

k_b = 1.380649*10**-23 * joule * kelvin**-1
"""Boltzmann constant"""

sigma_sb = pi**2*k_b**4 / (60 * h_bar**3 * c**2)
"""Stefan-Boltzmann constant"""

e = 1.602176634*10**-19 * coulomb
"""Elementary charge"""

N_A = 6.02214076*10**23 * mole**-1
"""Avogadro constant"""

R = N_A * k_b
"""Molar gas constant"""

m_e = 9.109383701528*10**-31 * 1000*gram
"""Electron mass"""

m_p = 1.6726219236951*10**-27 * 1000*gram
"""Proton mass"""

m_n = 1.6749274980495*10**-27 * 1000*gram
"""Neutron mass"""
