import customtkinter as ctk


def show_custom_messagebox(title, message):
    popup = ctk.CTkToplevel()
    popup.title(title)
    popup.resizable(False, False)

    #popup background color
    popup.configure(fg_color="#2b2b2b")

    width, height = 360, 160
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    popup.geometry(f"{width}x{height}+{x}+{y}")

    # Frame with icon and message
    content_frame = ctk.CTkFrame(popup, fg_color="transparent")
    content_frame.pack(expand=True, fill="both", padx=15, pady=15)

    # Info icon
    #icon_label = ctk.CTkLabel(content_frame, text="🛈", font=("Arial", 32))
    #icon_label.grid(row=0, column=0, padx=(0, 10), sticky="n")

    # Message
    text_label = ctk.CTkLabel(content_frame, text=message, wraplength=260, anchor="w", justify="left")
    text_label.grid(row=0, column=1, sticky="w")

    # OK Button
    ok_button = ctk.CTkButton(popup, text="OK", command=popup.destroy)
    ok_button.pack(pady=(0, 15))


    # Block the main window until the popup is closed
    popup.grab_set()
