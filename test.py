s = input()
if s == "":
    print("an empty string")
else:
    print(len(s))

# try:
#     a = int(input())
#     if a < 0:
#         print("negative input")
#     res = 1
#     for i in range(1, a + 1):
#         res *= i
#     print(res)
# except ValueError:
#     print("invalid data types")

# try:
#     a,b=map(float,input().split())
#     print(a+b)
# except ValueError:
#     print("input is not a valid float")


# try:
#     n = float(input())
#     if n < 0:
#         print("negative number")
#     else:
#         print(n**0.5)
# except ValueError:
#     print("Invalid input")

# try:
#     a, b = map(int, input().split())
#     print("a / b =", a / b)
# except ZeroDivisionError:
#     print("Error: division by zero")
# except ValueError:
#     print("Error: invalid integer input")

# weight, height = map(float, input().split())
# avg_bmi = weight / (height * height)
# # print(round(avg_bmi, 2))
# print(f"{avg_bmi:.2f}")

# c = float(input())
# f = c * 9 / 5 + 32
# print(f"{c}oC = {f}oF")


# s = "123"
# n = int(s)
# res = n * 2
# print(res)


# s = input()
# sum = 0
# for i in s:
#     if i == "a":
#         sum += 1
# print(sum)


# try:
#     age_input = int(input())
#     age=int(age_input)
#     if age >= 120 or age <=1:
#         print("Invalid age")
#     else:
#         print("OK")
# except ValueError:
#     print("Invalid input")

# def greet(name="Student"):
#     print(f"Hello, {name}!")
# greet()
# greet("qtitpc")
# greet("qtung")

# n = list(map(int, input().split()))
# maximum = n[0]
# for num in n:
#     if num > maximum:
#         maximum = num
# print(maximum)
#
