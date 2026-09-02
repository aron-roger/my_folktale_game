
#Starting at Game
#v.a.d.o
time_limit = 17
time_elapsed = 0
game_running = True

# honestly i got to learn enum for this one and arrays.
from enum import Enum
from turtle import right
class Speed(Enum):
    VADO = 1
    MEDIC = 2
    ENGINEER = 5
    CAPTAIN = 10

left = ["VADO", "MEDIC", "ENGINEER", "CAPTAIN"]
Right = []

# honestly i got to learn enum for this one and arrays. And it is all kinda messy and crupy, but it works. I will refactor it later.
print ("DISCLAIMER: This game is a work in progress, and may have bugs or errors. Please reload the game if you encounter any issues. Thank you for playing, it has a correct logic to sequence the characters to get to the escape pod. Thank you for playing.")
print ("You wake up to continous beeping and a red light flashing.")
print ("The space shuttle you are traveling has be infected by a strange entity in space.")
print ("There it only one way to the escape pod, for walking through the zero gravity bridge with a single thruster that can only carry two people at a time.")
print ("Also you have a limited time and each crew member has different speeds to get to escape pod, including yourself.")
print ("You must find the correct order to get everyone to the escape pod before the shuttle is completely infected and destroyed.")
print ("SYSTEM ALERT: VADO PROTOCOL INITIATED.")
print ("You have " + str(time_limit) + " minutes to get everyone to the escape pod.")
print ("The crew members are: ")
print ("1. Vado - 1 minute to cross the bridge")
print ("2. Medic - 2 minutes to cross the bridge")
print ("3. Engineer - 5 minutes to cross the bridge")
print ("4. Captain - 10 minutes to cross the bridge")
print ("the limit to cross the bridge at one time is 2 crew members, and they must cross at the speed of the slowest member")
while time_elapsed <= time_limit and len(left) > 0 and game_running == True:
    first_crosser = Speed(int(input("Who will cross the bridge, the integers before characters represent minutes, you may enter minutes? (1: Vado, 2: Medic, 5: Engineer, 10: Captain) ")))
    if first_crosser.name not in left:
        print ("That character is not on the left side of the bridge, please choose again.")
        
    second_crosser = Speed(int(input("Who will cross the bridge with " + str(first_crosser.name) + "? ")))
    if second_crosser.name not in left:
     print ("That character is not on the left side of the bridge, please choose again.")
   
    speed1 = first_crosser.value
    speed2 = second_crosser.value
    time_taken = max(speed1, speed2)
    time_elapsed += time_taken
    for person in [first_crosser.name, second_crosser.name]:
        if person in left:
            left.remove(person)
            Right.append(person)
    print ("Time elapsed: " + str(time_elapsed) + " minutes")
    if time_elapsed <= time_limit and len(left) == 0:
        print ("Congratulations! You have successfully VADO.")
        break
    elif time_elapsed > time_limit:
        print ("You have failed to get everyone to the escape pod in time. The shuttle has been destroyed.")
        print ("Do you want to try again? (y/n)")
        retry = input()
        if retry == "y":
            time_elapsed = 0
            left = ["VADO", "MEDIC", "ENGINEER", "CAPTAIN"]
            Right = []
            print ("You have chosen to try again.")
            game_running = True
            continue
        else:
            print ("You have chosen to quit. Goodbye.")
            game_running = False
    else:
        back_crosser = Speed(int(input("Who now will cross the bridge back? (1: Vado, 2: Medic, 5: Engineer, 10: Captain) ")))
        if back_crosser.name in Right:
            Right.remove(back_crosser.name)
            left.append(back_crosser.name)
        else:
            print ("That character is not on the right side of the bridge, please choose again.")
        speed3 = back_crosser.value
        time_elapsed += speed3
        for person in [back_crosser.name]:
            if person in Right:
                Right.remove(person)
                left.append(person)
        print ("Time elapsed: " + str(time_elapsed) + " minutes")
                        

# tomorrow: It needs a reset option, and a way re populate arrays accordingly. Also, a way to not let charcters who are on the right side cross the bridge again.
  