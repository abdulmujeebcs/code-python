""""
Dictionary: To associate keys and values together. only strings and integers will be used as key in dictionary.
They are unordered, mutable change value after created & don't allow duplicate keys
"""

friends = [
    {"name": "Rolf", "age": 30},
    {"name": "John", "age": 20},
    {"name": "Wick", "age": 27},
]

print(friends[1]["name"])

student_attendance = {"Rolf": 96, "Bob": 80, "Adam": 100}
# for student in student_attendance:
# print(f"{student}: {student_attendance[student]}")

# better way
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

if "Bob" in student_attendance:
    print("Bob Does not attend any class")


print(student_attendance.values())

# Exercise
my_dictionary = {'a': 1, 'b': 2, 'c': 3}
items = list(my_dictionary.items())
print(items)
"""
Methods
myDic.keys()
myDic.values()
myDic.items() return all (key, value) pairs as tuples
myDic.get("Key") return the key according to value
myDic.update(newDic) insert the specified items into the dictionary
"""
