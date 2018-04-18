#strings are immutable

string = "abcdefg"
print(string[0])
# cannot do string[0] = 'f'
print(string[:-1]) #up to but not including
print(string[1:])

#string formatting
print("hello {} {}".format('there', 'more'))

x = "item one: {y} item two: {x}".format(x='cat', y='dog')

print(x)