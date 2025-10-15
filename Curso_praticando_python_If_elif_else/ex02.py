#Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.
#Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.

at_a=int(input('Informe os dias para a atividade A: '))
at_b=int(input('Informe os dias para a atividade B: '))
at_c=int(input('Informe os dias para a atividade C: '))

if at_a < 0 or at_b < 0 or at_c < 0:
    print('Erro: os dias não podem ser negativos.')
else:
    soma = at_a + at_b + at_c   
    print(f'Tempo total necessário em dias é de {soma}') 