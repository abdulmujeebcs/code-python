# First Class Functions: functions are just variables  you can pass them in arguments to the function
def divide(divisor, divider):
    if divider == 0:
        raise ZeroDivisionError("Divisor should not be zero.")
    return divisor / divider


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 5, operator=divide)
print(result)


def search(sequence, expected, finder):
    for seq in sequence:
        if finder(seq) == expected:
            return seq
    raise RuntimeError("could not find element")


friends = [
    {"name": "Rolf Smith", "age": 34},
    {"name": "John wick", "age": 20},
    {"name": "Bob Smith", "age": 20}
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "John wick", get_friend_name))
# OR print(search(friends, "John wick", lambda friend: friend["name"]))
