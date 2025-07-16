# Calculadora com múltiplos argumentos.

class Calculadora :
    def somar(self, *args) :
        return sum(args)


# Criar oobjeto calculadora
calc = Calculadora()


# Passagem dos argumentos (Quantos desejar)

print(calc.somar(2,6))  # Retorna 8
print(calc.somar(1, 2, 3, 4, 5))  # Retorna 15