"""
Ce fichier contient les "vues" Django.
Chaque vue est une fonction qui :
1. Reçoit une requête HTTP (request)
2. Traite les données (formulaires, calculs...)
3. Retourne une page HTML (render)
"""
from django.shortcuts import render
from .forms import OperationForm, ComparaisonForm
from .utils import detect_type, perform_operation, get_type_info


def home(request):
    """
    Vue de la page d'accueil.
    Affiche simplement le template home.html
    
    Args:
        request: Objet contenant les infos de la requête HTTP
    
    Returns:
        Une page HTML rendue
    """
    return render(request, 'operations/home.html')


def types_info(request):
    """
    Vue de la page d'information sur les types.
    Récupère les infos des types et les envoie au template.
    
    Args:
        request: Objet requête
    
    Returns:
        Page HTML avec les informations sur tous les types
    """
    types_data = get_type_info()
    return render(request, 'operations/types_info.html', {'types': types_data})


def operation_view(request, operation):
    """
    Vue principale pour toutes les opérations.
    Gère l'affichage du formulaire et le traitement des données.
    
    Args:
        request: Objet requête
        operation: Type d'opération ('addition', 'soustraction', etc.)
    
    Returns:
        Page HTML avec le formulaire ou les résultats
    """
    result_data = None
    form = None
    
    # Détermine quel formulaire utiliser
    if operation == 'comparaison':
        form_class = ComparaisonForm
    else:
        form_class = OperationForm
    
    # Si l'utilisateur a soumis le formulaire (méthode POST)
    if request.method == 'POST':
        form = form_class(request.POST)
        
        # Vérifie que le formulaire est valide
        if form.is_valid():
            # Récupère les valeurs saisies
            raw_value1 = form.cleaned_data['value1']
            raw_value2 = form.cleaned_data['value2']
            
            # Détecte automatiquement les types
            value1, type1 = detect_type(raw_value1)
            value2, type2 = detect_type(raw_value2)
            
            # Effectue l'opération
            operation_result = perform_operation(value1, value2, operation)
            
            # Prépare les données pour l'affichage
            result_data = {
                'raw_value1': raw_value1,
                'raw_value2': raw_value2,
                'value1': value1,
                'value2': value2,
                'type1': type1,
                'type2': type2,
                'operation': operation,
                'operation_result': operation_result,
            }
            
            # Prépare les données pour le graphique
            if operation != 'comparaison' and operation_result['success']:
                # Crée des données pour visualiser l'opération
                result_data['chart_data'] = {
                    'labels': ['Valeur 1', 'Valeur 2', 'Résultat'],
                    'values': []
                }
                
                # Essaie de convertir en nombres pour le graphique
                try:
                    chart_val1 = float(value1) if isinstance(value1, (int, float)) else 0
                    chart_val2 = float(value2) if isinstance(value2, (int, float)) else 0
                    chart_result = float(operation_result['result']) if isinstance(operation_result['result'], (int, float)) else 0
                    
                    result_data['chart_data']['values'] = [chart_val1, chart_val2, chart_result]
                except:
                    # Si conversion impossible, pas de graphique
                    result_data['chart_data'] = None
    
    else:
        # Si méthode GET (première visite), crée un formulaire vide
        form = form_class()
    
    # Prépare le contexte pour le template
    context = {
        'form': form,
        'operation': operation,
        'operation_name': get_operation_name(operation),
        'result_data': result_data,
    }
    
    return render(request, 'operations/operation.html', context)


def get_operation_name(operation):
    """
    Retourne le nom français de l'opération.
    
    Args:
        operation: Code de l'opération
    
    Returns:
        Nom français de l'opération
    """
    names = {
        'addition': 'Addition',
        'soustraction': 'Soustraction',
        'multiplication': 'Multiplication',
        'division': 'Division',
        'modulo': 'Modulo',
        'concatenation': 'Concaténation',
        'comparaison': 'Comparaison',
    }
    return names.get(operation, operation.capitalize())