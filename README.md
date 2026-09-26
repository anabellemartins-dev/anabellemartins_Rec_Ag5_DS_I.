📌 Sobre o projeto
Programa em Python desenvolvido durante um programa de iniciação em tecnologia. A calculadora ajuda o usuário a estimar quanto um aparelho elétrico consome de energia por mês,
e quanto isso custa em reais, a partir de dados simples de uso informados por ele mesmo.

🐍 Linguagem
Python 3

🧮 Fórmula utilizada
Consumo mensal (kWh):
consumoMensal = (potencia * horasDia * 30) / 1000
Custo estimado (R$):
custoEstimado = consumoMensal * valorKwh
O valor do kWh utilizado no cálculo é fixo em R$ 0,75.

⚙️ Como funciona
O programa solicita:
🔌 O nome do aparelho (ex.: Geladeira)
💡 A potência do aparelho, em watts (W)
⏱️ O tempo médio de uso diário, em horas
E exibe o consumo mensal estimado, em kWh, junto com o custo aproximado em reais.

▶️ Como executar
Certifique-se de ter o Python 3 instalado e rode, no terminal:
python3 app.py
Em seguida, digite o nome do aparelho, a potência e as horas de uso diário quando solicitado.

🧪 Exemplo de execução
Digite o nome do aparelho: Geladeira
Digite a potência do aparelho (em watts): 150
Digite o tempo médio de uso diário (em horas): 10
Aparelho: Geladeira
Consumo estimado: 45.0 kWh/mês
Custo estimado: R$ 33.75

🎓 Atividade
Projeto desenvolvido para a disciplina de Desenvolvimento de Sistemas I — programa de iniciação em tecnologia.
