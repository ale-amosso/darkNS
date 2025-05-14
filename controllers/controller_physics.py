from functions.dm_flux import total_DM_mass

def get_total_flux_DM():
    """Retrieve the total dm mass passing through the NS and formats it."""
    total_mass = total_DM_mass()  # Calculation
    formatted_mass = "{:.2e}".format(total_mass).replace("e+", "×10^")
    return f"The total dark matter mass passing through the neutron star per unit time is {formatted_mass}"
