import functools

"""
Technical Detail: The @functools.wraps decorator uses the function
functools.update_wrapper() to update special attributes like
__name__ and __doc__ that are used in the introspection.
"""

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

@decorator
def decorate_this_function(# pass something here):
    # do something here
    return # return something here
