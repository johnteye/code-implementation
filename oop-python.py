class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        #self.__age = age (access modifier to tell you not to access it cos it's private)


    def description(self):
        return f"{self.name} is {self.age} years old"


person1 = Person("John", 19)


print(person1.description())

class African(Person):
    def speaks(self, language = "Igbo"):
        return f"{self.name} speaks {language}"
        #super().speaks() - used for overriding inheritance from super class
person2 = African("Princess", 24)

print(person2.speaks())
