class Korean:
    """Korean speaker"""
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong"

class British:
    """English speaker"""
    def __init__(self):
        self.name = "British"

    # Note the difference method name here!
    def speak_english(self):
        return "Hello"

class Adapter:
    """This changes the generic method name to individualized method names"""
    def __init__(self, object, **adapted_method):
        """Change the name of the method"""
        self._object = object


        # add a new dictionary item that establishes the mapping between the generic method name: speak()
        # and the concrete method. For example, speak() will be translated to spreak_korean() if the
        # mapping says so
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the rest of the attributes"""
        return getattr(self._object, attr)
# list to store speak objects
objects = []

# Create a Korean object
korean = Korean()
# Create a British object
british = British()
# append the objects
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print("{} says {}\n".format(obj.name, obj.speak()))
