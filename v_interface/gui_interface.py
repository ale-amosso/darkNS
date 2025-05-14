# GUI (graphical user interface)

# STANDARD
import threading

# THIRD PARTY
import customtkinter as ctk

# INTERNAL (GUI)
from v_interface import set_gui_elements as set_gui_el
from v_interface.gui_modules import (gui_frames, button_events as events)
from v_interface.gui_modules.gui_labels import build_labels, build_settings_label
from v_interface.gui_modules.gui_buttons import (build_target_buttons, build_operators_f_buttons,
                                                 build_operators_s_buttons, build_settings_button,
                                                 build_settings_enter_button)
from v_interface.gui_modules.progress_bar import ProgressBarComponent
from v_interface.gui_modules import custom_popup as popup

# INTERNAL (Controller)
from controllers.controller_physics import get_total_flux_DM
from settings.integration_settings import DEFAULT_INTEGRATION_SETTINGS, DEFAULT_DM_RANGE_SETTINGS, \
    parse_scientific_input
from v_interface.gui_modules import gui_settings_panel as settings_panel
from v_interface.gui_modules import gui_inputs as inputs


def get_default_settings():
    return {
        "integration_precision": DEFAULT_INTEGRATION_SETTINGS.copy(),
        "dm_mass_range": DEFAULT_DM_RANGE_SETTINGS.copy()
    }


class GUIInterface:
    def __init__(self):
        # CREATES THE WINDOW
        self.root = ctk.CTk()
        set_gui_el.set_appearance(self.root)

        # FRAME INITIALIZATION: GUI frames for different sections of the interface
        self.print_frame = None
        self.target_frame = None
        self.settings_frame = None
        self.box_frame = None

        # LABELS INITIALIZATION: Labels displayed in the GUI
        self.operators_S_label = None
        self.target_label = None
        self.operators_F_label = None
        self.informative_label = None

        # WIDGET INITIALIZATION: Widget for switching settings view
        self.settings_switch = None

        # TEXT VARIABLES
        self.previous_text = ""
        self.selected_target = None  # Store selected target
        self.print_result_text = None

        # SETTINGS INITIALIZATION: Input and buttons fields for integration and DM mass range settings
        self.settings_entry = None
        self.range_summary = None
        self.default_range_button = None
        self.min_entry = None
        self.max_entry = None
        self.points_entry = None
        self.neval_entry = None
        self.nitn_entry = None
        self.alpha_entry = None
        self.enter_btn = None

        # Current state of the input parameters
        self.settings_state = get_default_settings()
        self.dm_range_locked = False
        self.integration_locked = False

        # BUTTONS: Operators and settings (segmented) button
        self.operator_buttons = []  # Store operator buttons
        self.segmented_button = None

        # PROGRESS BAR: Progress bar widget shown during computation
        self.progress = None

        # COMPUTING THREAD: Threading for running long computations without freezing the GUI
        self.stop_event = threading.Event()
        self.current_thread = None

        # BUILD GUI
        self.build_interface()
        self.create_widgets()

    def run(self):
        self.root.mainloop()

    def build_interface(self):
        gui_frames.build_frames(self)

    def create_widgets(self):
        # Set up static labels
        self.create_labels()

        # Create target and operator buttons
        self.create_buttons()

        # Add a dynamic label for user messages: Es. "You chose neutron target with operator O_1F"
        self.create_informative_label()

        # Add a toggle to show/hide advanced settings
        self.create_settings_switch()

        # Set up the text area for displaying text, as the information about the model
        self.create_textbox()

        # Show initial result (total DM flux)
        self.add_text_to_print_frame(get_total_flux_DM())

        # Add a progress bar for tracking computation
        self.create_progress_bar()

    def create_labels(self):
        build_labels(self.target_frame)

    def create_informative_label(self):
        self.informative_label = set_gui_el.set_informative_label("", self.target_frame, row=99, column=0)

    def create_settings_switch(self):
        self.settings_switch = set_gui_el.set_settings_switch(self.settings_frame, lambda: settings_panel.toggle_settings_panel(self)
)

    def create_buttons(self):
        build_target_buttons(self.target_frame, "normal", self.on_button_model_click, self.on_target_button_click)
        self.segmented_button = build_settings_button(self.settings_frame, lambda val: settings_panel.display_settings_fields(self, val)
)
        self.segmented_button.grid_remove()

        # Create operator buttons and store them
        self.operator_buttons = []  # Reset operator buttons list
        self.operator_buttons.extend(
            build_operators_f_buttons(self.target_frame, "normal", self.on_button_operator_click))
        self.operator_buttons.extend(
            build_operators_s_buttons(self.target_frame, "normal", self.on_button_operator_click))

    def create_textbox(self):
        self.print_result_text = ctk.CTkTextbox(self.print_frame, wrap="word")
        self.print_result_text.pack(expand=True, fill="both")
        self.print_result_text.configure(font=('Tahoma', 15))

    def create_progress_bar(self):
        self.progress = ProgressBarComponent(self.target_frame)

    def add_text_to_print_frame(self, new_text, clear_text=False):
        if clear_text:
            self.print_result_text.delete("1.0", "end")
            self.previous_text = ""
        self.previous_text += new_text + "\n"
        self.print_result_text.insert("end", self.previous_text)

    def update_progress(self, value):  # value in [0.0, 1.0]
        self.progress.update(value)
        if value >= 1.0:
            self.progress.hide()

    def cancel_calculation(self):
        self.stop_event.set()
        self.progress.hide()
        self.informative_label.grid_remove()

    def on_target_button_click(self, target):
        events.handle_target_click(self, target)

    def on_button_model_click(self, target):
        events.handle_model_click(self)

    def on_button_operator_click(self, operator):
        events.handle_operator_click(self, operator, self.settings_state)

    def enable_operator_buttons(self):
        """Enable all operator buttons"""
        for button in self.operator_buttons:
            button.configure(state="normal")  # Enable buttons








