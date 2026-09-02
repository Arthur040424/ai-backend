class Person:
  def __init__(self, name, age):
          self.name = name
          self.age = age

  def introduce(self):
          return f"Hi, I'm {self.name} and I'm {self.age} years old."

arthur = Person("Arthur", 20)
print(arthur.introduce())

jane = Person("Jane", 25)
print(jane.introduce())