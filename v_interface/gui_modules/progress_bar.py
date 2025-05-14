import customtkinter as ctk


class ProgressBarComponent:
    def __init__(self, parent_frame, width=400, height=20, row=100, column=0, columnspan=5):
        self.frame = ctk.CTkFrame(parent_frame, fg_color="transparent")

        # Percent label
        self.label = ctk.CTkLabel(
            master=self.frame,
            text="0%",
            text_color="white",
            font=("Tahoma", 14)
        )
        self.label.grid(row=0, column=0, pady=(0, 5))

        # Progress bar
        self.bar = ctk.CTkProgressBar(master=self.frame, width=width, height=height, border_width=1)
        self.bar.grid(row=1, column=0, pady=(0, 5))

        # Cancel button (initially no command)
        self.cancel_button = ctk.CTkButton(
            master=self.frame,
            text="Cancel",
            fg_color="#3a3f4b",
            hover_color="#aa3333",
            text_color="white",
            command=lambda: None  # placeholder
        )
        self.cancel_button.grid(row=2, column=0, pady=(0, 10))

        # Default grid config
        self._grid_args = {"row": row, "column": column, "columnspan": columnspan, "pady": (10, 0)}

        self.hide()

    def grid(self, **kwargs):
        args = {**self._grid_args, **kwargs}
        self.frame.grid(**args)

    def update(self, value: float):
        self.bar.set(value)
        self.label.configure(text=f"{int(value * 100)}%")
        self.label.update_idletasks()

    def show(self, on_cancel=None):
        if on_cancel:
            self.cancel_button.configure(command=on_cancel)
        self.grid()

    def hide(self):
        self.frame.grid_remove()
