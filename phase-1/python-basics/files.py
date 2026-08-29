with open("greeting.txt", "w") as f:
    f.write("Hello, this file was written by python.\n")

try:
    with open("missing.txt", "r") as f:
        contents = f.read()
        print(contents)
except FileNotFoundError:
    print("Error: The file does not exist.")