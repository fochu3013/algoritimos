import random
import math
import numpy as np
import matplotlib.pyplot as plt

def integrand(x):
    return math.sqrt(x**2 + 1)

def monte_carlo_integral(num_points):
    integral_sum = 0

    for _ in range(num_points):
        x = random.uniform(0, 1)
        integral_sum += integrand(x)

    approximation = (integral_sum / num_points) 

    return approximation


num_points_100 = 100
num_points_1000 = 1000


approximation_100 = monte_carlo_integral(num_points_100)
approximation_1000 = monte_carlo_integral(num_points_1000)

print(f"Aproximação para {num_points_100} pontos: {approximation_100}")
print(f"Aproximação para {num_points_1000} pontos: {approximation_1000}")

plt.figure(figsize=(6, 4))


x_values = np.linspace(0, 1, 1000)
y_values = [integrand(x) for x in x_values]

plt.subplot(1, 2, 1)
plt.scatter(np.random.rand(num_points_100), [integrand(random.uniform(0, 1)) for _ in range(num_points_100)], color='blue', s=10)
plt.plot(x_values, y_values, color='red', label='Integral Exata')
plt.title(f'Valores gerados e Integral Exata ({num_points_100} pontos)')
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(np.random.rand(num_points_1000), [integrand(random.uniform(0, 1)) for _ in range(num_points_1000)], color='green', s=10)
plt.plot(x_values, y_values, color='red', label='Integral Exata')
plt.title(f'Valores gerados e Integral Exata ({num_points_1000} pontos)')
plt.legend()

plt.tight_layout()
plt.show()
