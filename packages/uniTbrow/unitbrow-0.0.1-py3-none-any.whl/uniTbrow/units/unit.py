from sympy import symbols, pi


class Dimension:
    def __init__(self, name, dimension=None):
        if dimension is None:
            self.name = name
            self.dimension = symbols(name)
        else:
            self.name = name
            self.dimension = dimension


metric_prefixes = [
    ("Q", ["quetta"], 10**30),
    ("R", ["ronna"], 10**27),
    ("Y", ["yotta"], 10**24),
    ("Z", ["zetta"], 10**21),
    ("E", ["exa"], 10**18),
    ("P", ["peta"], 10**15),
    ("T", ["tera"], 10**12),
    ("G", ["giga"], 10**9),
    ("M", ["mega"], 10**6),
    ("k", ["kilo"], 10**3),
    ("h", ["hecto"], 10**2),
    ("da", ["deka"], 10**1),
    ("d", ["deci"], 10**-1),
    ("c", ["centi"], 10**-2),
    ("m", ["milli"], 10**-3),
    ("μ", ["micro"], 10**-6),
    ("n", ["nano"], 10**-9),
    ("p", ["pico"], 10**-12),
    ("f", ["femto"], 10**-15),
    ("a", ["atto"], 10**-18),
    ("z", ["zepto"], 10**-21),
    ("y", ["yocto"], 10**-24),
    ("r", ["ronto"], 10**-27),
    ("q", ["quecto"], 10**-30)
]


class Unit:
    def __init__(self, dimension: Dimension, abbr_symbol: str, alternates: list, metric=True, base=True, base_conversion=None):
        assert base or (base_conversion is not None), "Need to provide a conversion to a base unit"
        self.dimension: Dimension = dimension
        self.symbol = symbols(abbr_symbol)
        self.alternates: list = alternates
        self.conversions: dict = dict()
        self.metric: bool = metric
        self.base: bool = base
        self.base_conversion = base_conversion

    # add_conversion defines the factor used to convert from other_unit to this unit
    def add_conversion(self, other_unit, expr):
        assert other_unit.dimension == self.dimension, "Dimension mismatch between " +\
                                                       self.dimension.dimension +\
                                                       " and " + other_unit.dimension.dimension
        self.conversions[other_unit] = expr

    def generate_metric_prefixes(self):
        if not self.metric:
            return []
        metric_units = []
        for abbr, alts, factor in metric_prefixes:
            alternates = []
            for prefix in alts:
                for suffix in self.alternates:
                    alternates.append(str(prefix+suffix))

            new_unit = Unit(self.dimension, abbr+str(self.symbol), alternates, metric=False, base=False, base_conversion=factor*self.symbol)
            new_unit.add_conversion(self, factor*self.symbol)
            self.add_conversion(new_unit, (1/factor)*new_unit.symbol)
            metric_units.append(new_unit)

        return metric_units

    def __repr__(self):
        return str(self.symbol)+"["+str(self.dimension.dimension)+"]"

    def __str__(self):
        string_to_return = str(self.symbol)
        string_to_return += "[" + str(self.dimension.dimension) + "]"
        if len(self.alternates) >= 1:
            string_to_return += "\t" + str(len(self.alternates)) + " alternate spellings"
            string_to_return += " (e.g. " + str(self.alternates[0]) + ")"
        return string_to_return


length = Dimension("length")
time = Dimension("time")
amount = Dimension("amount")
current = Dimension("current")
temperature = Dimension("temperature")
luminous_intensity = Dimension("luminous_intensity")
mass = Dimension("mass")

# Base Units
metre = Unit(length, "m", ["meter", "metre", "meters", "metres"])
second = Unit(time, "s", ["second", "seconds", "sec", "secs"])
mole = Unit(amount, "mole", ["mol", "moles"])
ampere = Unit(current, "A", ["ampere", "amps", "amperes", "amp"])
kelvin = Unit(temperature, "K", ["kelvin"])
candela = Unit(luminous_intensity, "cd", ["candela"])
gram = Unit(mass, "g", ["gram", "grams"])

# Derived Units
frequency = Dimension("frequency", time.dimension**-1)
hertz = Unit(frequency, "Hz", ["hertz"], base=False, base_conversion=(1/second.symbol))
angle = Dimension("angle", length.dimension/length.dimension)
radian = Unit(angle, "rad", ["radians", "radian"], base=False, base_conversion=1)
solid_angle = Dimension("solid_angle", (length.dimension**2)/(length.dimension**2))
steradian = Unit(solid_angle, "sr", ["steradians", "steradian"], base=False, base_conversion=1)
force = Dimension("force", mass.dimension*length.dimension/(time.dimension**2))
newton = Unit(force, "N", ["newtons", "newton"], base=False, base_conversion=(1000*gram.symbol*metre.symbol/(second.symbol**2)))
pressure = Dimension("pressure", force.dimension*length.dimension**-2)
pascal = Unit(pressure, "Pa", ["pascals", "pascal"], base=False, base_conversion=(1000*gram.symbol * metre.symbol**-1 * second.symbol**-2))
energy = Dimension("energy", force.dimension*length.dimension)
joule = Unit(energy, "J", ["joule", "joules"], base=False, base_conversion=(1000*gram.symbol * metre.symbol**2 * second.symbol**-2))
power = Dimension("power", energy.dimension / time.dimension)
watt = Unit(power, "W", ["watt", "watts"], base=False, base_conversion=(1000*gram.symbol * metre.symbol**2 * second.symbol**-3))
charge = Dimension("charge", time.dimension * current.dimension)
coulomb = Unit(charge, "C", ["coulombs", "coulomb"], base=False, base_conversion=(second.symbol * ampere.symbol))
electric_potential = Dimension("electric_potential", power.dimension / current.dimension)
volt = Unit(electric_potential, "V", ["volts", "volt"], base=False, base_conversion=(1000*gram.symbol * metre.symbol**2 * second.symbol**-3 * ampere.symbol**-1))
capacitance = Dimension("capacitance", charge.dimension / electric_potential.dimension)
farad = Unit(capacitance, "F", ["farads", "farad"], base=False, base_conversion=((1000*gram.symbol)**-1 * metre.symbol**-2 * second.symbol**4 * ampere.symbol**2))
resistance = Dimension("resistance", electric_potential.dimension / current.dimension)
ohm = Unit(resistance, "Ω", ["ohms", "ohm"], base=False, base_conversion=(1000*gram.symbol * metre.symbol**2 * second.symbol**-3 * ampere.symbol**-2))
conductance = Dimension("conductance", 1 / resistance.dimension)
siemens = Unit(conductance, "S", ["siemens", "siemen", "mho", "mhos"], base=False, base_conversion=((1000*gram.symbol)**-1 * metre.symbol**-2 * second.symbol**3 * ampere.symbol**2))
magnetic_flux = Dimension("magnetic_flux", energy.dimension / current.dimension)
weber = Unit(magnetic_flux, "Wb", ["weber", "webers"], base=False, base_conversion=(1000*gram.symbol * metre.symbol**2 * second.symbol**-2 * ampere.symbol**-1))
magnetic_induction = Dimension("magnetic_induction", magnetic_flux.dimension * length.dimension**-2)
tesla = Unit(magnetic_induction, "T", ["tesla", "teslas"], base=False, base_conversion=(1000*gram.symbol * second.symbol**-2 * ampere.symbol**-1))
electric_inductance = Dimension("electric_inductance", resistance.dimension * time.dimension)
henry = Unit(electric_inductance, "H", ["henry", "henrys"], base=False, base_conversion=(1000*gram.symbol * metre.symbol**2 * second.symbol**-2 * ampere.symbol**-2))

# Astronomical Units
mass_sun = Unit(mass, "M_⊙", ["solar_mass", "solar_masses", "M_sun"], metric=False, base=False, base_conversion=(1.98847*10**33 * gram.symbol))
parsec = Unit(length, "pc", ["parsec", "parsecs"], base=False, base_conversion=(3.0856775814913*10**16*metre.symbol))
astronomical_unit = Unit(length, "AU", ["au", "astronomical_units", "astronomical_unit"], metric=False, base=False, base_conversion=(1.495978707*10**11*metre.symbol))
lightyear = Unit(length, "ly", ["lightyear", "lyr", "lyrs", "lightyears", "light_year", "light_years"], base=False, base_conversion=(9460730472580800*metre.symbol))
solar_luminosity = Unit(power, "L_⊙", ["L_sun", "solar_luminosity", "solar_luminosities"], metric=False, base=False, base_conversion=(3.828*10**26*watt.base_conversion))

# Additional length units
fermi = Unit(length, "fermi", ["fermis"], base=False, base_conversion=(10**-15*metre.symbol))
angstrom = Unit(length, "Å", ["angstrom", "angstroms"], metric=False, base=False, base_conversion=(100*10**-12*metre.symbol))
micron = Unit(length, "micron", ["microns"], metric=False, base=False, base_conversion=(10**-6*metre.symbol))
yard = Unit(length, "yd", ["yards", "yds", "yard"], metric=False, base=False, base_conversion=(0.9144*metre.symbol))
foot = Unit(length, "ft", ["feet", "foot"], metric=False, base=False, base_conversion=(yard.base_conversion/3))
inch = Unit(length, "in", ["inch", "inches"], metric=False, base=False, base_conversion=(foot.base_conversion/12))
mile = Unit(length, "mile", ["miles"], metric=False, base=False, base_conversion=(foot.base_conversion*5280))
fathom = Unit(length, "fathom", ["fathoms"], metric=False, base=False, base_conversion=(6 * foot.base_conversion))
nautical_mile = Unit(length, "nmi", ["NM", "M", "nautical_mile", "nautical_miles"], metric=False, base=False, base_conversion=(1852*metre.symbol))
furlong = Unit(length, "furlong", ["furlongs"], metric=False, base=False, base_conversion=(220*yard.base_conversion))

# Additional time units
minute = Unit(time, "min", ["mins", "minutes", "minute"], metric=False, base=False, base_conversion=(60*second.symbol))
hour = Unit(time, "hr", ["hrs", "hours", "hour"], metric=False, base=False, base_conversion=(3600*second.symbol))
day = Unit(time, "day", ["days"], metric=False, base=False, base_conversion=(86400*second.symbol))
week = Unit(time, "week", ["weeks"], metric=False, base=False, base_conversion=(7*86400*second.symbol))
year = Unit(time, "yr", ["year", "years", "yrs"], base=False, base_conversion=(86400*365.25*second.symbol))

# Additional temperature units
# TODO celsius = Unit(temperature, "°C", ["degrees_celsius", "°celsius", "celsius"], base=False, base_conversion=(1 + 273.15 * kelvin.symbol))
# TODO fahrenheit = Unit(temperature, "°F", ["degrees_fahrenheit", "°fahrenheit", "fahrenheit"], base=False, base_conversion=(1))
rankine = Unit(temperature, "°R", ["rankine", "degrees_rankine", "°rankine"], base=False, base_conversion=((5/9)*kelvin.symbol))

# Additional luminosity units
luminous_flux = Dimension("luminous_flux", luminous_intensity.dimension * solid_angle.dimension)
lumen = Unit(luminous_flux, "lm", ["lumen", "lumens"], base=False, base_conversion=(candela.symbol * steradian.symbol))
illuminance = Dimension("illuminance", luminous_flux.dimension * length.dimension**-2)
lux = Unit(illuminance, "lx", ["lux"], metric=False, base=False, base_conversion=(candela.symbol * steradian.symbol * metre.symbol**-2))
foot_candle = Unit(illuminance, "fc", ["foot_candle", "ft_c"], metric=False, base=False, base_conversion=(lumen.base_conversion * foot.base_conversion**-2))
phot = Unit(illuminance, "ph", ["phot", "phots"], metric=False, base=False, base_conversion=(10000 * lux.base_conversion))

# Additional mass units
tonne = Unit(mass, "t", ["tonne", "tonnes", "metric_ton", "metric_tons"], metric=False, base=False, base_conversion=(1000000*gram.symbol))
dalton = Unit(mass, "Da", ["u", "dalton", "daltons"], base=False, base_conversion=(1.6604390666050*10**-24*gram.symbol))
slug = Unit(mass, "sl", ["slug", "slugs"], metric=False, base=False, base_conversion=(14593.90*gram.symbol))
pound = Unit(mass, "lb", ["lbs", "pound", "pounds"], metric=False, base=False, base_conversion=(453.59237*gram.symbol))
ounce = Unit(mass, "oz", ["ounce", "ounces"], metric=False, base=False, base_conversion=(pound.base_conversion/16))
ton = Unit(mass, "tons", ["ton", "short_ton", "short_tons"], metric=False, base=False, base_conversion=(2000*pound.base_conversion))
long_ton = Unit(mass, "long_tons", ["long_ton", "imperial_ton", "imperial_tons", "displacement_ton", "displacement_tons"], metric=False, base=False, base_conversion=(2240*pound.base_conversion))
carat = Unit(mass, "ct", ["carat", "carats"], base=False, base_conversion=(0.2*gram.symbol))
imperial_carat = Unit(mass, "imp_ct", ["imp_carat", "imp_carats", "imperial_carat", "imperial_carats"], metric=False, base=False, base_conversion=(0.00705*ounce.base_conversion))

# Additional force units
pound_force = Unit(force, "lbf", ["pound_force, pound_of_force"], metric=False, base=False, base_conversion=(4.4482216152605*newton.base_conversion))
dyne = Unit(force, "dyn", ["dyne", "dynes"], metric=False, base=False, base_conversion=(10**-5*newton.base_conversion))
poundal = Unit(force, "pdl", ["poundal"], metric=False, base=False, base_conversion=(pound.base_conversion * foot.base_conversion * second.symbol**-2))

# Additional energy units
erg = Unit(energy, "erg", ["ergs"], metric=False, base=False, base_conversion=(10**-7*joule.base_conversion))
calorie = Unit(energy, "cal", ["calorie", "calories"], base=False, base_conversion=(4.184*joule.base_conversion))
electron_volt = Unit(energy, "eV", ["electronvolt", "electronvolts", "electron_volt", "electron_volts"], base=False, base_conversion=(1.602176634*10**-19 * joule.base_conversion))

# Additional power units
metric_horsepower = Unit(power, "hp", ["hp_M", "horsepower", "metric_horsepower"], base=False, base_conversion=(735.49875*watt.base_conversion))
mechanical_horsepower = Unit(power, "hp_I", ["mechanical_horsepower", "imperial_horsepower"], metric=False, base=False, base_conversion=(550*foot.base_conversion*pound_force.base_conversion / second.symbol))
electical_horsepower = Unit(power, "hp_E", ["electrical_horsepower"], metric=False, base=False, base_conversion=(746*watt.base_conversion))
boiler_horsepower = Unit(power, "hp_S", ["boiler_horsepower"], metric=False, base=False, base_conversion=(9812.5*watt.base_conversion))

# Additional pressure units
bar = Unit(pressure, "bar", ["bars"], base=False, base_conversion=(100000*pascal.base_conversion))
standard_atmosphere = Unit(pressure, "atm", ["atmosphere", "atmospheres", "standard_atmosphere", "standard_atmospheres"], metric=False, base=False, base_conversion=(101325*pascal.base_conversion))
millimetre_mercury = Unit(pressure, "mmHg", ["mm_Hg"], metric=False, base=False, base_conversion=(133.322*pascal.base_conversion))
inch_mercury = Unit(pressure, "inHg", ["in_Hg"], metric=False, base=False, base_conversion=(3386.389*pascal.base_conversion))
torr = Unit(pressure, "Torr", ["torr"], metric=False, base=False, base_conversion=((101325/760)*pascal.base_conversion))

# Additional angular measurements
degree = Unit(angle, "°", ["deg", "degree", "degrees", "arcdegree", "arcdegrees", "degree_of_arc", "degrees_of_arc", "arc_degree", "arc_degrees"], metric=False, base=False, base_conversion=((pi/180)*radian.base_conversion))
turn = Unit(angle, "tr", ["pla", "turn", "turns"], metric=False, base=False, base_conversion=(2*pi*radian.base_conversion))
gradian = Unit(angle, "gon", ["ᵍ", "grad", "grade", "grads", "grades"], metric=False, base=False, base_conversion=((pi/200)*radian.base_conversion))
square_degree = Unit(solid_angle, "square_deg", ["sq_deg", "square_degree", "square_degrees"], metric=False, base=False, base_conversion=((pi/180)**2 * steradian.base_conversion))
arcminute = Unit(angle, "arcmin", ["arc_minute", "arc_minutes", "arcminute", "arcminutes", "minute_arc", "minutes_arc"], metric=False, base=False, base_conversion=(degree.base_conversion / 60))
arcsecond = Unit(angle, "as", ["arcsec", "asec", "arc_second", "arc_seconds", "arcsecond", "arcseconds", "second_of_arc", "seconds_of_arc"], base=False, base_conversion=(arcminute.base_conversion / 60))


# Additional volume units
volume = Dimension("volume", length.dimension**3)
litre = Unit(volume, "L", ["l", "ℓ", "liter", "litre", "liters", "litres"], base=False, base_conversion=(10**-3 * metre.symbol))
us_gallon = Unit(volume, "US_gal", ["US_gallon", "US_gallons"], metric=False, base=False, base_conversion=(231*inch.base_conversion**3))
us_dry_gallon = Unit(volume, "US_dry_gal", ["US_dry_gallon", "US_dry_gallons"], metric=False, base=False, base_conversion=(268.8025*inch.base_conversion**3))
imperial_gallon = Unit(volume, "imp_gal", ["imperial_gallon", "imp_gallon", "imperial_gallons", "imp_gallons"], metric=False, base=False, base_conversion=(4.54609*litre.base_conversion))
us_quart = Unit(volume, "US_qt", ["US_quart", "US_quarts"], metric=False, base=False, base_conversion=(us_gallon.base_conversion / 4))
us_dry_quart = Unit(volume, "US_dry_qt", ["US_dry_quarts", "US_dry_quart"], metric=False, base=False, base_conversion=(us_dry_gallon.base_conversion / 4))
imperial_quart = Unit(volume, "imp_qt", ["imperial_quart", "imp_quart", "imperial_quarts", "imp_quarts"], metric=False, base=False, base_conversion=(imperial_gallon.base_conversion / 4))
# TODO cup https://en.wikipedia.org/wiki/Cup_(unit)
# TODO tablespoon https://en.wikipedia.org/wiki/Tablespoon
# TODO teaspoon https://en.wikipedia.org/wiki/Teaspoon
us_fluid_ounce = Unit(volume, "US_fl_oz", ["US_fluid_ounce", "US_fluid_ounces"], metric=False, base=False, base_conversion=(us_gallon.base_conversion / 128))
imperial_fluid_ounce = Unit(volume, "imp_fl_oz", ["imp_fluid_ounce", "imp_fluid_ounces", "imperial_fluid_ounce", "imperial_fluid_ounces"], metric=False, base=False, base_conversion=(imperial_gallon.base_conversion / 160))
us_peck = Unit(volume, "US_peck", ["US_pecks"], metric=False, base=False, base_conversion=(2*us_gallon.base_conversion))
imperial_peck = Unit(volume, "imp_peck", ["imp_pecks", "imperial_peck", "imperial_pecks"], metric=False, base=False, base_conversion=(2*imperial_gallon.base_conversion))
us_bushel = Unit(volume, "US_bushel", ["US_bushels", "US_bu", "US_bsh"], metric=False, base=False, base_conversion=(8*us_gallon.base_conversion))
imperial_bushel = Unit(volume, "imp_bushel", ["imp_bushels", "imperial_bushel", "imperial_bushels", "imp_bu", "imp_bsh"], metric=False, base=False, base_conversion=(8*imperial_gallon.base_conversion))

# Additional velocity units
velocity = Dimension("velocity", length.dimension / time.dimension)
mile_per_hour = Unit(velocity, "mph", ["miles_per_hour", "mile_per_hour"], metric=False, base=False, base_conversion=(mile.base_conversion / hour.base_conversion))
knot = Unit(velocity, "kt", ["knots", "kn", "knot"], metric=False, base=False, base_conversion=(1852 * metre.symbol / hour.base_conversion))

# Additional area units
area = Dimension("area", length.dimension**2)
acre = Unit(area, "acre", ["ac", "acres"], metric=False, base=False, base_conversion=(4840 * yard.base_conversion**2))
hectare = Unit(area, "ha", ["hectare", "hectares"], metric=False, base=False, base_conversion=(10**4 * metre.symbol**2))

units = [
    # Base Units
    metre, second, mole, ampere, kelvin, candela, gram,

    # Derived Units
    hertz, radian, steradian, newton, pascal, joule, watt, coulomb, volt, farad, ohm, siemens, weber, tesla, henry,

    # Astronomical Units
    mass_sun, parsec, astronomical_unit, lightyear, solar_luminosity,

    # Additional length units
    fermi, angstrom, micron, yard, foot, inch, mile, fathom, nautical_mile, furlong,

    # Additional time units
    minute, hour, day, week, year,

    # Additional temperature units
    rankine,  # TODO celsius, fahrenheit

    # Additional luminosity units
    lumen, lux, foot_candle, phot,

    # Additional mass units
    tonne, dalton, slug, pound, ounce, ton, long_ton, carat, imperial_carat,

    # Additional force units
    pound_force, dyne, poundal,

    # Additional energy units
    erg, calorie, electron_volt,

    # Additional power units
    metric_horsepower, mechanical_horsepower, electical_horsepower, boiler_horsepower,

    # Additional pressure units
    bar, standard_atmosphere, millimetre_mercury, inch_mercury, torr,

    # Additional angle units
    degree, turn, gradian, square_degree, arcminute, arcsecond,

    # Additional volume units
    litre, us_gallon, us_dry_gallon, imperial_gallon, us_quart, us_dry_quart, imperial_quart, us_fluid_ounce, imperial_fluid_ounce, us_peck, imperial_peck, us_bushel, imperial_bushel,

    # Additional velocity units
    mile_per_hour, knot,

    # Additional area units
    acre, hectare,
]


for unit in list(units):
    for prefix in unit.generate_metric_prefixes():
        units.append(prefix)

unit_dictionary = dict()
reverse_unit_dictionary = dict()
for unit in units:
    unit_dictionary[str(unit.symbol)] = unit.symbol
    reverse_unit_dictionary[unit.symbol] = unit
    for alternate in unit.alternates:
        unit_dictionary[alternate] = unit.symbol


def parse_unit(unit_string):
    return reverse_unit_dictionary[unit_dictionary[unit_string]]

