#Carlos quer monitorar seu orçamento mensal para  evitar gastos excessivos. Ele estabeleceu um limite de R$3.000,00 para seus gastos e precisa d eum oprograma que ajude a controlar suas despesas. O programa deve receber o total de gastos realizadas e informar se ele ulltrapassou o limite ou ainda está dentro do orçamento
limite = 3000
despesas = float(input('Digite o total das despesas do mês (R$): '))

if despesas > limite:
    print('Atenção! Você ultrapassou o limite do orçamento.')
else:
    print(f'Está dentro do orçamento de R$3.000,00')    