#Second Part of the task
from functions import open_file_in_vscode, list_installed_extensions, add, multiply, divide
print("Opening README in VS Code...")
open_file_in_vscode("README.md")
print("Installed extensions:")
list_installed_extensions()

sum_result = add(2.5, 3.7)
print("2.5 + 3.7 =", sum_result)

multiply_result = multiply(1.5, 4)
print("1.5 x 4 =", multiply_result)

divide_result = divide(7.5, 2.5)
print("7.5 / 2.5 =", divide_result)

first_number = float(input("Type the first number: "))
second_number = float(input("Type the second number: "))

print("Sum:", add(first_number, second_number))
print("Multiplication:", multiply(first_number, second_number))
print("Division:", divide(first_number, second_number))
