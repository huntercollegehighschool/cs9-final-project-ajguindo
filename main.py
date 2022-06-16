"""
Name(s): Lauren Nam and Amira J Guindo
Name of Project: Choose Your Own Adventure: Escape Room Edition
"""

#Write the main part of your program here. Use of the other pages is optional.

import os

def start():
  print("You must escape the room. Find key #34 before it’s too late to get out. You can start by searching the bed, mirror, closet, or boxes. What do you choose?")
  choice = input("Enter 1 for the boxes, 2 for the mirror, 3 for the closet, or 4 for the bed. Enter number: ")
  if choice == '1':
    import page1
  elif choice == '2':
    import page2
  elif choice == '3':
    import page3
  elif choice == '4':
    import page4
  else: 
    print("That's not a valid input.")
    choice = input("Enter 1 for the boxes, 2 for the mirror, 3 for the closet, or 4 for the bed. Enter number: ")
    os.system('clear')

      
 


x=1
if x==1:
  start()
  x=2