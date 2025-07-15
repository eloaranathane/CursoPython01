# Exercício: Idade
# Perguntar ano de nascimento e ano atual e retornar idade e perguntar se deseja novo teste

executar = True
while executar :
    anoNasc = int(input('Em que ano você nasceu? '))
    anoAtual = int(input('Em que ano estamos? '))
    idade = anoAtual - anoNasc
    print('Você tem '+ str(idade) + ' anos.')
    opcao = input('\n Deseja tentar novamente? \n [1]Sim  \n [2]Não ')
    if opcao == '2' : 
        executar = False

print('-------- Segundo Exercício Usando Funções --------')

def calcular_idade() :
    anoNsc = int(input('Em que ano você nasceu? '))
    anoAtl = int(input('Em que ano estamos? '))
    idade = anoAtl - anoNsc
    print('Você tem ' + str(idade) + ' anos.')

def perguntar_novamente() :
    opcao = input('Deseja testar novamente? Sim ou Não')
    if opcao in "Sim" :
        iniciarprograma()
    else :
        print('Encerrando programa! Até mais.')
    
def iniciarprograma() :
    calcular_idade()
    perguntar_novamente()

# Chamada Inicial
iniciarprograma()

print('-------- Terceiro Exercício Usando Funções --------')
# Para se caso houver erro de digitação nas respostas

def calcular_idade() :
    anoNsc = int(input('Em que ano você nasceu? '))
    anoAtl = int(input('Em que ano estamos? '))
    idade = anoAtl - anoNsc
    print('Você tem ' + str(idade) + ' anos.')

def perguntar_novamente() :
    opcao = input('Deseja testar novamente? Sim ou Não')
    if opcao.lower() in ['sim','s','sm','siim','simm'] :
        iniciarprograma()
    else :
        print('Encerrando programa! Até mais.')
    
def iniciarprograma() :
    calcular_idade()
    perguntar_novamente()

# Chamada Inicial
iniciarprograma()
