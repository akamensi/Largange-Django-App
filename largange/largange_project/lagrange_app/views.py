from django.shortcuts import render
from .forms import LagrangeForm
import sympy as sp

# ---------------------------------------------------------------
# views.py
# Ce fichier contient les vues de l'application lagrange_app.
#
# - lagrange_interpolation : fonction qui calcule le polynôme de Lagrange
# - index                 : vue principale avec le formulaire et le résultat
# - def_view              : vue affichant la définition/concept de Lagrange
# ---------------------------------------------------------------

def lagrange_interpolation(abscisses, ordonnees):
    """
    Calcule le polynôme d'interpolation de Lagrange pour les points donnés.
    abscisses : liste des x
    ordonnees : liste des y
    Retourne un polynôme sympy simplifié.
    """
    x = sp.Symbol('x')
    n = len(abscisses)
    P = 0

    for i in range(n):
        xi, yi = abscisses[i], ordonnees[i]
        Li = 1
        for j in range(n):
            if i != j:
                xj = abscisses[j]
                Li *= (x - xj) / (xi - xj)
        P += yi * Li

    return sp.simplify(P)

def index(request):
    """
    Vue principale : affiche le formulaire et le résultat du calcul.
    """
    result = None
    latex = None

    if request.method == 'POST':
        form = LagrangeForm(request.POST)
        if form.is_valid():
            try:
                abscisses = [float(i) for i in form.cleaned_data['abscisses'].split(',')]
                ordonnees = [float(i) for i in form.cleaned_data['ordonnees'].split(',')]

                if len(abscisses) != len(ordonnees):
                    result = "Erreur : Les deux listes doivent être de même taille."
                else:
                    poly = lagrange_interpolation(abscisses, ordonnees)
                    result = str(poly)
                    latex = sp.latex(poly)
            except Exception as e:
                result = f"Erreur : {e}"
    else:
        form = LagrangeForm()

    return render(request, 'largange/index.html', {'form': form, 'result': result, 'latex': latex})

def def_view(request):
    """
    Vue pour la page de définition/concept de Lagrange.
    """
    return render(request, 'largange/def.html')