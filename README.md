# Custom Logger
This is a simple Python package that provides a logging function to log errors with traceback information.

## Installation
You can install the package using pip:

```python
pip install custom_logger
```

## Usage
To use the logging function, simply import it from the package and call it in your code:


```python Copy code
from custom_logger.logger import logger

def my_function():
    try:
        # Some code that may raise an error
    except Exception as e:
        logger()
```

By default, the logger will log only errors to both the console and a log file called example.log in the current directory. You can customize the logging behavior by passing arguments to the logger() function:

```python
logger(verbosity_level=2, log_to='console')
```

The verbosity_level argument controls the level of logging detail, with higher values producing more detailed logs. The log_to argument controls where the logs are sent, and can be set to 'file' to log to a file only, 'console' to log to the console only, or 'both' to log to both.

## License
This package is licensed under the MIT License. See the LICENSE file for more information.