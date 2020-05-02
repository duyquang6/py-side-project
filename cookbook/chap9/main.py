# 9.1. Putting a Wrapper Around a Function
#region
# import time
# from functools import wraps


# def timethis(func):
#     '''
#     Decorator that reports the execution time.
#     '''
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(func.__name__, end-start)
#         return result
#     return wrapper


# @timethis
# def countdown(n):
#     '''
#     Count down
#     '''
#     while n > 0:
#         n -= 1


# countdown(10000000)


# class A:
#     @classmethod
#     def method(cls):
#         pass


# class B:
#     # Equivalent definition of a class method
#     def method(cls):
#         pass
#     method = classmethod(method)
#endregion


# 9.2. Preserving Function Metadata When Writing Decorators
#region
# import time
# from functools import wraps

# def timethis(func):
#     '''
#     Decorator that reports the execution time.
#     '''
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(func.__name__, end-start)
#         return result
#     return wrapper

# @timethis
# def countdown(n):
#     '''
#     Count down
#     '''
#     while n > 0:
#         n -= 1
#endregion

### 9.3. Unwrapping a Decorator
#region
# from functools import wraps

# def decorator1(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Decorator 1')
#         return func(*args, **kwargs)
#     return wrapper

# def decorator2(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Decorator 2')
#         return func(*args, **kwargs)
#     return wrapper

# @decorator1
# @decorator2
# def add(x, y):
#     return x + y

# add(2, 3)
# add.__wrapped__(2, 3)
#endregion

### 9.4. Defining a Decorator That Takes Arguments
#region
from functools import wraps
import logging

def logged(level, name=None, message=None):
    '''
    Add logging to a function.  level is the logging
    level, name is the logger name, and message is the
    log message.  If name and message aren't specified,
    they default to the function's module and name.
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')
#endregion