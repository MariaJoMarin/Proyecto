from tkinter import *

MenuInicio=Tk()
MenuInicio.title("Menu pacientes")
MenuInicio.geometry("600x340")
MenuInicio.resizable(0,0)

mensaje1=Label(MenuInicio,text="Consulta de citas",font=("Arial Bold",16), justify=CENTER)
mensaje1.place(x=200,y=75)
hayCitas=Label(MenuInicio,text="Segun nuetos registros usted tiene cita el dia ",font=("Arial",12), justify=CENTER)
hayCitas.place(x=85,y=150)
diaCita=Label(MenuInicio,text="2 de junio ",font=("Arial",12), justify=CENTER)##
diaCita.place(x=320,y=150) ##
doctorCitas=Label(MenuInicio,text="con el doctor/a",font=("Arial",12), justify=CENTER)
doctorCitas.place(x=390,y=150)
nombreDoctor=Label(MenuInicio,text="Alonso Romero",font=("Arial",12), justify=CENTER)##
nombreDoctor.place(x=85,y=170)##
horario1=Label(MenuInicio,text="a las ",font=("Arial",12), justify=CENTER)
horario1.place(x=198,y=170)
horario2=Label(MenuInicio,text="9 a.m",font=("Arial",12), justify=CENTER)##
horario2.place(x=225,y=170)##

NohayCitas=Label(MenuInicio,text="Segun nuetos registros usted no tiene citas pendientes ",font=("Arial",12), justify=CENTER)
NohayCitas.place(x=105,y=150)


CerrarSecion2=Button(MenuInicio,text="Volver al menu de pacientes")
CerrarSecion2.place(x=510,y=300)
MenuInicio.mainloop()

#Hay que cambiar los nombres como los declare,esos los puse asi por el momento