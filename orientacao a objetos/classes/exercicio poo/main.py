from classes import Banco, Cliente, ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Carlos', 50)
cliente2 = Cliente('Fátima', 19)
cliente3 = Cliente('Rodrigo', 26)

conta1 = ContaPoupanca(1111, 234567, 0)
conta2 = ContaCorrente(3333, 248547, 0)
conta3 = ContaPoupanca(7777, 111354, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

banco.inserir_cliente(cliente3)
banco.inserir_conta(conta3)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(0)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado')

if banco.autenticar(cliente3):
    cliente1.conta.depositar(50)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado')