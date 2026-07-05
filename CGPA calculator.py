# PERSONAL POCKET CGPA CALCULATOR


print("    PERSONAL POCKET CGPA CALCULATOR")

num_courses = int(input("Enter the number of courses: "))

total_grade_points = 0
total_units = 0

for i in range(num_courses):
    print(f"\nCourse {i+1}")

    unit = int(input("Course Unit: "))
    score = float(input("Course Score: "))

    if score >= 70:
        grade = "A"
        point = 5
    elif score >= 60:
        grade = "B"
        point = 4
    elif score >= 50:
        grade = "C"
        point = 3
    elif score >= 45:
        grade = "D"
        point = 2
    elif score >= 40:
        grade = "E"
        point = 1
    else:
        grade = "F"
        point = 0

    print("Grade:", grade)
    print("Grade Point:", point)

    total_grade_points += point * unit
    total_units += unit

cgpa = total_grade_points / total_units

print("\n==============================")
print("Total Units:", total_units)
print("CGPA:", round(cgpa, 2))

if cgpa >= 4.50:
    print("Class: First Class")
elif cgpa >= 3.50:
    print("Class: Second Class Upper")
elif cgpa >= 2.40:
    print("Class: Second Class Lower")
elif cgpa >= 1.50:
    print("Class: Third Class")
else:
    print("Class: Pass")