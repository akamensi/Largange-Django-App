from django.urls import path
from . import views

# ---------------------------------------------------------------
# urls.py
# Ce fichier définit les routes (URL) de l'application lagrange_app.
#
# - ''      : page d'accueil, vue index (nommée 'idx')
# - 'def/'  : page de définition/concept, vue def_view (nommée 'def')
# ---------------------------------------------------------------


urlpatterns = [
    path('', views.index, name='idx'), # Accueil : formulaire d'interpolation
    path('def/', views.def_view, name='def'), # Page concept/définition de Lagrange
]