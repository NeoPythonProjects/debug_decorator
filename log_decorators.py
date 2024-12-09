import functools

from datetime import datetime as dt

# global switch
# SWITCH = "" frees up the individual choices
SWITCH = "log"

def log_mode(mode):
    """
    decorator takes 1 'mode' argument
    mode = 'print' or 'log' or 'off'
    'print' prints to the terminal
    'log' saves to a logfile
    'off' ignores extra functionality

    foo is the log function
    have the printing or logging happen in the decorator
    that avoids needing to define the mode in every log() call or changing the default value of the mode argument
    With the decorator you only need to change the decorator at the top of the function
    Decorator calls the function so the function name is available (function name is not available in the function itself)

    Downside is that everything will always be printed or logged
    What if I want to only log or print certain functions
    I then need a mode variable in the decorator above the function
    :param mode: 'print' or 'log' or 'off'
    :return: decorated foo as wrapper
    """
    def decorator(foo):
        # keep introspection of inner functions intact
        @functools.wraps(foo)
        def wrapper(*args, **kwargs):
            # 1. get the output from the decorated function
            lst_output = foo(*args, **kwargs)
            # 2. read the function name
            # which can't be read from within the function itself
            # use a decorator to pass the function into and then the name is available
            lst_output.append(foo.__name__)
            # 3. print or log
            date_str = dt.now().strftime("%d%b%Y")
            if mode == 'print':
                print(date_str, lst_output[-1], lst_output[:-1])
            elif mode == 'log':
                with open('log.txt', 'a') as f:
                    f.write(f"{date_str}:{lst_output[-1]} -> {lst_output[:-1]}")
                    f.write('\n')
            elif mode == 'off':
                pass
            else:
                print("mode needs to be set to either 'print' or 'log'")
            # return the executed function func(), or the object that represents it
            return lst_output
        # return wrapper function (don't execute)
        return wrapper
    return decorator


@log_mode('log')
def log(content) -> list:
    """
    This is the log function that will be called instead of a print function
    :param content: object that needs to get logged or printed
    :return:
    """
    output = []
    if type(content) == dict:
        # convert dictionary to list
        # add key - value pair to list a single string k:v
        output = [f"{str(k)}:{str(v)}"
                  for k, v in content.items()]
    elif type(content) == list:
        output = content
    else:
        output.append(content)
    return output


def log_or_print(content, mode):
    # process the content into a list
    output = []
    if type(content) == dict:
        # convert dictionary to list
        # add key - value pair to list a single string k:v
        output = [f"{str(k)}:{str(v)}"
                  for k, v in content.items()]
    elif type(content) == list:
        output = content
    else:
        output.append(content)

    # decide on output based on mode
    date_str = dt.now().strftime("%d%b%Y")
    if mode == 'print':
        print(date_str, output)
    elif mode == 'log':
        with open('log.txt', 'a') as f:
            f.write(f"{date_str}:{output}")
            f.write('\n')
    elif mode == "off":
        pass
    else:
        raise Exception(f"mode {mode} not recognised in log_or_print -> should be 'print', 'log' or 'off'")


def func(var1, var2, *args, kwvar1, kwvar2):
    log(locals())
    for i in range(3):
        log(locals())
    return None


def log_(mode):
    """
    shows a wat to pass the decorator parameter value to the decorated foo
    :param mode:
    :return:
    """
    def decorator(foo):
        # keep introspection of inner functions intact
        @functools.wraps(foo)
        def wrapper(*args, **kwargs):
            # execute original function but populate test_mode parameter
            # if test_mode is passed as a keyword variable it will be overwritten
            # if test-mode isn't passed as a keyword, it's added to the dict here
            kwargs["test_mode"] = mode
            foo_result = foo(*args, **kwargs)
            # add functionality: none
            # return the executed original function
            return foo_result
        return wrapper
    return decorator

@log_("print" if not SWITCH else SWITCH)
def test(test_mode=""):
    # pass the parameter value of the decorator tp the decorated function
    # downside is that you need to pass the test_mode as an arg or kwarg in every
    # decorated function
    # upside is you can for each function decide what to do with the output

    # so, either you decorate the log function to pass from decorator to log function
    # in which case the logging is the same wherever it's applied
    # or
    # the logging is specific for each decorated foo (not log function), but then you need
    # to pass the test_mode from decorator to foo to log-function
    str = {"e": [1,2,3], "f": [4,567]}
    log_or_print(str, test_mode)

if __name__ == "__main__":
    # func(1,2,3,4,5,6, kwvar1="kw1", kwvar2="kw2")
    test()

