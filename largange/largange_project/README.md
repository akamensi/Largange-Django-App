# Interpolation de Lagrange – Projet Django

Ce projet est une application web simple permettant de calculer et visualiser le polynôme d’interpolation de Lagrange à partir de points donnés.  
Réalisé par **Akez Mohamed** pour la société **Smart Conseil**.

---

## Sommaire

- [Prérequis](#prérequis)
- [Installation du projet](#installation-du-projet)
- [Création de l’application Django](#création-de-lapplication-django)
- [Configuration des fichiers](#configuration-des-fichiers)
- [Lancement du serveur](#lancement-du-serveur)
- [Utilisation](#utilisation)
- [Structure du projet](#structure-du-projet)
- [Personnalisation](#personnalisation)
- [Aide](#aide)

---

## Prérequis

- Python 3.10 ou supérieur
- pip (installé avec Python)

---

## Installation du projet

1. **Créer un dossier de travail**  
     
   `C:\Users\HP\Desktop\smart_conseil`

2. **Ouvrir l’invite de commandes dans ce dossier**  
   (Maj + clic droit > "Ouvrir une fenêtre de commandes ici" ou utilisez le terminal de VS Code)

3. **Créer un environnement virtuel :**
   ```bat
   virtualenv largange
   ```

4. **Activer l’environnement virtuel :**
   ```bat
   largange\Scripts\activate
   ```

5. **Installer Django et les dépendances :**
   ```bat
   pip install django sympy
   ```

---

## Création de l’application Django

1. **Créer un projet Django (si ce n’est pas déjà fait) :**
   ```bat
   django-admin startproject largange_project
   ```

2. **Créer l’application principale :**
   ```bat
   python manage.py startapp lagrange_app
   ```

3. **Ajouter l’application dans `INSTALLED_APPS` du fichier :**
   ```
   largange_project/settings.py
   ```
   ```python
   'lagrange_app.apps.LagrangeAppConfig',
   ```

---

## Configuration des fichiers

1. **Créer la structure des dossiers :**
   ```
   largange_project/
        lagrange_app/
           forms.py
           views.py
           urls.py
        largange_project/
           static/
               css/
                   style.css
           settings.py
           urls.py
        templates/
                largange/
                   index.html
                   def.html
                parts/
                   navbar.html
                   footer.html
                base.html
        db.sqlite3
        manage.py
        README.md
   ```

2. **Configurer les templates et les fichiers statiques dans `settings.py` :**
   ```python
   TEMPLATES = [
       {
           ...
           'DIRS': [os.path.join(BASE_DIR, 'templates')],
           ...
       },
   ]

   STATIC_ROOT = os.path.join(BASE_DIR, 'static')  
   STATIC_URL = 'static/'
   STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'largange_project/static'),  in the project
  ]
   ```

3. **Créer les fichiers HTML et CSS selon les exemples du projet.**

4. **Configurer les routes dans :**
   - `lagrange_app/urls.py`
   - `largange_project/urls.py`

---

## Lancement du serveur

1. **Appliquer les migrations :**
   ```bat
   python manage.py migrate
   ```

2. **Démarrer le serveur de développement :**
   ```bat
   python manage.py runserver
   ```

3. **Accéder à l’application :**
   - Ouvrez [http://127.0.0.1:8000/](http://127.0.0.1:8000/) dans votre navigateur.

---

## Utilisation

- **Accueil :** Saisissez les abscisses et ordonnées séparées par des virgules, puis cliquez sur « Calculer ».
- **Concept :** Cliquez sur « Largange Concept » dans la barre de navigation pour lire la définition mathématique.

---

## Structure du projet

- `lagrange_app/` : logique métier, formulaires, vues.
- `largange_project/static/css/style.css` : styles personnalisés.
- `largange_project/templates` : , templates.
- `templates/parts/navbar.html` et `footer.html` : navigation et pied de page.
- `templates/largange/index.html` : page principale.
- `templates/largange/def.html` : explication du concept.

---

## Personnalisation

- Modifiez les couleurs et le style dans `style.css`.
- Ajoutez d’autres pages ou fonctionnalités selon vos besoins.

---


**© 2025 Smart Conseil – Développé par Akez