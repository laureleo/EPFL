n = input("Quel est votre nom ?\n ")
print("Bonjour ", n)

class Personne:
    """Return the pathname of the KOS root directory."""
    def __init__(self, nom, age):
        """ Constructeur. """

        self.nom = nom
        self.age = age

    def anniversaire(self):
        """ Missing docstring """
        self.age += 1
