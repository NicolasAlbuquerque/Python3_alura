#Lucas trabalha com TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele que rum programam que receba a temperatuda atual como entrada e, se necessãrio exiba uma mensagem de alerta.

temp = int(input('Digite a temperatura atual: '))

if temp > 25:
    print('Alerta! temperatuda acima do limite pertmitido')
else:
    print('Temperatura dentro do limite.')    