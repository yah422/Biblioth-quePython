# Classe Livre pour modéliser un livre
class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True  # Attribut pour savoir si le livre est disponible
    
    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print(f"Vous avez emprunté '{self.titre}' de {self.auteur}.")
        else:
            print(f"Le livre '{self.titre}' est déjà emprunté.")

    def rendre(self):
        if not self.disponible:
            self.disponible = True
            print(f"Vous avez rendu '{self.titre}'.")
        else:
            print(f"Le livre '{self.titre}' n'a pas été emprunté.")

# Classe Bibliothèque pour gérer une collection de livres
class Bibliotheque:
    def __init__(self):
        self.livres = []  # Liste de livres dans la bibliothèque
    
    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Le livre '{livre.titre}' a été ajouté à la bibliothèque.")
    
    def afficher_livres(self):
        print("\nLivres disponibles dans la bibliothèque :")
        for livre in self.livres:
            dispo = "Disponible" if livre.disponible else "Emprunté"
            print(f"{livre.titre} par {livre.auteur} - {dispo}")

# Utilisation des classes
biblio = Bibliotheque()

# Ajouter des livres
livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
livre2 = Livre("1984", "George Orwell")
biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)

# Afficher les livres disponibles
biblio.afficher_livres()

# Emprunter un livre
livre1.emprunter()

# Afficher les livres après l'emprunt
biblio.afficher_livres()

# Rendre un livre
livre1.rendre()

# Afficher les livres après le retour
biblio.afficher_livres()
