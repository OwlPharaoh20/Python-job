#A list is a colection which is ordered and changeable. Allows duplicate members.
#Lists are pretty much the same as arrays



#Create list
numbers = [1,2,3,4,5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

#Use a constructor
numbers2 = list((1,2,3,4,5))


#get value
print(fruits[1])

#get length 
print(len(fruits))

#append to list
fruits.append('Mangos')

#remove from list
fruits.remove('Grapes')

#insert into position
fruits.insert(2, 'Strawberries')

#remove with pop
fruits.pop(2)

#reverse list
fruits.reverse()

#sort list
fruits.sort()

#reverse sort
fruits.sort(reverse=True)






print(fruits)
