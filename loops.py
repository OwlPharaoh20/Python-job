# A for loop is used for iterating over a sequence(That can be a list, a tuple, a dictionary, a set or a string)


people = ['John', 'Paul', 'George', 'Ringo']


#Simple for loop
#for person in people:
    #print(f'Current Person: {person}')


#Break
#for person in people:
    #if person == 'George':
        #break
    #print(f'Current Person: {person}')



#Continue
#for person in people:
    #if person == 'George':
        #continue
    #print(f'Current Person: {person}')



#range 
#for i in range(len(people)):
    #print(people[i])


#range 2
#for i in range(0, 11):
   # print(f'Number: {i}')



#A while loop runs a block of code as long as its condition remains true

count = 0 
while count <= 10:
    print(f'count: {count}')
    #increment
    count += 1