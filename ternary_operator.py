"""
 Clever If / Ternary Operator using Python Tuple (false_value, true_value) [<Condition>] In this case we declare the
 False and True values inside a tuple at index 0 and 1 respectively. Based on the condition, if the result is False,
 that is 0 the value at index 0 gets executed. If the condition results in True, the value at index 1 of the tuple
 is executed.
"""

# 0 - 50K salary then tax would be 10%
# 50k - tax would be 20%
sal = float(input("Enter your salary"))
tax = sal* (0.2, 0.1) [sal <= 50000]
print(tax)


# Program to demonstrate ternary operator using if else
a = 10
b = 20

# python ternary operator
min = "a is minimum" if a < b else "b is minimum"

print(min)
