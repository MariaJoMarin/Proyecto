from tkinter import *

MenuDoctor=Tk()
MenuDoctor.title("Menu doctores")
MenuDoctor.geometry("800x550")
MenuDoctor.resizable(0,0)

Label(MenuDoctor,text="Bienvenido Doctor",font=("Arial Bold",18), justify=CENTER).place(x=300,y=55)
Label(MenuDoctor,text="Que desea realizar ",font=("Arial Bold",12), justify=CENTER).place(x=320,y=130)

crear=Button(MenuDoctor,text="Crear un expediente").place(x=140,y=275)
consultar=Button(MenuDoctor,text="Consultar un expediente").place(x=320,y=275)
modificar=Button(MenuDoctor,text="Modificar un expediente").place(x=525,y=275)

CerrarSecion=Button(MenuDoctor,text="Cerrar sesión").place(x=675,y=485)
MenuDoctor.mainloop()
