if 1<2:
    print('yes')

if 1 > 2:
    print('first')
else:
    print('second')

# elif short for else if

#loops

# For loops

seq = [1,2,3,4,5,6]

for item in seq:
    print(item)

d = {'sam':1, 'frank':2, 'dan':3}

for item in d: #prints the keys in dictionary
    print(item)

#tuples
my_pairs = [(1,2),(3,4),(5,6)]

#tuple unpacking
for (tup1,tup2) in my_pairs:
    print(tup1)
    print(tup2)

i = 1

while i < 5:
    print("i is {}".format(i))
    i = i + 1

#range
a = list(range(0,20,4)) #(start,end,add)
print(a)

# list comprehension
x = [1,2,3,4]

out = []
for item in x:
    out.append(item**2)

print(out)

#can be written as

out2 = [num**2 for num in x]
print(out2)
