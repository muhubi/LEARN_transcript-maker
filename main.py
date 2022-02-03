# Obtain Student Info
# name = input("What is the student's name? ")
# student_id = input("What is the student's ID#? ")
# student_grad = input("What year does this student graduate? ")
# major = input("What is the student's major? ")
# student_GPA = float(input("What is the student's GPA? "))
# student_credits = float(input("How many credits has the student earned? "))

# Test Student Info
name = "Andrew Mahabee"
student_id = "2000005"
student_grad = "2018"
major = "Biomedical Sciences"
student_GPA = 3.9
student_credits = 120

# University Requirements
passing_GPA = 2.7
required_credits = 120
remaining_credits = int(required_credits) - int(student_credits)

# University Cover Letter
print("")
print("QUINNIPIAC UNIVERSITY")
print("275 MOUNT CARMEL AVENUE, HAMDEN, CT 06518")
print("203.680.6355 | registrar@qu.edu")
print("OFFICE OF STUDENT REGISTRAR")
print("")
print("----------------------------------------------------------")
print("OFFICIAL TRANSCRIPT RECORD")
print("----------------------------------------------------------")
print("")
print("STUDENT NAME: " + name)
print("STUDENT ID: " + student_id)
print("STUDENT GRADUATION YEAR: " + student_grad)
print("")
print("DEGREE IN: " + major)

# Define Student's Latin Honors
if student_GPA >= 3.7 and student_credits >= required_credits:
    rank = "Summa Cum Lauda"
elif student_GPA >= 3.4 and student_credits >= required_credits:
    rank = "Magna Cum Lauda"
elif student_GPA >= 3.2 and student_credits >= required_credits:
    rank = "Cum Lauda"
elif student_GPA >= passing_GPA and student_credits >= required_credits:
    rank = "Graduate"
else:
    rank = "FAILED"
print("ACADEMIC ACHIEVEMENT: " + rank)

# Display the student's overall GPA letter grade
if student_GPA >= 4.0:
    letter_grade = "A"
elif student_GPA >= 3.7:
    letter_grade = "A-"
elif student_GPA >= 3.3:
    letter_grade = "B+"
elif student_GPA >= 3.0:
    letter_grade = "B"
elif student_GPA >= 2.7:
    letter_grade = "B-"
elif student_GPA >= 2.3:
    letter_grade = "C+"
elif student_GPA >= 2.0:
    letter_grade = "C"
else:
    letter_grade = "FAILURE"
print("OVERALL GRADE: " + letter_grade)