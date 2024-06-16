# Comprehension List
# It specifies an operation to be applied to each item in an existing list and returns a new list with the results of
# these operations.
numbers = [2, 5, 6, 7]
doubled = []

for num in numbers:
    doubled.append(num * 2)

# print(doubled)

# Python has much more way to do this with Comprehension
numbers = [2, 5, 6, 7]
comprehensionList = [x * 2 for x in numbers]
print(comprehensionList)
