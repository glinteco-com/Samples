class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def greet(self):
        print(
            f"Hi, I'm {self.name}, a {self.major} major, and I'm {self.age} years old."
        )
