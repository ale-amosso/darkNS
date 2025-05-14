from v_interface.gui_modules.gui_buttons import build_settings_enter_button
from settings.integration_settings import parse_scientific_input
from v_interface.gui_modules import custom_popup as popup


def on_dm_range_enter(gui):
    gui.dm_range_locked = True

    try:
        m_min = parse_scientific_input(gui.min_entry.get())
        m_max = parse_scientific_input(gui.max_entry.get())
        points = int(gui.points_entry.get())

        gui.settings_state["dm_mass_range"] = {
            "use_default": False,
            "min": m_min,
            "max": m_max,
            "points": points
        }

        for entry in [gui.min_entry, gui.max_entry, gui.points_entry]:
            entry.configure(state='disabled', fg_color="#1e1e1e", text_color="#5a5a5a")

        build_btn_change(gui)

    except ValueError as e:
        popup.show_custom_messagebox("Invalid Input", str(e))


def on_dm_range_change(gui):
    gui.dm_range_locked = False

    for entry in [gui.min_entry, gui.max_entry, gui.points_entry]:
        entry.configure(state="normal", fg_color="#343638", text_color="#ffffff")

    if gui.enter_btn:
        gui.enter_btn.grid_remove()
    gui.enter_btn = build_settings_enter_button(gui.settings_frame, lambda: on_dm_range_enter(gui), "Enter")


def build_btn_change(gui):
    if gui.enter_btn:
        gui.enter_btn.grid_remove()
    gui.enter_btn = build_settings_enter_button(gui.settings_frame, lambda: on_dm_range_change(gui), "Change")


def on_integration_enter(gui):
    gui.integration_locked = True

    try:
        neval = int(gui.neval_entry.get())
        nitn = int(gui.nitn_entry.get())
        alpha = float(gui.alpha_entry.get())

        gui.settings_state["integration_precision"] = {
            "use_default": False,
            "neval": neval,
            "nitn": nitn,
            "alpha": alpha
        }

        for entry in [gui.neval_entry, gui.nitn_entry, gui.alpha_entry]:
            entry.configure(state='disabled', fg_color="#1e1e1e", text_color="#5a5a5a")

        build_btn_change_integration(gui)

    except ValueError as e:
        popup.show_custom_messagebox("Invalid Input", str(e))


def on_integration_change(gui):
    gui.integration_locked = False

    for entry in [gui.neval_entry, gui.nitn_entry, gui.alpha_entry]:
        entry.configure(state="normal", fg_color="#343638", text_color="#ffffff")

    if gui.enter_btn:
        gui.enter_btn.grid_remove()
    gui.enter_btn = build_settings_enter_button(gui.settings_frame, lambda: on_integration_enter(gui), "Enter")


def build_btn_change_integration(gui):
    if gui.enter_btn:
        gui.enter_btn.grid_remove()
    gui.enter_btn = build_settings_enter_button(gui.settings_frame, lambda: on_integration_change(gui), "Change")
