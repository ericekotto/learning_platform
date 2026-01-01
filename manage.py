# -*- coding: utf-8 -*-
# ========================================
# manage.py (À la racine du projet)
# ========================================
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_platform.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()


# ========================================
# populate_courses.py (Script de peuplement - À la racine)
# ========================================
"""
Script pour créer les cours et exercices de démonstration
Exécutez : python populate_courses.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_platform.settings')
django.setup()

from courses.models import Course, Exercise


def create_courses():
    """Crée les 4 cours principaux"""
    
    print("Création des cours...")
    
    # COURS 1 : Variables et instructions de base
    course1, created = Course.objects.get_or_create(
        course_type='variables',
        defaults={
            'title': 'Variables et Instructions de Base',
            'description': 'Apprenez les fondamentaux de la programmation : qu\'est-ce qu\'une variable, comment la déclarer et l\'utiliser.',
            'content': '''
# Variables et Instructions de Base

## Qu'est-ce qu'une variable ?
Une variable est comme une boîte dans laquelle on peut stocker des informations. En programmation, on donne un nom à cette boîte pour pouvoir y accéder plus tard.

## Déclaration d'une variable
En Python : `nom = "Jean"`
En C : `int age = 25;`
En JavaScript : `let ville = "Yaoundé";`

## Types de données
- **Entiers (int)** : nombres entiers (ex: 10, -5, 0)
- **Flottants (float)** : nombres décimaux (ex: 3.14, -0.5)
- **Chaînes (string)** : texte (ex: "Bonjour", 'Python')
- **Booléens (bool)** : vrai/faux (True/False)

## Instructions de base
- **Affectation** : `x = 10` (donner une valeur à une variable)
- **Affichage** : `print(x)` (afficher la valeur)
- **Opérations arithmétiques** : +, -, *, /, %
''',
            'importance': '''Les variables sont LA BASE de tout programme informatique. Sans variables, impossible de stocker des données, faire des calculs ou garder des informations en mémoire. C'est comme essayer de cuisiner sans avoir de récipients pour mettre les ingrédients !''',
            'when_to_use': '''Utilisez des variables TOUJOURS quand vous devez :
- Stocker une information pour la réutiliser plus tard
- Faire des calculs avec des données
- Garder le résultat d'une opération
- Rendre votre code plus lisible en donnant des noms significatifs aux valeurs''',
            'possible_operations': '''
- Déclarer une variable : `x = 5`
- Modifier une variable : `x = x + 1`
- Additionner : `resultat = a + b`
- Soustraire : `diff = a - b`
- Multiplier : `produit = a * b`
- Diviser : `quotient = a / b`
- Concaténer des chaînes : `nom_complet = prenom + " " + nom`
- Comparer des valeurs : `est_egal = (a == b)`
''',
            'impossible_operations': '''
- Utiliser une variable avant de la déclarer
- Additionner directement un nombre et une chaîne (il faut convertir)
- Utiliser des caractères spéciaux dans les noms de variables (@, #, -, espaces)
- Commencer un nom de variable par un chiffre
''',
            'order': 1,
            'youtube_search_query': 'cours algorithmique variables débutant français'
        }
    )
    if created:
        print(f"✓ Cours créé : {course1.title}")
    
    # COURS 2 : Instructions conditionnelles
    course2, created = Course.objects.get_or_create(
        course_type='conditionals',
        defaults={
            'title': 'Instructions Conditionnelles',
            'description': 'Apprenez à faire des choix dans vos programmes avec if, else, elif.',
            'content': '''
# Instructions Conditionnelles

## Qu'est-ce qu'une condition ?
Une condition permet à votre programme de prendre des décisions. "Si X est vrai, alors faire Y, sinon faire Z".

## Structure if
```python
if age >= 18:
    print("Vous êtes majeur")
```

## Structure if-else
```python
if note >= 10:
    print("Admis")
else:
    print("Recalé")
```

## Structure if-elif-else
```python
if note >= 16:
    print("Excellent")
elif note >= 14:
    print("Bien")
elif note >= 10:
    print("Passable")
else:
    print("Insuffisant")
```

## Opérateurs de comparaison
- `==` : égal à
- `!=` : différent de
- `>` : supérieur à
- `<` : inférieur à
- `>=` : supérieur ou égal
- `<=` : inférieur ou égal

## Opérateurs logiques
- `and` : ET logique
- `or` : OU logique
- `not` : NON logique
''',
            'importance': '''Les conditions sont essentielles pour créer des programmes intelligents qui s'adaptent aux différentes situations. C'est ce qui permet à un programme de prendre des décisions automatiquement !''',
            'when_to_use': '''Utilisez des conditions quand :
- Vous devez tester une valeur avant d'agir
- Votre programme doit se comporter différemment selon les cas
- Vous devez valider des données (âge valide, mot de passe correct, etc.)
- Vous voulez éviter des erreurs (division par zéro, etc.)''',
            'possible_operations': '''
- Comparer deux valeurs : `if x > y:`
- Tester l'égalité : `if nom == "Jean":`
- Combiner des conditions : `if age >= 18 and permis == True:`
- Vérifier l'appartenance : `if ville in ["Yaoundé", "Douala"]:`
- Tester le type : `if isinstance(x, int):`
''',
            'impossible_operations': '''
- Utiliser = au lieu de == pour comparer (= est pour l'affectation)
- Oublier les : à la fin de la condition
- Mal indenter le code sous le if
- Comparer des types incompatibles sans conversion
''',
            'order': 2,
            'youtube_search_query': 'cours algorithmique conditions if else français'
        }
    )
    if created:
        print(f"✓ Cours créé : {course2.title}")
    
    # COURS 3 : Structures itératives (boucles)
    course3, created = Course.objects.get_or_create(
        course_type='loops',
        defaults={
            'title': 'Structures Itératives (Boucles)',
            'description': 'Apprenez à répéter des actions avec les boucles for et while.',
            'content': '''
# Structures Itératives (Boucles)

## Qu'est-ce qu'une boucle ?
Une boucle permet de répéter une série d'instructions plusieurs fois sans avoir à réécrire le code.

## Boucle for
Utilisée quand on connaît le nombre d'itérations :
```python
for i in range(5):
    print(f"Tour numéro {i}")
```

```python
fruits = ["pomme", "banane", "orange"]
for fruit in fruits:
    print(fruit)
```

## Boucle while
Utilisée quand on répète tant qu'une condition est vraie :
```python
compteur = 0
while compteur < 10:
    print(compteur)
    compteur += 1
```

## Contrôle des boucles
- `break` : sort de la boucle immédiatement
- `continue` : passe à l'itération suivante
- `else` : exécuté si la boucle se termine normalement

## Boucles imbriquées
```python
for i in range(3):
    for j in range(3):
        print(f"{i},{j}")
```
''',
            'importance': '''Les boucles évitent la répétition de code et permettent de traiter de grandes quantités de données efficacement. Imaginez devoir écrire 1000 fois la même instruction manuellement !''',
            'when_to_use': '''Utilisez des boucles quand :
- Vous devez répéter une action plusieurs fois
- Vous parcourez une liste, un tableau ou une collection
- Vous traitez des données en série
- Vous attendez qu'une condition soit remplie
- Vous générez des motifs ou des séquences''',
            'possible_operations': '''
- Parcourir une liste : `for element in liste:`
- Compter de 0 à n : `for i in range(n):`
- Répéter tant que : `while condition:`
- Sortir d'une boucle : `break`
- Passer à l'itération suivante : `continue`
- Boucles imbriquées : for dans for
''',
            'impossible_operations': '''
- Modifier la liste en cours de parcours (peut causer des bugs)
- Oublier d'incrémenter le compteur dans while (boucle infinie !)
- Utiliser break en dehors d'une boucle
- Oublier les : à la fin de for ou while
''',
            'order': 3,
            'youtube_search_query': 'cours algorithmique boucles for while français'
        }
    )
    if created:
        print(f"✓ Cours créé : {course3.title}")
    
    # COURS 4 : Fonctions et procédures
    course4, created = Course.objects.get_or_create(
        course_type='functions',
        defaults={
            'title': 'Fonctions et Procédures',
            'description': 'Apprenez à créer des fonctions réutilisables pour organiser votre code.',
            'content': '''
# Fonctions et Procédures

## Qu'est-ce qu'une fonction ?
Une fonction est un bloc de code réutilisable qui effectue une tâche spécifique. C'est comme une mini-machine qu'on peut utiliser plusieurs fois.

## Déclaration d'une fonction
```python
def saluer(nom):
    print(f"Bonjour {nom} !")

saluer("Marie")  # Appel de la fonction
```

## Fonction avec retour
```python
def additionner(a, b):
    resultat = a + b
    return resultat

somme = additionner(5, 3)  # somme vaut 8
```

## Paramètres et arguments
- **Paramètres** : variables dans la définition
- **Arguments** : valeurs passées lors de l'appel

```python
def calculer_aire(longueur, largeur):  # paramètres
    return longueur * largeur

aire = calculer_aire(5, 3)  # arguments
```

## Paramètres par défaut
```python
def saluer(nom, message="Bonjour"):
    print(f"{message} {nom} !")

saluer("Jean")  # Utilise "Bonjour"
saluer("Marie", "Bonsoir")  # Utilise "Bonsoir"
```

## Fonctions vs Procédures
- **Fonction** : retourne une valeur
- **Procédure** : effectue une action sans retour (ou return None)

## Portée des variables
- Variables **locales** : définies dans la fonction
- Variables **globales** : définies hors de toute fonction
''',
            'importance': '''Les fonctions sont essentielles pour :
- Éviter la répétition de code (DRY : Don't Repeat Yourself)
- Organiser le code en blocs logiques
- Faciliter la maintenance et les tests
- Rendre le code plus lisible et compréhensible
- Permettre la réutilisation du code''',
            'when_to_use': '''Créez une fonction quand :
- Vous répétez le même code plusieurs fois
- Vous avez un bloc de code qui fait une tâche spécifique
- Vous voulez tester une partie de votre code isolément
- Vous voulez partager du code avec d'autres développeurs
- Votre code dépasse 50-100 lignes (divisez-le en fonctions)''',
            'possible_operations': '''
- Définir une fonction : `def ma_fonction():`
- Appeler une fonction : `ma_fonction()`
- Retourner une valeur : `return resultat`
- Passer des paramètres : `def func(param1, param2):`
- Paramètres par défaut : `def func(x=0):`
- Retourner plusieurs valeurs : `return a, b, c`
- Fonctions récursives : une fonction qui s'appelle elle-même
''',
            'impossible_operations': '''
- Utiliser une fonction avant de la définir
- Oublier les parenthèses lors de l'appel
- Passer le mauvais nombre d'arguments
- Utiliser return en dehors d'une fonction
- Oublier les : après def
''',
            'order': 4,
            'youtube_search_query': 'cours algorithmique fonctions procédures français'
        }
    )
    if created:
        print(f"✓ Cours créé : {course4.title}")
    
    print(f"\n{Course.objects.count()} cours créés au total !")
    return [course1, course2, course3, course4]


def create_exercises():
    """Crée des exercices pour chaque cours"""
    
    print("\nCréation des exercices...")
    
    courses = Course.objects.all()
    
    # Exercices pour VARIABLES
    course_var = Course.objects.get(course_type='variables')
    exercises_var = [
        {
            'title': 'Déclaration de variable',
            'question': 'Quelle est la syntaxe correcte pour déclarer une variable "age" avec la valeur 25 en Python ?',
            'option_a': 'age = 25',
            'option_b': 'int age = 25',
            'option_c': 'var age = 25',
            'option_d': '25 = age',
            'correct_answer': 'A',
            'explanation': 'En Python, on utilise simplement le signe = pour affecter une valeur à une variable. Pas besoin de spécifier le type.',
            'difficulty': 'easy',
            'points': 10,
            'order': 1
        },
        {
            'title': 'Types de données',
            'question': 'Quel est le type de la variable : x = "123"',
            'option_a': 'Entier (int)',
            'option_b': 'Chaîne de caractères (string)',
            'option_c': 'Flottant (float)',
            'option_d': 'Booléen (bool)',
            'correct_answer': 'B',
            'explanation': 'Les guillemets indiquent qu\'il s\'agit d\'une chaîne de caractères, même si le contenu ressemble à un nombre.',
            'difficulty': 'easy',
            'points': 10,
            'order': 2
        },
        {
            'title': 'Opération arithmétique',
            'question': 'Quel est le résultat de : x = 10 + 5 * 2',
            'option_a': '30',
            'option_b': '20',
            'option_c': '25',
            'option_d': '17',
            'correct_answer': 'B',
            'explanation': 'La multiplication a la priorité sur l\'addition : 5*2=10, puis 10+10=20.',
            'difficulty': 'medium',
            'points': 15,
            'order': 3
        },
    ]
    
    for ex_data in exercises_var:
        ex, created = Exercise.objects.get_or_create(
            course=course_var,
            title=ex_data['title'],
            defaults=ex_data
        )
        if created:
            print(f"  ✓ Exercice : {ex.title}")
    
    # Exercices pour CONDITIONNELLES
    course_cond = Course.objects.get(course_type='conditionals')
    exercises_cond = [
        {
            'title': 'Structure if simple',
            'question': 'Que va afficher ce code ?\nage = 20\nif age >= 18:\n    print("Majeur")',
            'option_a': 'Majeur',
            'option_b': 'Mineur',
            'option_c': 'Rien',
            'option_d': 'Erreur',
            'correct_answer': 'A',
            'explanation': 'La condition age >= 18 est vraie (20 >= 18), donc "Majeur" sera affiché.',
            'difficulty': 'easy',
            'points': 10,
            'order': 1
        },
        {
            'title': 'Opérateur de comparaison',
            'question': 'Quel opérateur teste l\'égalité entre deux valeurs ?',
            'option_a': '=',
            'option_b': '==',
            'option_c': '!=',
            'option_d': '===',
            'correct_answer': 'B',
            'explanation': '== teste l\'égalité, = est pour l\'affectation, != teste la différence.',
            'difficulty': 'easy',
            'points': 10,
            'order': 2
        },
        {
            'title': 'Conditions multiples',
            'question': 'Quelle condition teste si x est entre 10 et 20 (inclus) ?',
            'option_a': 'if x > 10 and x < 20:',
            'option_b': 'if x >= 10 and x <= 20:',
            'option_c': 'if 10 < x < 20:',
            'option_d': 'if x == 10 or x == 20:',
            'correct_answer': 'B',
            'explanation': 'On utilise >= et <= pour inclure les bornes, et "and" pour combiner les conditions.',
            'difficulty': 'medium',
            'points': 15,
            'order': 3
        },
    ]
    
    for ex_data in exercises_cond:
        ex, created = Exercise.objects.get_or_create(
            course=course_cond,
            title=ex_data['title'],
            defaults=ex_data
        )
        if created:
            print(f"  ✓ Exercice : {ex.title}")
    
    # Exercices pour BOUCLES
    course_loops = Course.objects.get(course_type='loops')
    exercises_loops = [
        {
            'title': 'Boucle for simple',
            'question': 'Combien de fois "Bonjour" sera affiché ?\nfor i in range(5):\n    print("Bonjour")',
            'option_a': '4 fois',
            'option_b': '5 fois',
            'option_c': '6 fois',
            'option_d': 'Infiniment',
            'correct_answer': 'B',
            'explanation': 'range(5) génère les nombres de 0 à 4, soit 5 itérations.',
            'difficulty': 'easy',
            'points': 10,
            'order': 1
        },
        {
            'title': 'Boucle while',
            'question': 'Quelle condition arrête cette boucle ?\nwhile x < 10:\n    x = x + 1',
            'option_a': 'Quand x est égal à 9',
            'option_b': 'Quand x est égal à 10',
            'option_c': 'Quand x est supérieur à 10',
            'option_d': 'Jamais',
            'correct_answer': 'B',
            'explanation': 'La boucle continue tant que x < 10. Elle s\'arrête quand x atteint 10.',
            'difficulty': 'medium',
            'points': 15,
            'order': 2
        },
        {
            'title': 'Instruction break',
            'question': 'Que fait l\'instruction "break" dans une boucle ?',
            'option_a': 'Passe à l\'itération suivante',
            'option_b': 'Sort de la boucle immédiatement',
            'option_c': 'Redémarre la boucle',
            'option_d': 'Met la boucle en pause',
            'correct_answer': 'B',
            'explanation': 'break permet de sortir immédiatement d\'une boucle, même si la condition n\'est pas fausse.',
            'difficulty': 'medium',
            'points': 15,
            'order': 3
        },
    ]
    
    for ex_data in exercises_loops:
        ex, created = Exercise.objects.get_or_create(
            course=course_loops,
            title=ex_data['title'],
            defaults=ex_data
        )
        if created:
            print(f"  ✓ Exercice : {ex.title}")
    
    # Exercices pour FONCTIONS
    course_func = Course.objects.get(course_type='functions')
    exercises_func = [
        {
            'title': 'Définition de fonction',
            'question': 'Quelle est la syntaxe correcte pour définir une fonction en Python ?',
            'option_a': 'function maFonction():',
            'option_b': 'def maFonction():',
            'option_c': 'func maFonction():',
            'option_d': 'define maFonction():',
            'correct_answer': 'B',
            'explanation': 'En Python, on utilise le mot-clé "def" pour définir une fonction.',
            'difficulty': 'easy',
            'points': 10,
            'order': 1
        },
        {
            'title': 'Retour de fonction',
            'question': 'Que va retourner cette fonction ?\ndef doubler(x):\n    return x * 2\nresultat = doubler(5)',
            'option_a': '5',
            'option_b': '10',
            'option_c': '25',
            'option_d': 'None',
            'correct_answer': 'B',
            'explanation': 'La fonction multiplie x par 2. Avec x=5, elle retourne 5*2=10.',
            'difficulty': 'easy',
            'points': 10,
            'order': 2
        },
        {
            'title': 'Paramètres de fonction',
            'question': 'Combien de paramètres a cette fonction ?\ndef calculer(a, b, c=0):',
            'option_a': '1 paramètre',
            'option_b': '2 paramètres',
            'option_c': '3 paramètres',
            'option_d': '4 paramètres',
            'correct_answer': 'C',
            'explanation': 'La fonction a 3 paramètres : a, b, et c (avec une valeur par défaut de 0).',
            'difficulty': 'medium',
            'points': 15,
            'order': 3
        },
    ]
    
    for ex_data in exercises_func:
        ex, created = Exercise.objects.get_or_create(
            course=course_func,
            title=ex_data['title'],
            defaults=ex_data
        )
        if created:
            print(f"  ✓ Exercice : {ex.title}")
    
    print(f"\n{Exercise.objects.count()} exercices créés au total !")


if __name__ == '__main__':
    print("=" * 60)
    print("PEUPLEMENT DE LA BASE DE DONNÉES")
    print("=" * 60)
    
    create_courses()
    create_exercises()
    
    print("\n" + "=" * 60)
    print("✅ BASE DE DONNÉES PEUPLÉE AVEC SUCCÈS !")
    print("=" * 60)
    print("\nVous pouvez maintenant :")
    print("1. Lancer le serveur : python manage.py runserver")
    print("2. Accéder à l'admin : http://127.0.0.1:8000/admin/")
    print("3. Créer des comptes étudiants et encadreurs")
    print("=" * 60)