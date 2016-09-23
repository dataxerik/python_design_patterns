class House(object): # The class being visited
    def accept(self, visitor):
        """interface to accept a visitor"""
        # Trigger the visiting operation

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist) # Note that we now have a reference to the HVAC specialist object
                                                     # in the hosue object!
    def work_on_electricity(self, electrician):
        # Note taht we now have a reference to the electrician in the house object!

    def __str__(self):
        """Simply return the class name when the House object in printed"""
        return self.__class__.__name__

class Visitor(object):
    """Abstract visitor"""
    def __str__(self):
        """Simply return the class name when the Visitor object is printed"""
        return self.__class__.__name__

class HvacSpecialist(Visitor): # Inherits from the parent class, Visitor
    """Concrete visitor: HVAC specialist"""
