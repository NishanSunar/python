students_score = input("Input a list of students score: ").split()
for n in range(0, len(students_score)):
    students_score[n] = int(students_score[n])
print(students_score)
highest = 0
for score in students_score:
    if score > highest:
        highest = score

print(f"The highest score is {highest}")