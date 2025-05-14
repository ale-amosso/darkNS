# Legend:
# Y_T= volume-averaged abundance
# n_T= average number density
from typing import Dict

from quantities import kg, MeV, cm, Quantity
from scipy.constants import physical_constants
import scipy.constants as const


target_components: dict[str, dict[str, Quantity | str | float] | dict[str, Quantity | str | float] | dict[str, Quantity | str | float] | dict[str, Quantity | str | float]] = {
    "electron": {
        "type": "relativistic",
        "Y_T": 0.06,
        "n_T": 1.27e+37 * cm ** (-3),
        "mass": const.electron_mass * kg,
        "mass_MeV": float(physical_constants["electron mass energy equivalent in MeV"][0]) * MeV,
        "p_F": 146 * MeV,
        "E_F": 146 * MeV,
    },
    "muon": {
        "type": "non-relativistic",
        "Y_T": 0.02,
        "n_T": 4.23e+36 * cm ** (-3),
        "mass": float(physical_constants["muon mass"][0]) * kg,
        "p_F": 50 * MeV,
        "E_F": 118 * MeV,
    },
    "proton": {
        "type": "non-relativistic",
        "Y_T": 0.07,
        "n_T": 1.48e+37 * cm ** (-3),
        "mass": const.proton_mass * kg,
        "mass_MeV": float(physical_constants["proton mass energy equivalent in MeV"][0]) * MeV,
        "p_F": 160 * MeV,
        "E_F": 951 * MeV,
    },
    "neutron": {
        "type": "non-relativistic",
        "Y_T": 0.93,
        "n_T": 1.97e+38 * cm ** (-3),
        "mass": const.neutron_mass * kg,
        "mass_MeV": float(physical_constants["neutron mass energy equivalent in MeV"][0]) * MeV,
        "p_F": 373 * MeV,
        "E_F": 1011 * MeV,
    }
}



