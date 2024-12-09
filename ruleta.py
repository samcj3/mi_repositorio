import tkinter as tk
import random
import time
def obtener_color(numero):
    if numero == 0:
        return "green"
    rojos = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
    return "red" if numero in rojos else "black"
def animacion_ruleta(numero_final):
    for _ in range(15):  
        numero_random = random.randint(0, 36)
        color_random = obtener_color(numero_random)
        resultado_label.config(text=f"{numero_random}", bg=color_random)
        ventana.update()
        time.sleep(0.05)  
    resultado_label.config(text=f"{numero_final}", bg=obtener_color(numero_final))
def girar_ruleta():
    numero = random.randint(0, 36)
    animacion_ruleta(numero)  
    color = obtener_color(numero)
    apuesta = apuesta_var.get()
    if color == apuesta:
        mensaje_label.config(text="¡Ganaste!", fg="green")
    elif color == "green":
        mensaje_label.config(text="Salió 0, ¡la casa gana!", fg="orange")
    else:
        mensaje_label.config(text="Perdiste", fg="red")
ventana = tk.Tk()
ventana.title("Ruleta")
ventana.geometry("300x300")
ventana.config(bg="#333")  
resultado_label = tk.Label(
    ventana, text="", font=("Helvetica", 28, "bold"), width=6, height=3,
    relief="solid", bd=2, bg="#222", fg="white", justify="center"
)
resultado_label.pack(pady=10)
girar_button = tk.Button(
    ventana, text="Girar Ruleta", command=girar_ruleta,
    font=("Helvetica", 14, "bold"), bg="#007acc", fg="white",
    relief="raised", bd=3, width=15
)
girar_button.pack(pady=10)
apuesta_frame = tk.LabelFrame(
    ventana, text="Elige tu apuesta", font=("Helvetica", 12),
    bg="#333", fg="white", bd=3, relief="ridge", padx=10, pady=10
)
apuesta_frame.pack(pady=5)
apuesta_var = tk.StringVar(value="red")
tk.Radiobutton(apuesta_frame, text="Rojo", variable=apuesta_var, value="red", 
               font=("Helvetica", 10), bg="#333", fg="red", selectcolor="black").pack(anchor="w")
tk.Radiobutton(apuesta_frame, text="Negro", variable=apuesta_var, value="black", 
               font=("Helvetica", 10), bg="#333", fg="black", selectcolor="black").pack(anchor="w")
mensaje_label = tk.Label(
    ventana, text="", font=("Helvetica", 14, "bold"), bg="#333", fg="white"
)
mensaje_label.pack(pady=10)

ventana.mainloop()
