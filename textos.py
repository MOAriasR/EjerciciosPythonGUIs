from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
root=tb.Window(themename='superhero')
root.title("Ejercicios de bootstrap")
root.iconbitmap('fx.ico')

root.title('PRACTICA DE LABELS Y BUTTONS')
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

btnenviar=tb.Button(text='Enviar',bootstyle='success, outline',command=changer)
btnenviar.pack(pady=10)

chkInteresado=tb.Checkbutton(root,text='Interesado?',bootstyle="info", variable=var1,
    onvalue=1,offvalue=0,command=checker)
chkInteresado.pack(pady=10)




root.bind('<Escape>', lambda e: root.destroy())


root.mainloop()