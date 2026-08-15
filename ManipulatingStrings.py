a: str = "Hello World" #Strings are arrays, and I am using the square brackets to access the specific elements of the string.

print(a[0])
print(a[3])
print(a[8])


for x in "Hello world": #Looping through the strings as they are arrays
    print(x)

for z in "Chocolate milkshake":
    print(z)


b: str = "Chocolate milkshake" #Using the function len() to see how many characters are held within specific strings
print(len(b))

c: str = "Chocolate icecream"
print(len(c))


d: str = "I love chocolate milkshake!" #Utilising the keyword "in" to find whether a word is contained within a string
print("love" in d)
print("yum" in d)

e: str = "I love Warhammer 40K"
print("Warhammer" in e)


f: str = "I love chocolate milkshake!" #Pairing the keyword "in" with if statements to find a word in a string and printing if it is in the string or not. This can also be used with the keywords "not in"
if "milkshake" in f:
    print("Yes, 'milkshake' is present")
else:
    print("No, 'milkshake' is not present")

g: str = "I love chocolate milkshake!"
if "spicy" in g:
    print("Yes, 'spicy' is present")
else:
    print("No, 'spicy' is not present")


h: str = "I love chocolate milkshake" #Exploring the concept of string slicing
print(h[2:5]) #This line specifies the start and end index for the string in the line above
print(h[7:26])
print(h[:6]) #This line will only print up to the 6th character in the array
print(h[7:]) #This line will only print from the 7th character in the array