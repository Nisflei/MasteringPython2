from random import randint

class bola:
    def __init__(self,material, formato, tamanho, cor):
        self.material = material
        self.formato = formato
        self.tamanho = tamanho
        self.cor = cor


print("+++++++++++++++ Usando uma classe+++++++++++++++++=")
# estou criando o objeto a partir do "molde" classe
futebol = bola('couro', 'redonda', '40cm', 'branca')
ping_pong = bola('pvc','redonda','1.5cm','amarela')

print(f'Objeto:  Bola de futebol  - {futebol.material}-{futebol.cor} ')
print(f'Objeto: Bola de Pingpong - {ping_pong.material}-{ping_pong.cor}')

print(futebol)
print(f'conteudo do OBJETO: {futebol.__dict__}')


# Usando conta corrente

class conta:
    def __init__(self, numero, digito, agencia, saldo):
        self.numero = numero
        self.digito = digito
        self.agencia = agencia
        self.saldo = saldo

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

    #getter
    @property
    def saldo(self):
        return self._saldo

    #setter
    @saldo.setter
    def saldo(self, valor):
        if isinstance(valor, str):
            print('Saldo deve ser numerico, saldo 0')
            self._saldo = 0
            return
        self._saldo = valor


print("   ")
print("Exemplo 2 - ContaCorrente")
conta1 = conta(100, 1, 1010, 50.01)
conta2 = conta(200, 2, 1010, 500)

print(conta1.__dict__)
print(conta2.__dict__)

conta1.dadosConta()
conta2.dadosConta()

# usar os metodos
print(f'Deposito 200: {conta1.depositar(200)}')
print(f'Saldo: {conta1.verificarSaldo()}')
print(f'Sacar 50.01: {conta1.sacar(50.01)}')
print(f'Saldo: {conta1.verificarSaldo()}')
print(f'Sacar 500: {conta1.sacar(500)}')
print(f'Saldo sem alteração: {conta1.verificarSaldo()}')

# gerando numero aleatorio
print(conta.gerarNumero())
conta3 = conta(conta.gerarNumero(), 0, 1010, 5000)
print(conta3.dadosConta())

# Getter / Setter
conta4 = conta(200,1,1010,'R$500')
print(conta4.dadosConta())
conta4.saldo = 100
print(conta4.dadosConta())



