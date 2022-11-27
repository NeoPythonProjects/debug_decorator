def foo(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    return None


foo(1,2,3,t=4)



