# Initial list
trainees = ["John", [2, ["James", "Mary"]]]

# 1. Display 2 from the list.
print(trainees[1][0])

# 2. Output James from the list.
print(trainees[1][1][0])

# 3. Using a method add 56 at the end of the list.
trainees.append(56)
print(trainees)

# 4. Using a method add the name Mike between James and Mary
trainees[1][1].insert(1, "Mike")
print(trainees)

# 5. Change the value of 2 to 8
trainees[1][0] = 8
print(trainees)

# 6. Remove John and Mary from the list.
trainees = ["John", [2, ["James", "Mary"]]]
trainees.remove("John")
trainees[0][1].remove("Mary")
print(trainees)

# 7. Using a function, determine the length of the list
length_of_list = len(trainees)
print(length_of_list)