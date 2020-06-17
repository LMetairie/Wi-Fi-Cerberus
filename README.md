# Projet CERBERUS
Mise en place d'un cluster de cartes Raspberry Pi capables de collecter des informations à partir des ondes Wi-Fi.
Le cluster de Raspberry Pi sera controlé à partir d'un serveur distant Django qui va mettre à disposition les données collectées et des statistiques.
 
## Django Server
Serveur Django version 0.2 Login et paneau d'administration ajoutées.
Pour lancer le serveur:
	Generer un env. python.
	- `python -m venv venv`
	Activer l'env.
	- `source ./venv/bin/activate`
	Installer les pacquets.
	- `pip install -r requirements.txt`
	Lancer le servuer.
	- `python manage.py runserver`

## Network Settings
Script bash pour activer la conexion Wi-Fi et connecter le device au reseau Fablab.

## Scanner Wi-Fi
Script python qui sera integré plus tard dans le serveur Django.
Le script collecte les données, les serialise et les envoye ensuite sur le serveur distant (thingSpeak pour le moment).	
