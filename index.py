user_input = input ("Please enter a Message: ")

print("The First character :",user_input[0])
print("The last character :", user_input[len(user_input)-1])
print("The middle character : ", user_input[round((len(user_input)-1)/2)])
print("Every index characters : ", user_input[::2])
print("Odd index characters :", user_input[1::2] )
print("Reversed message: ", user_input[::-1] )
