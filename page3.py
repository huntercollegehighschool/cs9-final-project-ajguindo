answer2 = input("You are now standing in front of the closet door. There is a lock. Do you have the combination? Enter 'yes or 'no': ")

if answer2 == 'no':
  choice4 = input("Go back and find the combination. Would you like to search the boxes, mirror, or bed? ")
  if choice4 == 'boxes': 
    import page1
  if choice4 == 'Boxes':
    import page1
  if choice4 == 'mirror':
    import page2
  if choice4 == 'Mirror':
    import page2
  if choice4 == 'bed': 
    import page4
  if choice4 == 'Bed': 
    import page4

if answer2 == "yes":
  choice5 = input("What is the combination? It is a three digit number: ")
  while choice5 != '149':
    print("Combination is incorrect. Try again.") 
    choice5 = input("Input the correct combination: ")
  if choice5 == '149':
    clothes = input("You found the closet! Search the clothes to find the key! To search the pockets of shorts say 'shorts', to search the pockets of the coat say 'coat', and to search the pockets of the jeans say 'jeans': ")
    while clothes != 'coat':
      print("There is nothing in this garment try again.")
      clothes = input("To search the pockets of shorts say 'shorts', to search the pockets of the coat say 'coat', and to search the pockets of the jeans say 'jeans': ")
    if clothes == 'coat':
      print("You found Key #34. You escaped the room! Congrats!")
    
  