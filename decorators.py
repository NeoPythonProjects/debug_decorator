import functools


def debugmode(mode):
    """
    decorator takes 1 'mode' argument
    mode = 'print' or 'log' or 'off'
    print prints to the terminal
    log saves to a logfile

    foo is the debug function
    have the printing or logging happen in the decorator
    that avoids needing to define the mode in every debug() call or changing the default value of the mode argument
    With the decorator you only need to change the decorator at the top of the function
    Decorator calls the function so the function name is available (function name is not available in the function itself)
    :param mode: 'print' or 'log' or 'off'
    :return:
    """
    def decorator(foo):
        # keep introspection of inner functions intact
        @functools.wraps(foo)
        def wrapper(*args, **kwargs):
            # 1. get the ouput from the decorated function
            lst_output = foo(*args, **kwargs)
            # 2. read function name
            # function name can't be read from within the function itself
            # use a decorator to pass the function into and then the name is available
            lst_output.append(foo.__name__)
            # 3. print of log
            if mode == 'print':
                print(lst_output[-1], lst_output[:-1])
            elif mode == 'log':
                with open('log.txt', 'a') as f:
                    f.write(f"{lst_output[-1]} -> {lst_output[:-1]}")
                    f.write('\n')
            elif mode == 'off':
                pass
            else:
                print("mode needs to be set to either 'print' or 'log'")
            # return the executed function func(), or the object that represents it
        # return wrapper function (don't execute)
        return wrapper
    return decorator


@debugmode('log')
def debug(content) -> list:
    output = []
    if type(content) == dict:
        # convert dictionary to list
        for k, v in content.items():
            # add key - value pair to list a single string k:v
            output.append(f"{str(k)}:{str(v)}")
    elif type(content) == list:
        output = content
    else:
        output.append(content)
    return output


def func(var1, var2, *args, kwvar1, kwvar2):
    debug(locals())
    for i in range(3):
        debug(locals())
    return None


if __name__ == "__main__":
    func(1,2,3,4,5,6, kwvar1="kw1", kwvar2="kw2")