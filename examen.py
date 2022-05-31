class Commande:
    def __init__(self,menu_taille,mon_argent):
        self.menu_taille=menu_taille
        self.mon_argent=mon_argent
        for key, (a,b) in dic.items():
            if key==self.menu_taille:
                print("vous avez choisi",a)

    def confirmation(self,c):
        if self.menu_taille in l1 :
            if c==1:
                print("vous avez validé la commande")
                for key, (a, b) in dic.items():
                    if key == self.menu_taille:
                        print("Le montant de la commande est", b, "dollars")
            elif c==2:
                print("Vous avez annulé la commande")
            else:
                print("On reconnait pas votre choix: commande annulée")
    def get_menut_taille(self):
        return self.menu_taille
    def addjuice(self):
        l=[]
        l.append(self.menu_taille)
        print("liste de votre commande est",l)
    def monney(self):
        for key, (a, b) in dic.items():
            if key == self.menu_taille:
                if self.mon_argent>b:
                    print("votre de monney est de ",self.mon_argent-b, "dollars")
                else:
                    print("Votre argent est insuffisant")


print("Bienvenu Chez Juice Maker")
print("liste des menus avec leur taille")
print("1:Boost_Small, 2:Boost_Medieum,3:Boost_Large,4:Fresh_Small, 5:Fresh_Medieum,6:Fresh_Large,7:Fusion_Small, 8:Fusion_Medieum,9:Fusion_Large,10:Detox_Small, 11:Detox_Medieum,12:Detox_Large")
a=int(input("Veillez choisir votre menu par exemple tapez 1 pour le menu Boost en taille Small: "))
dic = {1: ("Boost_Small",5), 2: ("Boost_Medieum",5.5), 3: ("Boost_Large",6), 4: ("Fresh_Small",4), 5: ("Fresh_Medieum",4.5),
               6: ("Fresh_Large",5), 7: ("Fusion_Small",5), 8: ("Fusion_Medieum",5.5), 9: ("Fusion_Large",6), 10: ("Detox_Small",3.5),
               11: ("Detox_Medieum",4), 12: ("Detox_Large",4.5)}
print("--------------commande1--------------------------------------")
commande3=Commande(3,10)
l1=[1,2,3,4,3,4,5,6,7,8,9,10,11,12]
if a in l1:
    commande1 = Commande(a,20)
    confirmations=int(input("Tapez 1: pour valider et 2: pour annuler"))
    commande1.confirmation(confirmations)
    if confirmations==1:
        commande1.monney()
        commande1.addjuice()
else:
    print("veillez choisir un menu existant")
print("-------------------------------------------------------------------------------------------")
print("--------------commande2--------------------------------------")
commande2=Commande(9,2)
commande2.monney()
commande2.addjuice()
print("--------------commande3--------------------------------------")
commande3=Commande(3,10)
commande3.monney()
commande3.addjuice()

