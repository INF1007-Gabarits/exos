class Roue:
    def __init__(self):
        self.diametre = 10


class Velo:
    def __init__(self, couleur="bleu", taille=50):
        self.couleur = couleur
        self.taille = taille
        self.position = 0
        self.roues = [Roue(), Roue()]

    def __del__(self):
        print(f"Mon beau velo {self.couleur} n'est plus")

    @property
    def taille(self):
        return self.__taille

    @taille.setter
    def taille(self, nouvelle_taille):
        if nouvelle_taille in [40, 45, 50, 55, 60]:
            self.__taille = nouvelle_taille
        else:
            print(f"erreur votre taille de {nouvelle_taille} n'existe pas")

    def avance(self):
        self.position += 1
        self.affiche_position()

    def recule(self):
        self.position -= 1
        self.affiche_position()

    def affiche_position(self):
        print(f'Position = {self.position}')

    def __add__(self, other):
        return self.taille + other.taille

    def __str__(self):
        return f"Je suis un beau velo {self.couleur}"

    def __lt__(self, other):
        return self.taille < other.taille


if __name__ == '__main__':
    monVelo = Velo(taille=50, couleur="bleu")
    tonVelo = Velo("rouge", 60)

    print(monVelo < tonVelo)







