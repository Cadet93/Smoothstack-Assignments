# 1. Create a list with one number, one word and one float value. Display the output of the list.

practice_list = [10, 'Hello', 5.5]

print(practice_list)


# 2. I have a nested list [1,1[1,2]], how to grab the value of 2 from the list.

matrix = [1,1,[1,2]]
print(matrix[2][1])


# 3. lst=['a','b','c'] What is the result of lst[1:]?

lst=['a','b','c']
print(lst[1:])


# 4. Create a dictionary with weekdays an keys and week index numbers as values.do assign dictionary to a variable

practice_dict = {"Sunday": 1, "Monday": 2, "Tuesday": 3, "Wednesday": 4, "Thursday": 5, "Friday": 6, "Saturday": 7}

print(practice_dict)


# 5. D={‘k1’:[1,2,3]} what is the output of d[k1][1]



D={'k1':[1,2,3]} 

print(D['k1'][1])


# 6. Can you create a list [1,[2,3]] into a tuple
# 
# We haven't covered tuples yet

# 7. With a single set function can you turn the word ‘Mississippi’ to distinct character word.

s= 'Mississippi'
s=set(s)

print(s)


#8. Can you add an element ‘X’ to the above created set

s.add("x")

print(s)


# 9. Output of set([1,1,2,3])

print(set([1,1,2,3]))


# Question:
#      Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and          3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
#      
# 	 Hints: 
# 	 Consider use range(#begin, #end) method

nl=[]

for x in range(2000, 3200):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
        
print (','.join(nl))


# Question:
# 
# 	Write a program which can compute the factorial of a given numbers.
# 	The results should be printed in a comma-separated sequence on a single line.
#     
# 	Suppose the following input is supplied to the program:
# 	8
# 	Then, the output should be:
# 	40320
# 	
# 
# 	Hints:
# 	In case of input data being supplied to the question, it should be assumed to be a console input.

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


x=int(input("Enter a number:"))

factorial = fact(x)

print(factorial)




