import numpy as np


def dm_range_array(integration_settings):
    dm_range_settings = integration_settings.get("dm_mass_range", {})

    if dm_range_settings is None or dm_range_settings.get("use_default") is True:
        return np.logspace(-8, 4, 20)  # Default range

    try:
        m_min = parse_exponential(dm_range_settings["min"])
        print(m_min)
        m_max = parse_exponential(dm_range_settings["max"])
        print(m_max)
        n_points = int(dm_range_settings["points"])
        print(n_points)
        return np.logspace(np.log10(m_min), np.log10(m_max), n_points)
    except (KeyError, ValueError, TypeError) as e:
        print(f"⚠️ Error: {e}")
        print("⚠️ Invalid DM mass settings provided. Using default range.")
        return np.logspace(-8, 4, 20)


# Reuse and custom this code if you want to split the range in different ways :)
#def dm_range_array(integration_settings):
    #very_light_mass = np.logspace(-10, -4, 10)
    #very_light_mass = np.logspace(-10, -4, 6)
    #light_mass = np.logspace(-4, -2, 5)
    #medium_mass = np.logspace(-2, 0, 10)
    #heavy_mass = np.logspace(0, 6, 10)
    #return np.concatenate((very_light_mass, light_mass, medium_mass, heavy_mass))



def parse_exponential(s):
    try:
        return float(s)  # try directly that value
    except ValueError:
        if "^" in s:
            base, exp = s.split("^")
            return float(base) ** float(exp)
        raise
