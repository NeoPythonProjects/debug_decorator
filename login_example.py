import functools

# mimic a user database via a list of dictionaries
user_list = [
{"user": "Steven", "pw": "test123"},
{"user": "Louise", "pw": "test456"}
]


def logged_in(my_func):
    # keep introspection intact
    @functools.wraps(my_func)
    def wrapper(*args, **kwargs):
        user = kwargs['user']
        pw = kwargs['pw']
        # DON'T LOOP OVER LISTS CROSS SELL
        # check user list for a match
        # for el in  user_list:
        #     if el['user'] == user and el['pw'] == pw:
        #         # execute
        #     else:
        #         # don't execute
        #         break
        if True in [True if (el['user'] == user and el['pw'] == pw) else False for el in user_list ]:
            # execute my_func
            print(f'user logged in is {user}')
            result = my_func(*args, **kwargs)
        else:
            # don't execute
            print(f'user: {user} has not logged in correctly')
            result = None
        return result
    return wrapper


@logged_in
def application_function(inp1, inp2, user, pw):
    # to use user and pw as kwargs, CALL THEM with =
    # user and pw are used by the decorator, not the application_function
    # see advanced module (my_func is overwritten
    print(f'the sum of {inp1} and {inp2} is {inp1 + inp2}')
    return None


if __name__ == '__main__':

    # matches = [True if (el['user'] == user and el['pw'] == pw) else False for el in user_list]
    # # print(matches[True].__index__())
    # if True in matches:
    #     print('ok')
    # else:
    #     print('no match')

    # from log in process or environment variables
    current_user = 'Louise'
    current_pw = 'test4567'

    application_function(4,6, user = current_user, pw = current_pw)