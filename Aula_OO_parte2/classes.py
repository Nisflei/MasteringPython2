from random import randint

#Associação
class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__contato = None

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def contato(self):
        return self.__contato

    @contato.setter
    def contato(self, contato):
        self.__contato = contato

class Email:
    def __init__(self, email):
        self.__email = email

    @property
    def email(self):
        return self.__email

    def ver(self):
        print(f'Contato: {self.__email}')

class Fone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def ver(self):
        print(f'Contato: ({self.ddd}) {self.numero}')

#Agregação
class Conta:
    def __init__(self, numero, digito, agencia, saldo):
        self.numero = numero
        self.digito = digito
        self.agencia = agencia
        self.saldo = saldo
        self.cliente = None
        self.__clienteComposicao = None   #cliente como Composicção exemplo

    def dadosConta(self):
        print(f'Agencia: {self.agencia} - cc:{self.numero}/{self.digito} - saldo:{self._saldo}')

    def depositar(self, valor):
        self._saldo = self._saldo + valor
        return True

    def sacar(self, valor):
        if (self._saldo - valor) < 0:
            print("Saldo insuficiente :(")
            return False
        self._saldo = self._saldo - valor
        return True

    def verificarSaldo(self):
        return self._saldo

    @staticmethod
    def gerarNumero():
        num = randint(1000, 1999)
        return num

    # getter
    @property
    def saldo(self):
        return self._saldo

    # setter
    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, str):
            print('Saldo deve ser numerico, saldo 0')
            self._saldo = 0
            return
        self._saldo = valor

    #metodo para Adicionar um Cliente a Conta (agrecação)
    def adicionar_cliente(self, cliente):
        self.cliente = cliente

    #Alterando para composição
    @property
    def clienteComposicao(self):
        return self.__clienteComposicao

    def adicionar_clienteComposicao(self,nome, cpf):
        self.__clienteComposicao = Cliente(nome, cpf)

#Herança

class Poupanca(Conta):
    def __init__(self, numero, digito, agencia, saldo, rendimento):
        Conta.__init__(self, numero, digito, agencia, saldo)
        self.rendimento = rendimento

    def creditar_rendimentos(self):
        self.saldo = self.rendimento + self.saldo
