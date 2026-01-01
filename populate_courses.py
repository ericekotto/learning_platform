# -*- coding: utf-8 -*-
"""
Script COMPLET pour créer les cours et exercices ENRICHIS
Exécutez : python populate_courses.py

✨ CONTIENT :
- 4 cours complets avec application interactive pour Variables
- 20 exercices sur les Variables (facile, moyen, difficile)
- 15 exercices sur les Conditionnelles
- 15 exercices sur les Boucles
- 15 exercices sur les Fonctions
TOTAL : 65 exercices !
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_platform.settings')
django.setup()

from courses.models import Course, Exercise


def create_courses():
    """Crée les 4 cours principaux"""
    
    print("=" * 70)
    print("CRÉATION DES COURS")
    print("=" * 70)
    
    # COURS 1 : Variables et instructions de base
    course1, created = Course.objects.get_or_create(
        course_type='variables',
        defaults={
            'title': 'Variables et Instructions de Base',
            'description': 'Apprenez les fondamentaux de la programmation avec une application interactive !',
            'content': '''# Variables et Instructions de Base

🧮 **Application Interactive Disponible !**

Ce cours comprend une application interactive vous permettant de tester en direct toutes les opérations sur les variables.

## Qu'est-ce qu'une variable ?
Une variable est comme une boîte dans laquelle on peut stocker des informations. En programmation, on donne un nom à cette boîte pour pouvoir y accéder plus tard.

## Déclaration d'une variable
En Python : nom = "Jean"
En C : int age = 25;
En JavaScript : let ville = "Yaoundé";

## Types de données
- **Entiers (int)** : nombres entiers (ex: 10, -5, 0)
- **Flottants (float)** : nombres décimaux (ex: 3.14, -0.5)
- **Chaînes (string)** : texte (ex: "Bonjour", 'Python')
- **Booléens (bool)** : vrai/faux (True/False)

## Instructions de base
- **Affectation** : x = 10 (donner une valeur à une variable)
- **Affichage** : print(x) (afficher la valeur)
- **Opérations arithmétiques** : +, -, *, /, %
''',
            'importance': '''Les variables sont LA BASE de tout programme informatique. Sans variables, impossible de stocker des données, faire des calculs ou garder des informations en mémoire. C'est comme essayer de cuisiner sans avoir de récipients pour mettre les ingrédients !

👉 **Utilisez l'application interactive** pour expérimenter avec les variables en temps réel !''',
            'when_to_use': '''Utilisez des variables TOUJOURS quand vous devez :
- Stocker une information pour la réutiliser plus tard
- Faire des calculs avec des données
- Garder le résultat d'une opération
- Rendre votre code plus lisible en donnant des noms significatifs aux valeurs''',
            'possible_operations': '''- Déclarer une variable : x = 5
- Modifier une variable : x = x + 1
- Additionner : resultat = a + b
- Soustraire : diff = a - b
- Multiplier : produit = a * b
- Diviser : quotient = a / b
- Concaténer des chaînes : nom_complet = prenom + " " + nom
- Comparer des valeurs : est_egal = (a == b)''',
            'impossible_operations': '''- Utiliser une variable avant de la déclarer
- Additionner directement un nombre et une chaîne (il faut convertir)
- Utiliser des caractères spéciaux dans les noms de variables (@, #, -, espaces)
- Commencer un nom de variable par un chiffre''',
            'order': 1,
            'youtube_search_query': 'cours algorithmique variables débutant français'
        }
    )
    if created:
        print(f"✓ Cours créé : {course1.title}")
    else:
        print(f"○ Cours existant : {course1.title}")
    
    # COURS 2 : Instructions conditionnelles
    course2, created = Course.objects.get_or_create(
        course_type='conditionals',
        defaults={
            'title': 'Instructions Conditionnelles',
            'description': 'Apprenez à faire des choix dans vos programmes avec if, else, elif.',
            'content': '''# Instructions Conditionnelles

## Qu'est-ce qu'une condition ?
Une condition permet à votre programme de prendre des décisions. "Si X est vrai, alors faire Y, sinon faire Z".

## Structure if
if age >= 18:
    print("Vous êtes majeur")

## Structure if-else
if note >= 10:
    print("Admis")
else:
    print("Recalé")

## Structure if-elif-else
if note >= 16:
    print("Excellent")
elif note >= 14:
    print("Bien")
elif note >= 10:
    print("Passable")
else:
    print("Insuffisant")

## Opérateurs de comparaison
- == : égal à
- != : différent de
- > : supérieur à
- < : inférieur à
- >= : supérieur ou égal
- <= : inférieur ou égal

## Opérateurs logiques
- and : ET logique
- or : OU logique
- not : NON logique
''',
            'importance': '''Les conditions sont essentielles pour créer des programmes intelligents qui s'adaptent aux différentes situations. C'est ce qui permet à un programme de prendre des décisions automatiquement !''',
            'when_to_use': '''Utilisez des conditions quand :
- Vous devez tester une valeur avant d'agir
- Votre programme doit se comporter différemment selon les cas
- Vous devez valider des données (âge valide, mot de passe correct, etc.)
- Vous voulez éviter des erreurs (division par zéro, etc.)''',
            'possible_operations': '''- Comparer deux valeurs : if x > y:
- Tester l'égalité : if nom == "Jean":
- Combiner des conditions : if age >= 18 and permis == True:
- Vérifier l'appartenance : if ville in ["Yaoundé", "Douala"]:
- Tester le type : if isinstance(x, int):''',
            'impossible_operations': '''- Utiliser = au lieu de == pour comparer (= est pour l'affectation)
- Oublier les : à la fin de la condition
- Mal indenter le code sous le if
- Comparer des types incompatibles sans conversion''',
            'order': 2,
            'youtube_search_query': 'cours algorithmique conditions if else français'
        }
    )
    if created:
        print(f"✓ Cours créé : {course2.title}")
    else:
        print(f"○ Cours existant : {course2.title}")
    
    # COURS 3 : Structures itératives (boucles)
    course3, created = Course.objects.get_or_create(
        course_type='loops',
        defaults={
            'title': 'Structures Itératives (Boucles)',
            'description': 'Apprenez à répéter des actions avec les boucles for et while.',
            'content': '''# Structures Itératives (Boucles)

## Qu'est-ce qu'une boucle ?
Une boucle permet de répéter une série d'instructions plusieurs fois sans avoir à réécrire le code.

## Boucle for
Utilisée quand on connaît le nombre d'itérations :
for i in range(5):
    print(f"Tour numéro {i}")

fruits = ["pomme", "banane", "orange"]
for fruit in fruits:
    print(fruit)

## Boucle while
Utilisée quand on répète tant qu'une condition est vraie :
compteur = 0
while compteur < 10:
    print(compteur)
    compteur += 1

## Contrôle des boucles
- break : sort de la boucle immédiatement
- continue : passe à l'itération suivante
- else : exécuté si la boucle se termine normalement

## Boucles imbriquées
for i in range(3):
    for j in range(3):
        print(f"{i},{j}")
''',
            'importance': '''Les boucles évitent la répétition de code et permettent de traiter de grandes quantités de données efficacement. Imaginez devoir écrire 1000 fois la même instruction manuellement !''',
            'when_to_use': '''Utilisez des boucles quand :
- Vous devez répéter une action plusieurs fois
- Vous parcourez une liste, un tableau ou une collection
- Vous traitez des données en série
- Vous attendez qu'une condition soit remplie
- Vous générez des motifs ou des séquences''',
            'possible_operations': '''- Parcourir une liste : for element in liste:
- Compter de 0 à n : for i in range(n):
- Répéter tant que : while condition:
- Sortir d'une boucle : break
- Passer à l'itération suivante : continue
- Boucles imbriquées : for dans for''',
            'impossible_operations': '''- Modifier la liste en cours de parcours (peut causer des bugs)
- Oublier d'incrémenter le compteur dans while (boucle infinie !)
- Utiliser break en dehors d'une boucle
- Oublier les : à la fin de for ou while''',
            'order': 3,
            'youtube_search_query': 'cours algorithmique boucles for while français'
        }
    )
    if created:
        print(f"✓ Cours créé : {course3.title}")
    else:
        print(f"○ Cours existant : {course3.title}")
    
    # COURS 4 : Fonctions et procédures
    course4, created = Course.objects.get_or_create(
        course_type='functions',
        defaults={
            'title': 'Fonctions et Procédures',
            'description': 'Apprenez à créer des fonctions réutilisables pour organiser votre code.',
            'content': '''# Fonctions et Procédures

## Qu'est-ce qu'une fonction ?
Une fonction est un bloc de code réutilisable qui effectue une tâche spécifique.

## Déclaration d'une fonction
def saluer(nom):
    print(f"Bonjour {nom} !")

saluer("Marie")

## Fonction avec retour
def additionner(a, b):
    resultat = a + b
    return resultat

somme = additionner(5, 3)

## Paramètres par défaut
def saluer(nom, message="Bonjour"):
    print(f"{message} {nom} !")

saluer("Jean")
saluer("Marie", "Bonsoir")

## Portée des variables
Variables locales : définies dans la fonction
Variables globales : définies hors de toute fonction
''',
            'importance': '''Les fonctions sont essentielles pour :
- Éviter la répétition de code (DRY : Don't Repeat Yourself)
- Organiser le code en blocs logiques
- Faciliter la maintenance et les tests
- Rendre le code plus lisible
- Permettre la réutilisation du code''',
            'when_to_use': '''Créez une fonction quand :
- Vous répétez le même code plusieurs fois
- Vous avez un bloc de code qui fait une tâche spécifique
- Vous voulez tester une partie de votre code isolément
- Votre code dépasse 50-100 lignes (divisez-le en fonctions)''',
            'possible_operations': '''- Définir une fonction : def ma_fonction():
- Appeler une fonction : ma_fonction()
- Retourner une valeur : return resultat
- Passer des paramètres : def func(param1, param2):
- Paramètres par défaut : def func(x=0):
- Retourner plusieurs valeurs : return a, b, c''',
            'impossible_operations': '''- Utiliser une fonction avant de la définir
- Oublier les parenthèses lors de l'appel
- Passer le mauvais nombre d'arguments
- Utiliser return en dehors d'une fonction
- Oublier les : après def''',
            'order': 4,
            'youtube_search_query': 'cours algorithmique fonctions procédures français'
        }
    )
    if created:
        print(f"✓ Cours créé : {course4.title}")
    else:
        print(f"○ Cours existant : {course4.title}")
    
    print(f"\n→ {Course.objects.count()} cours au total dans la base de données")
    return [course1, course2, course3, course4]


def create_variables_exercises():
    """Crée 20 exercices ENRICHIS sur les Variables"""
    
    print("\n📦 Création des exercices sur les VARIABLES (20 exercices)...")
    
    course = Course.objects.get(course_type='variables')
    
    exercises = [
        # ========== FACILE (10 exercices) ==========
        {
            'title': 'Déclaration de variable simple',
            'question': 'Quelle est la syntaxe correcte pour déclarer une variable "age" avec la valeur 25 en Python ?',
            'option_a': 'age = 25',
            'option_b': 'int age = 25',
            'option_c': 'var age = 25',
            'option_d': '25 = age',
            'correct_answer': 'A',
            'explanation': 'En Python, on utilise simplement le signe = pour affecter une valeur à une variable.',
            'difficulty': 'easy',
            'points': 10,
            'order': 1
        },
        {
            'title': 'Identification du type - Chaîne',
            'question': 'Quel est le type de la variable : x = "123"',
            'option_a': 'Entier (int)',
            'option_b': 'Chaîne de caractères (string)',
            'option_c': 'Flottant (float)',
            'option_d': 'Booléen (bool)',
            'correct_answer': 'B',
            'explanation': 'Les guillemets indiquent une chaîne de caractères, même si le contenu ressemble à un nombre.',
            'difficulty': 'easy',
            'points': 10,
            'order': 2
        },
        {
            'title': 'Type entier',
            'question': 'Parmi ces valeurs, laquelle est un entier (int) ?',
            'option_a': '3.14',
            'option_b': '"42"',
            'option_c': '42',
            'option_d': 'True',
            'correct_answer': 'C',
            'explanation': '42 sans guillemets ni virgule est un entier.',
            'difficulty': 'easy',
            'points': 10,
            'order': 3
        },
        {
            'title': 'Type flottant',
            'question': 'Quel est le type de : prix = 19.99',
            'option_a': 'Entier',
            'option_b': 'Flottant',
            'option_c': 'Chaîne',
            'option_d': 'Booléen',
            'correct_answer': 'B',
            'explanation': 'Un nombre avec une virgule (point) est un flottant (float).',
            'difficulty': 'easy',
            'points': 10,
            'order': 4
        },
        {
            'title': 'Type booléen',
            'question': 'Quelles sont les valeurs possibles d\'un booléen en Python ?',
            'option_a': '0 et 1',
            'option_b': 'True et False',
            'option_c': 'Oui et Non',
            'option_d': 'Vrai et Faux',
            'correct_answer': 'B',
            'explanation': 'En Python, les booléens sont True (vrai) et False (faux), avec une majuscule.',
            'difficulty': 'easy',
            'points': 10,
            'order': 5
        },
        {
            'title': 'Affectation de valeur',
            'question': 'Que fait cette instruction : x = 10',
            'option_a': 'Compare x et 10',
            'option_b': 'Affiche 10',
            'option_c': 'Affecte la valeur 10 à x',
            'option_d': 'Crée une erreur',
            'correct_answer': 'C',
            'explanation': 'Le signe = sert à affecter (donner) une valeur à une variable.',
            'difficulty': 'easy',
            'points': 10,
            'order': 6
        },
        {
            'title': 'Modification de variable',
            'question': 'Quelle est la valeur de x après ces instructions ?\nx = 5\nx = 10',
            'option_a': '5',
            'option_b': '10',
            'option_c': '15',
            'option_d': 'Erreur',
            'correct_answer': 'B',
            'explanation': 'La deuxième affectation remplace la première valeur. x vaut maintenant 10.',
            'difficulty': 'easy',
            'points': 10,
            'order': 7
        },
        {
            'title': 'Concaténation simple',
            'question': 'Que donne : "Hello" + " " + "World"',
            'option_a': 'Hello World',
            'option_b': 'HelloWorld',
            'option_c': 'Hello + World',
            'option_d': 'Erreur',
            'correct_answer': 'A',
            'explanation': 'Le + concatène (assemble) les chaînes. Les espaces sont inclus.',
            'difficulty': 'easy',
            'points': 10,
            'order': 8
        },
        {
            'title': 'None',
            'question': 'Que représente la valeur None en Python ?',
            'option_a': 'Zéro',
            'option_b': 'Chaîne vide',
            'option_c': 'Absence de valeur',
            'option_d': 'Faux',
            'correct_answer': 'C',
            'explanation': 'None représente l\'absence de valeur, c\'est différent de 0 ou d\'une chaîne vide.',
            'difficulty': 'easy',
            'points': 10,
            'order': 9
        },
        {
            'title': 'Nom de variable valide',
            'question': 'Quel nom de variable est VALIDE en Python ?',
            'option_a': '2variable',
            'option_b': 'ma-variable',
            'option_c': 'ma_variable',
            'option_d': 'ma variable',
            'correct_answer': 'C',
            'explanation': 'Un nom de variable peut contenir des lettres, chiffres et _ mais ne peut pas commencer par un chiffre ou contenir des espaces/tirets.',
            'difficulty': 'easy',
            'points': 10,
            'order': 10
        },
        
        # ========== MOYEN (7 exercices) ==========
        {
            'title': 'Opération arithmétique - Priorité',
            'question': 'Quel est le résultat de : x = 10 + 5 * 2',
            'option_a': '30',
            'option_b': '20',
            'option_c': '25',
            'option_d': '17',
            'correct_answer': 'B',
            'explanation': 'La multiplication a la priorité : 5*2=10, puis 10+10=20.',
            'difficulty': 'medium',
            'points': 15,
            'order': 11
        },
        {
            'title': 'Division entière vs division décimale',
            'question': 'Quelle est la différence entre 7/2 et 7//2 en Python ?',
            'option_a': 'Aucune différence',
            'option_b': '7/2 donne 3.5, 7//2 donne 3',
            'option_c': '7/2 donne 3, 7//2 donne 3.5',
            'option_d': 'Les deux donnent une erreur',
            'correct_answer': 'B',
            'explanation': '/ fait une division décimale (3.5), // fait une division entière (3).',
            'difficulty': 'medium',
            'points': 15,
            'order': 12
        },
        {
            'title': 'Modulo',
            'question': 'Que donne 17 % 5 ?',
            'option_a': '3',
            'option_b': '2',
            'option_c': '3.4',
            'option_d': '0',
            'correct_answer': 'B',
            'explanation': 'Le modulo (%) donne le reste de la division : 17 ÷ 5 = 3 reste 2.',
            'difficulty': 'medium',
            'points': 15,
            'order': 13
        },
        {
            'title': 'Multiplication de chaîne',
            'question': 'Que donne "Ha" * 3 ?',
            'option_a': 'HaHaHa',
            'option_b': 'Ha3',
            'option_c': '3Ha',
            'option_d': 'Erreur',
            'correct_answer': 'A',
            'explanation': 'On peut multiplier une chaîne par un entier pour la répéter.',
            'difficulty': 'medium',
            'points': 15,
            'order': 14
        },
        {
            'title': 'Addition impossible',
            'question': 'Que se passe-t-il avec : x = 5 + "10"',
            'option_a': 'x vaut 15',
            'option_b': 'x vaut 510',
            'option_c': 'x vaut "510"',
            'option_d': 'Erreur (types incompatibles)',
            'correct_answer': 'D',
            'explanation': 'On ne peut pas additionner directement un nombre et une chaîne. Il faut convertir.',
            'difficulty': 'medium',
            'points': 15,
            'order': 15
        },
        {
            'title': 'Conversion de type',
            'question': 'Comment convertir la chaîne "123" en entier ?',
            'option_a': 'integer("123")',
            'option_b': 'int("123")',
            'option_c': 'to_int("123")',
            'option_d': '"123".to_int()',
            'correct_answer': 'B',
            'explanation': 'La fonction int() convertit une chaîne en entier.',
            'difficulty': 'medium',
            'points': 15,
            'order': 16
        },
        {
            'title': 'Échange de variables',
            'question': 'Comment échanger les valeurs de a et b en Python ?\na = 5, b = 10',
            'option_a': 'a = b\nb = a',
            'option_b': 'temp = a\na = b\nb = temp',
            'option_c': 'a, b = b, a',
            'option_d': 'B et C sont corrects',
            'correct_answer': 'D',
            'explanation': 'Les deux méthodes fonctionnent, mais a, b = b, a est la syntaxe Python idiomatique.',
            'difficulty': 'medium',
            'points': 15,
            'order': 17
        },
        
        # ========== DIFFICILE (3 exercices) ==========
        {
            'title': 'Opérations combinées complexes',
            'question': 'Quel est le résultat de : (10 + 5) * 2 - 3 * 4',
            'option_a': '18',
            'option_b': '22',
            'option_c': '26',
            'option_d': '30',
            'correct_answer': 'A',
            'explanation': '(10+5)*2 - 3*4 = 15*2 - 12 = 30 - 12 = 18. Parenthèses d\'abord, puis *, puis -.',
            'difficulty': 'hard',
            'points': 20,
            'order': 18
        },
        {
            'title': 'Type dynamique',
            'question': 'Après ces instructions, quel est le type de x ?\nx = 10\nx = "10"\nx = x + "0"',
            'option_a': 'Entier',
            'option_b': 'Flottant',
            'option_c': 'Chaîne',
            'option_d': 'Erreur',
            'correct_answer': 'C',
            'explanation': 'x devient "100" (chaîne). Python permet de changer le type d\'une variable.',
            'difficulty': 'hard',
            'points': 20,
            'order': 19
        },
        {
            'title': 'Affectations multiples',
            'question': 'Après : a = b = c = 5\nc = 10\nQuelles sont les valeurs de a, b, c ?',
            'option_a': '5, 5, 5',
            'option_b': '10, 10, 10',
            'option_c': '5, 5, 10',
            'option_d': '5, 10, 10',
            'correct_answer': 'C',
            'explanation': 'L\'affectation multiple donne 5 à a, b et c. Puis c change seul à 10. a et b restent à 5.',
            'difficulty': 'hard',
            'points': 20,
            'order': 20
        },
    ]
    
    count = 0
    for ex_data in exercises:
        ex, created = Exercise.objects.get_or_create(
            course=course,
            title=ex_data['title'],
            defaults=ex_data
        )
        if created:
            count += 1
            print(f"  ✓ [{ex_data['difficulty'].upper()}] {ex.title}")
    
    print(f"→ {count} nouveaux exercices créés sur les Variables !")
    return count


def create_conditionals_exercises():
    """Crée 15 exercices sur les Conditionnelles"""
    
    print("\n🔀 Création des exercices sur les CONDITIONNELLES (15 exercices)...")
    
    course = Course.objects.get(course_type='conditionals')
    
    exercises = [
        # FACILE (5 exercices)
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
            'title': 'Opérateur d\'égalité',
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
            'title': 'Structure if-else',
            'question': 'Que fait le else dans une structure if-else ?',
            'option_a': 'Ajoute une condition supplémentaire',
            'option_b': 'S\'exécute si la condition if est fausse',
            'option_c': 'S\'exécute toujours',
            'option_d': 'Termine le programme',
            'correct_answer': 'B',
            'explanation': 'Le bloc else s\'exécute uniquement si la condition du if est fausse.',
            'difficulty': 'easy',
            'points': 10,
            'order': 3
        },
        {
            'title': 'Opérateur de différence',
            'question': 'Que teste l\'opérateur != ?',
            'option_a': 'Égalité',
            'option_b': 'Supériorité',
            'option_c': 'Différence',
            'option_d': 'Infériorité',
            'correct_answer': 'C',
            'explanation': '!= teste si deux valeurs sont différentes (non égales).',
            'difficulty': 'easy',
            'points': 10,
            'order': 4
        },
        {
            'title': 'Syntaxe if',
            'question': 'Quel est le symbole obligatoire à la fin d\'un if en Python ?',
            'option_a': ';',
            'option_b': ':',
            'option_c': '{',
            'option_d': 'Aucun',
            'correct_answer': 'B',
            'explanation': 'En Python, on doit mettre deux-points : à la fin d\'un if.',
            'difficulty': 'easy',
            'points': 10,
            'order': 5
        },
        
        # MOYEN (7 exercices)
        {
            'title': 'Conditions multiples avec and',
            'question': 'Quelle condition teste si x est entre 10 et 20 (inclus) ?',
            'option_a': 'if x > 10 and x < 20:',
            'option_b': 'if x >= 10 and x <= 20:',
            'option_c': 'if 10 < x < 20:',
            'option_d': 'if x == 10 or x == 20:',
            'correct_answer': 'B',
            'explanation': 'On utilise >= et <= pour inclure les bornes, et "and" pour combiner.',
            'difficulty': 'medium',
            'points': 15,
            'order': 6
        },
        {
            'title': 'Opérateur or',
            'question': 'Quand (x == 5 or y == 10) est-elle vraie ?',
            'option_a': 'Seulement si x=5 ET y=10',
            'option_b': 'Si x=5 OU y=10 (ou les deux)',
            'option_c': 'Jamais',
            'option_d': 'Seulement si x=5',
            'correct_answer': 'B',
            'explanation': 'L\'opérateur or est vrai si AU MOINS une des conditions est vraie.',
            'difficulty': 'medium',
            'points': 15,
            'order': 7
        },
        {
            'title': 'Structure elif',
            'question': 'À quoi sert elif ?',
            'option_a': 'Terminer une condition',
            'option_b': 'Tester une autre condition si la première est fausse',
            'option_c': 'Répéter une condition',
            'option_d': 'Inverser une condition',
            'correct_answer': 'B',
            'explanation': 'elif (else if) permet de tester une autre condition si les précédentes sont fausses.',
            'difficulty': 'medium',
            'points': 15,
            'order': 8
        },
        {
            'title': 'Opérateur not',
            'question': 'Que donne : not (5 > 3)',
            'option_a': 'True',
            'option_b': 'False',
            'option_c': '5',
            'option_d': '3',
            'correct_answer': 'B',
            'explanation': '5 > 3 est True, donc not True donne False. not inverse le résultat.',
            'difficulty': 'medium',
            'points': 15,
            'order': 9
        },
        {
            'title': 'Conditions imbriquées',
            'question': 'Combien de blocs if peut-on imbriquer maximum ?',
            'option_a': '1',
            'option_b': '3',
            'option_c': '10',
            'option_d': 'Pas de limite (mais déconseillé)',
            'correct_answer': 'D',
            'explanation': 'On peut imbriquer autant de if qu\'on veut, mais trop nuit à la lisibilité.',
            'difficulty': 'medium',
            'points': 15,
            'order': 10
        },
        {
            'title': 'Comparaison de chaînes',
            'question': 'Que donne : "abc" < "xyz"',
            'option_a': 'True',
            'option_b': 'False',
            'option_c': 'Erreur',
            'option_d': '0',
            'correct_answer': 'A',
            'explanation': 'Python compare les chaînes par ordre alphabétique. "abc" vient avant "xyz".',
            'difficulty': 'medium',
            'points': 15,
            'order': 11
        },
        {
            'title': 'Priorité des opérateurs',
            'question': 'Quelle condition est évaluée en premier ?\nif x > 5 and y < 10 or z == 3:',
            'option_a': 'x > 5',
            'option_b': 'and',
            'option_c': 'or',
            'option_d': 'Les comparaisons, puis and, puis or',
            'correct_answer': 'D',
            'explanation': 'Priorité : comparaisons d\'abord, puis and, puis or.',
            'difficulty': 'medium',
            'points': 15,
            'order': 12
        },
        
        # DIFFICILE (3 exercices)
        {
            'title': 'Conditions complexes',
            'question': 'Après ce code, quelle est la valeur de resultat ?\nx = 15\nif x > 10:\n    if x < 20:\n        resultat = "A"\n    else:\n        resultat = "B"\nelse:\n    resultat = "C"',
            'option_a': 'A',
            'option_b': 'B',
            'option_c': 'C',
            'option_d': 'Erreur',
            'correct_answer': 'A',
            'explanation': 'x=15 : x>10 est vrai, puis x<20 est vrai, donc resultat="A".',
            'difficulty': 'hard',
            'points': 20,
            'order': 13
        },
        {
            'title': 'Expression conditionnelle ternaire',
            'question': 'Que donne : resultat = "Pair" if 10 % 2 == 0 else "Impair"',
            'option_a': '"Pair"',
            'option_b': '"Impair"',
            'option_c': 'True',
            'option_d': 'Erreur',
            'correct_answer': 'A',
            'explanation': '10 % 2 == 0 est vrai (10 est pair), donc resultat = "Pair". C\'est une expression ternaire.',
            'difficulty': 'hard',
            'points': 20,
            'order': 14
        },
        {
            'title': 'Court-circuit logique',
            'question': 'Dans (False and fonction()), la fonction() sera-t-elle appelée ?',
            'option_a': 'Oui, toujours',
            'option_b': 'Non, car False and X est toujours False',
            'option_c': 'Seulement si fonction() retourne True',
            'option_d': 'Cela dépend',
            'correct_answer': 'B',
            'explanation': 'Python utilise l\'évaluation paresseuse : si le premier terme d\'un and est False, il ne teste pas la suite.',
            'difficulty': 'hard',
            'points': 20,
            'order': 15
        },
    ]
    
    count = 0
    for ex_data in exercises:
        ex, created = Exercise.objects.get_or_create(
            course=course,
            title=ex_data['title'],
            defaults=ex_data
        )
        if created:
            count += 1
            print(f"  ✓ [{ex_data['difficulty'].upper()}] {ex.title}")
    
    print(f"→ {count} nouveaux exercices créés sur les Conditionnelles !")
    return count


def create_loops_exercises():
    """Crée 15 exercices sur les Boucles"""
    
    print("\n🔄 Création des exercices sur les BOUCLES (15 exercices)...")
    
    course = Course.objects.get(course_type='loops')
    
    exercises = [
        # FACILE (5 exercices)
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
            'difficulty': 'easy',
            'points': 10,
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
            'difficulty': 'easy',
            'points': 10,
            'order': 3
        },
        {
            'title': 'Instruction continue',
            'question': 'Que fait continue dans une boucle ?',
            'option_a': 'Sort de la boucle',
            'option_b': 'Passe à l\'itération suivante',
            'option_c': 'Redémarre la boucle',
            'option_d': 'Met en pause',
            'correct_answer': 'B',
            'explanation': 'continue saute le reste du code et passe directement à l\'itération suivante.',
            'difficulty': 'easy',
            'points': 10,
            'order': 4
        },
        {
            'title': 'Range de base',
            'question': 'Que génère range(3) ?',
            'option_a': '1, 2, 3',
            'option_b': '0, 1, 2',
            'option_c': '0, 1, 2, 3',
            'option_d': '1, 2',
            'correct_answer': 'B',
            'explanation': 'range commence à 0 et s\'arrête avant le nombre donné : 0, 1, 2.',
            'difficulty': 'easy',
            'points': 10,
            'order': 5
        },
        
        # MOYEN (7 exercices)
        {
            'title': 'For avec liste',
            'question': 'for x in [1, 2, 3]: combien d\'itérations ?',
            'option_a': '2',
            'option_b': '3',
            'option_c': '4',
            'option_d': '1',
            'correct_answer': 'B',
            'explanation': 'La liste contient 3 éléments, donc 3 itérations.',
            'difficulty': 'medium',
            'points': 15,
            'order': 6
        },
        {
            'title': 'Range avec paramètres',
            'question': 'Que génère range(2, 5) ?',
            'option_a': '2, 3, 4',
            'option_b': '2, 3, 4, 5',
            'option_c': '3, 4, 5',
            'option_d': '2, 5',
            'correct_answer': 'A',
            'explanation': 'range(début, fin) commence à début et s\'arrête avant fin : 2, 3, 4.',
            'difficulty': 'medium',
            'points': 15,
            'order': 7
        },
        {
            'title': 'While True',
            'question': 'Quel est le danger de while True: ?',
            'option_a': 'Aucun',
            'option_b': 'Boucle infinie sans break',
            'option_c': 'Erreur de syntaxe',
            'option_d': 'Dépend du contexte',
            'correct_answer': 'B',
            'explanation': 'while True crée une boucle infinie. Il faut un break pour sortir.',
            'difficulty': 'medium',
            'points': 15,
            'order': 8
        },
        {
            'title': 'Boucles imbriquées',
            'question': 'Combien de tours au total ?\nfor i in range(2):\n    for j in range(2):',
            'option_a': '2',
            'option_b': '4',
            'option_c': '8',
            'option_d': '16',
            'correct_answer': 'B',
            'explanation': '2 tours extérieurs × 2 tours intérieurs = 4 tours au total.',
            'difficulty': 'medium',
            'points': 15,
            'order': 9
        },
        {
            'title': 'Enumerate',
            'question': 'for i, v in enumerate(["a", "b"]): que vaut i ?',
            'option_a': '"a", "b"',
            'option_b': '0, 1',
            'option_c': 'Les indices',
            'option_d': 'Les valeurs',
            'correct_answer': 'B',
            'explanation': 'enumerate renvoie les indices : i vaut 0 puis 1.',
            'difficulty': 'medium',
            'points': 15,
            'order': 10
        },
        {
            'title': 'Len et range',
            'question': 'for i in range(len([1, 2, 3])): combien de tours ?',
            'option_a': '2',
            'option_b': '3',
            'option_c': '4',
            'option_d': '6',
            'correct_answer': 'B',
            'explanation': 'len([1, 2, 3]) = 3, donc range(3) donne 0, 1, 2 : 3 tours.',
            'difficulty': 'medium',
            'points': 15,
            'order': 11
        },
        {
            'title': 'Else avec boucle',
            'question': 'Quand le else d\'une boucle for s\'exécute-t-il ?',
            'option_a': 'Toujours',
            'option_b': 'Si pas de break',
            'option_c': 'Jamais',
            'option_d': 'Si break',
            'correct_answer': 'B',
            'explanation': 'Le else d\'une boucle s\'exécute si la boucle se termine normalement (sans break).',
            'difficulty': 'medium',
            'points': 15,
            'order': 12
        },
        
        # DIFFICILE (3 exercices)
        {
            'title': 'Affichage d\'un compteur',
            'question': 'Qu\'affiche ce code ?\nc = 0\nwhile c < 3:\n    print(c)\n    c += 1',
            'option_a': '0, 1, 2',
            'option_b': '0, 1, 2, 3',
            'option_c': '1, 2, 3',
            'option_d': 'Boucle infinie',
            'correct_answer': 'A',
            'explanation': 'c commence à 0. La boucle affiche 0, 1, 2 puis s\'arrête quand c=3.',
            'difficulty': 'hard',
            'points': 20,
            'order': 13
        },
        {
            'title': 'Modification en cours',
            'question': 'Quel est le danger de modifier une liste pendant son parcours ?\nfor i in liste:\n    liste.append(i)',
            'option_a': 'Aucun',
            'option_b': 'Peut créer une boucle infinie',
            'option_c': 'Erreur de syntaxe',
            'option_d': 'Dépend',
            'correct_answer': 'B',
            'explanation': 'Modifier la liste en cours de parcours peut créer une boucle infinie ou des bugs.',
            'difficulty': 'hard',
            'points': 20,
            'order': 14
        },
        {
            'title': 'Compréhension de liste',
            'question': 'Que donne [x * 2 for x in range(3)] ?',
            'option_a': '[0, 2, 4]',
            'option_b': '[0, 1, 2]',
            'option_c': '[2, 4, 6]',
            'option_d': 'Erreur',
            'correct_answer': 'A',
            'explanation': 'range(3) donne 0, 1, 2. Multiplié par 2 : [0, 2, 4].',
            'difficulty': 'hard',
            'points': 20,
            'order': 15
        },
    ]
    
    count = 0
    for ex_data in exercises:
        ex, created = Exercise.objects.get_or_create(
            course=course,
            title=ex_data['title'],
            defaults=ex_data
        )
        if created:
            count += 1
            print(f"  ✓ [{ex_data['difficulty'].upper()}] {ex.title}")
    
    print(f"→ {count} nouveaux exercices créés sur les Boucles !")
    return count


def create_functions_exercises():
    """Crée 15 exercices sur les Fonctions"""
    
    print("\n⚙️ Création des exercices sur les FONCTIONS (15 exercices)...")
    
    course = Course.objects.get(course_type='functions')
    
    exercises = [
        # FACILE (5 exercices)
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
            'difficulty': 'easy',
            'points': 10,
            'order': 3
        },
        {
            'title': 'Appel de fonction',
            'question': 'Comment appeler une fonction nommée "afficher" ?',
            'option_a': 'afficher',
            'option_b': 'afficher()',
            'option_c': 'call afficher',
            'option_d': 'afficher[]',
            'correct_answer': 'B',
            'explanation': 'On appelle une fonction avec des parenthèses : afficher().',
            'difficulty': 'easy',
            'points': 10,
            'order': 4
        },
        {
            'title': 'Fonction sans return',
            'question': 'Que retourne une fonction sans instruction return ?',
            'option_a': '0',
            'option_b': 'None',
            'option_c': 'False',
            'option_d': 'Erreur',
            'correct_answer': 'B',
            'explanation': 'Une fonction sans return retourne None par défaut.',
            'difficulty': 'easy',
            'points': 10,
            'order': 5
        },
        
        # MOYEN (7 exercices)
        {
            'title': 'Arguments',
            'question': 'Combien d\'arguments sont passés ?\nfonction(1, 2)',
            'option_a': '0',
            'option_b': '1',
            'option_c': '2',
            'option_d': '3',
            'correct_answer': 'C',
            'explanation': 'Deux valeurs sont passées : 1 et 2. Ce sont 2 arguments.',
            'difficulty': 'medium',
            'points': 15,
            'order': 6
        },
        {
            'title': 'Paramètre par défaut',
            'question': 'Que retourne cette fonction ?\ndef f(x=5):\n    return x\nf()',
            'option_a': '0',
            'option_b': '5',
            'option_c': 'None',
            'option_d': 'Erreur',
            'correct_answer': 'B',
            'explanation': 'Sans argument, la fonction utilise la valeur par défaut x=5.',
            'difficulty': 'medium',
            'points': 15,
            'order': 7
        },
        {
            'title': 'Portée des variables',
            'question': 'Une variable locale est visible où ?',
            'option_a': 'Partout dans le programme',
            'option_b': 'Uniquement dans la fonction',
            'option_c': 'Nulle part',
            'option_d': 'Cela dépend',
            'correct_answer': 'B',
            'explanation': 'Une variable locale n\'existe que dans la fonction où elle est définie.',
            'difficulty': 'medium',
            'points': 15,
            'order': 8
        },
        {
            'title': 'Return multiple',
            'question': 'Que retourne : return a, b',
            'option_a': 'Seulement a',
            'option_b': 'Seulement b',
            'option_c': 'Un tuple (a, b)',
            'option_d': 'Erreur',
            'correct_answer': 'C',
            'explanation': 'return a, b retourne un tuple contenant les deux valeurs.',
            'difficulty': 'medium',
            'points': 15,
            'order': 9
        },
        {
            'title': 'Lambda',
            'question': 'Qu\'est-ce que lambda x: x * 2 ?',
            'option_a': 'Une fonction anonyme',
            'option_b': 'Une variable',
            'option_c': 'Une boucle',
            'option_d': 'Une erreur',
            'correct_answer': 'A',
            'explanation': 'lambda crée une fonction anonyme (sans nom) en une seule ligne.',
            'difficulty': 'medium',
            'points': 15,
            'order': 10
        },
        {
            'title': 'Fonction récursive',
            'question': 'Une fonction qui s\'appelle elle-même est ?',
            'option_a': 'Une boucle',
            'option_b': 'Une fonction récursive',
            'option_c': 'Une erreur',
            'option_d': 'Impossible',
            'correct_answer': 'B',
            'explanation': 'La récursivité permet à une fonction de s\'appeler elle-même.',
            'difficulty': 'medium',
            'points': 15,
            'order': 11
        },
        {
            'title': 'Args variables',
            'question': 'Que permet *args dans une fonction ?',
            'option_a': '1 seul paramètre',
            'option_b': 'Nombre variable de paramètres',
            'option_c': 'Une liste obligatoire',
            'option_d': 'Un dictionnaire',
            'correct_answer': 'B',
            'explanation': '*args permet de passer un nombre variable d\'arguments.',
            'difficulty': 'medium',
            'points': 15,
            'order': 12
        },
        
        # DIFFICILE (3 exercices)
        {
            'title': 'Arguments nommés',
            'question': 'Est-ce valide ?\ndef f(a, b):\n    return a + b\nf(b=2, a=1)',
            'option_a': 'Non',
            'option_b': 'Oui',
            'option_c': 'Erreur de syntaxe',
            'option_d': 'Dépend',
            'correct_answer': 'B',
            'explanation': 'Les arguments nommés permettent de les passer dans n\'importe quel ordre.',
            'difficulty': 'hard',
            'points': 20,
            'order': 13
        },
        {
            'title': 'Closure',
            'question': 'Une fonction définie dans une autre fonction conserve-t-elle les variables ?',
            'option_a': 'Non',
            'option_b': 'Oui (closure)',
            'option_c': 'Erreur',
            'option_d': 'Dépend',
            'correct_answer': 'B',
            'explanation': 'Une closure conserve l\'accès aux variables de la fonction parente.',
            'difficulty': 'hard',
            'points': 20,
            'order': 14
        },
        {
            'title': 'Docstring',
            'question': 'À quoi sert une docstring ?\ndef f():\n    """Documentation"""',
            'option_a': 'Un commentaire',
            'option_b': 'Documentation de la fonction',
            'option_c': 'Une erreur',
            'option_d': 'Rien',
            'correct_answer': 'B',
            'explanation': 'Les docstrings (""") servent à documenter les fonctions.',
            'difficulty': 'hard',
            'points': 20,
            'order': 15
        },
    ]
    
    count = 0
    for ex_data in exercises:
        ex, created = Exercise.objects.get_or_create(
            course=course,
            title=ex_data['title'],
            defaults=ex_data
        )
        if created:
            count += 1
            print(f"  ✓ [{ex_data['difficulty'].upper()}] {ex.title}")
    
    print(f"→ {count} nouveaux exercices créés sur les Fonctions !")
    return count


if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("🚀 PEUPLEMENT DE LA BASE DE DONNÉES - PLATEFORME ENS YAOUNDÉ")
    print("=" * 70)
    
    create_courses()
    
    total = 0
    total += create_variables_exercises()
    total += create_conditionals_exercises()
    total += create_loops_exercises()
    total += create_functions_exercises()
    
    print("\n" + "=" * 70)
    print("✅ BASE DE DONNÉES PEUPLÉE AVEC SUCCÈS !")
    print("=" * 70)
    print(f"\n📊 STATISTIQUES :")
    print(f"   • {Course.objects.count()} cours créés")
    print(f"   • {Exercise.objects.count()} exercices au total")
    print(f"   • {total} nouveaux exercices ajoutés")
    print("\n🎯 COMMANDES SUIVANTES :")
    print("   1. python manage.py runserver")
    print("   2. Ouvrez http://127.0.0.1:8000/")
    print("   3. Créez un compte et testez !")
    print("=" * 70)