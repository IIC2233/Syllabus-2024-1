# from functools import wraps
# import signal
# import platform

# """
# Código del TimeoutError extraido y adaptado de
# https://github.com/pnpnpn/timeout-decorator/tree/master
# """
# N_SECOND = 1


# class TimeoutError(AssertionError):

#     """Thrown when a timeout occurs in the `timeout` context manager."""

#     def __init__(self, value="Timed Out"):
#         self.value = value

#     def __str__(self):
#         return repr(self.value)


# def timeout(seconds=None):
#     def decorate(function):
#         def handler(signum, frame):
#             raise TimeoutError("Timeout")

#         @wraps(function)
#         def new_function(*args, **kwargs):
#             new_seconds = kwargs.pop("timeout", seconds)
#             if new_seconds:
#                 old = signal.signal(signal.SIGALRM, handler)
#                 signal.setitimer(signal.ITIMER_REAL, new_seconds)

#             if not seconds:
#                 return function(*args, **kwargs)

#             try:
#                 return function(*args, **kwargs)
#             finally:
#                 if new_seconds:
#                     signal.setitimer(signal.ITIMER_REAL, 0)
#                     signal.signal(signal.SIGALRM, old)

#         if platform.system().lower() == "windows":
#             return function
#         return new_function

#     return decorate

## FUNCION PARA WINDOWS, LO ANTERIOR FUNCIONA PARA MAC


import threading
import functools

def timeout(seconds=10, error_message="El tests no finaliza dentro del tiempo máximo asignado."):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = [Exception(error_message)]

            def target():
                try:
                    result[0] = func(*args, **kwargs)
                except Exception as e:
                    result[0] = e

            thread = threading.Thread(target=target)
            thread.daemon = True
            thread.start()
            thread.join(seconds)
            if isinstance(result[0], Exception):
                raise result[0]
            return result[0]
        
        return wrapper
    
    return decorator