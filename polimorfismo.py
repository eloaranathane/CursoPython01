# Trabalhando com orientação a objeto e polimorfismo

class Animal :
    def fazer_som(self) :
        pass

class Cachorro(Animal) :
    def fazer_som(self) :
        return "Au au"

class Gato(Animal) :
    def fazer_som(self) :
        return "Miau"
    
# Usando o polimorfismo
def fazer_animal_falar(animal: Animal) :
    print(animal.fazer_som())

# Criando os objetos
cachorro = Cachorro()
gato = Gato()

# Chamando o método de cada animal de forma polimorfica
fazer_animal_falar(cachorro)
fazer_animal_falar(gato)

# Os objetos tem seus respetivos métodos (qualificação do objeto)