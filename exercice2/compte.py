class CompteBancaire:
    
    taux_interet = 0.02

    def __init__(self, titulaire, solde, decouvert_autorise=0):
        self.titulaire = titulaire
        self.solde = solde
        self.decouvert_autorise = decouvert_autorise
        self.historique = []

    def deposer(self, montant):
        self.solde += montant
        self.historique.append(f"+ {montant} | solde : {self.solde}")
    
    def retirer(self, montant):
        if self.solde - montant >= -self.decouvert_autorise:
            self.solde -= montant
            self.historique.append(f"- {montant} | solde : {self.solde}")
            return True
        print("opération refusée")
        return False

    def virement(self, autre_compte, montant):
        if self.retirer(montant):
            autre_compte.deposer(montant)

    def afficher_historique(self):
        print(f"historique {self.titulaire}:")
        for operation in self.historique:
            print(operation)

    def appliquer_interets(self):
        if self.solde > 0:
            self.deposer(self.solde * self.taux_interet)


      
      
      

       


                                



