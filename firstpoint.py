def calculate_operation(number1: float, number2: float, operator: str):
    """
    this function performs the specified operation between two operands.

    the arguments of the function are 
        number1 (float): First operand.
        number2 (float): Second operand.
        operator (str): Character representing the operation (+, -, *, or /).

    Returns:
        float: Result of the operation.
    """
    if operator == "+":
        result = number1 + number2  # Adds operands if the operator is "+"
    elif operator == "-":
        result = number1 - number2  # Subtracts operands if the operator is "-"
    elif operator == "*":
        result = number1 * number2  # Multiplies operands if the operator is "*"
    elif operator == "/":
        if number2 != 0:
            result = number1 / number2  # Divides operands if the operator is "/"
        else:
            print("Error: Cannot divide by zero.")
            return None  # Returns None if division by zero is attempted
    else:
        print("Error: Invalid operator. Use +, -, *, or /.")
        return None  # Returns None if the operator is invalid

    return result  # Returns the result of the operation

# Example of usage
number1 = float(input("Enter the first operand: "))  # Asks the user for the first operand
number2 = float(input("Enter the second operand: "))  # Asks the user for the second operand
operator = str(input("Enter the operator (+, -, *, /): "))  # Asks the user for the operator

result = calculate_operation(number1, number2, operator)  # Calls the function
if result is not None:
    print(f"Result: {result}")  # Prints the result if it is not None
