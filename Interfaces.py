from tkinter import *
import cmath

temFrame = Tk()

temFrame.title("Calculos")
temFrame.geometry("1000x400")
temFrame.config(bg="blue")

temFrame = Frame(temFrame, width=1600, height=600)
temFrame.pack()

num_pant01R = StringVar()
num_pant01I = StringVar()
num_pant02R = StringVar()
num_pant01I = StringVar()

dato= globals()
def captnum01():
    dato = getdouble(num_pant01R.get())
    print("dato1", dato)
    multi = dato + dato
    print("mult", multi)
    return dato, multi
N01label = Label(temFrame, text="Impedancia de Carga", padx=10, pady=5)
N01label.grid(row=0, column=0)
N01caja = Entry(temFrame, textvariable=num_pant01R)
N01caja.grid(row=0, column=1)
N01label = Label(temFrame, text="Real", padx=10, pady=5)
N01label.grid(row=0, column=2)
N01boton = Button(temFrame, text="ingresar", padx=30, pady=10,command=captnum01)
N01boton.grid(row=0, column=3)
N01caja = Entry(temFrame, textvariable=num_pant01I)
N01caja.grid(row=0, column=4)
N01label = Label(temFrame, text="j  Imaginario", padx=10, pady=10)
N01label.grid(row=0, column=5)
N01boton = Button(temFrame, text="ingresar", padx=30, pady=10,command=captnum01)
N01boton.grid(row=0, column=6)
dato1 = captnum01()
N01label = Label(temFrame, text="Valor Digitado", dato1, padx=10, pady=5)
N01label.grid(row=0, column=7)





N02caja = Entry(temFrame)
N02caja.grid(row=1, column=1)
N02label = Label(temFrame, text="Impedancia del Caracteristica", padx=5, pady=5)
N02label.grid(row=1, column=0)

N031caja = Entry(temFrame)
N031caja.grid(row=2, column=1)
N03label = Label(temFrame, text="Frecuencia de Operacion", padx=5, pady=5)
N03label.grid(row=2, column=0)


temFrame.mainloop()
