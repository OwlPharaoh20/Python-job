#A dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

#print(person, type(person))

#use constructor
#person2 = dict(first_name='John', last_name='Doe', age=30)
#print(person2, type(person2))


#Get value
#print(person['first_name'])
#print(person.get('last_name'))

#Add Key/Value
person['phone'] = '555-555-5555'

#print(person)

#Get dict keys
#print(person.keys())

#Get dict items
#print(person.items())


#Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

print(person)
print(person2)