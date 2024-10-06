# Gestion d'une bibliothèque

Ce projet est une application simple en Python pour gérer une bibliothèque, permettant de gérer des livres et leur disponibilité. Les utilisateurs peuvent emprunter et rendre des livres.

## Fonctionnalités

- **Ajouter des livres** : Ajouter de nouveaux livres à la bibliothèque.
- **Afficher les livres disponibles** : Voir une liste de tous les livres et leur état (disponible ou emprunté).
- **Emprunter un livre** : Changer l'état d'un livre pour indiquer qu'il a été emprunté.
- **Rendre un livre** : Permet de rendre un livre et de le marquer comme disponible.

## Structure du projet

Le projet contient deux classes principales :

1. **Classe `Livre`** :
   - Attributs : 
     - `titre` : Titre du livre.
     - `auteur` : Auteur du livre.
     - `disponible` : Indicateur booléen de la disponibilité du livre.
   - Méthodes :
     - `emprunter()` : Change l'état de disponibilité du livre à `False`.
     - `rendre()` : Remet le livre à l'état `True` (disponible).

2. **Classe `Bibliotheque`** :
   - Attributs :
     - `livres` : Liste des livres dans la bibliothèque.
   - Méthodes :
     - `ajouter_livre(livre)` : Ajoute un livre à la collection.
     - `afficher_livres()` : Affiche tous les livres avec leur état.
