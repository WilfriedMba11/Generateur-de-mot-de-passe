from generator import generer_mot_de_passe
from checker import verifier_mot_de_passe

def menu():
    mot_de_passe = ""
    while True:
        print("\n--- MENU ---")
        print("1. Générer ou entrer un mot de passe")
        print("2. Tester le mot de passe")
        print("3. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            sous_choix = input("Voulez-vous (G)énérer ou (E)ntrer un mot de passe ? ").lower()
            if sous_choix == "g":
                mot_de_passe = generer_mot_de_passe()
                print(f"Mot de passe généré : {mot_de_passe}")
            elif sous_choix == "e":
                mot_de_passe = input("Entrez votre mot de passe : ")
            else:
                print("Choix invalide.")
        
        elif choix == "2":
            if mot_de_passe:
                force, conseils = verifier_mot_de_passe(mot_de_passe)
                print(f"Niveau de sécurité : {force}")
                if conseils:
                    print("Pour améliorer votre mot de passe, vous pouvez :")
                    for c in conseils:
                        print(f"- {c}")
                else:
                    print("Votre mot de passe est déjà robuste !")
            else:
                print("Veuillez d'abord entrer ou générer un mot de passe (option 1).")
        
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    menu()