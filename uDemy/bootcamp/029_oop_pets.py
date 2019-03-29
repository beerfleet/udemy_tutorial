""" Pet class """

class Pet:
    
    allowed_species = ("dog", "cat", "perroquet", "hamster", "squirrel")

    def __init__(self, name, species):
        self.name = name
        self._check_is_allowed(species)
        self.species = species

    def set_species(self, species):
        self._check_is_allowed(species)
        self.species = species

    def get_species(self):
        return self.species

    def _check_is_allowed(self, species):
         if not species.lower() in Pet.allowed_species:
            raise ValueError(f"{species} species not allowed")
    

cat = Pet("Jorien", "PerroQuet")
print(cat.get_species())
cat.set_species("squirrel")
print(cat.get_species())