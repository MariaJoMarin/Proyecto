from tkinter import *

CrearExpediente=Tk()
CrearExpediente.title("Menu para crear expedientes")
CrearExpediente.geometry("800x550")
CrearExpediente.resizable(0,0)

informacion=Label(CrearExpediente,text="INFORMACION DEL NUEVO PACIENTE",font=("Arial",16,"bold","italic"), justify=CENTER).place(x=210,y=55)

ingresoCedulaNuevo = Label(CrearExpediente,text="Ingrese el número de cédula del paciente del que se va a crear el expediente",font=(14)).place(x=5,y=120)
nuevaCedula=Entry(CrearExpediente)
nuevaCedula.place(x=550,y=124)

ingresoNombreNuevo = Label(CrearExpediente,text="Ingrese el nombre completo del paciente",font=(14)).place(x=5,y=170)
nuevoNombre=Entry(CrearExpediente)
nuevoNombre.place(x=300,y=174)

ingresoEdad = Label(CrearExpediente,text="Ingrese la edad del paciente",font=(14)).place(x=5,y=220)
nuevaEdad=Entry(CrearExpediente)
nuevaEdad.place(x=215,y=224)

registroInformacion=Label(CrearExpediente,text="Información resgristrada",font=("Arial",16,"bold","italic"), justify=CENTER).place(x=260,y=310)


cedula=Label(CrearExpediente)
cedula.place(x=435,y=353)

nombre=Label(CrearExpediente)
nombre.place(x=432,y=402)

edad=Label(CrearExpediente)
edad.place(x=351,y=452)

def presionar():
    txt1=nuevaCedula.get()
    txt2=nuevoNombre.get()
    txt3=nuevaEdad.get()

    Label(CrearExpediente,text="El número de cedula ingresado es:",font=(14), justify=CENTER).place(x=190,y=350)
    cedula.config(text=txt1)
    Label(CrearExpediente,text="El nombre completo ingresado es:",font=(14), justify=CENTER).place(x=190,y=400)
    nombre.config(text=txt2)
    Label(CrearExpediente,text="La edad ingresada es:",font=(14), justify=CENTER).place(x=190,y=450)
    edad.config(text=txt3)


botonCrear=Button(CrearExpediente,text="Haz click aquí",command=presionar) 
botonCrear.place(x=20,y=270)
Label(CrearExpediente,text="*Por favor darle al boton una vez haya terminado",font=(14)).place(x=130,y=270)


CerrarSecion=Button(CrearExpediente,text="Volver al Menu de doctores").place(x=634,y=510)

CrearExpediente.mainloop()
