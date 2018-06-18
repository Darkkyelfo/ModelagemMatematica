from numpy import e

class FuncaoModelo(object):

    def __init__(self, funcao,variaveis, derivada="0"):
        self.funcao = funcao
        self.variaveis = variaveis
        self.derivada = derivada

    def getValorFuncao(self, valores):
        return eval(self.funcao, self.__setChaves(valores))

    def getValorDerivada(self, valores):
        return eval(self.derivada, self.__setChaves(valores))


    def __setChaves(self, valores):
        chaves = {"e": e}  # numero de Euler
        for i, key in enumerate(self.variaveis):
            chaves.update({key: valores[i]})
        return chaves
