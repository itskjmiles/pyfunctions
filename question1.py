# Task 1
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

# Task 2
def get_operation():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            return int(choice)
        else:
            print("Invalid input. Please enter 1, 2, 3, or 4.")

def get_numbers():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    return x, y

# Task 3
def calculator():
    operation = get_operation()
    x, y = get_numbers()

    if operation == 1:
        print("Result:", add(x, y))
    elif operation == 2:
        print("Result:", subtract(x, y))
    elif operation == 3:
        print("Result:", multiply(x, y))
    elif operation == 4:
        result = divide(x, y)
        if isinstance(result, str):
            print(result)
        else:
            print("Result:", result)

if __name__ == "__main__":
    calculator()
