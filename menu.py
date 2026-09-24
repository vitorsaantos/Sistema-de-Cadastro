from pessoa.cadastro import cadastro_pessoa
from pessoa.lista import lista_usuarios, lista_pessoas, selecionar_usuario

print('===== SISTEMA DE CADASTRO =====  ')
print(' 1 - Cadastrar pessoa \n 2 - Listar pessoas \n 3 - Sair')


while True:
    entrada_sistema = int(input('Digite o número desejado: '))

    if entrada_sistema == 1:
        print('Você acessou o casdastro de pessoa')
        usuario = cadastro_pessoa()
        lista_pessoas.append(usuario)
    
        

    elif entrada_sistema == 2:
        print('Você acessou a lista de pessoas')
        lista_usuarios()
        selecionar_usuario()
        

        
          
    elif entrada_sistema == 3:
        print('Volte sempre!')
        break


