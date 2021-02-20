# 1.  Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included).

nl=[]

for x in range(1500, 2700):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
        
print (','.join(nl))


# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ] 
# Expected Output : 
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius 

celsius = int(input("Enter temperature in celsius: "))

fahrenheit = (celsius * 9/5) + 32

print('%.0f°C is %0.0f in Fahrenheit' %(celsius, fahrenheit))

fahrenheit = int(input("Enter temperature in fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9
print('%.0f°F is %.0f in Celsius' %(fahrenheit, celsius))


# 3. Write a Python program to guess a number between 1 to 9.
# 
#   Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct,
#   on successful guess, user will get a "Well guessed!" message, and the program will exit.


import random

target_num = random.randint(1, 9)
print(target_num)
guess_num = 0
print(guess_num)

while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
    
print('Well guessed!')
    
    
# 4. Write a Python program to construct the following pattern, using a nested for loop.
# 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")


# 5. Write a Python program that accepts a word from the user and reverse it. Go to the editor

word = input("Enter a word:")

reversed = word[::-1]

print(reversed)


# 6. Write a Python program to count the number of even and odd numbers from a series of numbers.
# 
#     Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
#     Expected Output : 
#     Number of even numbers : 5
#     Number of odd numbers : 4

num_list = [1,2,3,4,5,6,7,8,9]
evens = 0
odds = 0

for num in num_list:
    if num % 2 == 0:
        evens += 1
    else:
        odds +=1

print("Number of even numbers: " + str(evens))
print("Number of odd numbers : " + str(odds))


# 8. Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for item in datalist:
   print ("Type of ",item, " is ", type(item))

# 9. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement. 
# Expected Output : 0 1 2 4 5 

for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")

