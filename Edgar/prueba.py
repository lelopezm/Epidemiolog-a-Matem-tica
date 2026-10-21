import matplotlib.pyplot as plt


x_values = [x / 10 for x in range(-100, 101)]
y_values = [x**2 for x in x_values]

plt.plot(x_values, y_values, label="y = x^2")
plt.title("Gráfica de y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()