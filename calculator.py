#!/usr/bin/env python3
"""
Simple Console Calculator
A basic calculator to help understand programming fundamentals
"""
def get_number(prompt):
    """Get a
 number from user input with error handling"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number")

def get_operator():
    """Get a valid mathematical operator from user"""
    while True:
        operator = input("Enter operator (+, -, *, /): ").strip()
        if operator in ['+', '-', '*', '/']:
            return operator
        print("Error: Please enter a valid operator (+, -, *, /)")

def calculate(num1, num2, operator):
    """Perform the calculation"""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2

def main():
    """Main calculator function"""
    print("=== Simple Console Calculator ===")
    print("This calculator performs basic mathematical operations")
    print()
    
    while True:
        # Get first number
        print("Enter first number:")
        num1 = get_number("> ")
        
        # Get operator
        operator = get_operator()
        
        # Get second number
        print("Enter second number:")
        num2 = get_number("> ")
        
        # Calculate and display result
        result = calculate(num1, num2, operator)
        print(f"\nResult: {num1} {operator} {num2} = {result}")
        
        # Ask if user wants to continue
        print("\n" + "="*40)
        choice = input("Do another calculation? (y/n): ").strip().lower()
        if choice != 'y':
            break
        print()
    
    print("\nThank you for using the calculator!")

if __name__ == "__main__":
    main()
