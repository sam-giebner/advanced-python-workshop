"""
This is a more advanced logging example.
Messages will print to the screen and to a log file.
"""

import logging

# Define log file name as script name, replacing .py with .log 
log_file = __file__.replace('.py', '.log')

# Create and configure logger
logging.basicConfig(
    filename = log_file, # Define log file path
    format = '%(asctime)s %(message)s', # Add date/time to log messages
    filemode = 'w', # ‘w’ overwrites existing log and ‘a’ appends to existing log
    level = logging.DEBUG) # Set logger to record debug or higher

# Add handler to print messages to terminal
logging.getLogger().addHandler(logging.StreamHandler())

# Log test messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')