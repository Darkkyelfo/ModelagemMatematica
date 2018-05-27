import abc
import numpy as np


class Funcao(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def getValor(self, valores):
        return valores


class FuncaoPVI(Funcao):
    '''
        Classe que representa uma função com PVI
    '''

    def __init__(self, pvi, n):
        self.pvi = pvi
        self.n = n

    def getValor(self, valores):
        return 0

    def getValorAnalitico(self, valores):
        return 0


class funcao1(FuncaoPVI):
    '''
        Classe que representa a EDO u' = -u^3;u(0) = 1
    '''

    def __init__(self):
        self.pvi = 1
        self.n = 0

    def getValor(self, valores):
        return -np.power(valores[0], 3)

    def getValorAnalitico(self, valores):
        return 1 / (np.sqrt(2 * valores[0] + 1))
