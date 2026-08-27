def classify_age(age):
  if age >= 18:
    print("Adult")
  elif 13 <= age <= 17:
    print("Teenager")
  else:
    print("Child")

result = classify_age(20)
print(result)
# result = classify_age(15)
# print(result)
# result = classify_age(5)
# print(result)
# result = classify_age(45)
# print(result)

# def is_even(number):
#   if number % 2 == 0:
#     return True
#   else:
#     return False

# result = is_even(4)
# print(result)

# result = is_even(7)
# print(result)