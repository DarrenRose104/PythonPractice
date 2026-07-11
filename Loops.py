for i in range(3):
    print('Hello')


names: list[str] = ["Bjorn", "james", "Steve"]

for name in names:
    print(f'Hello {name}')
    print('How are you?')


i: int = 0

while i < 3:
    print(i)
    i+= 1


a: int = 0

while a < 11:
    print(a)
    a+= 1


food: list[str] = ['Cheese', 'Bacon', 'blueberries', 'Raspberries', 'Bananas', 'Greek yoghurt']

for food in food:
    print(f'Do you have {food}?')
    print('Thank you for your help!')