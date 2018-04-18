#lists


mylist = [1,2,3]
print(mylist[0])
print(mylist[1:])

#lists are mutable
mylist[0] = 5
print(mylist)

mylist.append('one')
print(mylist)

mylist.append([7,8])
print(mylist)

#use .extend to combine two lists
#.pop() pops off the element at the end of the list #can specify index to pop
mylist.pop(0)
print(mylist)

#.reverse() changes list inplace
#.sort() changes list inplace

#list comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]

first_col = [row[0] for row in matrix]
print(first_col)

#len() to get length of list
len([1,2,3]) #3

