name = "Arthur"
age = 15
is_learning = True

print(name)
print(age)
print(is_learning)

age_str = "3"
print(age_str)
print(type(age_str))
print(type(age))

print(age + 5)
print(age_str + "5")

print(int(age_str) + 5)

# print(int("hello") + 5)

if age >= 18:
    print("You are an adult")
# elif 13 <= age <= 17: also works the same way
elif age >= 13 and age <= 17:
    print("You are a teenager")


ages = [15, 22, 8, 30, 13]

for age in ages:
    if age >= 18:
        print(age, "is an adult")
    elif 13 <= age <= 17:
        print(age, "is a teenager")
    else:
        print(age, "is a child")