
    #Lorsque je crée mon robot, je veux pouvoir lui attribuer un nom
    #Mon robot doit pouvoir s'allumer
    #Mon robot doit pouvoir s'éteindre
    #Mon robot doit pouvoir charger sa batterie à 100%, allumé ou non
    #Le temps de charge ne peut pas être immédiat (10s max)
    #Mon robot doit afficher sont % de batterie durant sa charge
    #Mon robot doit pouvoir enregistrer une vitesse de déplacement
    #Mon robot doit pouvoir me donner sa vitesse de déplacement
    #Mon robot doit pouvoir arrêter son déplacement sur commande
    #Mon robot doit pouvoir me fournir un résumé de son état global
import time

class Robot():

    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
    

    def Allume(self):
        
        self.__power = True
        

    def Eteindre(self):
        
        self.__power = False


    def Charge(self, Niveau=None):
	
        if type(Niveau) == int:
        
            self.__battery_level = Niveau
        
        elif Niveau is None:
            return "Mise de la Batterie 100%"

    def chargetest(self, level=None):
        batterie=self.__battery_level
        for i in range(level):
            if batterie<=level:
                print("la batterie est chargé à:", batterie, "%")
                batterie=batterie+10
                time.sleep(1)

        self.__battery_level=batterie-10


    def nom(self, Nom):
        self.__name = Nom
        

    def stop(self):
        
        self.__current_speed = 0
        print("Arret du Robot")
        
        
    def Speed(self, vitesse):
        
        self.__current_speed = vitesse
        
    
    @property
    def affichSpeed(self):
        print("Sa vitesse est de:")
        return self.__current_speed
    
    @property
    def afficheCharge(self):
        print("Le Niveau de Charge:")
        return self.__battery_level

    @property
    def affichNom(self):
        print("Le nom du robot est: ")
        return self.__name

    @property
    def affichEtat(self):
        if self.__power == True:

            self.__states = 'running'
            return self.__states

        else:

            self.__states = 'shutdown'
            return self.__states

    def status(self):
        print("---STATUS---")
        print(self.affichEtat)
        print(self.affichNom)
        print(self.afficheCharge)
        print(self.affichSpeed)
        print("--------------")

print(__name__)

if __name__=='__main__':
    r = Robot()
    entrernom=input('Entrer le nom du robot:')
    r.Allume()
    r.nom(entrernom)
    r.Chargetest(0)
    r.Speed(250)
    r.status()
    r.stop()
