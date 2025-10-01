class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description  
        self.is_caught = is_caught

    def speak(self):
        print(f"{self.name, self.name}!")

    def display_details(self):
        print(f"Entry: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Types: {', '.join(self.types)}")
        print(f"Description: {self.description}")
        print(f"Caught: {'Yes' if self.is_caught else 'No'}")

pikachu = Pokemon(25, "Pikachu", ["Electric"], "When several of these Pokémon gather, their electricity could build and cause lightning storms.", True)
bulbasaur = Pokemon(1, "Bulbasaur", ["Grass", "Poison"], "A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.", False)
pikachu.speak()
bulbasaur.speak()