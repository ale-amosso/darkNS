import numpy as np
import vegas
import functions.physics_helpers as h
from dictionaries.dict_target_components import target_components
from dictionaries.dict_operators import operators
from quantities import GeV, s, m
from scipy.constants import c
from settings.integration_settings import DEFAULT_INTEGRATION_SETTINGS

# GENERAL GLOBALS
c = c * m / s


def calculate_integral(operator, m_dm, E_dm, k_dm, target, integration_settings):
    # TARGET
    p_F = target_components[target]["p_F"].rescale(GeV)
    E_F = target_components[target]["E_F"].rescale(GeV)
    V_F = h.get_V_F(target)

    if target == "electron":
        m_target = target_components["electron"]["mass_MeV"].rescale(GeV)
    else:
        m_target = np.sqrt(E_F ** 2 - p_F ** 2)

    def integrand(x):
        # Vegas needs an array for the variables
        cos_psi, alpha, p, cos_theta, phi = x
        p_GeV = p * GeV
        #if p > p_F:
        #    return 0
        # Get the mandelstam variables, Moeller velocity, target Energy and Halo Energy
        mandelstam, v_mol, E_p, E_halo = get_kinematics(p_GeV, m_dm, E_dm, k_dm, cos_theta, cos_psi, target)

        # Get the chosen operator
        op = get_operator(operator, mandelstam["t"], m_target, m_dm, mandelstam["s"])

        # THETA_CONDITIONS
        theta_1_value, theta_3_value = get_theta_conditions(mandelstam, E_p, k_dm, E_dm, cos_theta, cos_psi, alpha,
                                                            p_GeV, m_dm, E_halo, target)

        #update_global_N_hit(m_dm, E_p, E_dm, k_dm, p, cos_psi, alpha, cos_theta, mandelstam["s"])
        #N_hit = h.get_N_hit(Delta_E,E_halo)
        integrand_value = ((p_GeV ** 2 / V_F) * (op / mandelstam["s"]) * v_mol) * theta_1_value * theta_3_value

        return integrand_value

    # Integral Limits
    cos_psi_limits = [-1, 1]
    alpha_limits = [0, 2 * np.pi]
    p_limits = get_p_limits(m_dm, target)
    cos_theta_limits = [-1, 1]
    phi_limits = [0, 2 * np.pi]

    integral = vegas.Integrator([cos_psi_limits, alpha_limits, p_limits, cos_theta_limits, phi_limits])

    # Integrate using Vegas library
    params = get_integration_params(integration_settings)
    # Default values are: nitn= 10, neval=5000 and alpha= 0.2
    if m_dm < 1e-2 * GeV:
        result = integral(integrand, nitn=params["nitn"], neval=params["neval"], alpha=params["alpha"])
    else:
        print(params["nitn"])
        result = integral(integrand, nitn=params["nitn"], neval=params["neval"])
    # Restore units after integration
    result_restored_units = result.mean * GeV ** 2
    return result_restored_units


def get_operator(operator, mandelstam_t, m_t, m_dm, mandelstam_s):
    operation = operators.get(operator)
    if operation:
        return operation(mandelstam_t, m_t, m_dm, mandelstam_s)
    else:
        print(f"Operator'{operator}' not found.")
        return None


def get_kinematics(p_GeV, m_dm, E_dm, k_dm, cos_theta, cos_psi, target):
    mandelstam = h.get_mandelstam_variables(p_GeV, m_dm, E_dm, cos_theta, k_dm, cos_psi, target)
    v_mol = h.get_v_mol(p_GeV, k_dm, m_dm, E_dm, cos_theta, target)
    E_p = h.getE_p(p_GeV, target)
    E_halo = h.get_E_halo(m_dm)

    return mandelstam, v_mol, E_p, E_halo


def get_theta_conditions(mandelstam, E_p, k_dm, E_dm, cos_theta, cos_psi, alpha, p_GeV, m_dm, E_halo, target):
    k_CM = h.get_k_CM(mandelstam["s"], E_p, k_dm, E_dm, cos_theta, p_GeV)
    Delta_E = h.get_Delta_E(E_p, E_dm, k_dm, p_GeV, k_CM, cos_psi, alpha, cos_theta, mandelstam["s"], m_dm)

    theta_1_value = h.get_theta_1_energy(Delta_E, E_halo)
    theta_3_value = h.get_theta_3_pauli(Delta_E, E_p, target)

    #E_F = target_components[target]["E_F"].rescale(GeV)

    return theta_1_value, theta_3_value


def get_delta(m_dm):
    a = 1  # 1
    b = 1  # 1
    m_dm = m_dm.magnitude
    m_dm_0 = 1e-2
    return 1 - np.exp(-a * (m_dm / m_dm_0) ** b)


def get_p_limits(m_dm, target):
    p_F = target_components[target]["p_F"].rescale(GeV)
    upper_limit_p = p_F.rescale(GeV)
    epsilon = 1e-1
    delta = get_delta(m_dm)
    print(m_dm, delta)
    if m_dm > 10 ** -2 * GeV:
        p_limits = [0, upper_limit_p]
    else:
        p_limits = [(1 - delta) * p_F.rescale(GeV), p_F.rescale(GeV)]
    return p_limits


def get_integration_params(settings):
    integration = settings.get("integration_precision", {})

    if integration is None or integration.get("use_default", True):
        return DEFAULT_INTEGRATION_SETTINGS.copy()

    try:
        return {
            "nitn": int(integration["nitn"]),
            "neval": int(integration["neval"]),
            "alpha": float(integration.get("alpha", DEFAULT_INTEGRATION_SETTINGS["alpha"]))
        }
    except (KeyError, ValueError, TypeError) as e:
        print(f"⚠️ Integration settings error: {e}")
        return DEFAULT_INTEGRATION_SETTINGS.copy()
