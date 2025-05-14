from v_interface import set_gui_elements as set_gui_el


def build_settings_entries(settings_frame, settings_type):

    if settings_type == "mass_range":
        set_gui_el.set_entry(settings_frame, "10^-8", 4, 1)
        set_gui_el.set_entry(settings_frame, "10^4", 5, 1)
        set_gui_el.set_entry(settings_frame, "20", 6, 1)

    elif settings_type == "integration_precision":
        set_gui_el.set_entry(settings_frame, "a", 4, 1)
        set_gui_el.set_entry(settings_frame, "b", 5, 1)
        set_gui_el.set_entry(settings_frame, "c", 6, 1)
    pass
