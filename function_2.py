from posixpath import splitext


def welcome (msg,nb):
    for _ in range(nb):
        print("Welcome Home ",msg)

    return f" {msg} is you at home ? I called you {nb} times !"

def return_split(ligne):
    name = ligne.split(' ',2)
    return name[0],name[1] 

def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]

    return initial

first_name= input('Enter your first name: ')
first_name_initial = get_initial(force_uppercase=False, name=first_name)

print('Your initial is: ' + first_name_initial)