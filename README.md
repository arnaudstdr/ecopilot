# Ecopilot

EcoPilot est une application web conçue pour aider les utilisateurs à suivre et gérer leurs dépenses quotidiennes. L'objectif est de fournir une interface intuitive permettant de visualiser facilement les habitudes de consommation financière et de gérer son budget de manière efficace.


## Fonctionnalités

- Suivi quotidien des dépenses : Enregistrez vos dépenses journalières avec des catégories personnalisées.
- Visualisation des données : Affichez des graphiques pour visualiser les tendances de vos dépenses sur des périodes définies.
- Budget mensuel : Définissez un budget et recevez des alertes si vos dépenses dépassent le seuil que vous avez fixé.
- Rapports détaillés : Consultez des rapports de dépenses pour comprendre vos habitudes de consommation et identifier les domaines où vous pouvez économiser.
- Interface intuitive : Simple à utiliser avec un design moderne pour une prise en main rapide.


## Capture d'écran


## Installation

1. Clonez ce dépôt sur votre machine locale :
```
git clone hhtps://github.com/arnaudstdr/ecopilot.git
```
2. Accédez au répertoire du projet :
```
cd ecopilot
```
3. Installez les dépendances nécessaires :
```
pip install -r requirements.txt
```
4. Lancer l'application en développement :
```
python3 manage.py runserver
```
5. Ouvrez votre navigateur et accédez à l'adresse suivante : `http://127.0.0.1:8000/`


## Technologie utilisées

- Python : Langage de programmation principal pour la logique de l'application.
- Django : Framework web utilisé pour le back-end de l'application.
- HTML/CSS : Structure et design de l'interface utilisateur.
- JavaScript : Interactivité des graphiques et autres composants front-end.
- SQLite : Base de données utilisée pour stocker les données des utilisateurs.
- Chart.js : Utilisé pour générer les graphiques interactifs des dépenses.


## Structure du projet

```
ecopilot/
│
├── ecopilot/                  # Contient les paramètres de configuration du projet Django
├── expenses/                  # Application principale gérant les dépenses
│   ├── migrations/            # Historique des migrations de base de données
│   ├── templates/             # Fichiers HTML
│   └── views.py               # Logique de gestion des vues et des routes
├── static/                    # Fichiers CSS et JavaScript
│   └── style.css              # Styles personnalisés pour l'application
├── db.sqlite3                 # Base de données SQLite
├── manage.py                  # Fichier d'entrée pour la gestion de Django
└── requirements.txt           # Liste des dépendances Python à installer
```


## Utilisation

1. Ajouter une dépense : Depuis l'interface, vous pouvez ajouter une dépense en précisant la date, la catégorie, et le montant.
2. Visualiser les dépenses : Consultez les graphiques générés pour suivre vos dépenses par catégorie et par période.
3. Gérer votre budget : Configurez un budget mensuel et consultez l'état actuel de vos dépenses par rapport à ce budget.


## License

Ce projet est sous licence MIT - consultez le fichier LICENSE pour plus de détails.


## Contact

Si vous avez des questions ou des suggestions, n'hésitez pas à me contacter :
- Nom : Arnaud Stadler
- Email : arnaud.stadler@ikmail.com
