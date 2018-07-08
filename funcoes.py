from numpy import e
from itertools import zip_longest


def create_dict(keys, values):
    d = dict(zip_longest(keys, values[:len(keys)]))
    d["e"] = e
    return d


def setChaves(variaveis, valores):
    chaves = {"e": e}  # numero de Euler
    for i, key in enumerate(variaveis):
        chaves[key] = valores[i]
    return chaves


class FuncaoModelo(object):

    def __init__(self, funcao, variaveis, derivada="0"):
        self.funcao = funcao
        self.variaveis = variaveis
        self.derivada = derivada

    def getValorFuncao(self, valores):
        return eval('lambda: ' + self.funcao, create_dict(self.variaveis, valores))()

    def getValorDerivada(self, valores):
        return eval(self.derivada, create_dict(self.variaveis, valores))


class FuncaoBasica(object):

    def getValorFuncao(self, valores):
        raise NotImplementedError("erro:implemente a funcao dx antes de usa-la.")

    def getValorDerivada(self, valores):
        raise NotImplementedError("erro:implemente a funcao dx antes de usa-la.")
