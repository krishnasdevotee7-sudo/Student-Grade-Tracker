students = [("Alice", 95), ("bob", 87), ("charlie", 92), ("diana", 78), ("eve", 88), ("frank", 91)]

# 1. Print Grades
for student, mark in students:
    if mark >= 90:
        print(f"{student} - {mark} - Grade A")
    elif mark >= 80: # Using elif stops a student from getting multiple grades
        print(f"{student} - {mark} - Grade B")
    elif mark >= 70:
        print(f"{student} - {mark} - Grade C")
    else:
        print(f"{student} - {mark} - Grade D")

print("-" * 30) # Visual separator

# 2. Calculate Average
tot = 0
for student, mark in students:
    tot = tot + mark

average = tot / len(students)
print(f"Total number of students: {len(students)}")
print(f"Average mark: {average:.1f}")

print("-" * 30)

# 3. Find Highest and Lowest
highest_mark = 0
highest_student = ""
lowest_mark = 100
lowest_student = ""

for student, mark in students:
    if mark > highest_mark:
        highest_mark = mark
        highest_student = student
    if mark < lowest_mark:
        lowest_mark = mark
        lowest_student = student

print(f"Highest: {highest_student} with {highest_mark}")
print(f"Lowest: {lowest_student} with {lowest_mark}")
