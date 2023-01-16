# # EXO 3

# ## Exigences

# * Mettre en avant un principe de classe abstraite
# * Mettre en avant un principe de polymorphisme
# * Mettre en avant un principe d'héritage multiple
# * Max 3 méthodes par classe (hors getter/setter)
# * Pas d'algorithmes complexes, juste des print ;)
# * En tant que client, je veux pouvoir jouer avec trois types/dérivés de robots différents

# ### Aide

# Sortez un bon vieux crayon pour schématiser vos dépendances d'héritages

from abc import ABCMeta, abstractmethod

""" You can use classes below or create your own 👍️"""

class UnmannedVehicle(metaclass=ABCMeta):
    """ 
        An autonomous vehicle have to do his mission automatically.
        This mission can be configured by an operator.
    """
    @abstractmethod
    def startmission(self):
        pass
        
    
    @abstractmethod
    def do_something_interesting(self):
        pass
        

    @abstractmethod
    def stopmission(self):
        pass
        
        
    
class AerialVehicle(metaclass=ABCMeta):

    """ A vehicle made for ground fields."""

    @abstractmethod
    def do_something_aerial_specific(self):
        pass

class GroundVehicle(metaclass=ABCMeta):

    """ A vehicle made for ground fields."""

    @abstractmethod
    def do_something_ground_specific(self):
        pass
    

class UnderseaVehicle(metaclass=ABCMeta):

    """ A vehicle made for ground fields."""
    
    @abstractmethod
    def do_something_undersea_specific(self):
        pass

class UAV(UnmannedVehicle, AerialVehicle):
    """Unmanned Aerial Vehicle"""
    
    def startmission(self):
        print("Debut de mission UAV")
         

    def stopmission(self):
        print("Arret de mission UAV")
        

    def do_something_interesting(self):
        print("Fonctionne")
        

    def do_something_aerial_specific(self):
        print("Vole")
        

class UUV(UnmannedVehicle, UnderseaVehicle):
    """Unmanned Undersea Vehicle"""
    
    def startmission(self):
        print("Debut de mission UUV")


    def stopmission(self):
       print("Arret de mission UUV")
        

    def do_something_interesting(self):
        print("Fonctionne")
        

    def do_something_undersea_specific(self):
        print("Navigue")
        

class UGV(UnmannedVehicle, GroundVehicle):
    """Unmanned Ground Vehicle"""
    
    def startmission(self):
        print("Debut de mission UGV")
        
        
    def stopmission(self):
        print("Arret de mission UGV")
        
    
    def do_something_interesting(self):
        print("Fonctionne")

    
    def do_something_ground_specific(self):
        print("Roule")
        

if __name__=='__main__':

    uav = UAV()
    uav.startmission()
    uav.do_something_interesting()
    uav.do_something_aerial_specific()
    uav.stopmission()

    ugv = UGV()
    ugv.startmission()
    ugv.do_something_interesting()
    ugv.do_something_ground_specific()
    ugv.stopmission()

    uuv = UUV()
    uuv.startmission()
    uuv.do_something_interesting()
    uuv.do_something_undersea_specific()
    uuv.stopmission()
