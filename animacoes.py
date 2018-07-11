import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import matplotlib.patches as patches

class AnimacaoQuadrado(object):

    def __init__(self, resultados, xmax=10, xmin=-10, ymax=10, ymin=-10):

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim(xmin, xmax)
        self.ax.set_ylim(ymin, ymax)

        self.resultados = resultados
        self.quadrado = np.zeros((4, 2))
        for linha in range(4):
            if (linha % 2 == 0):
                self.quadrado[linha][0] = self.resultados[0] - 0.5 if linha ==0 else self.resultados[0] + 0.5
                self.quadrado[linha][1] = 0 if linha == 0 else 1
            else:
                self.quadrado[linha][0] = self.resultados[0] + 0.5 if linha == 1 else self.resultados[0] - 0.5
                self.quadrado[linha][1] = 0 if linha == 1 else 1
        # self.quadrado =  np.array([[4.5, 0], [5.5, 0], [5.5, 1], [4.5, 1]])
        # print(self.quadrado)

        self.go = patches.Polygon(self.quadrado, closed=True, fc='r', ec='r')
        self.patch = self.ax.add_patch(self.go)


    def init(self):
        return self.patch,

    def animate(self, i):
        self.quadrado[:, 0] += i / 2
        self.go.set_xy(self.quadrado)
        self.patch = self.ax.add_patch(self.go)
        return self.patch,

    def executar(self):
        return animation.FuncAnimation(self.fig, self.animate, self.resultados, init_func=self.init,
                                      interval=1000, blit=True)
        # plt.show()

# xmax = 10
# xmin = -10
# ymax = 10
# ymin = -10
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_xlim(xmin, xmax)
# ax.set_ylim(ymin, ymax)
#
# resultados = np.arange(1, 5)
# quadrado = np.zeros((4, 2))
# for linha in range(4):
#     if (linha % 2 == 0):
#         quadrado[linha][0] = resultados[0] - 0.5 if linha == 0 else resultados[0] + 0.5
#         quadrado[linha][1] = 0 if linha == 0 else 1
#     else:
#         quadrado[linha][0] = resultados[0] + 0.5 if linha == 1 else resultados[0] - 0.5
#         quadrado[linha][1] = 0 if linha == 1 else 1
#
#
# go = patches.Polygon(quadrado, closed=True, fc='r', ec='r')
# patch = ax.add_patch(go)
#
#
# def init():
#     return patch,
#
#
# def animate(i):
#     quadrado[:, 0] += i
#     go.set_xy(quadrado)
#     patch = ax.add_patch(go)
#     return patch,
#
#
# ani = animation.FuncAnimation(fig, animate, resultados, init_func=init,
#                               interval=1000, blit=True)
# plt.show()

a = AnimacaoQuadrado(np.arange(1,8))
ani = a.executar()
plt.show()