from v_interface import set_gui_elements as set_gui_el
import customtkinter as ctk


def build_frames(gui):
    gui.box_frame = set_gui_el.set_frame(gui.root, True, "both", 0, 0, 0)
    gui.target_frame = set_gui_el.set_side_frame(gui.box_frame, True, "both", 10, 10, 10)
    #gui.print_frame = set_gui_el.set_side_frame(gui.box_frame, True, "both", 10, 10, 10)

    # Vertical column box
    gui.right_column_frame = set_gui_el.set_side_frame(gui.box_frame, True, "both", 10, 10, 10)
    gui.right_column_frame.grid_rowconfigure(0, weight=3)  # print_frame più BASSO
    gui.right_column_frame.grid_rowconfigure(1, weight=3)  # settings_frame più ALTO

    gui.right_column_frame.grid_columnconfigure(0, weight=0, minsize=800)

    # Print area (textbox)
    gui.print_frame = ctk.CTkFrame(gui.right_column_frame)
    gui.print_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)

    # Input area (settings)
    gui.settings_frame = ctk.CTkFrame(gui.right_column_frame, fg_color="#2a2a2a",
                                      corner_radius=8, width=800)
    gui.settings_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    gui.settings_frame.grid_columnconfigure(0, weight=1)
    gui.settings_frame.grid_columnconfigure(1, weight=1)
