import math
from dictionaries.dict_neutron_star import neutron_star
from dictionaries.dict_dark_matter import dark_matter
from functions.parameters_calc import gamma_esc
from quantities import km, GeV, s


pi = math.pi
v_halo = dark_matter["dark_matter"]["v_halo"]
v_halo = v_halo.rescale(km/s)
v_esc = dark_matter["dark_matter"]["v_esc"]
v_esc = v_esc.rescale(km/s)
R_star = neutron_star["neutron_star"]["R_star"] # km
gamma_esc = gamma_esc()
rho = dark_matter["dark_matter"]["rho"]
rho = rho.rescale(GeV / km ** 3)


def impact_parameter():
    b_impact = R_star * (v_esc / v_halo) * gamma_esc
    return b_impact


def total_DM_mass():
    b = impact_parameter()
    m_tot_DM = pi * b ** 2 * v_halo * rho
    return m_tot_DM
