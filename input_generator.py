import random

main_file = open('input.txt', "w")
main_array = []

n = 200000
constraints = [1, 10**3]

for i in range(n):
    main_array.append(str(random.randrange(*constraints)))

main_file.write(str(n) + '\n' + " ".join(main_array))