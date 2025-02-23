student_height = input("Input a list of students: ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)
count = 0
sum = 0
for height in student_height:
    sum += height
    count += 1

average = sum / count
print(f"The average height of the students is {average}")