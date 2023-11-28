# Get input from the user
marks = float(input("Enter student marks (between 0 and 100): "))


if 80 <= marks <= 100:
    grade = "A"
elif 60 <= marks <= 79:
    grade = "B"
elif 50 <= marks <= 59:
    grade = "C"
elif 40 <= marks <= 49:
    grade = "D"
else:
    grade = "E"

# Print the result
print(f"The grade for {marks} marks is: {grade}")