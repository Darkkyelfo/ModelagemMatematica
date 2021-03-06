import sys
import numpy as np


class EulerExplicito(object):

    def solucionar(self, funcoes, pvi, h, tmax):
        self.tmax = tmax
        self.h = h
        self.resultados = []
        t = pvi[-1]
        for valor in pvi:
            self.resultados.append([valor])
        while t <= tmax:
            resultados = [row[-1] for row in self.resultados]
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
        self.ks = np.array(self.ks, np.float32)
        cont = 1
        while t <= tmax:
            self.__acharInclinacoes(funcoes)
            for i in range(tamanho):
                r = self.resultados[i]
                r.append(r[-1] + (self.h / 6) * np.sum(self.ks[i] * [1, 2, 2, 1]))
            t = pvi[-1] + self.h * cont
            cont += 1
            self.resultados[-1].append(t)

    def __getKmeio(self, funcao, resultados, coluna):
        valores = np.copy(resultados)
        ks = np.append((self.h / 2) * self.ks[:, coluna - 1], [self.h / 2])
        valores = valores + ks
        return funcao.getValorFuncao(valores)

    def __getKFinal(self, funcao, resultados, coluna):
        valores = np.copy(resultados)
        ks = np.append(self.h * self.ks[:, coluna - 1], [self.h])
        valores = valores + ks
        return funcao.getValorFuncao(valores)

    def __acharInclinacoes(self, funcoes):
        resultados = [row[-1] for row in self.resultados]
        col = self.ks.shape[1]
        row = self.ks.shape[0]
        for coluna in range(col):
            for linha in range(row):
                if (coluna == 0):  # incio
                    self.ks[linha][coluna] = funcoes[linha].getValorFuncao(resultados)
                elif (coluna == 3):  # o fim
                    self.ks[linha][coluna] = self.__getKFinal(funcoes[linha], resultados, coluna)
                else:  # e o meio
                    self.ks[linha][coluna] = self.__getKmeio(funcoes[linha], resultados, coluna)

    def eixoX(self):
        return self.resultados[-1]
