from pessoa.cadastro import cadastro_pessoa
import pessoa.lista

print('===== SISTEMA DE CADASTRO =====  ')
print(' 1 - Cadastrar usuário \n 2 - Listar usuário \n 3 - Sair')

usuarios = pessoa.lista.carregar_usuarios()
pessoa.lista.lista_pessoas = usuarios

while True:
    try:
        entrada_sistema = int(input('Digite o número desejado: '))
    except ValueError:
        print(f'Digite apenas número!')
        continue

    if entrada_sistema == 1:
        print('Você acessou o cadastro de usuário.')
        print('Durante o cadastro, digite "0" a qualquer momento para cancelar.')
        usuario = cadastro_pessoa()
        if usuario is not None:
            pessoa.lista.lista_pessoas.append(usuario)
            pessoa.lista.salvar_usuario()
       
    elif entrada_sistema == 2:
        print('Você acessou a lista de usuários.')
        pessoa.lista.lista_usuarios()
        pessoa.lista.selecionar_usuario()
                
    elif entrada_sistema == 3:
        print('Você saiu do sistema.')
        break

    else:
        print('Opção inválida!')
       


