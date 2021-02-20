# Three is a Crowd - Part 2
# 
#      Save your program from Three is a Crowd under a new name.
#      Add an else statement to your if tests. If the else statement is run, have it print a
#     message that the room is not very crowded.

def crowd_test(names):
  if len(names) > 3:
    print("The room is crowded.")
  else:
    print("The room is not very crowded.")

names = ["Anthony", "Paul", "Ben", "Beth", "Marco"]

crowd_test(names)

del names[0:3]

print(names)

crowd_test(names)

