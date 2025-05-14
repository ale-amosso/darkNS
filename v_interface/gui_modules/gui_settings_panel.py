from v_interface.gui_modules.gui_labels import build_settings_label
from v_interface.gui_modules.gui_buttons import build_settings_button, build_settings_enter_button
from settings.integration_settings import DEFAULT_INTEGRATION_SETTINGS, DEFAULT_DM_RANGE_SETTINGS
from v_interface import set_gui_elements as set_gui_el
from v_interface.gui_modules import gui_inputs as inputs

def toggle_settings_panel(gui):
    """Show or hide the settings section depending on the toggle state."""
    if gui.settings_switch.get():  # active
        gui.segmented_button = build_settings_button(
            gui.settings_frame,
            lambda val: display_settings_fields(gui, val)
        )
        gui.segmented_button.grid(row=1, column=0, columnspan=3, padx=10, pady=(0, 10), sticky="w")
        gui.segmented_button.set("DM Mass Range")
        display_settings_fields(gui, "DM Mass Range")
    else:
        gui.segmented_button.grid_remove()
        clear_settings_fields(gui)


def display_settings_fields(gui, value):
    """Dynamically create input fields based on the selected settings category (e.g., mass range or integration precision)"""
    clear_settings_fields(gui)

    if value == "DM Mass Range":
        build_settings_label(gui.settings_frame, "mass_range")
        integration_settings = gui.settings_state["dm_mass_range"]

        default_min = str(integration_settings.get("dm_mass_range", DEFAULT_DM_RANGE_SETTINGS["min"]))
        default_max = str(integration_settings.get("dm_mass_range", DEFAULT_DM_RANGE_SETTINGS["max"]))
        default_points = str(integration_settings.get("dm_mass_range", DEFAULT_DM_RANGE_SETTINGS["points"]))

        gui.min_entry = set_gui_el.set_entry(gui.settings_frame, default_min, 4, 1)
        gui.max_entry = set_gui_el.set_entry(gui.settings_frame, default_max, 5, 1)
        gui.points_entry = set_gui_el.set_entry(gui.settings_frame, default_points, 6, 1)

        if gui.dm_range_locked:
            gui.min_entry.configure(state='disabled', fg_color="#1e1e1e", text_color="#5a5a5a")
            gui.max_entry.configure(state='disabled', fg_color="#1e1e1e", text_color="#5a5a5a")
            gui.points_entry.configure(state='disabled', fg_color="#1e1e1e", text_color="#5a5a5a")
            inputs.build_btn_change(gui)

        else:
            gui.enter_btn = build_settings_enter_button(gui.settings_frame, lambda: inputs.on_dm_range_enter(gui),
                                                        "Enter")

    elif value == "Integration Precision":
        build_settings_label(gui.settings_frame, "integration_precision")
        integration_settings = gui.settings_state["integration_precision"]

        default_neval = str(integration_settings.get("neval", DEFAULT_INTEGRATION_SETTINGS["neval"]))
        default_nitn = str(integration_settings.get("nitn", DEFAULT_INTEGRATION_SETTINGS["nitn"]))
        default_alpha = str(integration_settings.get("alpha", DEFAULT_INTEGRATION_SETTINGS["alpha"]))

        gui.neval_entry = set_gui_el.set_entry(gui.settings_frame, default_neval, 4, 1)
        gui.nitn_entry = set_gui_el.set_entry(gui.settings_frame, default_nitn, 5, 1)
        gui.alpha_entry = set_gui_el.set_entry(gui.settings_frame, default_alpha, 6, 1)

        if gui.integration_locked:
            gui.neval_entry.configure(state='disabled', fg_color="#1e1e1e", text_color="#5a5a5a")
            gui.nitn_entry.configure(state='disabled', fg_color="#1e1e1e", text_color="#5a5a5a")
            gui.alpha_entry.configure(state='disabled', fg_color="#1e1e1e", text_color="#5a5a5a")
            inputs.build_btn_change_integration(gui)

        else:
            gui.enter_btn = build_settings_enter_button(gui.settings_frame, lambda: inputs.on_integration_enter(gui), "Enter")



def clear_settings_fields(gui):
    """Remove all settings widgets in rows >= 4."""
    for widget in gui.settings_frame.grid_slaves():
        if int(widget.grid_info()["row"]) >= 4:
            widget.grid_remove()
