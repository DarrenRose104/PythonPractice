while True:

    user_input: str = input('You: ')

    if user_input == 'Hello':
        print('Bot: Hello')
    elif user_input == 'How are you?':
        print('Bot: Good, how are you?')
    elif user_input == 'bye!':
        print('Bot: bye!')
    else:
        print('Bot: Sorry, I did not understand that')