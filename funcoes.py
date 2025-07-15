# Entendendo Funções em Python

def minhaFuncao() :
    print("Olá Mundo")

minhaFuncao()
minhaFuncao()
minhaFuncao()
minhaFuncao()

alunos = ['Jesreel','Eloara','Emily','Alice','Andressa','Davi']
cursos = ['Python','PHP','SQL']

# Trabalhando com Variáveis de Função
def minhaFuncaoMelhorada(animal, primaveras) :
    print('Você gosta de ',animal, ' e ele tem ', primaveras,'anos')
    # print(Você gosta de ' + str(animal))

petCliente = input('Qual seu animal preferido? ')
idadePet = input('Qual a idade do seu ' + petCliente)
minhaFuncaoMelhorada(petCliente, idadePet)
minhaFuncaoMelhorada('iguana', '4')

print('--------------- Exercício ---------------')

def funcaoCriativa(anoNascimento, anoCorrente, idade) :
    print()

anoNascimento= input('Que ano você nasceu? ')
anoCorrente = input('Que ano nós estamos? ')
idade = ('Você tem ' )