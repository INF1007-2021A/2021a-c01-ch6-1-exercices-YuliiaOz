#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        print('Entrez 10 valeurs de type entier, float ou string: ')
        liste_de_valeurs = [(input()), (input()), (input()), (input()), (input()), (input()), (input()), (input()), (input()), (input())]
        pass
    liste_de_valeurs.sort()
    return [liste_de_valeurs]


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        print('Entrez deux chaînes de caractères pour voir si elles sont des anagrammes: ')
        pass

    chaine1 = list(input())
    chaine2 = list(input())

    chaine1.sort()
    chaine2.sort()
    return (chaine1 == chaine2)


def contains_doubles(items: list) -> bool:
    my_list = [3, 3, 5, 6, 1, 1]
    return len(my_list) != len(set(my_list))


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    #print(f"On essaie d'ordonner les valeurs...")
    #print('Voilà les valeurs ordonnées: ', order())

    #print("On vérifie les anagrammes...")
    #print("Est-ce que c'est un anagrammes?", anagrams())

    #my_list = [3, 3, 5, 6, 1, 1]
    #print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()


