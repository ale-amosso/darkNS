import math

from dictionaries.dict_dark_matter import dark_matter
from quantities import c

v_esc = dark_matter["dark_matter"]["v_esc"]


def gamma_esc():
    gamma_esc_squared = c / (c ** 2 - v_esc ** 2)
    gamma_esc_calc = math.sqrt(gamma_esc_squared)
    return gamma_esc_calc
