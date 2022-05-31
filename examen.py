class Commande:
    def __init__(self,menu_taille):
        self.menu_taille=menu_taille
        for key, (a,b) in dic.items():
            if key==self.menu_taille:
                print("vous avez choisi",a)

    def confirmation(self,c):
        if self.menu_taille in l1 :
            if c==1:
                print("vous avez confirmé la commande")
                for key, (a, b) in dic.items():
                    if key == self.menu_taille:
                        print("Veillez insérer votre carte. Le montant de la commande est", b, "dollars")
            elif c==2:
                print("Vous avez annulé la commande")
            else:
                print("On reconnait pas votre choix: commande annulée")

print("Bienvenu Chez Juice Maker")
print("liste des menus avec leur taille")
print("1:Boost_Small, 2:Boost_Medieum,3:Boost_Large,4:Fresh_Small, 5:Fresh_Medieum,6:Fresh_Large,7:Fusion_Small, 8:Fusion_Medieum,9:Fusion_Large,10:Detox_Small, 11:Detox_Medieum,12:Detox_Large")
a=int(input("Veillez choisir votre menu par exemple tapez 1 pour le menu Boost en taille Small "))
dic = {1: ("Boost_Small",5), 2: ("Boost_Medieum",5.5), 3: ("Boost_Large",6), 4: ("Fresh_Small",4), 5: ("Fresh_Medieum",4.5),
               6: ("Fresh_Large",5), 7: ("Fusion_Small",5), 8: ("Fusion_Medieum",5.5), 9: ("Fusion_Large",6), 10: ("Detox_Small",3.5),
               11: ("Detox_Medieum",4), 12: ("Detox_Large",4.5)}
l1=[1,2,3,4,3,4,5,6,7,8,9,10,11,12]
if a in l1:
    commande = Commande(a)
    confirmations=int(input("Tapez 1: pour confirmer et 2: pour annuler"))
    commande.confirmation(confirmations)
else:
    print("veillez choisir un menu existant")
