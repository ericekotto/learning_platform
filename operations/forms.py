"""
Ce fichier définit les formulaires Django.
Les formulaires permettent de créer des champs de saisie HTML
et de valider automatiquement les données entrées.
"""
from django import forms


class OperationForm(forms.Form):
    """
    Formulaire pour saisir deux valeurs et effectuer une opération.
    
    - value1 et value2 : champs de texte pour entrer les valeurs
    - required=True : les champs sont obligatoires
    - widget : définit l'apparence du champ HTML
    """
    value1 = forms.CharField(
        label='Première valeur',
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ex: 42, 3.14, "Bonjour", True'
        })
    )
    
    value2 = forms.CharField(
        label='Deuxième valeur',
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ex: 10, 2.5, "Monde", False'
        })
    )


class ComparaisonForm(forms.Form):
    """
    Formulaire spécial pour les comparaisons.
    Identique au formulaire d'opération de base.
    """
    value1 = forms.CharField(
        label='Première valeur',
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ex: 42, 3.14, "A"'
        })
    )
    
    value2 = forms.CharField(
        label='Deuxième valeur',
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Ex: 10, 2.5, "B"'
        })
    )