# v_interface/gui_modules/button_events.py
from controllers.controller_plot import start_calculation_thread


def handle_target_click(gui, target):
    from functions import dm_mass, targets
    from v_interface.gui_modules import gui_target_info, string_utils as utils

    #target_info = gui_target_info.get_target_info(target, dm_mass, targets, utils)
    #gui.add_text_to_print_frame(target_info, clear_text=True)
    gui.selected_target = target
    gui.enable_operator_buttons()


def handle_model_click(gui):
    from v_interface.gui_modules import info_model
    model_text = info_model.get_infomodel()
    gui.add_text_to_print_frame(model_text, clear_text=True)


def handle_operator_click(gui, operator, settings):
    from v_interface.gui_modules import custom_popup as popup

    if gui.selected_target is None:
        popup.show_custom_messagebox("Warning", "Select a target first!")
        return

    if gui.selected_target == "electron":
        popup.show_custom_messagebox("Selected items:",
                                     "Electron interactions are not available yet. Hang tight — "
                                     "they'll join the party soon! :)")
        return
    gui.informative_label.grid()
    gui.informative_label.configure(
        text=f"You selected: {gui.selected_target} target with {operator} operator"
    )
    start_calculation_thread(gui, operator, settings)

def handle_segmented_button_click(gui):
    pass