answer1 = input("You are looking at the mirror. On the mirror there are notes. Do you want to proceed or go search something else? Choose to 'Proceed' or 'Search something else'(exactly as written in quotes): ")
if answer1 == 'Proceed':
  choice2 = input("Continue to the mirror. There is a three digit number written on the note. 149. These numbers make up the combination to a lock somewhere else in this room. Type 1 to proceed: " )
  if choice2 == '1':
    choice3 = input("There is a hidden message on the mirror. It says, 'What we wear is hidden beneath a silver lock. To find the key, one must knock!' Type where you want to go after this? Boxes, closet, or bed: ")
    if choice3 == 'boxes': 
      import page1
    elif choice3 == 'Boxes':
      import page1 
    elif choice3 == 'Closet': 
      import page3 
    elif choice3 == 'closet': 
      import page3  
    elif choice3 == 'Bed':
      import page4 
    elif choice3 == 'bed':
      import page4
if answer1 == 'Search something else': 
  somewhere = input("Where do you want to go? Boxes, closet, or bed? ")
  if somewhere == 'boxes': 
    import page1
  elif somewhere == 'Boxes':
    import page1 
  elif somewhere == 'Closet': 
    import page3 
  elif somewhere == 'closet': 
    import page3  
  elif somewhere == 'Bed':
    import page4 
  elif somewhere == 'bed':
    import page4




          