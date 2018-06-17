import sys
import numpy as np
from numba import jit


class EulerExplicito(object):

    def solucionar(self, funcoes, pvi, h, tmax):
        self.tmax = tmax
        self.h = h
        self.resultados = []
        t = pvi[-1]
        for valor in pvi:
            self.resultados.append([valor])
        while t <= tmax:
            resultados = np.array(self.resultados, np.float32)[:, -1]
            for i, func in enumerate(funcoes):
                r = self.resultados[i]
                r.append(r[-1] + self.h * func.getValorFuncao(resultados))
            t = self.h + t
            self.resultados[-1].append(t)

    def eixoX(self):
        return self.resultados[-1]


class Newton(object):

    def zeroFx(self, x0, funcao, e):
        xk = x0
        iteracoes = 0
        erro = sys.maxsize
        while erro >= e:
            xkant = xk
            xk = xk - (funcao.getValorFuncao([xk]) / funcao.getValorDerivada([xk]))
            erro = np.fabs(xk - xkant)
            iteracoes = iteracoes + 1
        return xk, iteracoes


class RungeKutta(object):

    def solucionar(self, funcoes, pvi, h, tmax):
        self.h = h
        self.resultados = []
        self.ks = []
        t = pvi[-1]
        tamanho = len(funcoes)
        for valor in pvi:
            self.resultados.append([valor])
        for i in funcoes:
            self.ks.append([0] * 4)
        self.ks = np.array(self.ks,np.float32)
        cont = 1
        while t <= tmax:
            self.__acharInclinacoes(funcoes)
            for i in range(tamanho):
                r = self.resultados[i]
                r.append(r[-1] + (self.h / 6) * np.sum(self.ks[i] * [1, 2, 2, 1]))
            t = pvi[-1] + self.h * cont
            cont += 1
            self.resultados[-1].append(t)

    # @jit
    def __getKmeio(self, funcao, resultados, coluna):
        valores = np.copy(resultados)
        tamanho = len(valores) - 1
        valores[tamanho] = valores[tamanho] + self.h / 2
        for i, k in enumerate(np.array(self.ks, np.float32)[:, coluna - 1]):
            valores[i] = valores[i] + (self.h / 2) * k

        return funcao.getValorFuncao(valores)

    # @jit
    def __getKFinal(self, funcao, resultados, coluna):
        valores = np.copy(resultados)
        tamanho = len(valores) - 1
        valores[tamanho] = valores[tamanho] + self.h / 2
        for i, k in enumerate(np.array(self.ks, np.float32)[:, coluna - 1]):
            valores[i] = valores[i] + self.h * k
        return funcao.getValorFuncao(valores)

    # @jit
    def __acharInclinacoes(self, funcoes):
        resultados = np.array(self.resultados, np.float32)[:, -1]
        for coluna in range(self.ks.shape[1]):
            for linha in range(self.ks.shape[0]):
                if (coluna == 0):  # incio
                    self.ks[linha][coluna] = funcoes[linha].getValorFuncao(resultados)
                elif (coluna == 3):  # o fim
                    self.ks[linha][coluna] = self.__getKFinal(funcoes[linha], resultados, coluna)
                else:  # e o meio
                    self.ks[linha][coluna] = self.__getKmeio(funcoes[linha], resultados, coluna)

    def eixoX(self):
        return self.resultados[-1]
