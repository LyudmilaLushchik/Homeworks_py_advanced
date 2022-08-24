from datetime import datetime
from functools import wraps
import os


def logger(path_to_log):
    def _logger(processing_function):
        
        @wraps(processing_function)        
        def log_report(*args, **kwargs):
                        
            result = processing_function(*args, **kwargs)
            date_time = f'{datetime.now()}'
            func_name = f'called function {processing_function.__name__}'
            with_args = f'with args {args} and kwargs {kwargs}'
            res = f'Get {result}'
            report = f'{date_time}\n {func_name}\n {with_args}\n {res}\n'

            if not os.path.exists(path_to_log):
                os.makedirs(path_to_log)

            with open(path_to_log+'//log.txt', 'a', encoding='utf-8') as res_file:
                res_file.write(report)
            
            return result

        return log_report

    return _logger