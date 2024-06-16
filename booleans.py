friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

# IN Keyword: It checks for membership in a list, tuple, set, or string.
print("Rolf" in friends)  # in keywords works in tuple, sets, lists and strings. use case: used to match with
# possible number of choices (active, inactive) status tuple

print(friends == abroad)
print(friends is abroad)  # because memory space is different in abroad due to new list it will True if we initialize
# it to friends like abroad = friends

# Comparisons: = == != > , <, >=, <=

# elif: It specifies another condition to check if the "If"  condition evaluates to False
