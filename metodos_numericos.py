import sys
import numpy as np


# class EulerExplicito(object):
#
#     def solucionar(self, funcaoPVI, h, xmin, xmax):
#         self.xmin = xmin
#         self.xmax = xmax
#         self.h = h
#         self.funcaoPVI = funcaoPVI
#         u = funcaoPVI.pvi
#         t = xmin
#         self.x = [t]
#         self.y = [u]
#         while t <= xmax:
#             u = u + self.h * self.funcaoPVI.getValor([u])
#             t = self.h + t
#             self.x.append(t)
#             self.y.append(u)
#
#     def gerarGrafico(self):
#         valoresReais = []
#         for x in self.x:
#             valoresReais.append(self.funcaoPVI.getValorAnalitico([x]))
#         plt.plot(self.x, valoresReais)
#         plt.plot(self.x, self.y, "o", markersize=2)
#         plt.show()


class EulerExplicito(object):

    def solucionar(self, funcoes, h, tmin, tmax):
        self.tmin = tmin
        self.tmax = tmax
        self.h = h
        self.ts = [self.tmin]
        self.resultados = []

        t = self.tmin

        for edo in funcoes:
            self.resultados.append([edo.getValorInicial()])

        while t <= tmax:
            for i, func in enumerate(funcoes):
                r = self.resultados[i]
                r.append(r[-1] + self.h * func.getValorFuncao(np.array(self.resultados)[:, -1]))
                t = self.h + t
                self.ts.append(t)

class Newton(object):

    def zeroFx(self,x0, funcao, e):
        xk = x0
        iteracoes = 0
        erro = sys.maxsize
        while erro >= e:
            xkant = xk
            xk = xk - (funcao.getValorFuncao([xk]) / funcao.getValorDerivada([xk]))
            erro = np.fabs(xk - xkant)
            iteracoes = iteracoes + 1
        return xk, iteracoes
