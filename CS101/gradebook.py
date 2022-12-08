# Script to fill in grades in a list format.
last_semester_gradebook = [["Politics", 80], [
    "Latin", 96], ["Dance", 97], ["Architecture", 65]]

# Begin list:
subjects = ["Physics", "Calculus", "Poetry", "History"]
grades = [98, 97, 85, 88]
gradebook = [["Physics", 98], ["Calculus", 97],
             ["Poetry", 85], ["History", 88]]

# Add Computer Science and Visual Arts.
gradebook.append(["Computer Science", 100])
gradebook.append(["Visual Arts", 93])

# Change grade for Visual Arts to 98 (add extra 5 points).
gradebook[-1][-1] = 98

# Remove grade from Poetry and change to a Pass/Fail option.
gradebook[2].remove(85)
gradebook[2].append("Pass")

# Add results from both semesters to form a cohesive list.
full_gradebook = last_semester_gradebook + gradebook
print("Grades: ", full_gradebook)
