# Calculadora de consumo elétrico
# Programa que estima o consumo mensal de energia de um aparelho e o
# custo aproximado desse consumo, com base na potência e no tempo de uso diário.

# Valor fixo do kWh usado para estimar o custo (em reais)
valor_kwh = 0.75

# Solicita ao usuário os dados do aparelho
nome_aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho (em watts): "))
horas_dia = float(input("Digite o tempo médio de uso diário (em horas): "))

# Cálculo do consumo mensal em kWh
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo do custo estimado, com base no valor fixo do kWh
custo_estimado = consumo_mensal * valor_kwh

# Exibição do resultado
print("Aparelho:", nome_aparelho)
print("Consumo estimado:", consumo_mensal, "kWh/mês")
print("Custo estimado: R$", custo_estimado)
