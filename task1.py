# Predefined dictionary of students and their marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 74
}

# Ask the user for a student's name
name = input("Enter the student's name: ")

# Retrieve and display marks or show 'not found'
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")