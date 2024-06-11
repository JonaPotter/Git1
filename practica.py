from tkinter import *
from tkinter import PhotoImage

# Crear la ventana principal
ventana = Tk()
ventana.title("Gamer-Gang")
ventana.resizable(True, True)
ventana.geometry("650x350")
ventana.config(bg="black")

# Cargar la imagen del cursor
cursor_image = PhotoImage(file="cursor.png")

# Crear un label transparente para mostrar la imagen del cursor
label = Label(ventana, image=cursor_image, bg="black")
label.place(x=0, y=0, relwidth=1, relheight=1)

# Actualizar la posición del label para que siga al cursor
def follow_cursor(event):
    label.place(x=event.x, y=event.y)

ventana.bind('<Motion>', follow_cursor)

# Iniciar el bucle principal de la ventana
ventana.mainloop()



