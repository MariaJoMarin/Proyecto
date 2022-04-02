from tkinter import *

MenuInicio=Tk()
MenuInicio.title("Menu pacientes")
MenuInicio.geometry("600x340")
MenuInicio.resizable(0,0)

titulo3=Label(MenuInicio,text="Bienvenido Paciente",font=("Arial Bold",16), justify=CENTER)
titulo3.place(x=200,y=55)
titulo4=Label(MenuInicio,text="Que desea realizar ",font=("Arial Bold",12), justify=CENTER)
titulo4.place(x=220,y=120)

solicitudCita=Button(MenuInicio,text="Solicitar una cita")
solicitudCita.place(x=50,y=200)
consultaCita=Button(MenuInicio,text="Consultar sobre una cita")
consultaCita.place(x=220,y=200)
consultaReceta=Button(MenuInicio,text="Consultar sobre una receta")
consultaReceta.place(x=410,y=200)

TerminarCerrarSecion=Button(MenuInicio,text="Cerrar sesión")
TerminarCerrarSecion.place(x=510,y=300)
MenuInicio.mainloop()