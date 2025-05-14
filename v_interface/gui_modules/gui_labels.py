from v_interface import set_gui_elements as set_gui_el


def build_labels(target_frame):
    set_gui_el.set_label("Choose a target", target_frame, 1, 0)
    set_gui_el.set_label("Choose a fermionic operator", target_frame, 5,
                         0)
    set_gui_el.set_label("Choose a scalar operator", target_frame, 8,
                         0)
    pass


def build_settings_label(settings_frame, setting_type):

    if setting_type == "mass_range":
        set_gui_el.set_label("Min (GeV)", settings_frame, 4, 0)
        set_gui_el.set_label("Max (GeV)", settings_frame, 5, 0)
        set_gui_el.set_label("Points", settings_frame, 6, 0)

    elif setting_type == "integration_precision":
        set_gui_el.set_label("neval", settings_frame, 4, 0)
        set_gui_el.set_label("nint", settings_frame, 5, 0)
        set_gui_el.set_label("alpha", settings_frame, 6, 0)
    pass
