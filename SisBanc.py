import textwrap

def menu():
    menu = '''\n
    *********************
    [D]\t Depositar
    [S]\t Sacar
    [E]\t Extrato
    [NC]\t nova conta
    [Q]\t Sair
    *********************
    ==>  '''
    return input(texterap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:  #evitando deposito de numeros negativos
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print('\nDepósito realizado com sucesso!')
        else:
            print('\nOperação falhou! O valor informado é inválido.')
        return saldo, etrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo  
    excedeu_limite = valor > limite            
    excedeu_saques = numero_saques > limite_seques
        
        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')

        elif excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite diario.')

        elif excedeu_saque:
            print('Operação falhou! Numero máximo de saques diario excedido.')

        elif valor > 0: 
            saldo -= valor
            extrato += f'saque: R$ {valor:.2f}\n'
            numero_saque +=1
            print('\nSaque realizado')
        else:
            print('Operação falhou! O valor informado é invalido.')

        return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):

    print('\n========== EXTRATO ==========')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo:  R$ {saldo:.2f}')
        print('=============================')

def criar_usuario(usuarios):
    cpf = input('Digite seu CPF: ')

    if usuario:
        print('\nJá existe usuário com este CPF!')
        return

    nome = input('informe o nome completo: ')
    data_nascimento = input('Informe a data nascimento: ')
    endereco = input('Informe o endereço: ')

    usuario.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('usuário criado')

def filtrar_usuario(usuarios):

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o cpf do usuario: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nconta criada com sucesso!')
        returne{'agencia':agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print('\nUsuário não encontardo, criação de conta encerrada!')

def 








def main():
saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUES = 3
AGENCIA = '0001'
usuario = []
contas = []

    while True:
        opcao = MENU()

        if opcao == 'D':
            valor = float(input('Informe o valor do depósito: '))
            saldo, extrato = depositar(saldo, valor, extrato)     
            
        elif opcao == 'S':
            valor = float(input('Informe o valor do saque: '))
            saldo, extrato = sacar(
                saldo = saldo,  
                limite = limite,
                valor = valor,
                extrato = extrato,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
            
        elif opcao == 'E':
            exibir_extrato(saldo, extrato = extrato)

        elif opcao =='NU':
            criar_usuario(usuarios)

        elif opcao == 'NC':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'Q':
            break

        else:
            print('Operação invalida! Por favor selecione novamente a operação desejada.')

main()