from tkinter import *

MenuDoctor=Tk()
MenuDoctor.title("Menu doctores")
MenuDoctor.geometry("600x340")
MenuDoctor.resizable(0,0)

Label(MenuDoctor,text="Bienvenido Doctor",font=("Arial Bold",16), justify=CENTER).place(x=200,y=55)
Label(MenuDoctor,text="Que desea realizar ",font=("Arial Bold",12), justify=CENTER).place(x=220,y=120)

crear=Button(MenuDoctor,text="Crear un expediente").place(x=50,y=200)
consultar=Button(MenuDoctor,text="Consultar un expediente").place(x=220,y=200)
modificar=Button(MenuDoctor,text="Modificar un expediente").place(x=410,y=200)

CerrarSecion=Button(MenuDoctor,text="Cerrar sesión").place(x=510,y=300)
MenuDoctor.mainloop()