def arithmetic_operations(num1, num2):
    """
    Perform basic arithmetic operations on two numbers.

    Parameters:
        num1 (float or int): The first number.
        num2 (float or int): The second number.

    Returns:
        tuple: A tuple containing the results of addition, subtraction,
               multiplication, and division (if num2 is not zero). If num2
               is zero, division result will be "Cannot divide by zero".
    """
    try:
        # Input Validation
        if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
            raise ValueError("Both inputs must be numeric")
        
        # Addition
        addition = num1 + num2
        
        # Subtraction
        subtraction = num1 - num2
        
        # Multiplication
        multiplication = num1 * num2
        
        # Division
        if num2 != 0:
            division = num1 / num2
        else:
            division = "Cannot divide by zero"
        
        return addition, subtraction, multiplication, division
    
    except Exception as e:
        return f"Error: {e}"

# Example usage
result_add, result_sub, result_mul, result_div = arithmetic_operations(10, 5)
print("Addition:", result_add)
print("Subtraction:", result_sub)
print("Multiplication:", result_mul)
print("Division:", result_div)