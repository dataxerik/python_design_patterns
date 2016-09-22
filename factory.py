class Dog:
    """A simple dog class"""
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"

class Cat:
    """A simple dog class"""
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow!"

def get_pet(pet="dog"):
    """The factory method"""

    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))

    return pets[pet]

print(get_pet("dog").speak())
print(get_pet("cat").speak())