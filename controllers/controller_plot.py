from functions.plot.lambda_plot import plot_lambda_dm
from v_interface.gui_modules import custom_popup as popup
import threading


def handle_plot_lambda(operator, target, integration_settings, progress_callback=None, stop_event=None):
    """Creates the plot for a specific operator."""
    print(target)
    return plot_lambda_dm(operator, target, integration_settings, progress_callback=progress_callback, stop_event=stop_event)


def start_calculation_thread(gui, operator, integration_settings):
    """
    Launches the calculation thread if no active one is running.
    """
    if gui.current_thread and gui.current_thread.is_alive():
        popup.show_custom_messagebox(
            "Warning", "⏳ A calculation is already running. Press Cancel to stop it before launching another."
        )
        return

    gui.progress.show(on_cancel=gui.cancel_calculation)
    gui.progress.update(0)

    gui.stop_event.set()
    gui.stop_event = threading.Event()

    thread = threading.Thread(
        target=handle_plot_lambda,
        args=(operator, gui.selected_target,integration_settings),
        kwargs={
            "progress_callback": gui.update_progress,
            "stop_event": gui.stop_event
        },
        daemon=True
    )
    thread.start()
    gui.current_thread = thread
