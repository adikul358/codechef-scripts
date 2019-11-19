def generateNextNumber():
  global main_array
  print("Current Array:", main_array, sep=" ")
  print("Last element:", main_array[-1], sep=" ")
  if main_array[-1] in main_array[:-1]:
    print("Last element is being repeated")
    main_array_reversed = [ele for ele in reversed(main_array[:-1])]
    l = len(main_array)-main_array_reversed.index(main_array[-1])-1
    print("Index of last repeated last element:", l, sep=" ")
    main_array.append(len(main_array)-l)
  else:
    print("Last element is not being repeated")
    main_array.append(0)
  print("Appended element:", main_array[-1], sep=" ")
  print("Current Array:", main_array, sep=" ")
  print()
  
main_array = [0]

for j in range(int(input())):
  for i in range(int(input())-1):
    generateNextNumber()
  print(main_array.count(main_array[-1]))
  print()
  print()