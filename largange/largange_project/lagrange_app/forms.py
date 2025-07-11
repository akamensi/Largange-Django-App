from django import forms

# ---------------------------------------------------------------
# forms.py
# Ce fichier définit le formulaire utilisé pour saisir les données
# nécessaires à l'interpolation de Lagrange dans l'application Django.
#
# - LagrangeForm : formulaire avec deux champs :
#     * abscisses  : les valeurs x, séparées par des virgules
#     * ordonnees  : les valeurs y, séparées par des virgules
#
# L'utilisateur doit entrer les abscisses et ordonnées sous forme de
# listes séparées par des virgules, par exemple :
#   abscisses : 1,2,3
#   ordonnees : 4,5,6
#
# Ces données seront ensuite traitées dans la vue pour calculer
# le polynôme d'interpolation de Lagrange.
# ---------------------------------------------------------------

class LagrangeForm(forms.Form):
    abscisses = forms.CharField(label="Les abscisses (x) (séparés par des virgules(,))")
    ordonnees = forms.CharField(label="Les ordonnées (y) (séparés par des virgules(,))")