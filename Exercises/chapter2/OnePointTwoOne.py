x = 2
y = 3

print('x = ', x)  # prints the value of x.

print('value of', x, '+', x, 'is', (x + x))  # prints the value of (x + x)

print('x = ')  # this is just a print statement

print((x + y), '= ', (y + x))  # prints the value of (x + y) and also (y + x).



radius = int(input('Enter radius: '))
pi = 3.14159

Diameter = 2 * radius
print(f'diameter is {Diameter}')

Circumference = 2 * pi * radius
print(f'Circumference is {Circumference}')

Area = pi * radius * radius
print(f'Area is {Area}')



rating = input('Enter an Integer  rating between 1 and 10')

# a = int(input('Enter an Integer  rating between 1 and 10'))
#
# print(rating + a)

# python does not collect other inputs via this method asides strings so it needs to be casted to an int.


# let x be the right operand

# let y be the right operand


x = 27.5
y = 2

print(27.5 + 2)

print(27.5 - 2)

print(27.5 * 2)

print(27.5 / 2)

print(27.5 // 2)



grade = 95

if grade >= 90:
    print('congratulations! your grade of', grade,
          ' has earned you an A in this Course')