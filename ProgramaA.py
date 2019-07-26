from tkinter import *

window = Tk()
window.title('Programa A')
window.geometry("400x200")

#No. Factura
L1 = Label(window, text='No. Factura')
L1.grid(row=3, column=0)
var1 = str()
NFactura = Entry(window, textvariable=var1)
NFactura.grid(row=3, column=1)
NFactura.focus_set()

#ID Cliente
L2 = Label(window, text='ID Cliente')
L2.grid(row=4, column=0)
var2 = str()
IDCliente = Entry(window, textvariable=var2)
IDCliente.grid(row=4, column=1)
IDCliente.focus_set()

#Fecha Factura
L3 = Label(window, text='Fecha Factura')
L3.grid(row=5, column=0)
var3 = str()
FFactura = Entry(window, textvariable=var3)
FFactura.grid(row=5, column=1)
FFactura.focus_set()

#Monto
L4 = Label(window, text='Monto')
L4.grid(row=6, column=0)
var4 = str()
Monto = Entry(window, textvariable=var4)
Monto.grid(row=6, column=1)
Monto.focus_set()

#Estado
L5 = Label(window, text='Estado')
L5.grid(row=7, column=0)
var5 = str()
Estado = Entry(window, textvariable=var5)
Estado.grid(row=7, column=1)
Estado.focus_set()

#Condiciones
L6 = Label(window, text='Condiciones')
L6.grid(row=8, column=0)
var6 = str()
Condiciones = Entry(window, textvariable=var6)
Condiciones.grid(row=8, column=1)
Condiciones.focus_set()

def escribir():
    fh = open("factura.txt", "w")
    datos = NFactura.get()+","+IDCliente.get()+","+FFactura.get()+","+Monto.get()+","+Estado.get()+","+Condiciones.get()
    print(datos)
    fh.write(datos)
    fh.close()


b = Button(window, text="Ingresar", command=escribir)
b.grid(row= 15, column= 0)
window.mainloop()
