from tkinter import *

ModificarExpediente=Tk()
ModificarExpediente.title("Menu para modificar expedientes")
ModificarExpediente.geometry("800x550")
ModificarExpediente.resizable(0,0)

Label(ModificarExpediente,text="Registro de expedientes",font=("Arial",16,"bold","italic"), justify=CENTER).place(x=280,y=55)

ingresoCedulaModificar = Label(ModificarExpediente,text="Ingrese el número de cédula del paciente",font=(14)).place(x=5,y=120)
cedulaModificar=Entry(ModificarExpediente)
cedulaModificar.place(x=300,y=124)


def presionar():
    
    Label(ModificarExpediente,text="Que desea modificar",font=("Arial",16,"italic"), justify=CENTER).place(x=287,y=285)
    
    agregarPadecimiento=Button(ModificarExpediente,text="Agregar un padecimiento") 
    agregarPadecimiento.place(x=50,y=360)

    agregarReceta=Button(ModificarExpediente,text="Agregar un padecimiento") 
    agregarReceta.place(x=315,y=360)
    
    AlturaPeso=Button(ModificarExpediente,text="Agregar un padecimiento") 
    AlturaPeso.place(x=613,y=360)
   


botonModificar=Button(ModificarExpediente,text="Haz click aquí",command=presionar) 
botonModificar.place(x=20,y=190)
Label(ModificarExpediente,text="*Por favor darle al boton una vez haya terminado",font=(14)).place(x=130,y=190)


volverMenuDoctores=Button(ModificarExpediente,text="Volver al Menu de doctores").place(x=634,y=510)

ModificarExpediente.mainloop()