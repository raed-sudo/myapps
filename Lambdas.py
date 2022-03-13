def sorter(item):
    return item['name']

presenters = [ 
    {'name':'Susan','age':50},
    {'name':'Christopher','age':47}
]

#presenters.sort(key=sorter)

print('----- by name -----'.upper())
presenters.sort(key=lambda item: item['name'])
print(presenters)

print('----- BY length -----'.upper())
presenters.sort(key=lambda item: len(item['name']))
print(presenters)
