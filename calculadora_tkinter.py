import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera claculadora")
ventana.geometry("400x300")

etiqueta1 = tk.Label(ventana, text="Calculadora")
etiqueta1.pack(pady=5)

entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)

entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

def sumar():
    num1 = int(entrada1.get())
    num2 = int(entrada2.get())
    etiqueta1.config(text=f"La suma de los dos números es de:{num1+num2}")

def restar():
    num1 = int(entrada1.get())
    num2 = int(entrada2.get())
    etiqueta1.config(text=f"La suma de los dos números es de:{num1 - num2}")

def multiplicar():
    num1 = int(entrada1.get())
    num2 = int(entrada2.get())
    etiqueta1.config(text=f"La suma de los dos números es de:{num1 * num2}")

def dividir():
    num1 = int(entrada1.get())
    num2 = int(entrada2.get())
    etiqueta1.config(text=f"La suma de los dos números es de:{num1 / num2}")

def limpiar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    etiqueta1.config(text="Calculadora")

boton_sumar = tk.Button(ventana, text="Suma", command=sumar)
boton_sumar.pack(pady=5)

boton_restar = tk.Button(ventana, text="Resta", command=restar)
boton_restar.pack(pady=5)

boton_multi = tk.Button(ventana, text="Multiplicación", command=multiplicar)
boton_multi.pack(pady=5)

boton_div = tk.Button(ventana, text="División", command=dividir)
boton_div.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=5)

ventana.mainloop()