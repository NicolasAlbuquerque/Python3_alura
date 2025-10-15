#Ana esta criando um sistema para calcular o IMC e fornecer recomendações básicas. O programa ddve receber o peso e a altura e exibir o calordo IMC, além de indicar se está abaixo do peso, com o peso normal ou acima do peso. Crie um programa que receba o peso em (Kg) e a altura (em metros) e calcule o IMC usanso a formila: IMC = peso / (altura ** 2) depois exiba o valor do imc e uma mendagem indicando se está acima abaixou o no peso ideal: abaixo do peso (imc < 18.5) peso normal ( 18.5 <= imc <25) acima do peso (imc >= 25)

peso= float(input('Informe o peso em Kg: '))
altura = float(input('Informa a altura em metros: '))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print(f'IMC = {imc}, indicando que está abaixo do peso.')
elif 18.5 <=  imc < 25:
    print(f'IMC = {imc}, indicando que está na faixa de peso ideal.')
else:
    print(f'IMC = {imc}, indicando que está acima do peso.')
