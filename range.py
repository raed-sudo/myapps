upper_number = int(input("How many valie should we preocess: "))
for number in range(1, upper_number + 1):
    if number % 3 == 0 and number % 5 == 0 :
        print(number, ' = FizzBuzz')
        continue
    elif number % 3 == 0 :
        print(number, ' = Fizz')
        continue
    elif number % 5 == 0: 
        print(number, ' = Buzz')
        continue
    else:
        print (number)
