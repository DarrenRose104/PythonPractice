a, b = 10, 'fiften'

try:
    print(a + b)
except TypeError as e:
    print('Please enter a number in the form of an integer or a float!')

print('Continuing with the program:')