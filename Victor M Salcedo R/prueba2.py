import numpy as np
import matplotlib.pyplot as plt

# Valores de x entre 0 y 1 (en radianes)
x = np.linspace(0, 1, 200)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Gráfica de sin(x) de 0 a 1")
plt.grid(True)
plt.show()