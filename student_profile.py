# Task 2: Input & Variables
full_name = input("Enter Student Full Name: ")
roll_number = input("Enter Roll Number: ")
program = input("Enter Program: ")
university_name = input("Enter University Name: ")
city = input("Enter City: ")
age = int(input("Enter Age: "))
hobby = input("Enter Hobby: ")

# Task 3: Operators Demonstration
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Arithmetic operators
print("==========Arithmetic Operations=============")
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2}")
print(f"Modulus: {num1} % {num2} = {num1 % num2}")
print(f"Exponent: {num1} ** {num2} = {num1 ** num2}")
print(f"Floor Division: {num1} // {num2} = {num1 // num2}")



# Comparison operators
print("===========Comparison Operations============")
print(f"Is num1 equal to num2? {num1 == num2}")
print(f"Is num1 not equal to num2? {num1 != num2}")

# Logical operators
print("==========Logical Operations================")
print(f"Is num1 greater than 10 and num2 less than 10? {num1 > 10 and num2 < 10}")
print(f"Is num1 greater than 10 or num2 less than 10? {num1 > 10 or num2 < 10}")

# Identity operators
print("=========Identity Operations===========")
print(f" num1 is to num2? {num1 is num2}")
print(f" num1 is not identical to num2? {num1 is not num2}")

# Membership operators
sample_list = [num1, num2]
print("===========Membership Operations========")
print(f"num1 in the sample list? {num1 in sample_list}")
print(f"num1 not in the sample list? {num1 not in sample_list}")

# Task 4: Python Strings & Formatting
greeting = "Hello"
formatted_string = f"{greeting}, {full_name}!"
print(formatted_string)

# Escape characters
print("===========Using escape characters=========")
print("This is a tab:\t and this is a new line:\n")

# String methods
print("========String Methods========")
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")
print(f"Title Case: {full_name.title()}")
print(f"Stripped: {full_name.strip()}")
print(f"Replaced: {full_name.replace('John', 'Jane')}")
print(f"Count of 'a': {full_name.count('a')}")

# Task 5: Final Output — Student Profile Card
print("----------------------------------------")
print("       STUDENT PROFILE SYSTEM")
print("----------------------------------------")
print(f"Name:            {full_name}")
print(f"Roll No:         {roll_number}")
print(f"Course:          {program}")
print(f"University:      {university_name}")
print(f"City:            {city}")
print(f"Age:             {age}")
print(f"Hobby:           {hobby}")
print("----------------------------------------")
print("Welcome to Python Programming!")

# Task 6: Bonus Task (Extra Credit)
save_profile = input("Do you want to save your profile? (yes/no): ")
if save_profile == 'yes':
    with open("student_profile.txt", "w") as file:
        file.write(f"Name: {full_name}\n")
        file.write(f"Roll No: {roll_number}\n")
        file.write(f"Course: {program}\n")
        file.write(f"University: {university_name}\n")
        file.write(f"City: {city}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Hobby: {hobby}\n")
    print("Profile saved to student_profile")