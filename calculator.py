#calculator.py

def get_numbers():
    try:
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second number: "))
        return num1, num2
    except ValueError:
        print("wrong input.")
        return None, None


def get_operation():    
    print("choose operation---")
    print("1. addition")
    print("2. subtract")
    print("3. division")
    print("4. multiplicaiton")

    operation = input("choose operation ( 1 / 2 / 3 / 4 ): ")
    if operation in ['1', '2', '3', '4']:
        return operation
    else:
        print('wrong input. choose between 1 to 4')
        return None
    
def perform_caculation(num1, num2, operation):
    if operation == '1':
        return num1 + num2
        
    elif operation == '2' :
        return num1 - num2
    
    elif operation == '3' :
        if num2 != 0:
            return num1 / num2
        else :
            print("error: wrong input (num2) cannot be 0.")
            return None

    elif operation == '4' :
        return num1 * num2


def calculate():
    num1, num2 = get_numbers()
    if num1 is None or num2 is None:
        return

    operation = get_operation()
    if operation is None:
        return
    
    result = perform_caculation(num1, num2, operation)
    if result is not None:
        print(f"result of {num1} and {num2} is {result}.")


#repeatedly run the program
while True:
    calculate()
    continue_calculation = input("continue calculation? (y/n): ")
    if continue_calculation.lower() != 'y':
        break