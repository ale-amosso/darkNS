import logging
from logging.handlers import SocketHandler

# Creation and configuration of the logger
log = logging.getLogger('Root logger')
log.setLevel(logging.DEBUG)  # Set the minimum level of the logs

# FileHandler configuration, for saving the logs in the debug_log.txt file
file_handler = logging.FileHandler("debug_log.txt", mode="w")  # Overwrite the existing file
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# SocketHandler configuration, for sending the log to  Cutelog
socket_handler = SocketHandler('127.0.0.1', 19996)
socket_handler.setLevel(logging.DEBUG)

# Add both Handlers in the logger
log.addHandler(file_handler)
log.addHandler(socket_handler)

# Expose the logger for the import
__all__ = ['log']
