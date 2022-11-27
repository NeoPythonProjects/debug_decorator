from decorators import decorator_debug


def func():
    for i in range(2):
        print(i)
    func_a = 10
    print(locals())
    return func_a


def debug(content: dict):
    print(content)


@decorator_debug
def test_function(pos1, pos2, *other, kw1=None, kw2=None, final=None):
    debug(locals())
    for i in range(4):
        debug(locals())
    return None


if __name__ == "__main__":
    result = test_function(1, 2, 3, 4, 5, 6, final=10)