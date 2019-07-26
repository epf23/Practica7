from tkinter import *
import sys

argument = str(sys.argv[1])
correctArg = argument.replace(']','').replace('[','').replace("'", "")


window = Tk()
window.title('Programa B')
window.geometry("1280x720")

L1 = Label(window, text='El ID ingresado fue:')
L1.grid(row=4, column=0)
L2 = Label(window, text=correctArg)
L2.grid(row=5, column=0)

if correctArg == "40215742756":
    seleccion = 1
elif correctArg == "40209553001":
    seleccion = 2
elif correctArg == "40209553002":
    seleccion = 3
elif correctArg == "40209553003":
    seleccion = 4
elif correctArg == "40209553004":
    seleccion = 5
else:
    seleccion = 6

L3 = Label(window, text='Su imagen correspondiente es:')
L3.grid(row=6, column=0)

canv = Canvas(window, width=1280, height=720, bg='white')
canv.grid(row=7, column=0)

img = PhotoImage(file="Facturas/Factura"+str(seleccion)+".gif")
canv.create_image(20,20, anchor=NW, image=img)

window.mainloop()
