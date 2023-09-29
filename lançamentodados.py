#gabriel fischer domakoski

import numpy as np

def calcular_probabilidade(N):
    Eventos = 0
    
    for i in range(N):
        x = np.random.randint(1, 7, size=4)
        y = np.where(x == 6)[0]
        
        if len(y) == 1 and y[0] == 3:
            Eventos += 1
    
    prob = Eventos / N
    return prob

N = 4
probabilidade = calcular_probabilidade(N)
print("Probabilidade:", probabilidade)
