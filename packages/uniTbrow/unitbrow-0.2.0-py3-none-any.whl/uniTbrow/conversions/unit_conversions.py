from uniTbrow.units import to_base_units
from .base_unit_systems import si, cgs


def to_si_units(expr):
    return si.convert(expr)


def to_cgs_units(expr):
    return cgs.convert(expr)


def convert(expr, new_units):
    return to_base_units(expr/new_units) * new_units
