import unit as u
from sympy import parse_expr, pi
from sympy.parsing.sympy_parser import T


unit_dictionary = u.unit_dictionary


def units(unit_string):
    return parse_expr(unit_string, transformations=T[:], local_dict=u.unit_dictionary)


def to_base_units(expr):
    changes = -1
    while changes != 0:
        changes = 0
        for unit in expr.free_symbols:
            try:
                true_unit = u.reverse_unit_dictionary[unit]
                # print("\t", unit, "==", repr(true_unit), "->", str(true_unit.base_conversion))
                if true_unit.base:
                    continue
                changes += 1
                expr = expr.subs(unit, true_unit.base_conversion)
            except KeyError:
                continue
    return expr


def to_si_units(expr):
    # Convert to our internal base units
    expr = to_base_units(expr)
    # Then convert grams to kilograms
    for unit in expr.free_symbols:
        try:
            true_unit = u.reverse_unit_dictionary[unit]
            if true_unit.dimension == u.mass:
                expr = expr.subs(unit, true_unit.conversions[u.parse_unit("kg")])
        except KeyError:
            continue
    return expr


def remove_units(expr):
    expr = to_base_units(expr)
    for unit in expr.free_symbols:
        if unit in u.reverse_unit_dictionary.keys():
            expr = expr.subs(unit, 1)

    return expr


def to_units(expr, units_expr):
    return to_base_units(expr/units_expr) * units_expr


c = 299792458*units("m * s**-1")
"""Speed of light in vacuum"""

G = 6.6743015*10**-11 * units("m**3 * kg**-1 * s**-2")
"""Newtonian gravitational constant"""

h = 6.62607015*10**-34 * units("J*Hz**-1")
"""Planck constant"""

h_bar = h/(2*pi)
"""Reduced Planck constant"""

mu_0 = 1.2566370621219*10**-6 * units("N*A**-2")
"""Vacuum magnetic permeability"""

epsilon_0 = 1/(mu_0*c**2)
"""Vacuum electric permittivity"""

k_e = 1/(4*pi*epsilon_0)
"""Coulomb constant"""

k_b = 1.380649*10**-23 * units("J*K**-1")
"""Boltzmann constant"""

sigma_sb = pi**2*k_b**4 / (60 * h_bar**3 * c**2)
"""Stefan-Boltzmann constant"""

e = 1.602176634*10**-19 * units("C")
"""Elementary charge"""

N_A = 6.02214076*10**23 * units("mol**-1")
"""Avogadro constant"""

R = N_A * k_b
"""Molar gas constant"""

m_e = 9.109383701528*10**-31 * units("kg")
"""Electron mass"""

m_p = 1.6726219236951*10**-27 * units("kg")
"""Proton mass"""

m_n = 1.6749274980495*10**-27 * units("kg")
"""Neutron mass"""
