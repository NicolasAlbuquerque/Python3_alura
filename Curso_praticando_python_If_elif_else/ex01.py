#Bruno geerencia um pequeno comércio e quer saber qual produto teve o melhor desempeno de vendas no mês passado.Ele registrou a quantidade vendida de produtos:maçã e banana; Agora ele precisa escrever um progrograma que  identifique e exiba qual deles teve maior venda.
#Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

maca = int(input('Digite a quantidade de maçãs vendidas: '))
banana= int(input('Digite a quantidade de bananas vendidas'))

if banana > maca:
    print('Banana teve mais vendas.')
elif maca > banana:
    print('Maça teve mais vendas.')
else:
    print('As duas venderam igualmente.')