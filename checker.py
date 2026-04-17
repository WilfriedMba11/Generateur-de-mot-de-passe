import re

def verifier_mot_de_passe(mot_de_passe):
    conseils = []
    niveau = 0

    # Longueur
    if len(mot_de_passe) >= 12:
        niveau += 2
    elif len(mot_de_passe) >= 8:
        niveau += 1
    else:
        conseils.append("Augmentez la longueur (au moins 12 caractères).")

    # Majuscules
    if re.search(r"[A-Z]", mot_de_passe):
        niveau += 1
    else:
        conseils.append("Ajoutez des lettres majuscules.")

    # Minuscules
    if re.search(r"[a-z]", mot_de_passe):
        niveau += 1
    else:
        conseils.append("Ajoutez des lettres minuscules.")

    # Chiffres
    if re.search(r"[0-9]", mot_de_passe):
        niveau += 1
    else:
        conseils.append("Ajoutez des chiffres.")

    # Caractères spéciaux
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", mot_de_passe):
        niveau += 1
    else:
        conseils.append("Ajoutez des caractères spéciaux (ex: !, @, #, $).")

    # Évaluation
    if niveau <= 2:
        force = "Faible"
    elif niveau <= 4:
        force = "Moyenne"
    else:
        force = "Forte"

    return force, conseils