from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from datetime import datetime as dt

root=tb.Window(themename='superhero')
root.title("Ejercicios de bootstrap")


root.title("Comboboxes' secrets")
root.iconbitmap('fx.ico')
root.geometry('500x350')
lblSaludo=tb.Label(root,text='Saludo',font=('Helvetica',18), bootstyle="info")
lblSaludo.pack(pady=10)
counter=0
var1=IntVar()
def changer():
    global counter
    counter += 1
    if counter % 2 == 0:
        lblSaludo.config(text='Hola Mundo!')
    else:
        lblSaludo.config(text='Adiós mundo cruel!')

def checker():
    if var1.get()==1:
         lblSaludo.config(text='Interesado')
    else:
         lblSaludo.config(text='No Interesado')

# Lista de días de la semana
dias_semana = [
    "Lunes",
    "Martes", 
    "Miércoles",
    "Jueves",
    "Viernes",
    "Sábado",
    "Domingo"
]

# Lista de meses del año
meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
]
varx=StringVar()
cbomeses=tb.Combobox(root,values=meses)
cbomeses.pack(pady=10)
cbomeses.current(dt.now().month-1)

diasem=dt.now().weekday
cbodiasem=tb.Combobox(root,values=dias_semana)
cbodiasem.pack(pady=10)
cbodiasem.current(5)



btnenviar=tb.Button(text='Enviar',bootstyle='success, outline',command=changer)
btnenviar.pack(pady=10)






root.bind('<Escape>', lambda e: root.destroy())


root.mainloop()