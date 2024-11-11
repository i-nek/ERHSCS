# Keywords
# False
# True
# None
# and
# break
# def
# if
# elif
# else
# return
# while
# or
# not

# conditionals
# if/elif/else
# conditions

num1 = 5
num2 = 2
x = 5 < 2 # false

def foo():
    if (x) :
        return True
    else:
        return False
def foo2():
    if (x):
        return True
    elif not (x):
        return False

print(x)
print(foo2())


x = 5 > 2 # true

if (x) :
     print("The statement is True")
else:
    print("The statement is False")

# User info
name = "Adrian James Pili"
age = 22
is_student = True

# Using a basic condition to check age and student status
if age >= 18:
    print(name + " is an adult.")
else:
    print(name + " is a minor.")

# Nested condition: checking if the person is a student
if is_student:
    print(name + " is a student and can receive a discount.")
else:
    print(name + " is not a student.")

# Performing and printing various operations
num1 = 15
num2 = 7

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Displaying results with concatenation
print(name + " performed some math operations:")
print("Addition: " + str(num1) + " + " + str(num2) + " = " + str(addition))
print("Subtraction: " + str(num1) + " - " + str(num2) + " = " + str(subtraction))
print("Multiplication: " + str(num1) + " * " + str(num2) + " = " + str(multiplication))
print("Division: " + str(num1) + " / " + str(num2) + " = " + str(division))

# Adding a complex condition to categorize the result
if addition > 20:
    print("The sum is a large number.")
elif addition == 20:
    print("The sum is exactly 20.")
else:
    print("The sum is a small number.")

# Using comparison operators with a variable
if age >= 18 and is_student:
    print(name + " is an adult and a student.")
elif age >= 18 and not is_student:
    print(name + " is an adult but not a student.")
        
