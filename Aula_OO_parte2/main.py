from classes import Cliente, Email, Fone, Conta, Poupanca

#Objeto Cliente
print('========= Clientes======')
cli1 = Cliente('Pedro','123.123.123')
cli1_email = Email('pedro@fiap.edu.br')
cli1.contato = cli1_email
print(cli1.__dict__)
cli1.contato.ver()

cli2 = Cliente('Ana', '987.987.987')
cli2_fone = Fone('11', '987987987')
cli2.contato = cli2_fone
print(cli2.__dict__)
cli2.contato.ver()

#Objeto Conta com AGREGAÇÃO de Cliente
print()
print('========= Conta Corrente + Cliente')
conta1 = Conta(100, 1, 1010, 50.01)
conta2 = Conta(200, 2, 1010, 500)
conta3 = Conta(300, 3, 1010, 500000)

#agregar os clientes
conta1.adicionar_cliente(cli1)
conta1.dadosConta()
print(f'Cliente: {conta1.cliente.nome}')
conta1.cliente.contato.ver()

conta2.adicionar_cliente(cli2)
conta2.dadosConta()
print(f'Cliente: {conta2.cliente.nome}')
conta2.cliente.contato.ver()

conta3.adicionar_cliente(cli1)
conta3.dadosConta()
print(f'Cliente: {conta3.cliente.nome}')
conta3.cliente.contato.ver()

# Objeto Conta com COMPOSICAO de CLIENTE

conta4 = Conta(400, 4, 1010, 800)
print(conta4.__dict__)
#conta4.clienteComposicao = cli1   não funciona porque esta protegido e precisa usar o metodo
conta4.adicionar_clienteComposicao('Jose', '741.852.852')
print(conta4.__dict__)
print()
conta4.dadosConta()
print(f'Cliente: {conta4.clienteComposicao.nome}')

#Objeto Poupança com HERANÇA Conta

print()
print('============== POUPANCA + CLIENTE')
poupa = Poupanca(500,5,1010,1000,50)
poupa.adicionar_clienteComposicao('Faulto Silva', '1234365789')
poupa.dadosConta()
poupa.creditar_rendimentos();
poupa.dadosConta()


