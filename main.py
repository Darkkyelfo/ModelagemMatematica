from funcoes import FuncaoBasica
from metodos_numericos import EulerExplicito, Newton, RungeKutta, np
import matplotlib.pyplot as plt

metodoEulerExp = EulerExplicito()
metodoNewton = Newton()
rungeKutta = RungeKutta()


class FuncaoB1(FuncaoBasica):
    def getValorFuncao(self, valores):
        return np.power(np.e, valores[0]) - 2

    def getValorDerivada(self, valores):
        return np.power(np.e, valores[0])


class FuncaoB2(FuncaoBasica):
    def getValorFuncao(self, valores):
        return np.e ** (-valores[1]) - 2 * valores[0]

    def getValorDerivada(self, valores):
        return 0


class FuncaoB2Exata(FuncaoBasica):
    def getValorFuncao(self, valores):
        return np.e ** (-valores[0]) + 2 * np.e ** (-2 * valores[0])

    def getValorDerivada(self, valores):
        return 0


class FuncaoB3(FuncaoBasica):
    def getValorFuncao(self, valores):
        return -0.16 * valores[0] + 0.08 * valores[0] * valores[1]

    def getValorDerivada(self, valores):
        return 0


class FuncaB4(FuncaoBasica):
    def getValorFuncao(self, valores):
        return 4.5 * valores[1] - 0.9 * valores[0] * valores[1]

    def getValorDerivada(self, valores):
        return 0


class massaMolaVelocidade(FuncaoBasica):
    def getValorFuncao(self, valores):
        return valores[1]

    def getValorDerivada(self, valores):
        return 0


class massaMolaAceleracao(FuncaoBasica):
    def getValorFuncao(self, valores):
        k = 5000
        m = 2
        L = 3
        return -k / m * (valores[0] - L)

    def getValorDerivada(self, valores):
        return 0


class MassaMolaAtritoAceleracao(FuncaoBasica):
    def getValorFuncao(self, valores):
        k = 5000
        m = 2
        L = 3
        u = 0.8
        N = 10
        return (-k * (valores[0] - L) - u * N*valores[1]) / m


if __name__ == '__main__':
    # Questão 1
    funcao1 = FuncaoB1()

    x, iteracoes = metodoNewton.zeroFx(0.8, funcao1, 0.01)
    print("valor de x para f(x) = 0 é aproximademente: %s.\nQuantidade de iteracoes:%s" % (x, iteracoes))

    # # Questão 2

    funcao2 = FuncaoB2()
    funcaoExata = FuncaoB2Exata()
    metodoEulerExp.solucionar([funcao2], [3, 0], 0.001, 3)
    rungeKutta.solucionar([funcao2], [3, 0], 0.001, 3)
    resultadoExato = []
    resultadoExatoR = []

    for x in metodoEulerExp.eixoX():
        resultadoExato.append(funcaoExata.getValorFuncao([x]))
    for x in rungeKutta.eixoX():
        resultadoExatoR.append(funcaoExata.getValorFuncao([x]))

    plt.figure(0)
    plt.plot(metodoEulerExp.eixoX(), resultadoExato, color='red', label='Analítico-Euler')
    plt.plot(rungeKutta.eixoX(), resultadoExatoR, color='yellow', label='Analítico-Kutta')
    plt.plot(metodoEulerExp.eixoX(), metodoEulerExp.resultados[0], color='blue', label="Euler")
    plt.plot(rungeKutta.eixoX(), rungeKutta.resultados[0], color='green', label="RungeKutta")
    plt.legend(loc='upper right', frameon=False)
    plt.show()

    # # Questão 3
    #
    funcao1 = FuncaoB3()
    funcao2 = FuncaB4()
    funcoes = [funcao1, funcao2]
    metodoEulerExp.solucionar(funcoes, [4, 4, 0], 0.001, 16)
    rungeKutta.solucionar(funcoes, [4, 4, 0], 0.001, 16)
    plt.figure(1)
    plt.plot(metodoEulerExp.eixoX(), metodoEulerExp.resultados[0], color='blue', label="Euler")
    plt.plot(rungeKutta.eixoX(), rungeKutta.resultados[0], color='red', label="RungeKutta")
    plt.legend(loc='upper right', frameon=False)
    plt.plot(metodoEulerExp.eixoX(), metodoEulerExp.resultados[1], color='blue', label="Euler")
    plt.plot(rungeKutta.eixoX(), rungeKutta.resultados[1], color='red', label="RungeKutta")
    plt.legend(loc='upper right', frameon=False)
    plt.show()

    # massa mola
    massaMola1 = massaMolaVelocidade()
    massaMola2 = massaMolaAceleracao()
    funcoes = [massaMola1, massaMola2]
    rungeKutta.solucionar(funcoes, [5, 0, 0], 0.001, 0.5)
    plt.figure(2)
    plt.plot(rungeKutta.eixoX(), rungeKutta.resultados[0], color='green', label="RungeKutta")
    plt.show()
    plt.figure(3)
    plt.plot(rungeKutta.eixoX(), rungeKutta.resultados[1], color='red', label="RungeKutta")
    plt.show()

    # massa mola com atrito
    massaMola1 = massaMolaVelocidade()
    massaMola2 = MassaMolaAtritoAceleracao()
    funcoes = [massaMola1, massaMola2]
    rungeKutta.solucionar(funcoes, [5, 0, 0], 0.001, 0.5)
    plt.figure(4)
    plt.plot(rungeKutta.eixoX(), rungeKutta.resultados[0], color='green', label="RungeKutta")
    plt.show()
    plt.figure(5)
    plt.plot(rungeKutta.eixoX(), rungeKutta.resultados[1], color='red', label="RungeKutta")
    plt.show()
    print("final")
