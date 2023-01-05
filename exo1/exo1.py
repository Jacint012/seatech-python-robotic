
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

class Robot():
    __name = "<unnamed>"
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
    
        
    def AfficheCharge(self):

        return self.__battery_level
        

    def Stop(self):
        
        self.__current_speed = 0
        
        
        
    def Move(self, speed):
        
        if type(speed) == int:
        
            self.__current_speed = speed
        
        
        
    def Speed(self):
        
        return self.__current_speed


r = Robot()
r.AfficheCharge()
