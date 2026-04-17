def afficher_conseils(conseils):
    if conseils:
        print("Pour améliorer votre mot de passe, vous pouvez :")
        for c in conseils:
            print(f"- {c}")
    else:
        print("Votre mot de passe est déjà robuste !")