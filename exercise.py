# Exercise1. Create variables of different data types
# • Create and print three variables: one integer, one float, and one string.

integer_variables = 21012007
float_variables = 6.5
string_variables = "Hi there, I'm Tung."
print(f"{integer_variables, float_variables, string_variables}")

# Exercise 2. Greet the user
# • Prompt the user to enter their name and print: "Hello, [Name]".

name = input("Put ur name: ")
print(f"Hello, {name}")


# Exercise 3. Display data type of variable x = 3.14
# • Use the type() function to print the data type of x = 3.14.

x = 3.14
print(f"{type(x)}")

# Exercise 4. Calculate the circumference of a circle
# • Define a constant PI = 3.14.
# • Calculate and print the circumference of a circle with radius r = 5

Pi = 3.14
r = 5
circumference = 2 * Pi * r
print(f"{circumference}")

# Exercise 5. Perform basic arithmetic with two numbers
# • Input two integers from the user.
# • Calculate and print their sum, difference, product (nhân), and quotient (thương).

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# Exercise 6. Function to calculate the sum of two numbers
# • Write a function sum_two_numbers(a, b) that returns the sum of two integers.
# • Call the function and print the result.

def sum_two_numbers(a, b):
    return a + b
print(sum_two_numbers(21, 7))

# Exercise 7. Declare, process, and display personal information
# • Create variables name, age, and average_score.
# • Use the type() function to display the data type of each variable.
# • Create a variable age_next_year by adding 1 to age, and doubled_score by
# doubling average_score.
# • Print all the information and their data types.

name = "qtitpc"
age = 18
average_score = 85.5
print(f"Name: {name}, {type(name)}")
print(f"Age: {age}, {type(age)}")
print(f"Average Score: {average_score}, {type(average_score)}")
age_next_year = age + 1
doubled_score = average_score * 2
print(f"Age Next Year: {age_next_year}, {type(age_next_year)}")
print(f"Doubled Score: {doubled_score}, {type(doubled_score)}")

# Exercise 8. Check if a number is even
# • Write a function is_even(n) that returns True if n is even, otherwise False.

n=int(input())
def is_even(x):
    if x%2==0:
        return True
    else:
        return False
print(is_even(n))

# Exercise 9. Find the maximum of three numbers
# • Input three numbers and print the largest one.

# n=map(int,input().split())
# print(max(n))

# n=map(int, input().split())
# list=list(n)
# for i in list(n):
#     if a[i] < a[i+1]:
#         print(a[i+1])
#     elif a[i] > a[i+1]:
#         print(a[i])
#     else:
#         print(a[i])

n=list(map(int, input().split()))
maximum=n[0]
for num in n:
    if num > maximum:
        maximum = num
print(maximum)

# Exercise 10. Function with default argument
# • Write a function greet(name="Student") that prints "Hello, Student!".
# • Call the function with and without providing an argument.

def greet(name="Student"):
    print(f"Hello, {name}!")
greet()
greet("qtitpc")
greet("qtung")


# Exercise 11. Validate age input
# • Prompt the user to enter their age.
# • Check if the age is between 1 and 120. Print a suitable message.

try:
    age_input = int(input())
    age=int(age_input)
    if age >= 120 or age <=1:
        print("Invalid age")
    else:
        print("OK")
except ValueError:
    print("Invalid input")

# Exercise 12. Count occurrences of character 'a'
# • Input a string and count the number of times the letter 'a' appears.

s = input()
sum = 0
for i in s:
    if i == "a":
        sum += 1
print(sum)

# Exercise 13. Convert string number to integer
# • Convert the string "123" into an integer, multiply it by 2, and print the result.

s = "123"
n = int(s)
res = n * 2
print(res)

# Exercise 14. Convert Celsius to Fahrenheit
# Write a program that converts a temperature from degrees Celsius to
# degrees Fahrenheit.
# • Ask the user to input the temperature in Celsius (as a float).
# • Use the formula: F = C × 9/5 + 32
# • Print the result in a formatted string.

c = float(input())
f = c * 9 / 5 + 32
print(f"{c}oC = {f}oF")

# Exercise 15. Calculate BMI (Body Mass Index)
# Write a program that calculates and displays the Body Mass Index (BMI).
# • Input: weight in kilograms and height in meters.
# • Formula: BMI = weight / (height * height)
# • Use float type and arithmetic operators.
# • Display the BMI rounded to 2 decimal places.
# If weight = 60kg and height = 1.65m → BMI ≈ 22.04


weight, height = map(float, input().split())
avg_bmi = weight / (height * height)
# print(round(avg_bmi, 2))
print(f"{avg_bmi:.2f}")


# Assignment - Exception Handling
# • Exercise 16: Input two integers from the keyboard and print the result of
# their division. Handle division by zero and invalid input types.


# • Exercise 17: Input a number and calculate its square root. If the input is
# negative, display an error message.


# • Exercise 18: Input two floating-point numbers and print their sum. Handle
# errors when the input is not a valid float.


# • Exercise 19: Input an integer and calculate its factorial. Handle errors for
# negative input or invalid data types.


# • Exercise 20: Input a string and print its length. Handle the case where the
# user enters an empty string by displaying an error message.
