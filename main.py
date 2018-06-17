from funcoes import FuncaoModelo
from metodos_numericos import EulerExplicito, Newton, RungeKutta
import matplotlib.pyplot as plt

metodoEulerExp = EulerExplicito()
metodoNewton = Newton()
rungeKutta = RungeKutta()

# Questão 1
funcao1 = FuncaoModelo("e**x - 2", ["x"], derivada="e**x")

x, iteracoes = metodoNewton.zeroFx(0, funcao1, 0.01)
print("valor de x para f(x) = 0 é aproximademente: %s.\nQuantidade de iteracoes:%s" % (x, iteracoes))

# Questão 2

funcao2 = FuncaoModelo("e**(-x)-2*y", ["y", 'x'])
funcaoExata = FuncaoModelo("e**(-x)+2*e**(-2*x)", ["x"])
metodoEulerExp.solucionar([funcao2], [3, 0], 0.001, 3)
rungeKutta.solucionar([funcao2], [3, 0], 0.001, 3)
resultadoExato = []
for x in metodoEulerExp.eixoX():
    resultadoExato.append(funcaoExata.getValorFuncao([x]))
plt.plot(metodoEulerExp.eixoX(), resultadoExato,color='red',label='Analitico')
plt.plot(metodoEulerExp.eixoX(), metodoEulerExp.resultados[0], color='blue', label="Euler")
plt.plot(rungeKutta.eixoX(), rungeKutta.resultados[0], color='green', label="RungeKutta")
plt.legend(loc='upper right', frameon=False)
plt.show()

# Questão 3

funcao1 = FuncaoModelo("-0.16*x+0.08*x*y", ["x", 'y'])
funcao2 = FuncaoModelo("4.5*y - 0.9*x*y", ["x", 'y'])
funcoes = [funcao1, funcao2]
metodoEulerExp.solucionar(funcoes, [4, 4, 0], 0.001, 16)
rungeKutta.solucionar(funcoes, [4, 4, 0], 0.001, 16)
plt.plot(metodoEulerExp.eixoX(), metodoEulerExp.resultados[0], color='blue', label="Euler")
plt.plot(rungeKutta.eixoX(), rungeKutta.resultados[0], color='green', label="RungeKutta")
plt.legend(loc='upper right', frameon=False)
plt.show()
plt.plot(metodoEulerExp.eixoX(), metodoEulerExp.resultados[1], color='blue', label="Euler")
plt.plot(rungeKutta.eixoX(), rungeKutta.resultados[1], color='green', label="RungeKutta")
plt.legend(loc='upper right', frameon=False)
plt.show()