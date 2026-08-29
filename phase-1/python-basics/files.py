import json

# with open("greeting.txt", "w") as f:
#     f.write("Hello, this file was written by python.\n")

# try:
#     with open("missing.txt", "r") as f:
#         contents = f.read()
#         print(contents)
# except FileNotFoundError:
#     print("Error: The file does not exist.")

data = {
    "name": "Arthur",
    "age": 20,
    "hobbies": ["reading", "coding"]
}

with open("profile.json", "w") as f:
    json.dump(data, f)

with open("profile.json", "r") as f:
    loaded_data = json.load(f)

print(loaded_data)
print(loaded_data["name"])
print(loaded_data["age"])
print(type(loaded_data["age"]))