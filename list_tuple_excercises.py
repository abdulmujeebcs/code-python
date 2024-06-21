# calculate count of student that having A grade using tuple
student_grades = ("A", "D", "C", "B", "A", "B", "C", "D", "A", "D")
print(student_grades.count("A"))

# check palindrome of elements in list
ele = [1, 2, 3, 2, 1]
reverse_list = []
# Reverse the list
for index in range(len(ele) - 1, -1, -1):
    reverse_list.append(ele[index])

print(("!! list is not palindrome !!", "List is palindrome") [reverse_list == ele])
