def debug(content, mode='log') -> None:
    """
    debug function writes to terminal or logfile the content variable.
    mode set to default 'print'
    
    further improvements:
    1. changing mode requires updating all debug statements, or the default mode
    2. function name is not available in function itself
    :param content: variable to write
    :param mode: 'print' to print to terminal, 'log' to log to local log.txt file
    :return: None 
    """
    if mode == 'print':
        print(content)
    elif mode == 'log':
        with open('log.txt', 'a') as f:
            for k, v in content.items():
                f.write(str(k))
                f.write(":")
                f.write(str(v)+" ")
            f.write('\n')
        f.close()
    else:
        print("mode needs to be set to either 'print' or 'log'")
        exit()
    return None


def func(var1, var2, *args, kwvar1, kwvar2):
    # calls the decorated debug function
    debug(locals())
    for i in range(3):
        debug(locals())
    return None


if __name__ == "__main__":
    func(1,2,3,4,5,6, kwvar1="kw1", kwvar2="kw2")

