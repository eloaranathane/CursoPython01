# Reconstrução da nossa calculadora de imposto de renda usando programação orientada a objeto

class TabelaIR() :
    def __init__(self) :
        self.tabela = [
    {"faixa":(0, 1903.98), "aliquota": 0, "deducao": 0},
    {"faixa":(1903.99, 2826.65), "aliquota": 7.5, "deducao": 142.80},
    {"faixa":(2826.66, 3751.05), "aliquota": 15, "deducao": 354.80},
    {"faixa":(3751.06, 4664.68), "aliquota": 22.5, "deducao": 636.13},
    {"faixa":(4664.69, float('inf')), "aliquota": 27.5, "deducao": 869.36}
    ]

class CalculadoraIR() :
    def __init__(self, salario, tabela_ir) :
        self.salario_bruto = salario
        self.tabela_ir = tabela_ir
    def calcular(self) :
        imposto = 0
        for categoria in self.tabela_ir.tabela :
            if self.salario_bruto > categoria["faixa"][0] and self.salario_bruto <= categoria["faixa"][1] :
                imposto = (self.salario_bruto * categoria["aliquota"]) / 100 + categoria["deducao"]
            break
        return imposto

tabela_ir = TabelaIR()
salario_bruto = float(input("Qual o seu salario bruto? "))
calculadora = CalculadoraIR(salario_bruto, tabela_ir)
imposto = calculadora.calcular()
print(f"O imposto de renda devido é R$ {imposto:.2f}")