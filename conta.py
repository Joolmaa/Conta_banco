from asyncio import selector_events

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de R$:{} Titular {} ".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_sacar):
        valor_disponivel_para_sacar = self.__limite + self.__saldo
        return valor_sacar <= (valor_disponivel_para_sacar)

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def __pode_transferir(self, valor_transferir):
        valor_disponivel_para_transferir = self.__limite + self.__saldo
        return valor_transferir <= (valor_disponivel_para_transferir)

    def transferir(self, valor_transferir, destino):
        if (self.__pode_transferir(valor_transferir)):
            self.saca(valor_transferir)
            destino.deposita(valor_transferir)
            print("Foi transferido R$:{}".format(valor_transferir))
        else:
            print("Você não pode transferir R$:{}, pq é maior que seu limite que é de R$:{}".format(
                valor_transferir, self.__limite))

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    def get_numero(self):
        return self.__numero

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
