from tkinter import *

ModificarExpediente=Tk()
ModificarExpediente.title("Modificación de expedientes")
ModificarExpediente.geometry("800x550")
ModificarExpediente.resizable(0,0)
Label(ModificarExpediente,text="¿Qué desea modificar?",font=("Arial Bold",18), justify=CENTER).place(x=260,y=55)
recetabutton = Button(ModificarExpediente, text="Agregar receta")
recetabutton.place(x=140,y=200)
padecimientobutton = Button(ModificarExpediente, text="Agregar padecimiento")
padecimientobutton.place(x=325,y=200)
alturabutton = Button(ModificarExpediente, text="Cambiar altura o peso")
alturabutton.place(x=545,y=200)
Label(ModificarExpediente,text="*Por favor darle al boton para guardar los cambios",font=(8)).place(x=434,y=470)
volverMenuDoctores=Button(ModificarExpediente,text="Volver al Menu de doctores").place(x=634,y=510)
ModificarExpediente.mainloop()

