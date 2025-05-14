import ctypes

import customtkinter as ctk


def set_appearance(root):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    root.title("Neutron Star Lab")  # Title of the window
    root.iconbitmap("space_icon.ico")  # Icon next to the title
    root.geometry('1200x650')

    # Change the icon in the Windows bar
    app_id = "neutron_lab.custom.app"  # Set an id for this application
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

    return root


def set_frame(master, expand, fill, padx, pady1, pady2):
    frame = ctk.CTkFrame(master=master)
    frame.pack(expand=expand, fill=fill, padx=padx, pady=(pady1, pady2))
    return frame


def set_side_frame(master, expand, fill, padx, pady1, pady2):
    frame = ctk.CTkFrame(master=master)
    frame.pack(expand=expand, fill=fill, padx=padx, pady=(pady1, pady2), side="left")
    return frame


def set_label(text, target_frame, row, column):
    target_label = ctk.CTkLabel(master=target_frame, text=text, font=("'Tahoma'", 14, "bold"))
    target_label.grid(row=row, column=column, sticky="w", padx=(10, 20), columnspan=2)
    return target_label


def set_informative_label(text, target_frame, row, column):
    informative_label = ctk.CTkLabel(master=target_frame, text=text, font=("'Tahoma'", 14, "bold"), width=300)
    informative_label.grid(row=row, column=column, sticky="w", padx=(10, 20), pady=(20, 20), columnspan=4)
    return informative_label


def button(frame, text, row, column, state):
    button_frame = ctk.CTkButton(master=frame, text=text, state=state)
    button_frame.grid(row=row, column=column, padx=(5, 10), pady=(10, 5))
    return button_frame


def segmented_button(frame, values):
    segmented_settings_button = ctk.CTkSegmentedButton(master=frame, values=values, width=400)
    segmented_settings_button.grid(row=2, column=0, columnspan= 1, padx=10, pady=10, sticky="w")
    segmented_settings_button.set("Standard")  # initial value
    return segmented_settings_button


def set_options(frame, values, column, command_function):
    option = ctk.CTkComboBox(master=frame, values=values, command=command_function)
    option.grid(column=column, padx=(5, 10), pady=(10, 5))
    return option


def set_settings_switch(setting_frame, toggle_settings_panel):
    settings_switch = ctk.CTkSwitch(master=setting_frame, font=("'Tahoma'", 14, "bold"),
                                    text="Enable Integration Settings",
                                    command=toggle_settings_panel)
    settings_switch.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    return settings_switch


def set_entry(frame, text, row, column):
    entry = ctk.CTkEntry(frame, width=100, placeholder_text=text)
    entry.grid(row=row, column=column)
    return entry
