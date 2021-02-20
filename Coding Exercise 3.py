
# 1. Write a string that returns just the letter ‘r’ from ‘Hello World’
# For example, ‘Hello World’[0] returns ‘H’.You should write one line of code. Don’t assign a variable name to the string.
# 

print('Hello World'[8])

# 2. String slicing to grab the word ‘ink’ from the word  ‘thinker’
# S='hello',what is the output of h[1]

s='thinker'[2:]
s= s[:-2]
print(s)

s='hello'
print(s[1])

# 3. S=’Sammy’ what is the output of s[2:]”

s = 'Sammy'
print(s[2:])


# 4. With a single set function can you turn the word ‘Mississippi’ to distinct character word.

s= 'Mississippi'
s=set(s)

print(s)


# 5. Your goal in this programming exercise is to determine, whether the phrase represents a palindrome or not.
# 
# Input data contains number of phrases in the first line.
# Next lines contain one phrase each.
# Answer should have a single letter (space separated) for each phrase: Y if it is a palindrome and N if not.

num_phrases = 3

phrase_1 = 'stras'
phrase_1 = phrase_1.lower()
print(phrase_1)
phrase_2 = 'O, a kak Uwakov lil vo kawu kakao!'
phrase_2 = phrase_2.lower()
phrase_2 = phrase_2.replace(',', "")
phrase_2 = phrase_2.replace('!', "")
phrase_2 = "".join(phrase_2.split())
phrase_3 = 'Some men interpret nine memos'
phrase_3 = phrase_3.lower()
phrase_3 = "".join(phrase_3.split())

p1_reversed = phrase_1[::-1]
print(p1_reversed)

p2_reversed = phrase_2[::-1]
print(p2_reversed)

p3_reversed = phrase_3[::-1]
print(p3_reversed)

if phrase_1 == p1_reversed:
    answer = 'Y'
else:
    answer = 'N'
    
if phrase_2 == p2_reversed:
    answer = answer + ' Y'
else:
    answer = answer + ' N'

if phrase_3 == p3_reversed:
    answer = answer + ' Y'
else:
    answer = answer + ' N'

print(answer)