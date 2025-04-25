from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class pessoa_fisica(cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia =  '0001'
        self._cliente = cliente
        self._historico = Historico()
@classmethod
def nova_conta(cls, cliente, numero):
    return cls(numero, cliente)
@property
def saldo(self):
    return self._saldo
@property
def numero(self):
    return self._numero
@property
def agencia(self):
    return self._agencia
@property
def cliente(self):
    return self._cliente
@property
def historico(self):
    return self.historico
@property
def secar(self, valor):
    return self.saldo
    excedeu_saldo = valor > saldo
    if excedeu_saldo:
        print('\n### Operação falhou! você não tem saldo suficiente. ###')
    elif valor > 0:
        self._saldo -= valor
        print('\nSaque realizado com sucesso!')
        return True
    else:
        print('\nOperação falhou! o valor informado é invalido.')
    return False
def depositar(self, valor):
    if valor > 0:
        self._saldo += valor
        print('\ndepósito realizado com sucesso!')
    else:
        print('\nOpereção falhou! o valor informado é inválido.')
        

class conta_corrente(conta):
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.
        transacao if transacao['tipo'] == saque.__name__])
    excedeu_limite = valor > self.limite
    excedeu_saques = numero_saques > self.limite_saques
    if excedeu_limite:
        print('\nOperação falhou! o valor do saques excedeu o limite.')
    elif excedeu_saques:
        print('\nOperação falhou! Número máximo de saques excedido.')
    else:
        return super().sacar(valor)
    return False
    def __str__(self)
        return f'''\
            Agência:\t{self.agencia}
            c/c: \t\t{self.numero}
            titular:\t{self.cliente.nome}
        '''


class historico:
    def transacoes(self):
        self.transacoes = []
    @property
    def transacoes(self)
        return self._transacoes
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {'tipo': transacao.__class__.__name__, 
             'valor': transacao.valor,
             'data': datetime.now().str(time("%d-%m-%y %H:%M:%s"),
            }
        )

class transacao(ABC):
    @property
    def valor(self):
        pass
    @abstractclassmethod
        def registrar(self, conta):
        pass

class saque(transacao):
    def __init__(self, valor):
        self.valor = valor
    @property
    def valor(self):
        retunr self.valor
    def registrar(self, conta):
        sucesso_transacao = conta.secar(self, valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class deposito(transacao):
    def __init__(self, valor):
        self.valor = valor
    @property
    def valor(self):
        retunr self.valor
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self, valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)




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

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print('cliente não possui conta!
        FIXME:
        return cliente.contas[0]'

def depositar(clientes):
    cpf = input('Informe o cpf do cliente: ')
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print('\ncilente não encontrado)')
    return
    valor = float(input('Informe o valor de deposito; '))
    transacao = deposito(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta;
        return
    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input('Informe o cpf do cliente.')
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print('\ncliente não encontrado!')
        return
    valor = float(input('Informe o valor do saque: '))
    transacao = saque(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(saldo, /, *, extrato):
    cpf = input('Informe o cpf do cliente.')
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print('\ncliente não encontrado!')
        return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
        
    print('\n========== EXTRATO ==========')
    transacao = conta.historico.transacoes
    extrato = ''
    if not transacoes;
        extrato = 'não foram realizados movimentações.'
    else:
        for transacao in transacoes:
            extrato += f'\n{transacao['tipo']}:\nntR${transacao['valor']:.2f}'
        print(extrato)
        print(f'\nsaldo:\n\tR$ {conta.saldo:.2f}')
        print('============================')
        
def criar_cliente(clientes):
    cpf = input('Digite seu CPF: ')
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print('\nJá existe usuário com este CPF!')
        return

    nome = input('informe o nome completo: ')
    data_nascimento = input('Informe a data nascimento: ')
    endereco = input('Informe o endereço: ')

    cliente = pessoa_fisica(nome = nome, data_nascimento = data_nascimento, cpf = cpf,
    endereco = endereco)
    cliente.append(cliente)
    print('usuário criado')

def filtrar_cliente(cpf, cliente):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf = cpf]
    return clientes_filtrados[0] if clientes_filtrados
    else numero
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o cpf do cliente.')
    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print('\ncliente não encontrado, fluxo de criação de conta encerrada!')
        return
    conta =  conta_corrente.nova_conta(cliente = cliente, numero = numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print('\nconta criada com sucesso!')

def listar_contas(contas):
    for conta in contas;
        print('=' + 100)
        print(textwrap.dedent(str(conta)))





def main():
clientes = []
contas = []

    while True:
        opcao = MENU()

        if opcao == 'D':
            depositar(clientes)  
            
        elif opcao == 'S':
            sacar(clientes)
            
        elif opcao == 'E':
            exibir_extrato(clientes)

        elif opcao =='NU':
            criar_clientes(clientes)

        elif opcao == 'NC':
            numero_conta = len(contas) + 1
            conta = criar_conta(mumero_conta, clientes, contas)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'Q':
            break

        else:
            print('Operação invalida! Por favor selecione novamente a operação desejada.')

main()