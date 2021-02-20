# Six is a Mob
# 
#      Save your program from Three is a Crowd - Part 2 under a new name.
#      Add some names to your list, so that there are at least six people in the list.
#      Modify your tests so that
#      If there are more than 5 people, a message is printed about there being a mob
#     in the room.
#      If there are 3-5 people, a message is printed about the room being crowded.d
#      If there are 1 or 2 people, a message is printed about the room not being
#     crowded.
#      If there are no people in the room, a message is printed abou the room being
#     empty.


def crowd_test(names):
  if len(names) > 5:
    print("Oh no, There is a mob in the room!")
  elif len(names) >= 3 and len(names) <= 5:
    print("The room is crowded.")
  elif len(names) > 0:
    print("The room is not crowded.")
  else:
    print("The room is empty")

names = ["Anthony", "Ben", "Beth", "Rufat", "Nicole", "Chandra"]

crowd_test(names)




