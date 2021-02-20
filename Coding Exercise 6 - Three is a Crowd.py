# Three is a Crowd
# 
#      Make a list of names that includes at least four people.
#      Write an if test that prints a message about the room being crowded, if there are more
#     than three people in your list.
#      Modify your list so that there are only two people in it. Use one of the methods for
#     removing people from the list, don&#39;t just redefine the list.
#      Run your if test again. There should be no output this time, because there are less than
#     three people in the list.
#      Bonus: Store your if test in a function called something like crowd_test.
#     

def crowd_test(names):
  if len(names) > 3:
    print("The room is crowded")

names = ["Anthony", "Paul", "Ben", "Beth", "Marco"]

crowd_test(names)

del names[0:3]

print(names)

crowd_test(names)




