 

a = int(input("a = "))
b = int(input("b = "))

if a < b :
    print(a,' < ',b)
else:
    print(a,' > ',b)

print('Hello Its me ')

name = input('What is your name ? ')

if len(name) >= 6 :
    print("Your Name is long")
elif len(name) == 5 :
    print("Your name is 5 characters")
elif len(name) >= 4 :
    print("Your name is 4 characters")
else:
    print('Your Name is shorter that 4 characters')