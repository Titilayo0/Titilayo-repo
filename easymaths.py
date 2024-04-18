def arithmetic_operations(num1, num2):
    # Addition
    addition = num1 + num2
    # Subtraction
    subtraction = num1 - num2
    # Multiplication
    multiplication = num1 * num2
    # Division
    # Checking if num2 is not zero to avoid division by zero error
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Cannot divide by zero"
    
    return addition, subtraction, multiplication, division


result_add, result_sub, result_mul, result_div = arithmetic_operations(10, 5)
print("Addition:", result_add)
print("Subtraction:", result_sub)
print("Multiplication:", result_mul)
print("Division:", result_div)