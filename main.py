from metodos_numericos import EulerExplicito
from funcoes import funcao1

metodoEuler = EulerExplicito()
f1 = funcao1()
metodoEuler.solucionar(f1, 0.1, 0, 5)
metodoEuler.gerarGrafico()
