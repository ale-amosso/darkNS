DEFAULT_INTEGRATION_SETTINGS = {
    "use_default": True,
    "neval": 5000,
    "nitn": 10,
    "alpha": 0.2
}

DEFAULT_DM_RANGE_SETTINGS = {
    "use_default": True,
    "min": "1e-8",
    "max": "1e4",
    "points": 50
}


def parse_scientific_input(s):
    """
    Parses a string in either float or scientific format.
    Supports formats like '1e-8', '0.001', or '10^-8'.
    """
    s = s.strip()
    try:
        return float(s)
    except ValueError:
        if "^" in s:
            base, exp = s.split("^")
            return float(base) ** float(exp)
        raise ValueError(f"Invalid input format: {s}")
