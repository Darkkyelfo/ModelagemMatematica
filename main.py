from funcoes import FuncaoModelo
from metodos_numericos import EulerExplicito, Newton

metodoEulerExp = EulerExplicito()
metodoNewton = Newton()

# Questão 1
# funcao1 = FuncaoModelo("e**x - 2",["x"],derivada="e**x")
#
# x, iteracoes = metodoNewton.zeroFx(0, funcao1, 0.01)
# print("valor de x para f(x) = 0 é aproximademente: %s.\nQuantidade de iteracoes:%s" % (x, iteracoes))

#Questão 2

funcao2 = FuncaoModelo("e**(-x)-2*y",["x","y"])

metodoEulerExp.solucionar([funcao2],[0,3],0,0.001,3)

