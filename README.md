# Projet CERBERUS 
<img src="./web_application/concepts/cerberus.png"  width="220" height="220">

## Description
Creation d'une application Web capable de collecter des données à partir d'un cluster de Raspberry Pi(s) deployée dans une area.  
Les données collectées par les Raspberry(s) seront envoyés vers un serveur en utilisant un appel API REST. Ces données seront ensuite verifiées et sauvegardées pour etres mises à disposition à travers une API.  
Le serveur utilisera le framework Django qui communiquera avec une base de données PostgreSQL. Les données seront mises à disposition à des client via l'API, dans notre cas une application Web React.

 
## Django Server
Nous allons utiliser les packages:
- "django" Framework de developpement web.
- "django rest framework" pour la creation de l'API.
- "psycopg2, sqlparse" pour communiquer avec la base de données PostgreSQL.
- "django-cors-headers" pour authoriser l'utilisation de cors.

## React WebApp
Nous allons utiliser les packages:
- "ant Design" librarie de componentes React.
- "Redux" librarie React pour faciliter la navigation dans l'application.
- "React leaflet" librarie de componentes de cartes.

## Network Settings
Script bash pour activer la conexion Wi-Fi et connecter le device au reseau Fablab.

## Scanner Wi-Fi
Script python qui sera integré plus tard dans le serveur Django.
Le script collecte les données, les serialise et les envoye ensuite sur le serveur distant (thingSpeak pour le moment).	
