# Destructing: To split a collection into separate variables

x,y = 11,22  # tuple
print(x, y)

student_attendance = {"Rolf": 96, "Bob": 80, "Adam": 100}

for tuplee in student_attendance.items():
    print(tuplee)

# Tuple list
people = [
    ("Bob", 42, "Mechanic"),
    ("Abdul", 25, "Software Engineer"),
    ("Rolf", 42, "Electrical Eng"),
]

for person in people:
    print(f"{person[0]}, Age: {person[1]}, Profession: {person[2]}")


head, *tail = [1,2,3,4,5,6]
print(head, tail)

# What does the underscore (_) variable represent in Python?
# Answer: A placeholder for a value that is being ignored.

name, _, profession = ("Bob", 42, "Mechanic")
print(name, profession)

# Reference URL: https://blog.teclado.com/destructuring-in-python/
