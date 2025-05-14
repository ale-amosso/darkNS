import math
from dictionaries.dict_neutron_star import neutron_star
from v_interface.gui_modules.string_utils import format_quantity, format_quantity_without_10
from functions.temperature import calc_Temp
from quantities import km, GeV, s


#TODO: T = calc_Temp_altro_articolo()


def get_infomodel():
    T = calc_Temp()
    R_star = neutron_star["neutron_star"]["R_star"]  # km
    M_star = neutron_star["neutron_star"]["M_star"]

    text = (
            "The model assumes neutrons, protons, electrons, and muons to be the sole stellar constituents in the "
            "core.\n\n" +
            "The benchmark values used for the neutron star are:\n" +
            "M_star = " + format_quantity(M_star) + "\n" +
            "R_star = " + format_quantity(R_star) + "\n" +
            "The temperature is " + format_quantity_without_10(T)
    )
    return text
