def calcul():
    return " Hello world !"
def welcome(name,age,sex):
    return f"Hello {name}, You have {age}, You are a {sex}"
def split_name(name):
    names = name.split()
    first_name = names[0]
    last_name = names[-1]
    return {
        'first_name': first_name,
        'last_name': last_name
    }
assert split_name("Kevin Bacon") == {
    "first_name": "Kevin",
    "last_name": "Bacon",
}, f"Expected {{'first_name': 'Kevin', 'last_name': 'Bacon'}} but received {split_name('Kevin Bacon')}"
def is_palindrome(item):
    return item == item[::-1]
print(is_palindrome('radar'))
#assert is_palindrome("radar") == True, f"Expected True but got {is_palindrome('radar')}"
#assert is_palindrome("stop") == True, f"Expected False but got {is_palindrome('stop')}"
def build_list(item, count=1):
    items = []
    for _ in range(count):
        items.append(item)
    return items
def get_lenght(list):
    count=0
    for element in list:
        count += 1
    return count
print(build_list('Apple',5))
apples= build_list('Apple',5)
print(len(apples))
apples.insert(get_lenght(apples),'Raed')
print(apples)