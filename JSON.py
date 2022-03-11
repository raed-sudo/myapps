# CREATE A DICTIONARY OBJECT : 
import json

person_dict = {'first':'Christopher','last':'Harrison'}

# ADD ADDITIONAL KEY PAIRS AS NEEDED TO DICTIONARY
person_dict['City']='Seattle'

# CONVERT DICTIONARY TO JSON OBJECT
person_json = json.dumps(person_dict)
print(person_json)

# CREATE STAFF DICTIONARY WHICH ASSIGNS A PERSON TO A ROLE
staff_dict ={}
staff_dict['Program Manager']=person_dict

# CONVERT?DICTIONARY TO JSON OBJECT
staff_json = json.dumps(staff_dict)

# PRINT JSON OBJECT
print(staff_json)

# CREATE A LIST OBJECT OF PROGRAMMING LANGUAGES
language_list = ['CSharp','Python','JavaScript']

#ADD LIST TO DICTIONARY 
person_dict['language']=language_list

#ADD LIST TO DICTIONARY TO JSON OBJECT
person_json = json.dumps(person_dict)
print(person_json) 

