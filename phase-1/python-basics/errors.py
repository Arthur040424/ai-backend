def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: cannot divide by zero")
    return None


print(divide(10, 2))
print(divide(10, 0))
print("Program kept running after the errors")
