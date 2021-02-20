# 1. Create a function func() which prints a text ‘Hello World’

def func():
    print("Hello World")

func()


# 2.Create a function which func1(name)  which takes a value name and prints the output “Hi My name is Google’

def func1(name):
    print(f"Hi, My name is {name}.")

func1('Google')

# 3.Define a function func3(x,y,z) that takes three arguments x,y,z 
# where z is true it will return x and when z is false it should return y . func3(‘hello’goodbye’,false)

def func3(x,y,z):
    if z == True:
        return x
    else:
        return y

result = func3('hello', 'goodbye', True)

print(result)

# 4.define a function func4(x,y) which returns the product of both the values.

def func4(x,y):
    z = x*y
    return z

total = func4(5,10)

print(total)


# 5. Define a function called as is_even that takes one argument , which returns true when even values is passed and false if it    is not.

def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False

even = is_even(8)

print(even)


# 6. Define a function that takes two arguments, and returns true if the first value is greater than the second value
#    and returns false if it is less than or equal to the second.

def compare(a,b):
    if a > b:
        return True
    else:
        return False

result = compare(4,2)

print(result)


# 7.Define a function which takes arbitrary number of arguments and returns the sum of the arguments.

def func_sum(*args):
    return sum(args)

total = func_sum(3,5,9)

print(total)


# 8.Define a function which takes arbitrary number of arguments and returns a list containing only the arguments that are even.

def func_evens(*args):
    return [n for n in args if n%2 == 0]

print(func_evens(1,2,3,4,5,6,7,8,9,10))


# 9.Define a function that takes a string and 
#   returns a matching string where every even letter is uppercase and every odd letter is lowercase 

def cap_string(st):
    res = []
    
    for index in range(len(st)):
        if index % 2 == 0:
            
            res.append(st[index].upper())
        else:
            res.append(st[index].lower())

    
    return ''.join(res)

print(cap_string('test'))


# 10. Write a function which gives lesser than a given number if both the numbers are even,
#     but returns greater if one or both or odd.

def even_odd(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return "lesser"
    else:
        return "greater"

print(even_odd(1,5))    


# 11.Write a function which takes  two-strings and returns true if both the strings start with the same letter.

def first_letter(str1, str2):
    if str1[0] == str2[0]:
        return True
    else:
        return False

print(first_letter('Fan', 'Heat'))

# 12.Given a value,return a value which is twice as far as other side of 7

def square_numbers(numlist):
    return [num ** 2 for num in numlist]

print(square_numbers([1,2,3,4,5]))

# 13. A function that capitalizes first and fourth character of a word in a string.

def cap_1and4(st):
    res = []
    #Iterate over the character
    for index in range(len(st)):
        if index == 0 or index == 3:
            #Refer to each character via index and append modified character to list
            res.append(st[index].upper())
        else:
            res.append(st[index].lower())

    #Join the list into a string and return
    return ''.join(res)

print(cap_1and4('Blizzard'))

