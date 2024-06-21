"""
The Collection of unordered items
Each element in the set unique and immutable
Set cannot store list and dictionary due to mutability
"""

l = ["Rob", "john", "walton", "alice"]  # add or remove elements and have keep in order
tpl = ("Rob", "alice")  # can not add/remove elements immutable + keep in order
setElements = {"Rob", "Wah", "Walton"}  # only unique elements in set and order is not guaranteed so we can't access
# element directly as we did in tuple and list like list[1]

l.append("John wick")
setElements.add("Smith")  # also have functions like intersection, union and difference
setElements.add("Smith")
# print(l)
print(setElements)
# https://blog.teclado.com/python-set-operators/

# How empty set defined Answer: set()