from tkinter import *

MenuInicio=Tk()
MenuInicio.title("Menu pacientes")
MenuInicio.geometry("600x340")
MenuInicio.resizable(0,0)

mensaje1=Label(MenuInicio,text="Consulta de Recetas",font=("Arial Bold",16), justify=CENTER)
mensaje1.place(x=200,y=75)

hayReceta=Label(MenuInicio,text="Segun nuestros registros usted tiene una receta de:",font=("Arial",12), justify=CENTER)
hayReceta.place(x=25,y=150)
receta=Label(MenuInicio,text="2 tabletas de Ibuprofeno ",font=("Arial",12), justify=CENTER)##
receta.place(x=387,y=150) ##


NohayRecetas=Label(MenuInicio,text="Segun nuestros registros usted no tiene recetas pendientes ",font=("Arial",12), justify=CENTER)
NohayRecetas.place(x=105,y=150)


finalCerrarSecion=Button(MenuInicio,text="Volver al menu de pacientes")
finalCerrarSecion.place(x=510,y=300)
MenuInicio.mainloop()

#Hay que cambiar los nombres como los declare,esos los puse asi por el momento
