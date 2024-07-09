#In Python, the == operator checks for equality of values, while the is operator checks for object identity.

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

# IN Keyword: It checks for membership in a list, tuple, set, or string.
print("Rolf" in friends)  # in keywords works in tuple, sets, lists and strings. use case: used to match with
# possible number of choices (active, inactive) status tuple

print(friends == abroad)
print(friends is abroad)

""""
== (Equality operator): Checks whether the values of two operands are equal.
is (Identity operator): Checks whether two operands are the same object in memory.
"""

# Comparisons: = == != > , <, >=, <=

# elif: It specifies another condition to check if the "If"  condition evaluates to False
