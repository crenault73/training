# Batiment

class Batiment:

    def __init__(self, adresse, nb_etages):
        self.adresse = adresse
        self.nb_etages = nb_etages

    def get_adresse(self):
        return self.adresse

    def get_nb_etages(self):
        return self.nb_etages

    #Surcharge default str
    def __str__(self):
        return "Adresse: "+self.adresse + ", nb d'étages: " + str(self.nb_etages)


class Immeuble(Batiment):

    def __init__(self, adresse, nb_etages, nb_balcons):
        super().__init__(adresse, nb_etages)
        self.nb_balcons = nb_balcons

    #Surcharge default str
    def __str__(self):
        return super().__str__() + ", Nb de balcons: " + str(self.nb_balcons)


class Supermarche(Batiment):

    def __init__(self, adresse, nb_etages, nb_rayons):
        super().__init__(adresse, nb_etages)
        self.nb_rayons = nb_rayons

    #Surcharge default str
    def __str__(self):
        return super().__str__() + ", Nb de rayons : " + str(self.nb_rayons)


class Banque(Batiment):

    def __init__(self, adresse, nb_etages, nb_coffres, nom):
        super().__init__(adresse, nb_etages)
        self.nb_coffres = nb_coffres
        self.nom = nom

    #Surcharge default str
    def __str__(self):
        return super().__str__() + ", Nb de coffres: " + str(self.nb_coffres) + ", Nom: " + self.nom
