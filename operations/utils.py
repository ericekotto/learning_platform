"""
Ce fichier contient toutes les fonctions utilitaires pour :
1. Détecter le type d'une donnée entrée par l'utilisateur
2. Effectuer les opérations entre différents types
3. Gérer les erreurs et incompatibilités
"""

def detect_type(value):
    """
    Détecte automatiquement le type d'une valeur entrée par l'utilisateur.
    
    Args:
        value: La valeur à analyser (toujours une chaîne au départ)
    
    Returns:
        tuple: (valeur_convertie, nom_du_type)
    """
    value = value.strip()
    
    # Vérifier si c'est un booléen (True/False)
    if value.lower() in ['true', 'false']:
        return value.lower() == 'true', 'booléen'
    
    # Vérifier si c'est None
    if value.lower() == 'none':
        return None, 'None'
    
    # Vérifier si c'est un entier
    try:
        int_val = int(value)
        return int_val, 'entier'
    except ValueError:
        pass
    
    # Vérifier si c'est un flottant (nombre décimal)
    try:
        float_val = float(value)
        return float_val, 'flottant'
    except ValueError:
        pass
    
    # Sinon, c'est une chaîne de caractères
    return value, 'chaîne'


def perform_operation(val1, val2, operation, val3=None):
    """
    Effectue l'opération demandée entre les valeurs.
    
    Args:
        val1: Première valeur (déjà convertie au bon type)
        val2: Deuxième valeur (déjà convertie au bon type)
        operation: Type d'opération ('addition', 'soustraction', etc.)
        val3: Troisième valeur optionnelle (pour certaines opérations)
    
    Returns:
        dict: Contient 'success' (bool), 'result' ou 'error', et 'explanation'
    """
    
    try:
        if operation == 'addition':
            # L'addition fonctionne avec : nombres entre eux, chaînes entre elles, listes
            if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
                result = val1 + val2
                return {
                    'success': True,
                    'result': result,
                    'explanation': f"Addition de nombres : {val1} + {val2} = {result}"
                }
            elif isinstance(val1, str) and isinstance(val2, str):
                result = val1 + val2
                return {
                    'success': True,
                    'result': result,
                    'explanation': f"Concaténation de chaînes : '{val1}' + '{val2}' = '{result}'"
                }
            else:
                return {
                    'success': False,
                    'error': f"Addition impossible entre {type(val1).__name__} et {type(val2).__name__}",
                    'explanation': "L'addition ne fonctionne qu'entre nombres ou entre chaînes de caractères."
                }
        
        elif operation == 'soustraction':
            # La soustraction ne fonctionne qu'avec des nombres
            if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
                result = val1 - val2
                return {
                    'success': True,
                    'result': result,
                    'explanation': f"Soustraction : {val1} - {val2} = {result}"
                }
            else:
                return {
                    'success': False,
                    'error': f"Soustraction impossible entre {type(val1).__name__} et {type(val2).__name__}",
                    'explanation': "La soustraction ne fonctionne qu'avec des nombres (entiers ou flottants)."
                }
        
        elif operation == 'multiplication':
            # Multiplication : nombres entre eux, chaîne × entier
            if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
                result = val1 * val2
                return {
                    'success': True,
                    'result': result,
                    'explanation': f"Multiplication : {val1} × {val2} = {result}"
                }
            elif isinstance(val1, str) and isinstance(val2, int):
                result = val1 * val2
                return {
                    'success': True,
                    'result': result,
                    'explanation': f"Répétition de chaîne : '{val1}' × {val2} = '{result}'"
                }
            elif isinstance(val1, int) and isinstance(val2, str):
                result = val1 * val2
                return {
                    'success': True,
                    'result': result,
                    'explanation': f"Répétition de chaîne : {val1} × '{val2}' = '{result}'"
                }
            else:
                return {
                    'success': False,
                    'error': f"Multiplication impossible entre {type(val1).__name__} et {type(val2).__name__}",
                    'explanation': "La multiplication fonctionne entre nombres, ou entre une chaîne et un entier."
                }
        
        elif operation == 'division':
            # Division : uniquement entre nombres
            if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
                if val2 == 0:
                    return {
                        'success': False,
                        'error': "Division par zéro impossible",
                        'explanation': "En mathématiques, on ne peut pas diviser par zéro."
                    }
                result = val1 / val2
                return {
                    'success': True,
                    'result': result,
                    'explanation': f"Division : {val1} ÷ {val2} = {result}"
                }
            else:
                return {
                    'success': False,
                    'error': f"Division impossible entre {type(val1).__name__} et {type(val2).__name__}",
                    'explanation': "La division ne fonctionne qu'avec des nombres."
                }
        
        elif operation == 'modulo':
            # Modulo : reste de la division entre nombres entiers
            if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
                if val2 == 0:
                    return {
                        'success': False,
                        'error': "Modulo par zéro impossible",
                        'explanation': "On ne peut pas calculer le modulo avec zéro comme diviseur."
                    }
                result = val1 % val2
                return {
                    'success': True,
                    'result': result,
                    'explanation': f"Modulo : {val1} % {val2} = {result} (reste de la division)"
                }
            else:
                return {
                    'success': False,
                    'error': f"Modulo impossible entre {type(val1).__name__} et {type(val2).__name__}",
                    'explanation': "Le modulo ne fonctionne qu'avec des nombres."
                }
        
        elif operation == 'concatenation':
            # Concaténation : conversion en chaîne et assemblage
            str1 = str(val1)
            str2 = str(val2)
            result = str1 + str2
            return {
                'success': True,
                'result': result,
                'explanation': f"Concaténation : '{str1}' + '{str2}' = '{result}' (tout est converti en texte)"
            }
        
        elif operation == 'comparaison':
            # Comparaison : fonctionne entre types compatibles
            comparisons = {
                'egal': (val1 == val2, f"{val1} == {val2}"),
                'different': (val1 != val2, f"{val1} != {val2}"),
            }
            
            # Comparaisons d'ordre uniquement pour types comparables
            if type(val1) == type(val2) and not isinstance(val1, bool):
                try:
                    comparisons['superieur'] = (val1 > val2, f"{val1} > {val2}")
                    comparisons['inferieur'] = (val1 < val2, f"{val1} < {val2}")
                    comparisons['sup_egal'] = (val1 >= val2, f"{val1} >= {val2}")
                    comparisons['inf_egal'] = (val1 <= val2, f"{val1} <= {val2}")
                except TypeError:
                    pass
            
            return {
                'success': True,
                'result': comparisons,
                'explanation': f"Comparaison entre {type(val1).__name__} et {type(val2).__name__}"
            }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'explanation': "Une erreur inattendue s'est produite."
        }


def get_type_info():
    """
    Retourne un dictionnaire avec toutes les informations sur les types de données.
    
    Returns:
        dict: Informations complètes sur chaque type
    """
    return {
        'entier': {
            'nom': 'Entier (int)',
            'description': "Un nombre entier sans décimales (ex: -5, 0, 42, 1000)",
            'exemples': ['42', '-17', '0', '999'],
            'operations_possibles': [
                'Addition avec d\'autres nombres',
                'Soustraction avec d\'autres nombres',
                'Multiplication avec d\'autres nombres',
                'Division avec d\'autres nombres',
                'Modulo avec d\'autres nombres',
                'Multiplication avec une chaîne (répétition)',
                'Toutes les comparaisons'
            ],
            'operations_impossibles': [
                'Addition avec une chaîne (sauf concaténation explicite)',
                'Opérations arithmétiques avec des booléens ou None'
            ]
        },
        'flottant': {
            'nom': 'Flottant (float)',
            'description': "Un nombre décimal avec virgule (ex: 3.14, -0.5, 2.0)",
            'exemples': ['3.14', '-0.5', '2.0', '99.99'],
            'operations_possibles': [
                'Addition avec d\'autres nombres',
                'Soustraction avec d\'autres nombres',
                'Multiplication avec d\'autres nombres',
                'Division avec d\'autres nombres',
                'Modulo avec d\'autres nombres',
                'Toutes les comparaisons'
            ],
            'operations_impossibles': [
                'Addition avec une chaîne',
                'Multiplication avec une chaîne',
                'Opérations arithmétiques avec des booléens ou None'
            ]
        },
        'chaine': {
            'nom': 'Chaîne de caractères (str)',
            'description': "Du texte entre guillemets (ex: 'Bonjour', 'Python', '123')",
            'exemples': ['Bonjour', 'Python', 'abc123', 'Hello World'],
            'operations_possibles': [
                'Addition (concaténation) avec d\'autres chaînes',
                'Multiplication avec un entier (répétition)',
                'Comparaisons (égalité, ordre alphabétique)',
                'Concaténation avec n\'importe quel type'
            ],
            'operations_impossibles': [
                'Soustraction',
                'Division',
                'Modulo',
                'Opérations arithmétiques classiques'
            ]
        },
        'booleen': {
            'nom': 'Booléen (bool)',
            'description': "Une valeur logique : True (vrai) ou False (faux)",
            'exemples': ['True', 'False'],
            'operations_possibles': [
                'Comparaisons d\'égalité',
                'Opérations logiques (and, or, not)'
            ],
            'operations_impossibles': [
                'Addition',
                'Soustraction',
                'Multiplication',
                'Division',
                'Modulo',
                'Comparaisons d\'ordre (>, <)'
            ]
        },
        'none': {
            'nom': 'None (NoneType)',
            'description': "Représente l'absence de valeur",
            'exemples': ['None'],
            'operations_possibles': [
                'Comparaison d\'égalité seulement'
            ],
            'operations_impossibles': [
                'Toutes les opérations arithmétiques',
                'Concaténation',
                'Comparaisons d\'ordre'
            ]
        }
    }