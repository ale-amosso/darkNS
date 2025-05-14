import numpy as np
import scipy.constants

import dictionaries.dict_neutron_star as neutron_star
import dictionaries.dict_target_components as target_components
import dictionaries.dict_dark_matter as dark_matter
import quantities
import sympy as sp


def calc_density(target):
    R_star = neutron_star.neutron_star["neutron_star"]["R_star"]
    R_star = R_star.rescale(quantities.cm)
    M_star = neutron_star.neutron_star["neutron_star"]["M_star"]
    Y_T = target_components.target_components[target]["Y_T"]
    m_n = target_components.target_components["neutron"]["mass"]
    V_star = (4 / 3) * np.pi * (R_star ** 3)
    print(V_star, m_n, Y_T, M_star)
    n_T = Y_T * M_star / V_star / m_n

    return n_T


def calc_F_volume(target):
    p_F = target_components.target_components[target]["p_F"]
    V_F = (4 / 3) * np.pi * (p_F ** 3)
    return V_F


def calc_delta_t():
    R_star = neutron_star.neutron_star["neutron_star"]["R_star"].rescale(quantities.m)
    delta_t = 2 * R_star / (scipy.constants.c * quantities.m / quantities.s)
    return delta_t


