age: int = 10 #The type annotation is ignored by the console however it is used to help developers and python to know what you are doing

first_name: str = "Bob"

print("Name: " + first_name + ", Age: " + str(age))

print(f"Name: {first_name}, Age: {age}")#F strings are used to help format the data within the print() parameters, it is the same as above however is a cleaner and tider way of printing the information

food: str = "Cheese"

number: int = 6

print(f"food: {food}, number: {number}")

place: str = "London"

measurement: float = 3.5

print(f"place: {place}, measurement: {measurement}cm")