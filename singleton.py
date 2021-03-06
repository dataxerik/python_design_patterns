# Borg design pattern singleton

class Borg:
    """Borg class making attributes global"""

    _shared_state = {}  # attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_state  # Make it an attribute dictionary


class Singleton(Borg):  # Inherits from the Borg class
    """This class now shares all of its attributes among its various instances"""

    # This essentially makes the singleton objects an object-oriented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
        # Returns the attribute dictionary for printing
        return str(self._shared_state
                   )

x = Singleton(HTTP = "Hyper Text Transfer Protocol")
# Let's create a singleton object and add our first acronym

# Print the object
print(x)
# Let's create another singleton object and if it refers to the same attribute dictionary by adding another example
y = Singleton(SMMP = "Simple Network Management Protocol")
# Print the object
print(y)
