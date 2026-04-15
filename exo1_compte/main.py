from compte_securise import CompteBancaire

def main():
    nom = input("Nom du titulaire : ")
    compte = CompteBancaire(nom, 100, 50)

    print(f"Bienvenue {compte.titulaire}")
    
    compte.deposer(50)
    compte.retirer(120)

    print(f"Solde final : {compte.solde}")
    compte.afficher_historique()

if __name__ == "__main__":
    main()