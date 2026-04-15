from compte_securise import CompteBancaire

def test_compte_bancaire():
    c = CompteBancaire("Alice", 500, 200)
    
    c.deposer(100)
    c.retirer(800)
    c.retirer(50)

    print(f"Solde actuel : {c.solde}")
    print(f"À découvert ? {c.est_a_decouvert}")
    print(f"Nombre d'opérations : {c.nb_operations}")

    print("-" * 20)
    c.afficher_historique()
    print("-" * 20)

    try:
        c.titulaire = ""
    except ValueError as e:
        print(f"Erreur capturée : {e}")

    try:
        c.deposer(True)
    except TypeError as e:
        print(f"Erreur capturée : {e}")

if __name__ == "__main__":
    test_compte_bancaire()