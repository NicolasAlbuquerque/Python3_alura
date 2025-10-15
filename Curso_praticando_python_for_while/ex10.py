#João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:

#O nome de usuário deve ter pelo menos 5 caracteres.
#A senha deve ter pelo menos 8 caracteres.
#João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

#Crie um programa que implemente essa lógica usando um laço while.
while True:

    usuario = input('Digite um usuário: ')
    senha = input('Informe a senha: ')

    if len(usuario) < 5:
        print('O usuário precisa ter ao menos 5 caracteres.')
        continue
    if len(senha) < 8:
        print('A Senha deve ter ao menos 8 caracteres')

    else:
        print('Usuário cadastrado com sucesso!')        
        ssbreak