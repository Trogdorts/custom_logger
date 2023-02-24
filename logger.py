import logging
import inspect
import sys

def logger(verbosity_level=0, log_to='both'):
    """
    Logs an error message with traceback information.

    Parameters:
    verbosity_level (int): The verbosity level of the logging output. The default is 0, which logs only errors.
    log_to (str): Where to send the logs. Can be 'file' to send logs only to a file, 'console' to send logs only to the console (stdout), or 'both' to send logs to both the file and the console. The default is 'both'.

    Raises:
    ValueError: If an invalid value is provided for the log_to argument.

    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create file handler
    file_handler = logging.FileHandler('example.log')
    file_handler.setLevel(logging.ERROR)

    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.ERROR)

    # Create formatter and add to handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to logger based on log_to argument
    if log_to == 'file':
        logger.addHandler(file_handler)
    elif log_to == 'console':
        logger.addHandler(console_handler)
    elif log_to == 'both':
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    else:
        raise ValueError(f"Invalid value for log_to argument: {log_to}")

    # Set logging level based on verbosity level
    if verbosity_level == 0:
        logger.setLevel(logging.ERROR)
    elif verbosity_level == 1:
        logger.setLevel(logging.WARNING)
    elif verbosity_level == 2:
        logger.setLevel(logging.INFO)
    elif verbosity_level >= 3:
        logger.setLevel(logging.DEBUG)

    # Get traceback information
    exc_type, exc_obj, tb = sys.exc_info()
    line_number = tb.tb_lineno
    function_name = inspect.currentframe().f_back.f_code.co_name
    calling_function_name = inspect.currentframe().f_back.f_back.f_code.co_name

    # Log error message with traceback information
    logger.error(f"Error in function {function_name} called from {calling_function_name} at line {line_number}")
