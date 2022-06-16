answer3 = input("You are standing in front of the bed. There are 3 cabinets on the side of the bed. If you want to search them, enter 'search'. If you want to search somewhere else, enter 'leave'. ")
if answer3 == 'leave':
  choice5 = input("Do you want to search the closet, boxes, or mirror? ")
  if choice5 == 'Closet': 
    import page3 
  elif choice5 == 'closet': 
    import page3 
  elif choice5 == 'mirror':
    import page2 
  elif choice5 == 'Mirror':
    import page2 
  elif choice5 == 'boxes':
    import page1
  elif choice5 == 'Boxes': 
    import page1
if answer3 == 'search':
  choice6 = input("There's cabinets L, M, and N. Enter the capital letter of the cabinet you want to search: ")
  while choice6 != "M": 
    print("There is nothing in this cabinet. Continue searching. ")
    choice6 = input("There's cabinets L, M, and N. Enter the capital letter of the cabinet you want to search: ")
  if choice6 == "M":
    choice7 = input("Yay! You found a clue that says to open box C on the floor. There is nothing else in this cabinet. Enter 1 to open box C, enter 2 to go to the mirror, and enter 3 to go to the closet.")
    if choice7 == "3": 
      import page3 
    elif choice7 == "2":
      import page2 
    elif choice7 == "1":
      choice8 = input("Yay! You have found a clue that says to go to the mirror. Write where you want to go after this? The closet, mirror, bed: ")
      if choice8 == 'Closet': 
        import page3 
      elif choice8 == 'closet': 
        import page3 
      elif choice8 == 'mirror':
        import page2 
      elif choice8 == 'Mirror':
        import page2 
      elif choice8 == 'Box C':
        choice9 = input("Yay! You have found a clue that says to go to the mirror. Enter where you would like to search next (the bed, closet, or mirror): ")
        if choice9 == 'Closet': 
          import page3 
        elif choice9 == 'closet': 
          import page3 
        elif choice9 == 'mirror':
          import page2 
        elif choice9 == 'Mirror':
          import page2 
        elif choice9 == 'Bed':
          import page4 
        elif choice9 == 'bed':
          import page4
  if choice6 == "N":
    print("There is nothing in this cabinet.")
 
