def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error: Division by zero is not allowed."
        else:
            return "Invalid operator. Please use +, -, *, or /."
        
        return f"Result: {result}"
    except ValueError:
        return "Error: Please enter valid numbers."

if __name__ == "__main__":
    print(calculator())
