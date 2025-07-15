from random import randint

# Jogo de adivinhação

print('------ Iniciando o Jogo de Adivinhação ------')
aleatorio = randint(1, 100)
chute = 0
chances = 10
while chute != aleatorio :
    chute = input('Chute um número entre 1 a 100:   ')
    if chute.isnumeric() :
        chute = int(chute)
        chances = chances - 1
        if chute == aleatorio :
            print('---------------------------------')
            print('Parabéns, você venceu. O número era {} e você tinha ainda {} chances'.format(aleatorio,chances))
            print('---------------------------------')
            break
        else :
            print('----')
            if chute > aleatorio :
                print('Você errou, Dica: É um número menor')
            else :
                print("Você errou, Dica: É um número maior")
            print('Você ainda tem {} chances.'.format(chances))
            print('----')
        if chances == 0:
            print('----')
            print('GAME OVER')
            print('Suas chances acabaram,você perdeu!')
            print('----')
            break
print('------ Fim do Jogo ------')