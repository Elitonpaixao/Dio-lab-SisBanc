menu = '''
**************
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair
**************
==>  '''

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(f'Escolha uma opoção {menu}').strip().upper()

    if opcao == 'D':
        valor = float(input('Informe o valor do depósito: '))


        if valor > 0:  #evitando deposito de numeros negativos
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == 'S':
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo  # Verificação do saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')

        elif excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite diario.')

        elif excedeu_saque:
            print('Operação falhou! Numero máximo de saques diario excedido.')

        elif valor > 0: # verificando operação de valor negativo
            saldo -= valor
            extrato += f'saque: R$ {valor:.2f}\n'
            numero_saque +=1

        else:
            print('Operação falhou! O valor informado é invalido.')


    elif opcao == 'E':
        print('\n========== EXTRATO ==========')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo:  R$ {saldo:.2f}')
        print('=============================')

    elif opcao == 'Q':
        break

    else:
        print('Operação invalida! Por favor selecione novamente a operação desejada.')