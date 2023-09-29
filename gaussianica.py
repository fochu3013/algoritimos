import random
import math

def myrand():
    return random.random()

def SPTINIK(m, s):
    p0, q0 = 0.322232431088, 0.099348462606
    p1, q1 = 1.0, 0.588581570495
    p2, q2 = 0.342242088547, 0.531103462366
    p3, q3 = 0.204231210245e-1, 0.103537752850
    p4, q4 = 0.453642210148e-4, 0.385607006340e-2

    u = myrand()
    print('U = ', round(u,5), end='')
    if u < 0.5:
        t = math.sqrt(-2.0 * math.log(u))
    else:
        t = math.sqrt(-2.0 * math.log(1.0 - u))

    p = p0 + t * (p1 + t * (p2 + t * (p3 + t * p4)))
    q = q0 + t * (q1 + t * (q2 + t * (q3 + t * q4)))
    if u < 0.5:
        z = (p / q) - t
    else:
        z = t - (p / q)
    return (m + s * z)

# gera 10 números aleatórios com distribuição normal padrão (média 0, desvio padrão 1)
print("Gera 10 números aleatórios com distribuição normal padrão (média 0, desvio padrão 1)\n")
for i in range(10):
    print(" e Numero = ", round(SPTINIK(0, 1),5))
