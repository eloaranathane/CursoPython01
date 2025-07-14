# Trabalhando com IF e testes
tipoEscola = input("Tipo do Colegio: \n [1] - Publico \n [2] - Particular \n Resposta: ")
nomeAluno = input("Qual o nome do aluno?")
freqAluno = input("Qual a frequência do aluno?")
mediaAluno = int(input("Qual a média do aluno?"))
#mediaEscola = input("Média de corte da Escola")
mediaEscola = 7
freqAluno = int(freqAluno)
'''
!= Diferente
== Igual
<= Menor ou Igual
>= Maior ou Igual
> Maior
< Menor
'''
if tipoEscola == "2" :
    print("----- Escola Particular -----")
    if mediaAluno >= mediaEscola and freqAluno >= 70 :
        print("Aprovado")
    else :
        print("Reprovado")
if tipoEscola == "1" :
    print("----- Escola Público -----")
    if mediaAluno >= mediaEscola or freqAluno >= 60 :
        print("Aprovado")
    else :
        print("Reprovado")

