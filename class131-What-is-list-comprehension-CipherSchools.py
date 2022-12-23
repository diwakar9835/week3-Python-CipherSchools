# list comprehension
# with the help of list comprehension we can create of list in one line

# create a list of square from 1 to 10
squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)

square2 = [i**2 for i in range(1,11)]
print(square2)

negative = []
for i in range(1,11):
    negative.append(-i)
print(negative)

# new_negative = [-i for i in range(1,11)]


names = ['Harshit', 'Mohit','Rohit']
new_list = ['H','M','R']
new_list = []
for name in names:
    new_list.append(name[0])
print(new_list)