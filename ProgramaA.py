from tkinter import *

window = Tk()
window.title('Programa A')
window.geometry("400x200")

#No. Factura
L1 = Label(window, text='No. Factura')
L1.grid(row=3, column=0)
var1 = str()
textbox1 = Entry(window, textvariable=var1)
textbox1.grid(row=3, column=1)
textbox1.focus_set()

#ID Cliente
L2 = Label(window, text='ID Cliente')
L2.grid(row=4, column=0)
var2 = str()
textbox2 = Entry(window, textvariable=var2)
textbox2.grid(row=4, column=1)
textbox2.focus_set()

#Fecha Factura
L3 = Label(window, text='Fecha Factura')
L3.grid(row=5, column=0)
var3 = str()
textbox3 = Entry(window, textvariable=var3)
textbox3.grid(row=5, column=1)
textbox3.focus_set()

#Monto
L4 = Label(window, text='Monto')
L4.grid(row=6, column=0)
var4 = str()
textbox4 = Entry(window, textvariable=var4)
textbox4.grid(row=6, column=1)
textbox4.focus_set()

#Estado
L5 = Label(window, text='Estado')
L5.grid(row=7, column=0)
var5 = str()
textbox5 = Entry(window, textvariable=var5)
textbox5.grid(row=7, column=1)
textbox5.focus_set()

#Condiciones
L6 = Label(window, text='Condiciones')
L6.grid(row=8, column=0)
var6 = str()
textbox6 = Entry(window, textvariable=var6)
textbox6.grid(row=8, column=1)
textbox6.focus_set()

def escribir():
    fh = open("factura.txt", "w")
    datos = textbox1.get()+","+textbox2.get()+","+textbox3.get()+","+textbox4.get()+","+textbox5.get()+","+textbox6.get()
    print(datos)
    fh.write(datos)
    fh.close()


b = Button(window, text="Ingresar", command=escribir)
b.grid(row= 15, column= 0)
window.mainloop()
