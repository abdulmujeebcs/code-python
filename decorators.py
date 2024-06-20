# Authentication Decorator: Decorators allow you to dynamically enhance or modify the behavior of functions. This can
# be particularly useful in scenarios where you need to enable or disable features conditionally.


# Readability and Maintenance
# Decorators can make the code more readable and maintainable by clearly indicating additional behaviors:
# @log_execution_time
# @require_authentication
# def process_data(data):
#     # Function logic here
#     pass

from decorators.auth import require_authentication


@require_authentication
def add(*args):
    total = 0
    for arg in args:
        total += arg

    return total


user = {"name": "John", "is_auth": True}
print(add(user, 1, 41, 5))
