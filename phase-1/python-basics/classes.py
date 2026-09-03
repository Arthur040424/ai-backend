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

class Student(Person):
        def __init__(self, name, age, school):
            super().__init__(name, age)
            self.school = school

        def introduce(self):
            return f"Hi, I'm {self.name},  {self.age} years old, and I study at {self.school}."

arthur_student = Student("Arthur", 20, "KINAP")
print(arthur_student.introduce())