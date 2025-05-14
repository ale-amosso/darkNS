from v_interface import set_gui_elements as set_gui_el
from v_interface.set_gui_elements import segmented_button
import customtkinter as ctk


def build_target_buttons(target_frame, state, on_button_model_click, on_button_click):
    # Target Buttons
    btn_ns_model = set_gui_el.button(target_frame, "Model", 0, 0, state)
    btn_ns_model.bind("<Button-1>", lambda event, target="Model": on_button_model_click(target))

    btn_electron = set_gui_el.button(target_frame, "e⁻", 3, 0, state)
    btn_electron.bind("<Button-1>", lambda event, target="electron": on_button_click(target))

    btn_muon = set_gui_el.button(target_frame, "μ⁻", 3, 1, state)
    btn_muon.bind("<Button-1>", lambda event, target="muon": on_button_click(target))

    btn_proton = set_gui_el.button(target_frame, "p", 4, 0, state)
    btn_proton.bind("<Button-1>", lambda event, target="proton": on_button_click(target))

    btn_neutron = set_gui_el.button(target_frame, "n", 4, 1, state)
    btn_neutron.bind("<Button-1>", lambda event, target="neutron": on_button_click(target))
    return [btn_neutron, btn_proton, btn_electron]


def build_operators_f_buttons(target_frame, state, on_button_operator_click):
    # Operators F Buttons
    btn_OF_1 = set_gui_el.button(target_frame, "O_F1", 6, 0, state)
    btn_OF_1.bind("<Button-1>", lambda event, operator="O_F1": on_button_operator_click(operator))

    btn_OF_2 = set_gui_el.button(target_frame, "O_F2", 6, 1, state)
    btn_OF_2.bind("<Button-1>", lambda event, operator="O_F2": on_button_operator_click(operator))

    btn_OF_3 = set_gui_el.button(target_frame, "O_F3", 6, 2, state)
    btn_OF_3.bind("<Button-1>", lambda event, operator="O_F3": on_button_operator_click(operator))

    btn_OF_4 = set_gui_el.button(target_frame, "O_F4", 6, 3, state)
    btn_OF_4.bind("<Button-1>", lambda event, operator="O_F4": on_button_operator_click(operator))

    btn_OF_5 = set_gui_el.button(target_frame, "O_F5", 6, 4, state)
    btn_OF_5.bind("<Button-1>", lambda event, operator="O_F5": on_button_operator_click(operator))

    btn_OF_6 = set_gui_el.button(target_frame, "O_F6", 7, 0, state)
    btn_OF_6.bind("<Button-1>", lambda event, operator="O_F6": on_button_operator_click(operator))

    btn_OF_7 = set_gui_el.button(target_frame, "O_F7", 7, 1, state)
    btn_OF_7.bind("<Button-1>", lambda event, operator="O_F7": on_button_operator_click(operator))

    btn_OF_8 = set_gui_el.button(target_frame, "O_F8", 7, 2, state)
    btn_OF_8.bind("<Button-1>", lambda event, operator="O_F8": on_button_operator_click(operator))

    btn_OF_9 = set_gui_el.button(target_frame, "O_F9", 7, 3, state)
    btn_OF_9.bind("<Button-1>", lambda event, operator="O_F9": on_button_operator_click(operator))

    btn_OF_10 = set_gui_el.button(target_frame, "O_F10", 7, 4, state)
    btn_OF_10.bind("<Button-1>", lambda event, operator="O_F10": on_button_operator_click(operator))
    return [btn_OF_1, btn_OF_2, btn_OF_3, btn_OF_4, btn_OF_5, btn_OF_6, btn_OF_7, btn_OF_8, btn_OF_9, btn_OF_10]


def build_operators_s_buttons(target_frame, state, on_button_operator_click):
    # Operators S Buttons
    btn_O_S1 = set_gui_el.button(target_frame, "O_S1", 9, 0, state)
    btn_O_S1.bind("<Button-1>", lambda event, operator="O_S1": on_button_operator_click(operator))

    btn_O_S2 = set_gui_el.button(target_frame, "O_S2", 9, 1, state)
    btn_O_S2.bind("<Button-1>", lambda event, operator="O_S2": on_button_operator_click(operator))

    btn_O_S3 = set_gui_el.button(target_frame, "O_S3", 9, 2, state)
    btn_O_S3.bind("<Button-1>", lambda event, operator="O_S3": on_button_operator_click(operator))

    btn_O_S4 = set_gui_el.button(target_frame, "O_S4", 9, 3, state)
    btn_O_S4.bind("<Button-1>", lambda event, operator="O_S4": on_button_operator_click(operator))
    return [btn_O_S1, btn_O_S2, btn_O_S3, btn_O_S4]


def build_settings_button(settings_frame, command):
    values = ["DM Mass Range", "Integration Precision"]
    settings_btn = segmented_button(settings_frame, values)
    settings_btn.configure(command=command)
    return settings_btn


def build_settings_enter_button(settings_frame, on_dm_range_enter, text):
    enter_btn = ctk.CTkButton(master=settings_frame, text=text, command=on_dm_range_enter, width=100)
    enter_btn.grid(row=7, column=1, pady=(5, 10))
    return enter_btn
