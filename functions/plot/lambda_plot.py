import csv

import numpy as np
import matplotlib.pyplot as plt
import functions.plot.vegas_integral as veg_int
import functions.physics_helpers as h
from tqdm import tqdm
import functions.plot.dm_mass_range as dm_mass
import seaborn as sns

from dictionaries.dict_target_components import target_components
from dictionaries.dict_neutron_star import neutron_star
from quantities import GeV, s, m
from scipy.constants import c

# GENERAL GLOBALS
c = c * m / s
N_hit = 1

# TARGET
R_star = neutron_star["neutron_star"]["R_star"].rescale(m)


def save_to_csv(m_dm_values, lambda_values, operator, target):
    print(f"Saving CSV: {operator}_lambda_values.csv")
    # Define CSV file name
    filename = operator + target + "_lambda_values.csv"

    #  If the file already exist, opens the file, otherwise it creates the file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Writes the header
        writer.writerow(["m_dm [GeV]", "Lambda [GeV]"])

        # Writes the data
        for m_dm, lambda_val in zip(m_dm_values, lambda_values):
            if lambda_val is not None:  # Skip None values
                writer.writerow([m_dm, lambda_val])


def plot_lambda_dm(operator, target, integration_settings, progress_callback=None, stop_event=None):
    # dark matter mass range
    m_dm_values = dm_mass.dm_range_array(integration_settings)

    # lambda values corresponding to the dark matter masses
    #lambda_values = np.array(
    #    [lambda_calc(m_dm, operator, target) for m_dm in tqdm(m_dm_values, desc="Calculating Lambda", unit="value")])

    lambda_values = []

    for i, m_dm in enumerate(tqdm(m_dm_values, desc="Computing Λ(m_dm)", total=len(m_dm_values))):
        if stop_event and stop_event.is_set():
            print("🛑 User interrupted the calculus")
            return  # interrupt thread
        lam = lambda_calc(m_dm, operator, target, integration_settings)
        lambda_values.append(lam)

        if progress_callback:
            progress_callback((i + 1) / len(m_dm_values))

    # PLOT
    plot_setup(m_dm_values, lambda_values, operator, target)
    plt.savefig(operator + '.png')
    plt.show()

    # SAVE DATA TO CSV
    save_to_csv(m_dm_values, lambda_values, operator, target)


def lambda_calc(m_dm, operator, target, integration_settings):
    # Kinematics
    m_dm = m_dm * GeV
    k_dm = h.get_k_dm(m_dm)
    E_dm = h.get_E_dm(m_dm)
    h_bar = h.get_h_bar()
    delta_t = h.get_delta_t()
    n_T = target_components[target]["n_T"].rescale(1 / m ** 3)

    # Integral
    integral_result = veg_int.calculate_integral(operator, m_dm, E_dm, k_dm, target, integration_settings)

    Lambda_4 = (n_T * delta_t * integral_result * (h_bar * c) ** 2) / ((8 * 2 * np.pi) ** 2)

    # Multiple scatter
    if N_hit > 1:
        for i in range(1, N_hit):
            Lambda_4 += Lambda_4 / i

    # Get Lambda value
    if Lambda_4 > 0:
        if operator not in ("O_S1", "O_S2"):
            Lambda = Lambda_4 ** (1 / 4)
        else:
            Lambda = Lambda_4 ** (1 / 2)

        return Lambda
    elif Lambda_4 == 0:
        print("Lambda_4 is null. Continue without returning a value")
    elif Lambda_4 < 0:
        print("Lambda_4 is negative. Continue without returning a value")

        return None


def update_global_N_hit(m_dm, E_p, E_dm, k_dm, p, cos_psi, alpha, cos_theta, mandelstam_s):
    global N_hit  # Use the global variable N_hit
    k_CM = h.get_k_CM(mandelstam_s, E_p, k_dm, E_dm, cos_theta, p)
    E_halo = h.get_E_halo(m_dm)

    return N_hit


# PLOT HELPERS
def plot_setup(m_dm_values, lambda_values, operator, target):
    sns.set_theme(style="whitegrid")
    # fig, ax = plt.subplots()  # Using plt.subplots in order to have 'ax' object
    fig, ax = plt.subplots(figsize=(8, 6))
    # sns.lineplot(x=m_dm_values, y=lambda_values, ax=ax, marker="o")
    ax.plot(m_dm_values, lambda_values)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('m_dm [GeV]')
    ax.set_ylabel('Lambda [GeV]')
    ax.set_title(operator + ' Plot' + " - " + target)
    ax.grid(True)
    ax.set_xlim(1e-8, 1e5)  # Limits the x-axis to the specified range
    ax.set_ylim(1e-4, 1e6)  # Limits the y-axis to the specified range

    # Calculate the aspect ratio considering the log scale
    # The formula is (log10(x_max) - log10(x_min)) / (log10(y_max) - log10(y_min))
    aspect_ratio = (np.log10(ax.get_xlim()[1]) - np.log10(ax.get_xlim()[0])) / \
                   (np.log10(ax.get_ylim()[1]) - np.log10(ax.get_ylim()[0]))

    ax.set_aspect(aspect_ratio, 'box')  # Set the aspect ratio
    pass

