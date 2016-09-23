class Subject(object):  # Represents what is being 'observed'
    def __init__(self):
        self._observers = []  # This is where references to all the observers are being kept
        # Note that his is a one-to-many relationship: there will be
        # one subject to be observed my multiple observers

    def attach(self, observer):
        # If the observer is not already in the observer list, append the observer to the list
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):  # Simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        # For all the observers in the list
        # Don't notify the observer who is actually updating the temperature
        # Alert the observer
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Core(Subject):  # inherits from the subject class
    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name  # set the name of the core
        self._temp = 0  # initialize the temperature of the core

    @property  # getter that gets the core temperature
    def temp(self):
        return self._temp

    @temp.setter  # Setter that sets the core temperature
    def temp(self, temp):
        self._temp = temp
        # Notify the observers whenever somebody changes the core temperature
        self.notify()


class TempViewer:
    def update(self, subject):  # Alert method that is invoked when the notify() method is concrete subject is invoked
        print("Temperature Viewer: {} has temperature {}".format(subject._name, subject._temp))


# Let's create our subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

# Let's create our observer
v1 = TempViewer()
v2 = TempViewer()

# Let's attach our observers to the first core
c1.attach(v1)
c2.attach(v2)

# Let's change the temperature of our first core
c1.temp = 80
c2.temp = 90
