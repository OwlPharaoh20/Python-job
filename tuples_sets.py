#A tuple is a collection which is ordered and unchangeable. Allows duplicate members.



#Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

print(fruits, fruits2)

#get value
print(fruits[1])

#cannot change value
#fruits[0] = 'Pears'


#get length
print(len(fruits))




#a set is a collection which is unordered and unindexed. No duplicate members

#create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

#check if in set
print('Apples' in fruits_set)

#add to set
fruits_set.add('Grape')



print(fruits_set)
