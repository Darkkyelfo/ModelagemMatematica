from funcoes import FuncaoModelo
from metodos_numericos import EulerExplicito, Newton
import matplotlib.pyplot as plt

metodoEulerExp = EulerExplicito()
metodoNewton = Newton()

# Questão 1
funcao1 = FuncaoModelo("e**x - 2", ["x"], derivada="e**x")

x, iteracoes = metodoNewton.zeroFx(0, funcao1, 0.01)
print("valor de x para f(x) = 0 é aproximademente: %s.\nQuantidade de iteracoes:%s" % (x, iteracoes))

# Questão 2

funcao2 = FuncaoModelo("-x**3", ["x"])
funcaoExata = FuncaoModelo("1/(2*x+1)**(1/2)", ["x"])
metodoEulerExp.solucionar([funcao2], [1, 0], 0.1, 5)
resultadoExato = []
for x in metodoEulerExp.eixoX():
    resultadoExato.append(funcaoExata.getValorFuncao([x]))
plt.plot(metodoEulerExp.eixoX(),resultadoExato)
plt.plot(metodoEulerExp.eixoX(), metodoEulerExp.resultados[0], "o", markersize=2)
plt.show()
