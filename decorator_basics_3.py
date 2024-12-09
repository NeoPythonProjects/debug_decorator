import functools

# Decorator
# = function of a function
# executes the original function
# adds functionality
# wraps up the results
# returns the results = original + new => that's why it needs to wrap these together
# so it can return them together


def my_decorator(my_func):
    # wraps up the results -> in a function, e.g. 'wrapper'
    # KEEP INTROSPECTION OF ORIGINAL FUNCTION INTACT
    @functools.wraps(my_func)
    def wrapper(*args, **kwargs):
        # executes the original function
        execution = my_func(*args, **kwargs)
        # adds functionality
        print('adding new functionality')
        # return original results
        return execution

    # return function that combines the original and new functionality
    return wrapper


@my_decorator
def test_function(inp):
    print(f'original functionality: print the my_func() input parameter value: {inp} ')


test_function(10)