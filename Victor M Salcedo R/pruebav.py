import tkinter as tk

ANCHO = 600
ALTO = 400
ESCALA = 30

ventana = tk.Tk()
ventana.title("Gráfica de y = x²")

grafica = tk.Canvas(ventana, width=ANCHO, height=ALTO, bg="white")
grafica.pack(padx=10, pady=10)

centro_x = ANCHO // 2
centro_y = ALTO - 40

# Ejes coordenados
grafica.create_line(30, centro_y, ANCHO - 20, centro_y, fill="black", arrow=tk.LAST)
grafica.create_line(centro_x, ALTO - 20, centro_x, 20, fill="black", arrow=tk.LAST)
grafica.create_text(ANCHO - 30, centro_y - 15, text="x")
grafica.create_text(centro_x + 15, 25, text="y")

# Dibuja y = x² usando puntos conectados.
puntos = []
for paso in range(-100, 101):
    x = paso / 10
    y = x**2
    px = centro_x + x * ESCALA
    py = centro_y - y * ESCALA
    puntos.extend((px, py))

grafica.create_line(*puntos, fill="blue", width=2, smooth=True)
grafica.create_text(centro_x + 10, centro_y + 20, text="0")
grafica.create_text(ANCHO // 2, 10, text="Gráfica de y = x²", anchor=tk.N)

ventana.mainloop()