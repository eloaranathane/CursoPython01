# Importar o modulo unittest que nos permite escrever testes automatizados
import unittest

# Importar as funções de teste
from teste_unitario import somar, subtrair, multiplicar, dividir

# Criar a classe que contem os testes unitarios para as funções de operação
class TesteOperacoes(unittest.TestCase):
    # Testar a função de soma
    def testar_soma(self):
        # Verificar se a soma de 2 e 3 é igual a 5
        self.assertEqual(somar(2,3), 5)
        # Verificar se a soma de -1 e 1 é igual a 0
        self.assertEqual(somar(-1,1), 0)
        # Verificar se a soma de -2 e -3 é igual a -5
        self.assertEqual(somar(-2,-3), -5)
    
    def testar_divisao(self):
        self.assertEqual(dividir(6,2), 3)
        self.assertEqual(dividir(-6,3), -2)
        self.assertEqual(dividir(6,-2), -3)
        with self.assertRaises(ValueError) :
            dividir(1,0)     # Vai dar erro quando realizar o teste, pois não é possível dividir por 0

    def testar_subtrair(self):
        self.assertEqual(subtrair(6,2), 4)
        self.assertEqual(subtrair(-6,3), -9)
        self.assertEqual(subtrair(6,-2), 4)

    def testar_multiplicar(self):
        self.assertEqual(multiplicar(6,2), 12)
        self.assertEqual(multiplicar(-6,3), -18)
        self.assertEqual(multiplicar(6,-2), -12)

# Permite que os testes sejam executados quando rodamos o arquivo diretamente
if __name__ == '__main__':
    unittest.main()  # Executa todos os testes definidos na classe