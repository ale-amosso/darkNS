import numpy as np
import scipy.constants
from quantities import GeV, s, m, eV
from scipy.constants import c
from functions.cute_logger import log

from dictionaries.dict_target_components import target_components
from dictionaries.dict_neutron_star import neutron_star
from dictionaries.dict_dark_matter import dark_matter



R_star = neutron_star["neutron_star"]["R_star"].rescale(m)


# GENERAL
c = c * m / s

# DARK MATTER
v_halo = 8e-4  # 7.34e-4  # dark_matter["dark_matter"]["v_halo"]  # Formula p.5 Joglekar
v_esc = 0.6  # v_esc = dark_matter["dark_matter"]["v_esc"] # Formula p.5 Joglekar
gamma_esc = dark_matter["dark_matter"]["gamma_esc"]
v_esc_not_natural = dark_matter["dark_matter"]["v_esc"]

def get_h_bar():
    h_bar = scipy.constants.physical_constants["reduced Planck constant in eV s"]
    h_bar = h_bar[0] * eV * s
    h_bar = h_bar.rescale(GeV * s)
    return h_bar


def get_E_halo(m_dm):  # Formula p.10
    E_halo = (1 / 2) * m_dm * v_halo ** 2
    return E_halo


def get_k_dm(m_dm):  # Formula at p.38 Joglekar
    k_dm = gamma_esc * v_esc * m_dm
    return k_dm


def get_E_dm(m_dm):  # Formula at p.38 Joglekar
    E_dm = gamma_esc * m_dm
    return E_dm


def get_E_CM(mandelstam_s):  # Formula p. 34 Joglekar
    E_CM = np.sqrt(mandelstam_s)
    return E_CM


def get_k_CM(mandelstam_s, E_p, k_dm, E_dm, cos_theta, p):  # Formula at p.35 Joglekar
    E_CM = get_E_CM(mandelstam_s)
    sen_theta = get_sen(cos_theta)
    E_tot = E_p + E_dm
    energies_factor = (2 * E_tot) / (E_tot + E_CM)

    k_CM_squared = (E_p ** 2 * k_dm ** 2 + E_dm ** 2 * p ** 2 - 2 * E_p * E_dm * (
            p * k_dm * cos_theta) - (p ** 2 * k_dm ** 2 * sen_theta ** 2)) / E_CM ** 2

    k_CM = np.sqrt(k_CM_squared)

    return k_CM


def get_m_target(target):
    p_F = target_components[target]["p_F"].rescale(GeV)
    E_F = target_components[target]["E_F"].rescale(GeV)
    if target == "electron":
        m_target = target_components["electron"]["mass_MeV"].rescale(GeV)
    else:
        m_target = np.sqrt(E_F ** 2 - p_F ** 2)
    return m_target


def get_mandelstam_variables(p, m_dm, E_dm, cos_theta, k_dm, cos_psi, target):
    # Calculate E_p
    E_p = getE_p(p, target)

    # Calculate s
    mandelstam_s = get_mandelstam_s(m_dm, E_p, p, E_dm, k_dm, cos_theta, target)

    # Calculate k_CM
    k_CM = get_k_CM(mandelstam_s, E_p, k_dm, E_dm, cos_theta, p)

    # Calculate t
    mandelstam_t = get_mandelstam_t(k_CM, cos_psi)

    return {
        "s": mandelstam_s,
        "t": mandelstam_t
    }


def getE_p(p, target):  # Formula at p.38 Joglekar
    m_target = get_m_target(target)
    E_p = np.sqrt(m_target ** 2 + p ** 2)
    return E_p


def get_mandelstam_s(m_dm, E_p, p, E_dm, k_dm, cos_theta, target):  # Formula p. 34
    m_target = get_m_target(target)
    mandelstam_s = m_target ** 2 + m_dm ** 2 + 2 * (E_p * E_dm - p * k_dm * cos_theta)
    return mandelstam_s


def get_mandelstam_t(k_CM, cos_psi):  # Formula p. 35 Joglekar
    mandelstam_t = -2 * k_CM ** 2 * (1 - cos_psi)
    return mandelstam_t


def get_V_F(target):  # Fermi Volume, p. 12 Joglekar
    p_F = target_components[target]["p_F"].rescale(GeV)
    V_F = (4 / 3 * np.pi * p_F.rescale(GeV) ** 3)
    return V_F


def get_v_mol(p, k_dm, m_dm, E_k, cos_theta, target):  # Formula at p.32
    E_p = getE_p(p, target)
    m_target = get_m_target(target)

    # Moeller velocity formula at p.9 Joglekar
    p_dot_k = (E_p * E_k - p * k_dm * cos_theta)  # four-vectors product
    num = p_dot_k ** 2 - m_target ** 2 * m_dm ** 2  # four-momentum

    v_mol = np.where(
        num > 0,  # Condition (if num>0)
        np.sqrt(num) / (E_p * E_k),  # then
        dark_matter["dark_matter"]["v_esc"]  # else, if num<=0
    )
    return v_mol


def get_beta_K_CM_cos_delta(E_p, k_dm, E_dm, p, cos_theta, mandelstam_s, gamma_ns):
    E_tot = E_p + E_dm
    E_CM = E_tot / gamma_ns

    p_cdot_k = abs(p) * abs(k_dm) * cos_theta

    num = (E_p * k_dm ** 2 - E_dm * p ** 2 + (E_p - E_dm) * p_cdot_k)
    den = E_CM * E_tot

    beta_kcm_cos_delta = num / den
    # log.info(f"E_p: {E_p}, E_dm: {E_dm}, k_dm: {k_dm}, p: {p}")
    # log.info(f"p_cdot_k: {p_cdot_k}, cos_theta:{cos_theta}, E_CM: {E_CM}, E_tot: {E_tot}")
    # log.info(f"num: {num}, den: {den}, beta_kcm_cos_delta: {beta_kcm_cos_delta}")

    return beta_kcm_cos_delta


def get_beta(E_p, E_dm, m_dm, p, k_dm, cos_theta):  # Formula at p.34
    total_momentum = np.sqrt(p ** 2 + k_dm ** 2 + 2 * p * k_dm * cos_theta)  # | p + k| = sqrt(p^2+k^2+ pk cos_theta)

    beta = total_momentum / (E_p + E_dm)
    return beta


def get_sen(cos_x):
    sen_x = np.sqrt(1 - cos_x ** 2)
    return sen_x


def get_gamma(beta):  # Formula at p.34
    gamma = 1 / np.sqrt(1 - beta ** 2)
    return gamma


def get_Delta_E(E_p, E_dm, k_dm, p, k_CM, cos_psi, alpha, cos_theta, mandelstam_s, m_dm):  # Joglekar p.37

    # Get parameters beta, gamma_ns, etc.
    beta_opposite = abs(- get_beta(E_p, E_dm, m_dm, p, k_dm, cos_theta))  # module of beta inverse
    gamma_ns = get_gamma(beta_opposite)
    # cos_psi = np.clip(cos_psi, -1, 1)
    sen_psi = get_sen(cos_psi)

    beta_kcm_cos_delta = get_beta_K_CM_cos_delta(E_p, k_dm, E_dm, p, cos_theta, mandelstam_s, gamma_ns)

    # log.info(f"m_dm:{m_dm}, k_dm:{k_dm}")
    # log.info(f"p: {p}, cos_psi: {cos_psi}, cos_theta: {cos_theta}")
    # log.info(f"beta_opposite: {beta_opposite},k_dm: {k_dm}, k_CM: {k_CM}, beta_kcm_cos_delta: {beta_kcm_cos_delta}")

    radicand = beta_opposite ** 2 * (k_CM ** 2) - beta_kcm_cos_delta ** 2

    if np.any(radicand < 0):
        log.error(f"Negative radicand: {radicand}, k_CM: {k_CM}, beta_kcm_cos_delta: {beta_kcm_cos_delta}")
        return 0 * GeV

    sqrt_term = np.sqrt(radicand)
    Delta_E = gamma_ns * beta_kcm_cos_delta * (1 - cos_psi) - gamma_ns * sqrt_term * sen_psi * np.cos(alpha)
    # log.info(f"m_n: {m_n}, m_dm: {m_dm}, gamma_esc: {gamma_esc},cos_psi:{cos_psi},1-cos_psi:{1-cos_psi} ")
    # log.info(f"E_p:{E_p}, E_F:{E_F},  E_F-E_p:{E_F-E_p}")
    # if Delta_E < 0:
    # log.warning(f"Negative Delta_E: {Delta_E}")
    # else:
    # if Delta_E+E_p-E_F<0:
    # log.debug(f"Delta_E is positive, but not enough: {Delta_E}")
    # elif Delta_E+E_p-E_F>0:
    # log.debug(f"Positive Delta_E, ok!: {Delta_E}")
    # log.info(f"----------------------------------------------------------------------------------")

    # cos_delta = get_cos_delta(E_p, k_dm, E_dm, p, cos_theta, mandelstam_s, beta_inverse, k_CM, gamma_ns)
    # sen_delta=get_sen(cos_delta)

    # Delta_E_old = (cos_delta*(1-cos_psi)-abs(sen_delta)*np.cos(alpha)*sen_psi)*(gamma_ns*beta_inverse*k_CM)
    # print(f"{cos_delta=}, {Delta_E_old=}")

    # Delta_E = gamma_ns * beta_kcm_cos_delta * (1 - cos_psi) - gamma_ns * np.sqrt(
    #   beta_inverse ** 2 * (k_CM ** 2) - beta_kcm_cos_delta ** 2) * sen_psi * np.cos(alpha)

    # if np.isnan(Delta_E):
    # print("cos_delta")
    #    print(cos_delta)

    return Delta_E


def get_delta_t():
    delta_t = 2 * R_star
    return delta_t


def get_theta_1_energy(Delta_E, E_halo):
    Delta_E = Delta_E.magnitude
    E_halo = E_halo.magnitude
    theta_value = np.heaviside(Delta_E - E_halo, 0)
    return theta_value


def get_theta_3_pauli(Delta_E, E_p, target):
    Delta_E = Delta_E.magnitude
    E_F = target_components[target]["E_F"].rescale(GeV)

    E_p = E_p.magnitude
    # print(f"{Delta_E=}, {E_Fermi=}, {E_p=}, {Delta_E + E_p - E_Fermi=}")
    theta_value = np.heaviside(Delta_E + E_p - E_F.magnitude, 0)
    return theta_value


def get_A(E_p, k_dm, E_dm, cos_theta, p):
    A = E_p ** 2 * k_dm ** 2 + E_dm ** 2 * p ** 2 - 2 * E_p * E_dm * (p * k_dm * cos_theta)
    return A


def get_B(E_p, k_dm, E_dm, cos_theta, p, E_CM):
    E = E_dm + E_p
    N = -p ** 2 * (k_dm * p * cos_theta) ** 2 - k_dm ** 2 * (k_dm * p * cos_theta) ** 2 + 2 * k_dm ** 2 * p ** 2 * (
            k_dm * p * cos_theta) - 2 * (k_dm * p * cos_theta) ** 3 + k_dm ** 4 * p ** 2 + k_dm ** 2 * p ** 4
    D = (E + E_CM) ** 2
    B = N / D
    return B


def get_C(E_p, k_dm, E_dm, p, E_CM, sen_theta):
    E = E_dm + E_p
    C = -2 * E * (k_dm ** 2 * p ** 2 * sen_theta ** 2) / (E + E_CM)
    return C


def k_CM_my_method(E_p, k_dm, E_dm, cos_theta, p, E_CM, sen_theta):
    A = get_A(E_p, k_dm, E_dm, cos_theta, p)
    B = get_B(E_p, k_dm, E_dm, cos_theta, p, E_CM)
    C = get_C(E_p, k_dm, E_dm, p, E_CM, sen_theta)

    k_CM_squared = (A + B + C) / E_CM ** 2

    k_CM = np.sqrt(k_CM_squared)

    return k_CM


def get_N_hit(Delta_E, E_halo, maxN=100):
    N_hit = 1
    solutions = []
    for N_hit in range(2, maxN + 1):
        # Calcolo dei due termini
        cond1 = np.heaviside(Delta_E.magnitude - E_halo.magnitude / N_hit, 0)

        if N_hit > 1:
            cond2 = np.heaviside((E_halo.magnitude / (N_hit - 1)) - Delta_E.magnitude, 0)
        else:
            cond2 = 0

        if cond1 * cond2 == 1:
            solutions.append(N_hit)

        print(f"N_hit: {solutions[-1]}")
        return solutions[-1]
