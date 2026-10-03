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

    opcoes_pessoa_selecionada = int(input('O que você deseja alterar? '))
    if opcoes_pessoa_selecionada == 1 :
        pessoa_selecionada['nome'] = input('Digite o Nome: ')
        print("alterado com sucesso!!!")

    elif opcoes_pessoa_selecionada == 2:
        pessoa_selecionada['sobrenome'] = input('Digite o Sobrenome: ')
        print("alterado com sucesso!!!")

    elif opcoes_pessoa_selecionada == 3:
            pessoa_selecionada['email'] = input('Digite o E-mail: ')
            print("alterado com sucesso!!!")

    elif opcoes_pessoa_selecionada == 4:
            pessoa_selecionada['telefone'] = input('Digite o numero Telefone: ')
            print("alterado com sucesso")

    elif opcoes_pessoa_selecionada == 5:
            pessoa_selecionada['cidade'] = input('Digite a Cidade: ')
            print("alterado com sucesso!!!")

    elif opcoes_pessoa_selecionada == 6:
            pessoa_selecionada['bairro'] = input('Digite o Bairro: ')
            print("alterado com sucesso!!!")

    elif opcoes_pessoa_selecionada == 7:
            pessoa_selecionada['rua'] = input('Digite a Rua: ')
            print("alterado com sucesso!!!")

    elif opcoes_pessoa_selecionada == 8:
        pessoa_selecionada['n_casa'] = input('Digite o n/casa: ')
        print("alterado com sucesso!!!")

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