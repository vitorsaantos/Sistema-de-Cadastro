import json

lista_pessoas = []

def lista_usuarios():
    for  contador, pessoa in enumerate(lista_pessoas):
        print(f'Pessoa {contador + 1}')
        print(f"Nome: {pessoa['nome']} {pessoa['sobrenome']}")
        print(f"E-mail: {pessoa['email']}")
        print(f"Telefone: {pessoa['telefone']}")
        print(f"Cidade: {pessoa['cidade']}")
        print(f"Bairro: {pessoa['bairro']}")
        print(f"Rua: {pessoa['rua']}")
        print(f"N/Casa: {pessoa['n_casa']}")
        print('----------------')


def selecionar_usuario():
    num_usuario = int(input('Digite o número do usuário que deseja editar ou ("0" para voltar): '))
    
    if num_usuario == 0:
        return 
    
    indice = num_usuario - 1 

    pessoa_selecionada = lista_pessoas[indice]
    print(f"Usuário selecionado(a): {pessoa_selecionada['nome']}")
    print(pessoa_selecionada['nome'] + " "  + pessoa_selecionada['sobrenome'])
    print(pessoa_selecionada['email'])
    print(pessoa_selecionada['telefone'])
    print(pessoa_selecionada['cidade'])
    print(pessoa_selecionada['bairro'])
    print(pessoa_selecionada['rua'])
    print(pessoa_selecionada['n_casa'])

    # Opções para usuário poder editar pessoa_selecionada
    print('1 - Nome')
    print('2 - Sobrenome')
    print('3 - E-mail')
    print('4 - Telefone')
    print('5 - Cidade')
    print('6 - Bairro')
    print('7 - Rua')
    print('8 - N_Casa')
    print('digite "0" a qualquer momento para cancelar')

    opcoes_pessoa_selecionada = int(input('O que você deseja alterar? '))
    if opcoes_pessoa_selecionada == 1 :
        novo_nome = input('Digite o nome: ')
        if novo_nome == '0':
            print('Cancelado!!!')

        else:
            pessoa_selecionada['nome'] = novo_nome
            print("alterado com sucesso!!!")
        

    elif opcoes_pessoa_selecionada == 2:
        novo_sobrenome = input('Digite o sobrenome: ')

        if novo_sobrenome == '0':
            print('Cancelado!!!')

        else:
            pessoa_selecionada['sobrenome'] = novo_sobrenome
            print("alterado com sucesso!!!")


    elif opcoes_pessoa_selecionada == 3:
        email = input('Digite o E-mail: ')
        if email == '0':
            print('Cancelado!!!')
            
        else:
            pessoa_selecionada['email'] = email
            print("alterado com sucesso!!!")

    elif opcoes_pessoa_selecionada == 4:
        novo_telefone = input('Digite o numero Telefone: ')

        if novo_telefone == '0':
            print('Cancelado!!!')
        
        elif len(novo_telefone) != 11:
            print('Telefone inválido!')
        
        elif not novo_telefone.isdigit():
            print('Digite apenas números!!!')

        else:
            pessoa_selecionada['telefone'] = novo_telefone
            print("alterado com sucesso")

    elif opcoes_pessoa_selecionada == 5:
        nova_cidade = input('Digite a Cidade: ')
        if nova_cidade == '0':
            print('Cancelado!!!')
        
        else:
            pessoa_selecionada['cidade'] = nova_cidade
            print("alterado com sucesso!!!")

    elif opcoes_pessoa_selecionada == 6:
        novo_bairro = input('Digite o Bairro: ')
        if novo_bairro == '0':
            print('Cancelado!!!')
        
        else:
            pessoa_selecionada['bairro'] = novo_bairro
            print("alterado com sucesso!!!")

    elif opcoes_pessoa_selecionada == 7:
        nova_rua = input('Digite a Rua: ')
        if nova_rua == '0':
            print('Cancelado!!!')
        
        else:
            pessoa_selecionada['rua'] = nova_rua
            print("alterado com sucesso!!!")

    elif opcoes_pessoa_selecionada == 8:
        novo_n_casa = input('Digite o n/casa: ')
        if novo_n_casa == '0':
            print('Cancelado!!!')
        
        else:
            pessoa_selecionada['n_casa'] = novo_n_casa
            print("alterado com sucesso!!!")

    elif opcoes_pessoa_selecionada == 0:
        print('Operação cancelada!!!')

    else:
         print('Opção inválida!')

    salvar_usuario()


# 1 - Abre o arquivo usuario.json em modo escrita para escrever os dados no arquivo
# 2 - Pegue o conteúdo de lista_pessoas e escreva/salve no arquivo
def salvar_usuario():
    with open("usuario.json", "w") as arquivo:
        json.dump(lista_pessoas, arquivo)

# 1 - Abre o arquivo usuario.json em modo leitura
# 2 - Pega o conteúdo do arquivo e transforma em dados Python
# 3 - Retorna esses dados para quem chamou a função
def carregar_usuarios():
    with open("usuario.json", "r") as arquivo:
        dados = json.load(arquivo)
    return dados

