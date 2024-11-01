from tkinter import *
ventana=Tk()
ventana.geometry('300x300')
ventana.title('Mi ventana')
#ventana.iconbitmap('icono.ico')
ventana.resizable(0,0) # no modificar tamaño ni horizontal ni vertical
marco=Frame(ventana, width=300, height=260)
marco.pack()


ventana.mainloop()



  