class CompteBancaire:
    def __init__(self, titulaire, solde, decouvert_autorise):
        self._historique = []
        self._nb_operations = 0
        self.decouvert_autorise = decouvert_autorise
        self.titulaire = titulaire
        self.solde = solde

    @property
    def titulaire(self):
        return self._titulaire
    
    @titulaire.setter
    def titulaire(self, valeur):
        if not isinstance(valeur, str) or valeur.strip() == "":
            raise ValueError("Le titulaire doit être une chaîne non vide")
        self._titulaire = valeur

    @property
    def decouvert_autorise(self):
        return self._decouvert_autorise
    
    @decouvert_autorise.setter
    def decouvert_autorise(self, valeur):
        if not isinstance(valeur, (int, float)) or isinstance(valeur, bool) or valeur < 0:
            raise ValueError("Le découvert autorisé doit être un nombre positif ou nul")
        self._decouvert_autorise = valeur

    @property
    def solde(self):
        return self._solde
    
    @solde.setter
    def solde(self, valeur):
        if valeur < -self._decouvert_autorise:
            raise ValueError("Le solde dépasse le découvert autorisé")
        self._solde = valeur

    @property
    def est_a_decouvert(self):
        return self._solde < 0
    
    @property
    def nb_operations(self):
        return self._nb_operations
    
    def deposer(self, montant):
        if isinstance(montant, bool):
            raise TypeError("Pas de booléen")
        if not isinstance(montant, (int, float)) or montant <= 0:
            raise ValueError("Montant invalide")
            
        self.solde += montant
        self._nb_operations += 1
        self._historique.append(f"+ {montant} | solde : {self.solde}")
        
    def retirer(self, montant):
        if isinstance(montant, bool):
            raise TypeError("Pas de booléen")
        if not isinstance(montant, (int, float)) or montant <= 0:
            return False
            
        if self.solde - montant >= -self.decouvert_autorise:
            self.solde -= montant
            self._nb_operations += 1
            self._historique.append(f"- {montant} | solde : {self.solde}")
            return True
        return False
    
    def afficher_historique(self):
        print(f"Historique de {self.titulaire}:")
        for operation in self._historique:
            print(operation)
     



            
                
              
        
        


            
 
        
        
        

