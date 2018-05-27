import matplotlib.pyplot as plt


class EulerExplicito(object):

    def solucionar(self, funcaoPVI, h, xmin, xmax):
        self.xmin = xmin
        self.xmax = xmax
        self.h = h
        self.funcaoPVI = funcaoPVI
        u = funcaoPVI.pvi
        t = xmin
        self.x = [t]
        self.y = [u]
        while t <= xmax:
            u = u + self.h * self.funcaoPVI.getValor([u])
            t = self.h + t
            self.x.append(t)
            self.y.append(u)

    def gerarGrafico(self):
        valoresReais = []
        for x in self.x:
            valoresReais.append(self.funcaoPVI.getValorAnalitico([x]))
        plt.plot(self.x, valoresReais)
        plt.plot(self.x, self.y,"o",markersize=2)
        plt.show()

