from uniTbrow.values.units.units import library
from uniTbrow.values.dimensions.dimensions import mass


def to_base_units(expr):
    changes = -1
    while changes != 0:
        changes = 0
        for unit in expr.free_symbols:
            try:
                true_unit = library.lookup(unit)
                if true_unit.base is True:
                    continue
                changes += 1
                expr = expr.subs(unit, true_unit.base)
            except KeyError:
                continue
    return expr


def to_si_units(expr):
    # Convert to our internal base units
    expr = to_base_units(expr)
    # Then convert grams to kilograms
    for unit in expr.free_symbols:
        try:
            true_unit = library.lookup(unit)
            if true_unit.dimension == mass:
                expr = expr.subs(unit, true_unit.conversions[library.lookup("kg")])
        except KeyError:
            continue
    return expr


def convert(expr, new_units):
    return to_base_units(expr/new_units) * new_units
