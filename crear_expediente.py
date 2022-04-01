from tkinter import *

CrearExpedinte=Tk()
CrearExpedinte.title("Menu para crear expedientes")
CrearExpedinte.geometry("800x550")
CrearExpedinte.resizable(0,0)

informacion=Label(CrearExpedinte,text="INFORMACION DEL NUEVO PACIENTE",font=("Arial",16,"bold","italic"), justify=CENTER).place(x=210,y=55)

ingresoCedulaNuevo = Label(CrearExpedinte,text="Ingrese el número de cédula del paciente del que seva a crear el expediente",font=(14)).place(x=5,y=120)
nuevaCedula=Entry(CrearExpedinte)
nuevaCedula.place(x=550,y=124)

ingresoNombreNuevo = Label(CrearExpedinte,text="Ingrese el nombre completo del paciente",font=(14)).place(x=5,y=170)
nuevoNombre=Entry(CrearExpedinte)
nuevoNombre.place(x=300,y=174)

ingresoEdad = Label(CrearExpedinte,text="Ingrese la edad del paciente",font=(14)).place(x=5,y=220)
nuevaEdad=Entry(CrearExpedinte)
nuevaEdad.place(x=215,y=224)

registroInformacion=Label(CrearExpedinte,text="Información resgristrada",font=("Arial",16,"bold","italic"), justify=CENTER).place(x=210,y=310)


cedula=Label(CrearExpedinte)
cedula.place(x=435,y=353)

nombre=Label(CrearExpedinte)
nombre.place(x=432,y=402)

edad=Label(CrearExpedinte)
edad.place(x=351,y=452)

def presionar():
    txt1=nuevaCedula.get()
    txt2=nuevoNombre.get()
    txt3=nuevaEdad.get()

    Label(CrearExpedinte,text="El número de cedula ingresado es:",font=(14), justify=CENTER).place(x=190,y=350)
    cedula.config(text=txt1)
    Label(CrearExpedinte,text="El nombre completo ingresado es:",font=(14), justify=CENTER).place(x=190,y=400)
    nombre.config(text=txt2)
    Label(CrearExpedinte,text="La edad ingresada es:",font=(14), justify=CENTER).place(x=190,y=450)
    edad.config(text=txt3)


botonCrear=Button(CrearExpedinte,text="Haz click aquí",command=presionar) #command=inicioDeSesion)
botonCrear.place(x=20,y=270)
Label(CrearExpedinte,text="*Por favor darle al boton una vez haya terminado",font=(14)).place(x=130,y=270)


CerrarSecion=Button(CrearExpedinte,text="Volver al Menu de doctores").place(x=634,y=510)

CrearExpedinte.mainloop()