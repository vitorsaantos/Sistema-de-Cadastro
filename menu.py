from pessoa.cadastro import cadastro_pessoa

print('===== SISTEMA DE CADASTRO =====  ')
print(' 1 - Cadastrar pessoa \n 2 - Listar pessoas \n 3 - Sair')

lista_pessoas = []

while True:
    entrada_sistema = int(input('Digite o número desejado: '))

    if entrada_sistema == 1:
        print('Você acessou o casdastro de pessoa')
        usuario = cadastro_pessoa()
        lista_pessoas.append(usuario)
    
        

    elif entrada_sistema == 2:
        print('Você acessou a lista de pessoas')
        print(lista_pessoas)


    elif entrada_sistema == 3:
        print('Volte sempre!')
        break


