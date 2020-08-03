# Projet CERBERUS 
<img src="./web_application/concepts/cerberus.png"  width="220" height="220">

## Description
Création d'une application Web capable de collecter des données à partir d'un cluster de Raspberry Pi(s) déployée dans une area.  
Les données collectées par les Raspberry(s) seront envoyés vers un serveur en utilisant un appel API REST. Ces données seront ensuite vérifiées et sauvegardées pour être mises à disposition à travers une API.  
Le serveur utilisera le framework Django qui communiquera avec une base de données PostgreSQL. Les données seront mises à disposition à des client via l'API, dans notre cas une application Web React.

 
## Django Server
Nous allons utiliser les packages:
- "django" Framework de développement web.
- "django rest framework" pour la création de l'API.
- "psycopg2, sqlparse" pour communiquer avec la base de données PostgreSQL.
- "django-cors-headers" pour autoriser l'utilisation de cors.
- "gdal" necessaire pour sauver les coordonnées géographiques dans Django. Erreur lors de la compilation du package (gcc exit code 1). Remplacé par FloatField.

### Etat actuel
Mise en place de contrôleurs REST capables d'envoyer la liste entière de adresses sauvegardées mais aussi ajouter/modifier des données.

## React WebApp
Nous allons utiliser les packages:
- "ant Design" libraire de composantes React.
- "Redux" libraire React pour faciliter la navigation dans l'application.
- "React leaflet" libraire de composantes de cartes.

## Network Settings
Script BASH pour activer la connexion Wi-Fi et connecter le device au réseau Fablab.

## Scanner Wi-Fi
Script Python qui sera intégré en tant que daemon dans les Raspberry Pi.
Le script collecte les données, les sérialise et les envoie ensuite sur le serveur distant (thingSpeak pour le moment).

## TODO(s)
### React: 
- Mettre en place la page d’accueil React.
- Ajouter l'application leaflet sur la page d’accueil et tester la carte avec les données reçus.
- Mettre en place le layout principal de la page d’accueil.  

### Django 
- Réaliser des checkers de formatage pour les données envoyées vers l'API.
- Creer le controlleur Authentication.

### Raspberry Pi
- Ajouter des règles pour quand envoyer à nouveau la liste de appareils détectées (ex: quand l'appareil n'est plus détectée, une fois tous les 5min etc..)
