def is_even(number):
    if number % 2 == 0:
         return True
    else:
	    return False

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
     print("Running helpers.py directly")
     print(is_even(4))