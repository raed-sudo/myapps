def print_something(message):
    print(message)

def add_to (num):
    return num +2
print_something('Hello World')
add_to(5)

def contact_card(name,age, car_model): 
    
    return f"{name} is {age} and drives a {car_model}"

print(contact_card('Kevin',28,'Honda Cevic'))

print(contact_card(age=28,car_model="ISUZU",name='Mohamed'))
