# Task 1: Dictionary of Student Marks

student_marks = {"Rahul": 85,"Priya": 90,"Aman": 78,"Neha": 92}

name = input("Enter student name: ")
if name in student_marks:
    print(f"{name}'s marks are: {student_marks[name]}")
else:
    print(f"Student '{name}' not found in the record.")


# Task 2: List Slicing and Reversing

numbers = list(range(1, 11))

first_five = numbers[:5]

reversed_list = first_five[::-1]

print("Extracted List:", first_five)
print("Reversed List:", reversed_list)
