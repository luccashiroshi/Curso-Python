class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            print(f'{self._nome} já está ligado.')
            return
        self._ligado = True
        print(f'{self._nome} ligou.')

    def deligar(self):
        if not self._ligado:
            print(f'{self._nome} não está ligado.')
            return
        self._ligado = False
        print(f'{self._nome} desligou.')
