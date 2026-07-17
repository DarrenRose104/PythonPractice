import random #Imports the random function into the code.

print('Hello! Welcome to the number guessing game! You have to guess between 1 and 100, however you only 10 chances to get it correct.') #Prints the statement placed within the parentheses.

number = random.randint(1, 100) #the two number within the parameter fields are what the random number will be and this is saved into the variable "number".

chances: int = 10 #This variable represents how many chances the user will get to guess.

guesses: int = 0 #This variable represents how many guesses the user has had.

while chances > guesses: #The while loop will only exit once guesses have exceeded the number of chances.

    guesses += 1 #The guesses variable is having 1 added for every guess that is made.

    try: #Used to execute code and handle errors in a way the user understands.
        user_input: int = int(input('Guess a number between 1 and 100: ')) #Used to capture the user input.

        if user_input == number:  #The if statement takes the value of the user input and checks if it is the same as the assigned value. If it is then the statement below will print.
            print('Correct! You guessed the number correctly.')

        elif user_input > number:  # The elif statement takes the value of the user input and checks if it is greater than the assigned value of number. If it is then the statement below will print.
            print('Too high! Try again.')

        elif user_input < number:  # The elif statement takes the value of the user input and checks if it is greater than the assigned value of number. If it is then the statement below will print.
            print('Too low! Try again.')

    except ValueError: #The exception is used with the try block to give feedback to the user so they can enter the correct data. ValueError is used because the code needs an integer and not a string.
        print('Please enter a number!')

print('You have run out of guesses! Feel free to try to guess the number again!')
