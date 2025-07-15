# Calculadora Básica em Python

# Função que gera o texto de introdução

def intro() :
    return '''
   ____      _            _           _                 
  / ___|__ _| | ___ _   _| | __ _  __| | ___  _ __ __ _ 
 | |   / _` | |/ __| | | | |/ _` |/ _` |/ _ \| '__/ _` |
 | |__| (_| | | (__| |_| | | (_| | (_| | (_) | | | (_| |
  \____\__,_|_|\___|\__,_|_|\__,_|\__,_|\___/|_|  \__,_|
                                                        
Feito por: 
   __   _                
  /  ` //                
 /--  // __ __.  __  __. 
(___,</_(_)(_/|_/ (_(_/|_
                         
'''
# Função que mostra o menu inicial

def mostrar_menu() :
    return '''
        [1] ou [+] para Somar
        [2] ou [-] para Subtrair
        [3] ou [*] para Multiplicar
        [4] ou [/] para Dividir
        [5] para Sair
        (ou digite sua opção: Somar / Subtrair / Multiplicar / Dividir / Sair)
'''
# Função que lê os valores

def ler_valores() :
    valor01 = int(input('Insira o primeiro valor: '))
    valor02 = int(input('Insira o segundo valor: '))
    return valor01, valor02

# Funções de cálculo
def somar(a ,b) :
    return a + b
def subtrair(a, b) :
    return a - b
def dividir(a, b) :
    return a / b 
def multiplicar(a, b) :
    return a * b

# Função para permanecer ou sair do programa
def desejacontinuar() :
    print('''
        [1] Não, desejo sair!
        [2] Sim, desejo realizar outro cálculo
    ''')
    opcao = input('Deseja realizar outra conta? ')
    return opcao != '1'

# Looping principal
executar = True
print(intro())
while executar :
    print(mostrar_menu())
    operador = input('Qual a sua opção? ').strip().lower()

    if operador in ['5','sair'] :
        print('Obrigada por usar a melhor calculadora')
        break

    v01, v02 = ler_valores()

    if operador in ['1','+','somar'] :
        resultado = somar(v01, v02)
    elif operador in ['2','-','subtrair'] :
        resultado = subtrair(v01, v02)
    elif operador in ['3','*','multiplicar'] :
        resultado = multiplicar(v01, v02)
    elif operador in ['4','/','dividir'] :
        resultado = dividir(v01, v02)
    else:
        print('Opção inválida. Tente novamente.')

    print('Resultado é: ' + str(resultado))
    executar = desejacontinuar()