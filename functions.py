def my_func(param1="default"):
    """
    THIS IS A DOCSTRING
    """
    print('my first function! {}'.format(param1))


my_func()

def addNums(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1 + num2
    else:
        return "need numbers"

result = addNums('2','3')
print(result)

#lambda expression
#lambda num:num%2 == 0

#filter
my_list = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0

evens = filter(even_bool, my_list)
print(list(evens))

evens2 = filter(lambda num:num%2 == 0, my_list)
print(list(evens2))

str = 'hello'
#str.lower()
#str.upper()
#str.split()

tweet = 'go sports! #sports'
a = tweet.split('#')[1]
print(a)
print('x' in [1,2,3])