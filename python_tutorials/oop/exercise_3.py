class Animal:
    def speak(self):
        print("Generic animal sound")


class Dog(Animal):
    def speak(self):
        print("Bark")


class Cat(Animal):
    def speak(self):
        print("Meow")
