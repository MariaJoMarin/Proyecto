from tkinter import * 
import random

randList=[]
credencialesDoctores = [[113409787,"Angelica Perez","AnP104"],[112652354,"Roberto Bermudez","Bz190955"],[119336712,"Evangelina Barcelo","435Be88"],[1104504382,"Luis Lopez","lL437636"]]
credencialesPacientes = [[112345678,"Pedro Sanchez","Pedr0"]]
expedientesPacientes = [[112345678,"Pedro Sanchez",32]]
intentos = 3
cedula = 0 
edad = 0
nombreCompleto = ""
#Holiz4 <3 143 1432 
citasMensuales={}
for i in range(0,30):
    for k in range(0,10):
        a=random.randint(0,3)
        randList.append(a)
    citasMensuales[i+1] = [[False,"7:00 am",credencialesDoctores[randList[0]][1],"Paciente"],[False,"8:00 am",credencialesDoctores[randList[1]][1],"Paciente"],[False,"9:00 am",credencialesDoctores[randList[2]][1],"Paciente"],[False,"10:00 am",credencialesDoctores[randList[3]][1],"Paciente"],[False,"11:00 am",credencialesDoctores[randList[4]][1],"Paciente"],[False,"12:00 pm",credencialesDoctores[randList[5]][1],"Paciente"],[False,"1:00 pm",credencialesDoctores[randList[6]][1],"Paciente"],[False,"2:00 pm",credencialesDoctores[randList[7]][1],"Paciente"],[False,"3:00 pm",credencialesDoctores[randList[8]][1],"Paciente"],[False,"4:00 pm",credencialesDoctores[randList[9]][1],"Paciente"]]


    

MenuInicio=Tk()
MenuInicio.title("Menu de Inicio")
MenuInicio.geometry("800x550")
MenuInicio.resizable(0,0)

#widgets iniciales
def menuPrincipal():
    bienvenida = Label(MenuInicio,text="Bienvenido al inicio de sesión del hospital",font=("Arial Bold",16), justify=CENTER)
    bienvenida.place(x=190,y=55)
    aviso = Label(MenuInicio,text="Por favor ingresar lo siguiente",font=("Arial",14), justify=CENTER)
    aviso.place(x=255,y=150)
    ingresoCedula = Label(MenuInicio,text="Ingrese su número de cédula",font=(16))
    ingresoCedula.place(x=25,y=250)
    cedula=Entry(MenuInicio)
    cedula.place(x=250,y=255)

    ingresoContrasenia = Label(MenuInicio,text="Digite su contraseña",font=(16))
    ingresoContrasenia.place(x=460,y=250)
    contrasenia=Entry(MenuInicio)
    contrasenia.place(x=630,y=255)
    
    def inicioDeSesion():
        global intentos
        cedulaLogIn = int(cedula.get())
        contraseniaLogIn = str(contrasenia.get())
        comprobador = False
        #Inicio sesion doctores
        for i in range(len(credencialesDoctores)):
            if cedulaLogIn in credencialesDoctores[i] and contraseniaLogIn in credencialesDoctores[i]:
                boton.place_forget() #.forget() elimina el widget para poder escribir más, hay que ir uno a uno
                bienvenida.place_forget()
                aviso.place_forget()
                ingresoCedula.place_forget()
                cedula.place_forget()
                ingresoContrasenia.place_forget()
                contrasenia.place_forget()
                comprobador = True

                titulo1=Label(MenuInicio,text="Bienvenido Doctor",font=("Arial Bold",18), justify=CENTER)
                titulo1.place(x=300,y=55)
                titulo2=Label(MenuInicio,text="Que desea realizar ",font=("Arial Bold",12), justify=CENTER)
                titulo2.place(x=320,y=135)
                
                def crearExpedientes():
                        titulo1.place_forget()
                        titulo2.place_forget()
                        crear.place_forget()
                        consultar.place_forget()
                        modificar.place_forget()
                        terminarSesion.place_forget()

                        informacion=Label(MenuInicio,text="INFORMACION DEL NUEVO PACIENTE",font=("Arial",16,"bold","italic"), justify=CENTER)
                        informacion.place(x=210,y=55)

                        ingresoCedulaNuevo = Label(MenuInicio,text="Ingrese el número de cédula del paciente del que se va a crear el expediente",font=(14))
                        ingresoCedulaNuevo.place(x=5,y=120)

                        nuevaCedula=Entry(MenuInicio)
                        nuevaCedula.place(x=550,y=124)

                        ingresoNombreNuevo = Label(MenuInicio,text="Ingrese el nombre completo del paciente",font=(14))
                        ingresoNombreNuevo.place(x=5,y=170)
                        nuevoNombre=Entry(MenuInicio)
                        nuevoNombre.place(x=300,y=174)

                        ingresoEdad = Label(MenuInicio,text="Ingrese la edad del paciente",font=(14))
                        ingresoEdad.place(x=5,y=220)
                        nuevaEdad=Entry(MenuInicio)
                        nuevaEdad.place(x=215,y=224)
                        
                        def registrar():
                            global registroInformacion
                            registroInformacion=Label(MenuInicio,text="Información resgristrada",font=("Arial",16,"bold","italic"), justify=CENTER)
                            registroInformacion.place(x=260,y=310)
                            cedula = int(nuevaCedula.get())
                            nombreCompleto = str(nuevoNombre.get())
                            nombreCompleto = nombreCompleto.title()
                            nombreCompleto = nombreCompleto.rstrip()
                            nombreCompleto = nombreCompleto.lstrip()
                            edad = int(nuevaEdad.get())
                            expedientesPacientes.append([cedula, nombreCompleto, edad])


                        botonCrear=Button(MenuInicio,text="Crear expediente",command=registrar) 
                        botonCrear.place(x=20,y=270)

                        def volver():
                            informacion.place_forget()
                            ingresoCedulaNuevo.place_forget()
                            nuevaCedula.place_forget()
                            ingresoNombreNuevo.place_forget()
                            nuevoNombre.place_forget()
                            ingresoEdad.place_forget()
                            nuevaEdad.place_forget()
                            registroInformacion.place_forget()
                            botonCrear.place_forget()
                            volverMenuDoctores.place_forget()
                            inicioDeSesion()


                        volverMenuDoctores=Button(MenuInicio,text="Volver al Menu de doctores", command=volver)
                        volverMenuDoctores.place(x=634,y=510)





                def consultarExpediente():
                        titulo1.place_forget()
                        titulo2.place_forget()
                        crear.place_forget()
                        consultar.place_forget()
                        modificar.place_forget()
                        terminarSesion.place_forget()

                        registro=Label(MenuInicio,text="Registro de expedientes",font=("Arial",16,"bold","italic"),justify=CENTER)
                        registro.place(x=280,y=55)

                        ingresoCedulaConsulta = Label(MenuInicio,text="Ingrese el número de cédula del paciente",font=(14))
                        ingresoCedulaConsulta.place(x=5,y=120)
                        cedulaConsulta=Entry(MenuInicio)
                        cedulaConsulta.place(x=300,y=124)
                        expediente=Label(MenuInicio,text="Expediente del paciente",font=("Arial",16,"bold","italic"), justify=CENTER)
                        expediente.place(x=260,y=285)

                        def busqueda():
                            global salidaExpediente
                            cedula = int(cedulaConsulta.get())
                            for i in range(len(expedientesPacientes)):
                                for k in range(len(expedientesPacientes[i])):
                                    if expedientesPacientes[i][k] == cedula:
                                        expedienteCorrecto = str(expedientesPacientes[i])
                                        salidaExpediente = Label(MenuInicio,text=expedienteCorrecto, font=(14))
                                        salidaExpediente.place(x=260, y=385)
                        
                        botonConsulta=Button(MenuInicio,text="Haz click aquí", command = busqueda) 
                        botonConsulta.place(x=20,y=190)
                        aviso=Label(MenuInicio,text="*Por favor darle al boton una vez haya terminado",font=(14))
                        aviso.place(x=130,y=190)
                        
                        
                        
                        def volver():
                            salidaExpediente.place_forget()
                            registro.place_forget()
                            ingresoCedulaConsulta.place_forget()
                            cedulaConsulta.place_forget()
                            expediente.place_forget()
                            botonConsulta.place_forget()
                            aviso.place_forget()
                            volverMenuDoctores.place_forget()
                            inicioDeSesion()
                        
                        volverMenuDoctores=Button(MenuInicio,text="Volver al Menu de doctores", command=volver)
                        volverMenuDoctores.place(x=634,y=510)

                        


                def modificarExpediente():
                        titulo1.place_forget()
                        titulo2.place_forget()
                        crear.place_forget()
                        consultar.place_forget()
                        modificar.place_forget()
                        terminarSesion.place_forget()

                        registro=Label(MenuInicio,text="Registro de expedientes",font=("Arial",16,"bold","italic"), justify=CENTER)
                        registro.place(x=280,y=55)
                        ingresoCedulaModificar = Label(MenuInicio,text="Ingrese el número de cédula del paciente",font=(14))
                        ingresoCedulaModificar.place(x=5,y=120)
                        cedulaModificar=Entry(MenuInicio)
                        cedulaModificar.place(x=400,y=124)

                        avisoModificar=Label(MenuInicio,text="Que desea modificar",font=("Arial",16,"italic"), justify=CENTER)
                        avisoModificar.place(x=287,y=285)
    
                        agregarPadecimiento=Button(MenuInicio,text="Agregar un padecimiento") 
                        agregarPadecimiento.place(x=50,y=360)

                        agregarReceta=Button(MenuInicio,text="Agregar una receta") 
                        agregarReceta.place(x=315,y=360)
    
                        AlturaPeso=Button(MenuInicio,text="Agregar altura o peso") 
                        AlturaPeso.place(x=613,y=360)

                        def volver():
                            registro.place_forget()
                            ingresoCedulaModificar.place_forget()
                            cedulaModificar.place_forget()
                            avisoModificar.place_forget()
                            agregarPadecimiento.place_forget()
                            agregarReceta.place_forget()
                            AlturaPeso.place_forget()
                            volverMenuDoctores.place_forget()
                            inicioDeSesion()

                        volverMenuDoctores=Button(MenuInicio,text="Volver al Menu de doctores",command=volver)
                        volverMenuDoctores.place(x=634,y=510)    

                def cerrarSesion():
                    titulo1.place_forget()
                    titulo2.place_forget()
                    crear.place_forget()
                    consultar.place_forget()
                    modificar.place_forget()
                    terminarSesion.place_forget()
                    menuPrincipal()

                crear=Button(MenuInicio,text="Crear un expediente", command = crearExpedientes)
                crear.place(x=140,y=275)
                consultar=Button(MenuInicio,text="Consultar un expediente", command = consultarExpediente)
                consultar.place(x=320,y=275)
                modificar=Button(MenuInicio,text="Modificar un expediente", command = modificarExpediente)
                modificar.place(x=525,y=275)
                terminarSesion=Button(MenuInicio,text="Cerrar sesión", command = cerrarSesion)
                terminarSesion.place(x=675,y=485)


           
        else:
            #Inicio sesion pacientes
            for i in range(len(credencialesPacientes)):
                if cedulaLogIn in credencialesPacientes[i] and contraseniaLogIn in credencialesPacientes[i]:
                    comprobador = True
                    boton.place_forget() #.forget() elimina el widget para poder escribir más, hay que ir uno a uno
                    bienvenida.place_forget()
                    aviso.place_forget()
                    ingresoCedula.place_forget()
                    cedula.place_forget()
                    ingresoContrasenia.place_forget()
                    contrasenia.place_forget()
                    comprobador = True

                    titulo3=Label(MenuInicio,text="Bienvenido Paciente",font=("Arial Bold",16), justify=CENTER)
                    titulo3.place(x=200,y=55)
                    titulo4=Label(MenuInicio,text="Que desea realizar ",font=("Arial Bold",12), justify=CENTER)
                    titulo4.place(x=220,y=120)


                    def consultarCita():
                        titulo3.place_forget()
                        titulo4.place_forget()
                        solicitudCita.place_forget()
                        consultaCita.place_forget()
                        consultaReceta.place_forget()
                        TerminarCerrarSecion.place_forget()

                        mensaje1=Label(MenuInicio,text="Consulta de citas",font=("Arial Bold",16), justify=CENTER)
                        mensaje1.place(x=200,y=75)
                        hayCitas=Label(MenuInicio)
                        hayCitas.place(x=85,y=150)
                        diaCita = Label(MenuInicio)
                        diaCita.place(x=320,y=150) ##
                        doctorCitas = Label(MenuInicio)
                        doctorCitas.place(x=390,y=150)
                        nombreDoctor = Label(MenuInicio)
                        nombreDoctor.place(x=85,y=170)##
                        horario1 = Label(MenuInicio)
                        horario1.place(x=198,y=170)
                        horario2 = Label(MenuInicio)
                        horario2.place(x=225,y=170)##
                        NohayCitas = Label(MenuInicio)
                        NohayCitas.place(x=105,y=150)
                        for i in expedientesPacientes:
                            if i[0] == cedulaLogIn:
                                nombrePaciente = i[1]

                        for i in citasMensuales.keys():
                            for k in citasMensuales[i]:
                                if nombrePaciente in k:
                                    hayCitas.config(text="Segun nuetos registros usted tiene cita el dia ",font=("Arial",12), justify=CENTER)
                                    diaCita.config(text=str(i),font=("Arial",12), justify=CENTER)##
                                    doctorCitas.config(text="con el doctor/a",font=("Arial",12), justify=CENTER)
                                    nombreDoctor.config(text=k[2],font=("Arial",12), justify=CENTER)##
                                    horario1.config(text="a las ",font=("Arial",12), justify=CENTER)
                                    horario2.config(text=k[1],font=("Arial",12), justify=CENTER)##
                                    
                                else:
                                    NohayCitas.config(text="Segun nuetos registros usted no tiene citas pendientes ",font=("Arial",12), justify=CENTER)
                                    

                        def volver():
                            mensaje1.place_forget()
                            hayCitas.place_forget()
                            diaCita.place_forget()
                            doctorCitas.place_forget()
                            nombreDoctor.place_forget()
                            horario1.place_forget()
                            horario2.place_forget()
                            NohayCitas.place_forget()
                            botonVolver.place_forget()
                            inicioDeSesion()

                        botonVolver=Button(MenuInicio,text="Volver al menu de pacientes",command=volver)
                        botonVolver.place(x=510,y=300)


                    def consultarReceta():
                        titulo3.place_forget()
                        titulo4.place_forget()
                        solicitudCita.place_forget()
                        consultaCita.place_forget()
                        consultaReceta.place_forget()
                        TerminarCerrarSecion.place_forget()

                        mensaje1=Label(MenuInicio)
                        mensaje1.config(text="Consulta de Recetas",font=("Arial Bold",16), justify=CENTER)
                        mensaje1.place(x=200,y=75)

                        hayReceta=Label(MenuInicio)
                        hayReceta.place(x=25,y=150)
                        receta=Label(MenuInicio)
                        receta.place(x=387,y=150) ##

                        NohayRecetas=Label(MenuInicio)
                        NohayRecetas.place(x=105,y=150)

                        for i in expedientesPacientes:
                                    if cedulaLogIn in i:
                                        try:
                                            if i[6] != "":
                                                hayReceta.config(text="Segun nuestros registros usted tiene una receta de:",font=("Arial",12), justify=CENTER)
                                            receta.config(text=i[6],font=("Arial",12), justify=CENTER)##
                                        except:
                                            NohayRecetas.config(text="Segun nuestros registros usted no tiene recetas pendientes ",font=("Arial",12), justify=CENTER)

                        def volver():
                            mensaje1.place_forget()
                            botonVolver.place_forget()
                            hayReceta.place_forget()
                            receta.place_forget()
                            NohayRecetas.place_forget()
                            inicioDeSesion()

                        botonVolver=Button(MenuInicio,text="Volver al menu de pacientes",command=volver)
                        botonVolver.place(x=510,y=300)
                        
                        
                    def cerrarSesion():
                        titulo3.place_forget()
                        titulo4.place_forget()
                        solicitudCita.place_forget()
                        consultaCita.place_forget()
                        consultaReceta.place_forget()
                        TerminarCerrarSecion.place_forget()
                        menuPrincipal()

                    
                    solicitudCita=Button(MenuInicio,text="Solicitar una cita")
                    solicitudCita.place(x=50,y=200)
                    consultaCita=Button(MenuInicio,text="Consultar sobre una cita", command=consultarCita)
                    consultaCita.place(x=220,y=200)
                    consultaReceta=Button(MenuInicio,text="Consultar sobre una receta",command=consultarReceta)
                    consultaReceta.place(x=410,y=200)

                    TerminarCerrarSecion=Button(MenuInicio,text="Cerrar sesión",command=cerrarSesion)
                    TerminarCerrarSecion.place(x=510,y=300)
                

        if comprobador == False:
            intentos = intentos - 1
            if intentos > 0:
                Label(text="Datos incorrectos, intente de nuevo").place(x=0, y=500)
            else:
                Label(text="Lo sentimos no se encuentra en nuestra base de datos").place(x=100, y=500)
    boton=Button(MenuInicio,text="Iniciar sesión",command=inicioDeSesion)
    boton.place(x=360,y=310)

menuPrincipal()
MenuInicio.mainloop()