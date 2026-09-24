lista_pessoas = []

def lista_usuarios():
    for  contador, pessoa in enumerate(lista_pessoas):
        print(f'Pessoa {contador + 1}')
        print(pessoa['nome'] + " "  + pessoa['sobrenome'])
        print(pessoa['email'])
        print(pessoa['telefone'])
        print(pessoa['cidade'])
        print(pessoa['bairro'])
        print(pessoa['rua'])
        print(pessoa['n_casa'])
        print('----------------')

def selecionar_usuario():
    num_usuario = int(input('Digite o número do usuário que deseja editar: '))
    indice = num_usuario - 1  

    pessoa_selecionada = lista_pessoas[indice]
    print(f'Usuário selecionado(a): {pessoa_selecionada['nome']}')
    print(pessoa_selecionada['nome'] + " "  + pessoa_selecionada['sobrenome'])
    print(pessoa_selecionada['email'])
    print(pessoa_selecionada['telefone'])
    print(pessoa_selecionada['cidade'])
    print(pessoa_selecionada['bairro'])
    print(pessoa_selecionada['rua'])
    print(pessoa_selecionada['n_casa'])
