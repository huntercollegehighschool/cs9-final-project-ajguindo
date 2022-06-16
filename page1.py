box = input("There are 3 boxes: Box A, B, and C. Which one do you want to search? : ")

while box != 'C':
  print("There is nothing in this box. Continue searching.")
  box = input("There are 3 boxes: Box A, B, and C. Which one do you want to search? Capital letter of box: ")

if box == 'C':
  answer = input("Yay! You have found a clue that says to go to the mirror. Enter where you want to search next (closet, mirror, or bed): ")
  if answer == "closet": 
    import page3 
  elif answer == "Closet":
    import page3 
  elif answer == "mirror":
    import page2  
  elif answer == "bed":
    import page4
  elif answer == "Mirror":
    import page2  
  elif answer == "Bed":
    import page4
