import functools

# Decorator
# = function of a function
# executes the original function
# adds functionality
# wraps up the results
# returns the results = original + new => that's why it needs to wrap these together
# so it can return them together


def debug_decorator(my_func):
    @functools.wraps(my_func)
    def wrapper(*args, **kwargs):
        # executes the original function
        execution = my_func(*args, **kwargs)
        k = 12
        # adds functionality
        print('adding new functionality')
        print(f'debugging function: {my_func.__name__}')
        # ADVANCED: wrapper replaces my_func, so locals() as available
        # but then the parameters IN my_func are not available, e.g. test_i
        # TODO: re-write debug without the need for the debug function? no, misses the test_i parameter values
        print(wrapper.__globals__)
        print(locals())

        # return original results
        return execution

    # return function that combines the original and new functionality
    return wrapper


@debug_decorator
def test_function(inp):
    print(f'original functionality: print the my_func() input parameter value: {inp} ')
    test_i = 5


test_function(10)