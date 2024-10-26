# GPA Calculator
# Point value grades (A = 4.0 | B = 3.0 | C = 2.0 | D = 1.0 | F = 0.0) 
# GPA = Total Points / Total Credits 


# Iteration 1
class1 = 4.0
class2 = 3.0
class3 = 2.0
class4 = 1.0

totalPoints = class1 + class2 + class3 + class4 
totalCredits = 4

GPA = totalPoints / totalCredits
print(GPA)

# Iteration 2
# added Input

class1 = input('Class 1: ')
class2 = input('Class 2: ')
class3 = input('Class 3: ')
class4 = input('Class 4: ')
totalPoints = class1 + class2 + class3 + class4 
totalCredits = 4

GPA = totalPoints / totalCredits
print(GPA)

# Iteration 3
# added for loop

classes = int(input('How many classes: ')
)
totalPoints = 0
totalCredits = classes

for x in range(int(classes)):
    classPoints = int(input('Class:'))
    totalPoints += classPoints

GPA = totalPoints / totalCredits
print(GPA)

# Iteration 4
# checks

classes = int(input('How many classes: '))

totalPoints = 0
totalCredits = classes

for x in range(classes):
    while True:
        try:
            classPoints = int(input('ClassPoints: '))
            totalPoints += classPoints
            break
        except ValueError:
            print("Please enter a valid number.")

GPA = totalPoints / totalCredits
print("GPA:", GPA)
