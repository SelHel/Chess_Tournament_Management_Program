*English version follows*

# Programme de gestion de tournois d'échecs

## Descriptif

Ce programme est une application hors ligne qui permet aux utilisateurs de gérer des tournois d'échecs.
L'utilisateur peut suivre et mettre à jour les résultats d'un tournoi au fur et à mesure.<br/>
La génération des paires de joueurs pour les matchs est gérée par un algorithme basé sur le système de tournois "suisse".<br/>
Il peut également générer des rapports et sauvegarder ou charger un tournoi à tout moment grâce à une base de données.

## Prérequis
* Python 3.9 ( lien de téléchargement: <https://www.python.org/downloads>)

## Installation du programme

Après avoir téléchargé le dossier **OpenclassroomsProject4-main.zip** depuis ce lien [GitHub](https://github.com/SelHel/OpenclassroomsProject4).  
Extraire les fichiers dans un dossier de votre choix.  
Ensuite, en utilisant le terminal sous Mac/Linux ou l'invite de commandes sous Windows :

* Placez vous dans le dossier courant.
* Créez un environnement virtuel :

```
python -m venv <your-virtual-env-name>
```
* Activez votre environnement virtuel sous Windows :

```
<your-virtual-env-name>\Scripts\activate.bat
```
* Activez votre environnement virtuel sous Mac/Linux :

```
source <your-virtual-env-name>/bin/activate
```
* Installez les modules nécessaires au bon fonctionnement du programme depuis le fichier requirements.txt

```
 pip install -r requirements.txt
```
## Exécution du programme
Pour éxécuter l'application lancez le script *"main.py"* :

```
python main.py

```
Le menu principal va apparaître, utilisez les numéros indiqués dans le(s) menu(s) pour naviguer et effectuer les actions voulues.

## Générer un rapport flake8
Un rapport ne montrant aucune erreur de peluchage dans le code peut être généré à partir du terminal.<br/> Dans le terminal, lancez la commande :

```
flake8 --format=html --htmldir=flake8_rapport
```
---

# Chess tournament management program

## Description

This program is an offline application that allows users to manage chess tournaments.
The user can follow and update the results of tournament. <br/>
It can generate reports and save or load tournament at any time with a database.

## Requirements
* Python 3.9 (download link: <https://www.python.org/downloads>)

## Program installation

Download the directory **OpenclassroomsProject4-main.zip** from this link
[GitHub](https://github.com/SelHel/OpenclassroomsProject4).  
Extract files in directory of your choice.<br/>
Then using the terminal on Mac and Linux or the command prompt on Windows:


* In current directory.
* Create a virtual environment :

```
python -m venv <your-virtual-env-name>
```
* Activate the virtual environment on Windows :

```
<your-virtual-env-name>\Scripts\activate.bat
```
* Activate the virtual environment on Mac/Linux :

```
source <your-virtual-env-name>/bin/activate
```
* Install the necessary modules from requirements.txt file.

```
 pip install -r requirements.txt
```
## Program execution
To run the application launch the script *"main.py"* :

```
python main.py

```
Use the numbers on the main menu to navigate and make choices.

## Generate flake8 report
A report certifying the flake8 compliance can be generated from the terminal.<br/> In the terminal, launch the command :

```
flake8 --format=html --htmldir=flake8_rapport
```



