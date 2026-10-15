#!/usr/bin/env python3
"""Le Pendu - un petit jeu de devinette de mots en terminal.

Lancement : python3 pendu.py
"""

import random
import unicodedata

VIES_MAX = 6

MOTS = {
    "Animaux": [
        "elephant", "girafe", "hérisson", "écureuil", "crocodile",
        "chauve-souris", "pieuvre", "flamant", "renard", "baleine",
    ],
    "Cuisine": [
        "ratatouille", "baguette", "croissant", "bouillabaisse",
        "tartiflette", "macaron", "camembert", "cassoulet", "clafoutis",
    ],
    "Informatique": [
        "clavier", "algorithme", "variable", "serveur", "python",
        "compilateur", "récursivité", "navigateur", "mémoire",
    ],
    "Géographie": [
        "montagne", "archipel", "volcan", "estuaire", "péninsule",
        "toundra", "glacier", "savane", "atoll",
    ],
}

POTENCE = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========""",
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========""",
]


def sans_accent(texte):
    """Retire les accents : 'écureuil' -> 'ecureuil'."""
    decompose = unicodedata.normalize("NFD", texte)
    return "".join(c for c in decompose if unicodedata.category(c) != "Mn")


def affiche_mot(mot, trouvees):
    """Affiche le mot avec des tirets bas pour les lettres non trouvées."""
    sortie = []
    for lettre in mot:
        if not lettre.isalpha():          # tiret, espace, apostrophe...
            sortie.append(lettre)
        elif sans_accent(lettre) in trouvees:
            sortie.append(lettre)
        else:
            sortie.append("_")
    return " ".join(sortie)


def mot_complet(mot, trouvees):
    return all(
        not l.isalpha() or sans_accent(l) in trouvees for l in mot
    )


def demande_lettre(proposees):
    """Boucle jusqu'à obtenir une lettre valide et non déjà jouée."""
    while True:
        saisie = input("Ta lettre : ").strip().lower()
        if len(saisie) != 1 or not saisie.isalpha():
            print("  → Entre une seule lettre, s'il te plaît.")
            continue
        lettre = sans_accent(saisie)
        if lettre in proposees:
            print(f"  → Tu as déjà proposé « {lettre} ».")
            continue
        return lettre


def une_partie():
    categorie = random.choice(list(MOTS))
    mot = random.choice(MOTS[categorie])
    lettres_mot = {sans_accent(l) for l in mot if l.isalpha()}

    proposees = set()
    trouvees = set()
    erreurs = 0

    print(f"\nCatégorie : {categorie}")
    print(f"Le mot fait {len(mot)} caractères.\n")

    while erreurs < VIES_MAX and not lettres_mot <= trouvees:
        print(POTENCE[erreurs])
        print("\n  " + affiche_mot(mot, trouvees))
        ratees = sorted(proposees - lettres_mot)
        print(f"  Lettres ratées : {' '.join(ratees) if ratees else '—'}")
        print(f"  Vies restantes : {VIES_MAX - erreurs}\n")

        lettre = demande_lettre(proposees)
        proposees.add(lettre)

        if lettre in lettres_mot:
            trouvees.add(lettre)
            print(f"\n✅ Bien vu, il y a des « {lettre} » !\n")
        else:
            erreurs += 1
            print(f"\n❌ Pas de « {lettre} »...\n")

    gagne = lettres_mot <= trouvees
    if gagne:
        print(f"  {affiche_mot(mot, trouvees)}")
        print(f"\n🎉 Gagné ! Le mot était « {mot} ».")
    else:
        print(POTENCE[VIES_MAX])
        print(f"\n💀 Perdu... Le mot était « {mot} ».")
    return gagne


def main():
    print("=" * 40)
    print("           L E   P E N D U")
    print("=" * 40)
    print(f"Devine le mot lettre par lettre. {VIES_MAX} erreurs maximum.")
    print("Les accents sont ignorés : tape 'e' pour 'é'.")

    victoires = parties = 0
    while True:
        victoires += une_partie()
        parties += 1
        print(f"\nScore : {victoires} victoire(s) sur {parties} partie(s).")

        rejouer = input("\nUne autre partie ? (o/n) ").strip().lower()
        if not rejouer.startswith("o"):
            print("À bientôt !")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nPartie interrompue. À bientôt !")