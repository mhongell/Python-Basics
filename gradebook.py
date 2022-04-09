### This is another project through CodeCademy where I learned how to compile lists and sublists ###

# Classes I took last semester with grades:
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Classes I am taking this semester:
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Gradebook list combining subjects and classes
gradebook = [["physiscs", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
#print(gradebook)

# Add more subjects
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Bonus 5 points to Visual Arts Class
gradebook[5][1] = 98

# Remove numerical grade for Poetry
gradebook[2].remove(85)

# Add "Pass" value to poetry sublist
gradebook[2].append("Pass")
print(gradebook)

# Combine last semester and current semester gradebooks to one big gradebook
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
