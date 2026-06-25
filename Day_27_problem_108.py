# Marksheet Generation System

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

print("Enter marks of 5 subjects (out of 100):")
m1 = float(input("Subject 1: "))
m2 = float(input("Subject 2: "))
m3 = float(input("Subject 3: "))
m4 = float(input("Subject 4: "))
m5 = float(input("Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

# Grade Calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Result
if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"

# Display Marksheet
print("\n" + "=" * 30)
print("          MARKSHEET")
print("=" * 30)
print("Name      :", name)
print("Roll No   :", roll_no)
print("-" * 30)
print("Subject 1 :", m1)
print("Subject 2 :", m2)
print("Subject 3 :", m3)
print("Subject 4 :", m4)
print("Subject 5 :", m5)
print("-" * 30)
print("Total Marks :", total, "/ 500")
print("Percentage  :", round(percentage, 2), "%")
print("Grade       :", grade)
print("Result      :", result)
print("=" * 30)