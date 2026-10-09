
def cadastro_pessoa():
    nome = input('Nome: ')
    campo_obrigatorio(nome)
    resultado = cancelar_cadastro(nome)
    if resultado == None:
        return None
    
    sobrenome = input('Sobrenome: ')
    campo_obrigatorio(sobrenome)
    resultado = cancelar_cadastro(sobrenome)
    if resultado == None:
        return None

    email = input('E-mail: ')
    campo_obrigatorio(email)
    resultado = cancelar_cadastro(email)
    if resultado == None:
        return None

    telefone = input('Telefone: ')
    campo_obrigatorio(telefone)
    resultado = cancelar_cadastro(telefone)
    if resultado == None:
        return None

    cidade = input('Cidade: ')
    campo_obrigatorio(cidade)
    resultado = cancelar_cadastro(cidade)
    if resultado == None:
        return None

        
    bairro = input('Bairro: ')
    campo_obrigatorio(bairro)
    resultado = cancelar_cadastro(bairro)
    if resultado == None:
        return None

    rua = input('Rua: ')
    campo_obrigatorio(rua)
    resultado = cancelar_cadastro(rua)
    if resultado == None:
        return None

    n_casa = input('N/CASA: ')
    campo_obrigatorio(n_casa)
    resultado = cancelar_cadastro(n_casa)
    if resultado == None:
        return None
    print('===== Cadastro Finalizado!!! ====')

# Dicionário
    pessoa = {
        'nome': nome,
        'sobrenome' : sobrenome,
        'email' : email,
        'telefone': telefone,
        'cidade': cidade,
        'bairro': bairro,
        'rua': rua,
        'n_casa': n_casa,
    }

    return pessoa

def cancelar_cadastro(valor):
    if valor == '0':
        print('Cadastro cancelado!!!')
        return None

    else:
        return valor

def campo_obrigatorio(campo):
    while campo == '':
        print('Campo obrigatório!!!')
        campo = input('Digite novamente: ')
    return campo