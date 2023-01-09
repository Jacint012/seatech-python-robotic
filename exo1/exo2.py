
# Réutiliser la class Robot faite dans l'exo 1. *Sans copier/coller dans le fichier ;)*
# Un humain doit posséder un sexe attribuable à sa création
# Un humain doit pouvoir manger un ou plusieurs aliments
# Un humain doit pouvoir digérer ce qu'il a mangé *pas très important, faire en dernier si vous avez le temps*
# Un Cyborg doit être une combinaison d'un humain et d'un robot
# Bonus : ajouter une méthode fun au Cyborg

from exo1 import Robot

class Human():   

    SEXE_POSSIBILITIES = ('M','F','X')
    __sexe='X'
    __food=[]

    def __init__(self, sexe):
        if sexe in self.SEXE_POSSIBILITIES:
            self.__sexe=sexe
        

    def eat (self,food):
        self.__food.append(food)

    @property
    def affichsexe (self):
        return self.__sexe
        

    @property
    def affichfood (self):
        return self.__food


class Cyborg(Robot, Human):   

    def __init__(self, name, sexe):
        
        #Robot.__init__(self, name)
        self.nom(name)
    
        Human.__init__(self, sexe)




h=Human('M')
print('le sexe est:')
print(h.affichsexe)
h.eat('coca')
print('la nourriture est:')
print(h.affichfood)

cyborg = Cyborg('Deux Ex Machina', 'M')
print(cyborg.affichNom)
print(cyborg.affichNom, 'sexe', cyborg.affichsexe)
print('Charging battery...')
cyborg.chargetest(30)
cyborg.status()
# cyborg.eat('banana')
# cyborg.eat(['coca', 'chips'])
# #cyborg.digest()