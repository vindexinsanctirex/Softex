class animal:
    def __init__(self, nome, habitat, hábito):
        self.nome = nome
        self.habitat = habitat
        self.hábito = hábito

    def exibir_informações(self):
        return f"Nome: {self.nome}, Habitat: {self.habitat}, Hábito: {self.hábito}"

class mamífero(animal):
    def __init__(self, nome, habitat, hábito, pelugem):
        super().__init__(nome, habitat, hábito)
        self.pelugem = pelugem

    def exibir_informações(self):
        info_base = super().exibir_informações()
        return f"{info_base}, Pelugem: {self.pelugem}"
    
class ave(animal):
    def __init__(self, nome, habitat, hábito, penugem):
        super().__init__(nome, habitat, hábito)
        self.penugem = penugem

    def exibir_informações(self):
        info_base = super().exibir_informações()
        return f"{info_base}, Penugem: {self.penugem}"
    
class réptil(animal):
    def __init__(self, nome, habitat, hábito, escamas):
        super().__init__(nome, habitat, hábito)
        self.escamas = escamas

    def exibir_informações(self):
        info_base = super().exibir_informações()
        return f"{info_base}, Escamas: {self.escamas}"
    

    
# Exemplos de uso
if __name__ == "__main__":
    leão = mamífero("Leão", "Savana", "Diurno", "Densa")
    print(leão.exibir_informações())

    águia = ave("Águia", "Montanhas", "Diurno", "Curta")
    print(águia.exibir_informações())

    cobra = réptil("Cobra", "Floresta", "Noturno", "Lisa")
    print(cobra.exibir_informações())


    