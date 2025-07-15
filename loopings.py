# Trabalhando com Loopings

palavra = "garrafinha"
contador = 0
print("Palavra escolhida: " , palavra)
for letra in palavra :
    print(contador, " - ", letra)
    contador = contador + 1

cidades = ['Londres','San Diego','Frankfurt','Paris','Toronto','Florida','Nova Iorque','Amsterda']

for cidade in cidades :
    print(cidade)

print(cidades[2])

print("----------------- While -----------------")

botaoExecutar = True #valor boolean
contador = 0
while botaoExecutar :
    print(contador)
    contador = contador + 1
    if contador >= 10 :
        botaoExecutar = False

print('--------------- Exercicio ---------------')

listaDeCompras = ['ovo','pão','leite','margarina','sabão em pó','amaciante','sabonete']

for produto in listaDeCompras :
    print(produto)

print('--------------- Correção do Professor ---------------')

contador = 1

for produto in listaDeCompras :
    #print('[', contador,']', produto)
    print('[' + str(contador) + '] ' + produto)
    contador = contador + 1
