from contapoupanca import ContaPoupanca
from contacorrente import ContaCorrente

cp = ContaPoupanca(1111, 2222, 1000)
cp.depositar(50)
cp.sacar(440)
cp.sacar(1000)

print('______________________________')

cc = ContaCorrente(agencia=1111, conta=3333, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)