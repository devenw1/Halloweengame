#Import
import time
#typewriter function 
def typewrite(string):
  liststring= list(string)7
  for char in liststring:
    print(char, end="", flush=True)
    time.sleep(0.05)
  return""



typewrite("You walk through the dark hall of Mainstreet at RM. And  see a paper on the wall. You approach it...\nYou read it to yourself\n")
typewrite("\"YOU MUST FIND THE PUMPKIN TO LEAVE... YOU HAVE 30 \nMINUTES\"\n")
typewrite("You take a minute to think when you see a man with a katana start walking toward you from the auditoritum\n")
floor = input(typewrite("Do you go to the first floor (1), second floor (2), or   third floor (3)? "))

if floor == "1":
  typewrite("You go to the first floor but didn't realize how close   the man was.\n")
  where = input(typewrite("Do you run (1) or hide (2)? "))
  if where == "1":
    typewrite("You run to the end of the hall and enter a room so he    doesn't see you.\n")
    search = input(typewrite("Should you search the room (1) or wait for the man to go by and leave (2)? "))
    if search == "1":
      typewrite("You start searching the room to see if there is any pumpkin. Suddenly you realize there is a hand on your shoulder. The killer got you.\n")
      print("\n")
      typewrite("Game over")
    elif search == "2":
      typewrite("You wait till you see a figure go by the window. Then \nwait another minute for good measure. Then you step out. \nBut that wasn't a good idea. The man was right there.\n")
      print("\n")
      typewrite("Game Over")
  elif where == "2":
    typewrite("You run into the room closest to you. Room 163. But it was a bad choice. There is no one to hide. The man \nenters behind you and kills you.\n")
    print("\n")
    typewrite("Game Over")
elif floor == "2":
  typewrite("You run up the stairs to the second floor.\n")
  wait = input(typewrite("Do you want to wait out the timer (1) or seach rooms (2)? "))
  if wait == "1":
    typewrite("You decide to wait out the timer to see what happens. Wasn't the best idea. The man found you as soon as the time struck 0")
    print("\n")
    typewrite("Game Over")
  elif wait == "2":
    typewrite("You go around search different rooms. But behind one of the doors you open you see the man.\n")
    print("\n")
    typewrite("Game Over")
elif floor == "3":
  typewrite("You run to the third floor and take a second to catch your breath.\n")
  direction = input(typewrite("Do you go left (1) or right (2)? "))
  if direction == "1":
    typewrite("You go left. Two things catch your eye. A cracked classroom and a cracked locker\n")
    door = input(typewrite("Do you check the door (1) or the locker (2) "))
    if door == "1":
      typewrite("You approach the door slowly...\nYou open it slowly and to your surprise there was nothing. Nothing but a note.\nIt says to look behind you...\nThe killed got you")
      print("\n")
      typewrite("Game Over")
    elif door == "2":
      typewrite("You walk over to the cautiously. You hear the squeak of a shoe from what sounds like the stairway. Without hesitation you open the locker.\n")
      print("\n")
      typewrite("You found the Pumpkin. You won the game!")
  elif direction =="2":
    typewrite("You go to the right and look through some rooms. While you were distracted the man found you.")
    print("\n")
    typewrite("Game over")


typewrite("\n\nThank You for Playing!!")
