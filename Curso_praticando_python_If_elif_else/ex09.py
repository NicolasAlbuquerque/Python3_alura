#Lucas está desenvolvendo um jogo e precisa de uma funcionalidade que verifique se um número é par ou ímpar. Essa verificação será usada para definir ações diferentes dentro do jogo. Escreva um programa que receba um número inteiro e exiba uma mensagem informando se ele é par ou ímpar.

num = int(input('Digite um número para descobrir se é Par ou Ímpar: '))

if num % 2 == 1:
    print(f'O número {num} é Impar')
else:
    print(f'O número {num} é Par.')    