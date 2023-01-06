
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

    def Chargetest(self, level=None):
        batterie=self.__battery_level
        for i in range(level):
            if batterie<=level:
                print("la batterie est chargé à:", batterie)
                batterie=batterie+10
                time.sleep(1)

        self.__battery_level=batterie-10


    def Nom(self, Nom):
        self.__name = Nom
        

    def Stop(self):
        
        self.__current_speed = 0
        
        
    def Speed(self, vitesse):
        self.__current_speed = vitesse
        
    
    @property
    def AffichSpeed(self):
        print("Sa vitesse est de:")
        return self.__current_speed
    
    @property
    def AfficheCharge(self):
        print("Le Niveau de Charge:")
        return self.__battery_level

    @property
    def AffichNom(self):
        print("Le nom du robot est: ")
        return self.__name

    @property
    def AffichEtat(self):
        if self.__power == True:
            print("Robot Allume")
            return self.__power
        else:
            print("Robot Eteint")
            return self.__power

    def Status(self):
        
        print(r.AffichEtat)
        print(r.AffichNom)
        print(r.AfficheCharge)
        print(r.AffichSpeed)


r = Robot()
r.Allume()
r.Nom("Robito")
r.Chargetest(100)
r.Speed(250)
r.Status()
