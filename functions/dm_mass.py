import numpy as np
from dictionaries.dict_target_components import target_components
from dictionaries.dict_dark_matter import dark_matter
from quantities import GeV


def parameters(target):
    p_F = target_components[target]["p_F"]
    m_t = target_components[target]["mass_MeV"]
    v_halo = dark_matter["dark_matter"]["v_halo_natural_units"]
    return p_F, m_t, v_halo


# Relativistic targets
def calc_rel_heavy_dm_mass(target):
    p_F, m_t, v_halo = parameters(target)
    mass_max = (p_F * 10e6).rescale(GeV)  # p_F/v_halo **2  p.17
    mass_min = p_F.rescale(GeV)
    mass = np.array([mass_min, mass_max])
    return mass


def calc_rel_very_heavy_dm_mass(target):
    p_F, m_t, v_halo = parameters(target)
    mass_min = (p_F * 10e6).rescale(GeV)  # p_F/v_halo **2 p.17
    print(mass_min)
    mass = np.array([mass_min])
    return mass


def calc_rel_light_dm_mass(target):
    p_F, m_t, v_halo = parameters(target)
    mass_max = p_F.rescale(GeV)
    mass_min = (m_t ** 2 / p_F).rescale(GeV)
    mass = np.array([mass_min, mass_max])
    return mass


def calc_rel_very_light_dm_mass(target):
    p_F, m_t, v_halo = parameters(target)
    mass_max = (m_t ** 2 / p_F).rescale(GeV)
    mass = np.array([0, mass_max])
    return mass


# Non-Relativistic targets
def calc_non_rel_heavy_dm_mass(target):
    p_F, m_t, v_halo = parameters(target)
    m_t_gev = m_t.rescale(GeV)
    print("mass heavy_dm_mass")
    print(m_t)
    mass_min = m_t_gev
    # mass_max = (m_t * 10e6).rescale(GeV)  # m_T/v_halo **2  p.17
    mass_max = m_t_gev/(v_halo**2)
    print("mass heavy")
    print(mass_max)
    mass = np.array([mass_min, mass_max])
    return mass


def calc_non_rel_very_heavy_dm_mass(target):
    p_F, m_t, v_halo = parameters(target)
    # mass_min = (m_t * 10e6).rescale(GeV)  # m_T/v_halo **2 p.17
    m_t_gev = m_t.rescale(GeV)
    print("very_heavy_dm_mass")
    print(m_t)
    mass_min = m_t_gev/v_halo**2
    print("mass heavy")
    print(mass_min)
    mass = np.array([mass_min])
    return mass


def calc_non_rel_light_dm_mass(target):
    p_F, m_t, v_halo = parameters(target)
    mass_max = m_t.rescale(GeV)
    mass = np.array([mass_max])
    return mass
