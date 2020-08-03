class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def say_hi(self):
        return "Hi, my name is " + self.name + " and I am " + str(self.age) + " years old"

jack = Person("Jack",21)
elvis = Person ("Elvis", 42)
print(jack.get_name())
print(elvis.get_age())
print(jack.say_hi())
