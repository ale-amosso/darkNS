def format_quantity(quantity):
    formatted_quantity = "{:.2e}".format(quantity).replace("e+", "×10^").replace("**", "^").replace("*", "x").replace(
        "e-", "×10^-")
    return formatted_quantity


def format_quantity_without_10(quantity):
    formatted_quantity = "{:.0f}".format(quantity)
    return formatted_quantity
