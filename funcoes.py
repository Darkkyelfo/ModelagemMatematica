from numpy import e


# class Funcao(object):
#
#     def getValor(self, valores):
#         return 0
#
#     def getValorDerivada(self,valores):
#         return 0
#
#
# class FuncaoPVI(Funcao):
#     '''
#         Classe que representa uma função com PVI
#     '''
#
#     def __init__(self, pvi, n):
#         self.pvi = pvi
#         self.n = n
#
#     def getValorAnalitico(self, valores):
#         return 0
#
#
#
# class funcao1(FuncaoPVI):
#     '''
#         Classe que representa a EDO u' = -u^3;u(0) = 1
#     '''
#
#     def __init__(self):
#         self.pvi = 1
#         self.n = 0
#
#     def getValor(self, valores):
#         return -np.power(valores[0], 3)
#
#     def getValorAnalitico(self, valores):
#         return 1 / (np.sqrt(2 * valores[0] + 1))


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
