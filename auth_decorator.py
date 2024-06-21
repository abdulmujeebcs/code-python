import functools


def require_authentication(function):
    @functools.wraps(function)
    def wrapper(auth_user, *args):
        if auth_user["is_auth"] is True:
            return function(*args)
        else:
            raise RuntimeError("User is not authenticated.")

    return wrapper
