# Create a dictionary mapping usernames to user tuples.

user_data = [
    ("admin1", "Rolf", "Address 1"),
    ("john-uk", "John", "Address 2"),
    ("mari5", "Maria", "Address 3"),
]

user_mapping = {user[0]: user for user in user_data}
print(user_mapping)
