def add(a: float, b: float) -> float: #Functions are designed to make the code more reusable. The parameters within the functions are called with the function calls. When the function os changed that also changes the data that is called
    print(f'Adding: {a} + {b}')
    return a + b

print(add(10, 15)) #Function call
print(add(15, 30)) #Function call

def subtract(a: float, b: float) -> float:
    print(f'Subtracting: {a} - {b}')
    return a - b

print(subtract(30, 20)) #Function call
print(subtract(100, 35)) #Function call

def multiply(a: float, b: float) -> float:
    print(f'Multiplying: {a} * {b}')
    return a * b

print(multiply(7, 6)) #Function call
print(multiply(8, 16)) #Function call

def divide(a: float,b: float) -> float:
    print(f'Dividing: {a} / {b}')
    return a / b

print(divide(14, 7)) #Function call
print(divide(21, 9)) #Function call

def greet(name: str, greeting: str) -> None:
    print(f'{greeting}, {name}!')

    greet('Bob', 'Ciao')
