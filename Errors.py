def divide(divisor, divider):
    if divider == 0:
        raise ZeroDivisionError("Divisor should not be zero.")
    return divisor / divider


grades = [23, 76, 89, 12, 66, 33]
# grades = [] #un comment this to check try catch
average = 0

try:
    average = divide(sum(grades), len(grades))
    average = round(average, 2)
except ZeroDivisionError:
    print("Average cannot be calculated due to empty grades")
else:
    print(f"Average of grades is {average}")

# For Custom Error Class just create any class and extend from ValueError and pass in one first line that's it
