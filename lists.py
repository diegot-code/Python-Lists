#___________________________________________________________________________________________________
# Python Lists

print("Starting intro to Python Lists...")

names = ["Stephen", "Josh", "Diego", "Liliana", "Ezra", "Maria", "Brandon", "David", "Stephanie"]

numbers = [5, 14, 75, 41, 51, 90, 3, 24, 89, 1, 7]

# print(names)

# print(numbers)

#___________________________________________________________________________________________________
# Access List

# print(names[0])

# print(names[4])

# print(names[3:])

# print(names[:3])

# print(names[3:5])

#___________________________________________________________________________________________________
# Update List Items

# print(names)

# names[2] = "William"

# print(names)

# names[4:] = ["George", "Sid"]

# print(names)

#___________________________________________________________________________________________________
# Remove List Items

# print(names)

# names.remove("Stephen")

# print(names)

# names.pop(4)

# print(names)

# names.pop()

# print(names)

#___________________________________________________________________________________________________
# Loop a List

# for name in names:
#     print(name)

# for name in range(len(names)):
#     print(names[name])

# [print(name) for name in names]

#___________________________________________________________________________________________________
# Copy a List

moreNames = names.copy()

# print(moreNames)

evenMoreNames = list(names)

# print(evenMoreNames)

tooManyNames = names

# print(tooManyNames)

#___________________________________________________________________________________________________
# Sort a List

# print(names)

names.sort()

# print(names)

# print(numbers)

numbers.sort()

print(numbers)
