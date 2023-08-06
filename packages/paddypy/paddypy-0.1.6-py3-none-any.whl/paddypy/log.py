
from functools import wraps
import time
import logging
import datetime
from opencensus.ext.azure.log_exporter import AzureLogHandler
from . import access

class CloudLogger():
    def __init__(self, app_logger_name, module_name, applicationinsights_key=None, logger_level=10):
        self.LOGGER_LEVEL = logger_level
        self.logger = self._get_logger(app_logger_name=app_logger_name, module_name=module_name, applicationinsights_key=applicationinsights_key, logger_level=self.LOGGER_LEVEL)
        self.logger.setLevel(level=logger_level)

        
    def _get_logger(self, app_logger_name, module_name, applicationinsights_key, logger_level):
        FMT = "[{levelname:^9}] {name}: {message}"
        FORMATS = {
            logging.DEBUG: FMT,
            logging.INFO: "\33[36m{fmt}\33[0m".format(fmt=FMT),
            logging.WARNING: "\33[33m{fmt}\33[0m".format(fmt=FMT),
            logging.ERROR: "\33[31m{fmt}\33[0m".format(fmt=FMT),
            logging.CRITICAL: "\33[1m\33[31m{fmt}\33[0m".format(fmt=FMT)
        }



        class CustomFormatter(logging.Formatter):
            def format(self, record):
                log_fmt = FORMATS[record.levelno]
                formatter = logging.Formatter(log_fmt, style="{")
                return formatter.format(record)

        

        handler = logging.StreamHandler()
        handler.setFormatter(CustomFormatter())
        logging.basicConfig(
            level=logger_level,
            handlers=[handler]
        )

        logger = logging.getLogger(app_logger_name).getChild(module_name)
        # Add the AzureLogHandler for Application Insights
        if applicationinsights_key:
            azure_handler = AzureLogHandler(connection_string=str(applicationinsights_key))
            azure_handler.setLevel(logger_level)
            logger.addHandler(azure_handler)
        return logger

    
    def timeit(self, silence_args=False):
        def actual_decorator(func):
            @wraps(func)
            def timeit_wrapper(*args, **kwargs):
                start_time = time.perf_counter()
                result = func(*args, **kwargs)
                end_time = time.perf_counter()
                total_time = end_time - start_time
                if silence_args:
                    arg_types = tuple(type(arg).__name__ for arg in args)
                    kwarg_types = {key: type(val).__name__ for key, val in kwargs.items()}
                    log_msg = f'Function {func.__name__}{arg_types} {kwarg_types} Took {total_time:.4f} seconds'
                else:
                    log_msg = f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds'

                self.logger.log(msg=log_msg, level=logging.INFO)
                return result
            return timeit_wrapper
        return actual_decorator


    def except_block(self, inst, exceptionMessage="No message"):
        exceptionMessage = exceptionMessage
        exceptionTimne = str(datetime.datetime.now())
        exceptionType = str(type(inst))
        exceptionArgument = str(inst.args)
        exceptionInstance = str(inst)
        self.logger.log(msg="Exception message: {message}".format(message=exceptionMessage), level=logging.ERROR)
        self.logger.log(msg="Exception occured at: {message}".format(message=exceptionTimne), level=logging.ERROR)
        self.logger.log(msg="Exception instance type: {message}".format(message=exceptionType), level=logging.ERROR)
        self.logger.log(msg="Exception argument: {message}".format(message=exceptionArgument), level=logging.ERROR)
        self.logger.log(msg="Exception instance: {message}".format(message=exceptionInstance), level=logging.ERROR)

