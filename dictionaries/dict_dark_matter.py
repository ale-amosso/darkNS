from quantities import cm, GeV, m, s, km
from scipy.constants import c

dark_matter = {
    "dark_matter": {
        "rho": 0.4 * (GeV / cm ** 3),
        "gamma_esc": 1.24,
        "v_esc": 0.6 * c * m / s,
        "v_halo": 8e-4 * c * m / s,  # dark matter velocity in the halo
        "v_halo_natural_units": 8e-4,  # dark matter velocity in the halo in natural units
        "m_X": 4.21e25 * GeV / s, # total DM passing through the neutron star per unit time
        "delta_T": 8.41e-5 * s #TODO: to check
    }
}
