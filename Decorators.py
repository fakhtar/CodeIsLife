def list_decorator(function):
    def wrapper(name):
        my_list = []
        for c in name:
            my_list.append(c)
        return my_list
    return wrapper


def title_decorator(function):
    def wrapper(name):
        to_title = function(name).title()
        return to_title
    return wrapper

def uppercase_decorator(function):
    def wrapper(name):
        to_upper = function(name).upper()
        return to_upper
    return wrapper

@list_decorator
@title_decorator
def say_hi (name):
    return 'Hello ' + name

print(say_hi('faisal'))