from tkinter.ttk import Combobox
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
MenuInicio.geometry("800x600")
MenuInicio.resizable(0,0)

#widgets iniciales
def menuPrincipal():
    errorInicio=Label(MenuInicio)
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
    contrasenia=Entry(MenuInicio,show="•")
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
                        terminarSesion.place_forget()

                        
                        registro=Label(MenuInicio,text="Registro de expedientes",font=("Arial",16,"bold","italic"),justify=CENTER)
                        registro.place(x=280,y=55)

                        ingresoCedulaConsulta = Label(MenuInicio,text="Ingrese el número de cédula del paciente",font=(14))
                        ingresoCedulaConsulta.place(x=5,y=120)
                        cedulaConsulta=Entry(MenuInicio)
                        cedulaConsulta.place(x=300,y=124)
                        expediente=Label(MenuInicio,text="Expediente del paciente",font=("Arial",16,"bold","italic"), justify=CENTER)
                        expediente.place(x=5,y=390)
                        noCedula = Label(MenuInicio,text="Numero de cédula")
                        noCedula.place(x=5, y=420)
                        salidaCedula = Label(MenuInicio)
                        salidaCedula.place(x=105, y=420)
                        nombrePaciente=Label(MenuInicio, text="Nombre")
                        nombrePaciente.place(x=205, y=420)
                        salidaNombre=Label(MenuInicio)
                        salidaNombre.place(x=255, y=420)
                        edadPaciente=Label(MenuInicio, text="Edad")
                        edadPaciente.place(x=365, y=420)
                        salidaEdad=Label(MenuInicio)
                        salidaEdad.place(x=405, y=420)
                        padecimientolbl = Label(MenuInicio)
                        padecimientolbl.place(x=5, y=200)
                        agregarPadecimiento = Entry(MenuInicio)
                        recetalbl = Label(MenuInicio)
                        recetalbl.place(x=300, y=200)
                        agregarReceta=Entry(MenuInicio)
                        alturalbl = Label(MenuInicio)
                        alturalbl.place(x=550, y=200)
                        agregarAltura=Entry(MenuInicio)
                        pesolbl=Label(MenuInicio)
                        pesolbl.place(x=5,y=240)
                        agregarPeso=Entry(MenuInicio)
                        modificarEx=Button(MenuInicio,text="Modificar expediente")
                        def busqueda():
                            global posicionExpediente
                            cedula = int(cedulaConsulta.get())
                            for i in range(len(expedientesPacientes)):
                                for k in range(len(expedientesPacientes[i])):
                                    if expedientesPacientes[i][k] == cedula:
                                        posicionExpediente = i
                                        salidaCedula.config(text=str(expedientesPacientes[i][0]), font=(14))
                                        salidaNombre.config(text=expedientesPacientes[i][1])
                                        salidaEdad.config(text=str(expedientesPacientes[i][2]))
                                        padecimientolbl.config(text="Agregar padecimiento")
                                        agregarPadecimiento.place(x=150,y=200)
                                        recetalbl.config(text="Agregar receta")
                                        agregarReceta.place(x=390,y=200)
                                        alturalbl.config(text="Agregar altura")
                                        agregarAltura.place(x=640,y=200)
                                        pesolbl.config(text="Agregar peso")
                                        agregarPeso.place(x=90,y=240)
                                        modificarEx.place(x=600,y=400)

                        def modficarExpediente():
                            if str(agregarAltura.get()) != "":
                                try: 
                                    expedientesPacientes[posicionExpediente][3] = str(agregarAltura.get())
                                except:
                                    expedientesPacientes[posicionExpediente].append(str(agregarAltura.get()))

                            if str(agregarPeso.get()) != "":
                                    try: 
                                        expedientesPacientes[posicionExpediente][4] = str(agregarPeso.get())
                                    except:
                                        expedientesPacientes[posicionExpediente].append(str(agregarPeso.get()))
                           
                            if agregarPadecimiento.get() != "":
                                expedientesPacientes[posicionExpediente].append(agregarPadecimiento.get())

                            if agregarReceta.get() != "":
                                expedientesPacientes[posicionExpediente].append(agregarReceta.get())

                            salidaExpediente.config(text="")
                            salidaExpediente.config(text=str(expedientesPacientes[posicionExpediente]))

                        botonConsulta=Button(MenuInicio,text="Buscar expediente", command = busqueda) 
                        botonConsulta.place(x=20,y=160)
                        modificarEx.config(command=modficarExpediente)
                        
                        
                        def volver():
                            noCedula.place_forget()
                            salidaCedula.place_forget()
                            nombrePaciente.place_forget()
                            salidaNombre.place_forget()
                            edadPaciente.place_forget()
                            salidaEdad.place_forget()
                            registro.place_forget()
                            ingresoCedulaConsulta.place_forget()
                            cedulaConsulta.place_forget()
                            expediente.place_forget()
                            botonConsulta.place_forget()
                            modificarEx.place_forget()
                            padecimientolbl.place_forget()
                            agregarPadecimiento.place_forget()
                            recetalbl.place_forget()
                            agregarReceta.place_forget()
                            alturalbl.place_forget()
                            agregarAltura.place_forget()
                            pesolbl.place_forget()
                            agregarPeso.place_forget()
                            
                            volverMenuDoctores.place_forget()
                            inicioDeSesion()
                        
                        volverMenuDoctores=Button(MenuInicio,text="Volver al Menu de doctores", command=volver)
                        volverMenuDoctores.place(x=634,y=510)

                        
                def cerrarSesion():
                    titulo1.place_forget()
                    titulo2.place_forget()
                    crear.place_forget()
                    consultar.place_forget()
                    terminarSesion.place_forget()
                    menuPrincipal()

                crear=Button(MenuInicio,text="Crear un expediente", command = crearExpedientes)
                crear.place(x=140,y=275)
                consultar=Button(MenuInicio,text="Consultar un expediente", command = consultarExpediente)
                consultar.place(x=320,y=275)
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
                    errorInicio.place_forget()

                    comprobador = True

                    titulo3=Label(MenuInicio,text="Bienvenido Paciente",font=("Arial Bold",16), justify=CENTER)
                    titulo3.place(x=200,y=55)
                    titulo4=Label(MenuInicio,text="Que desea realizar ",font=("Arial Bold",12), justify=CENTER)
                    titulo4.place(x=220,y=120)


                    def solicitarCita():
                        titulo3.place_forget()
                        titulo4.place_forget()
                        solicitudCita.place_forget()
                        consultaCita.place_forget()
                        consultaReceta.place_forget()
                        TerminarCerrarSecion.place_forget()
                        
                        hayCitas=Label(MenuInicio)
                        hayCitas.place(x=85,y=250)
                        diaCita = Label(MenuInicio)
                        diaCita.place(x=360,y=250) ##
                        doctorCitas = Label(MenuInicio)
                        doctorCitas.place(x=390,y=250)
                        nombreDoctor = Label(MenuInicio)
                        nombreDoctor.place(x=85,y=270)##
                        horario1 = Label(MenuInicio)
                        horario1.place(x=228,y=270)
                        horario2 = Label(MenuInicio)
                        horario2.place(x=265,y=270)##

                        horarioCitas = Combobox(state="readonly")
                        rb1=Button(MenuInicio,text="1")
                        rb1.place(x=5, y=20)
                        rb2=Button(MenuInicio, text="2")
                        rb2.place(x=45, y=20)
                        rb3=Button(MenuInicio, text="3")
                        rb3.place(x=85, y=20)
                        rb4=Button(MenuInicio, text="4")
                        rb4.place(x=125, y=20)
                        rb5=Button(MenuInicio, text="5")
                        rb5.place(x=165, y=20)
                        rb6=Button(MenuInicio, text="6")
                        rb6.place(x=205, y=20)
                        rb7=Button(MenuInicio, text="7")
                        rb7.place(x=245, y=20)
                        rb8=Button(MenuInicio, text="8")
                        rb8.place(x=5, y=60)
                        rb9=Button(MenuInicio, text="9")
                        rb9.place(x=45, y=60)
                        rb10=Button(MenuInicio, text="10")
                        rb10.place(x=85, y=60)
                        rb11=Button(MenuInicio, text="11")
                        rb11.place(x=125, y=60)
                        rb12=Button(MenuInicio, text="12")
                        rb12.place(x=165, y=60)
                        rb13=Button(MenuInicio, text="13")
                        rb13.place(x=205, y=60)
                        rb14=Button(MenuInicio, text="14")
                        rb14.place(x=245, y=60)
                        rb15=Button(MenuInicio, text="15")
                        rb15.place(x=5, y=100)
                        rb16=Button(MenuInicio, text="16")
                        rb16.place(x=45, y=100)
                        rb17=Button(MenuInicio, text="17")
                        rb17.place(x=85, y=100)
                        rb18=Button(MenuInicio, text="18")
                        rb18.place(x=125, y=100)
                        rb19=Button(MenuInicio, text="19")
                        rb19.place(x=165, y=100)
                        rb20=Button(MenuInicio, text="20")
                        rb20.place(x=205, y=100)
                        rb21=Button(MenuInicio, text="21")
                        rb21.place(x=245, y=100)
                        rb22=Button(MenuInicio, text="22")
                        rb22.place(x=5, y=140)
                        rb23=Button(MenuInicio, text="23")
                        rb23.place(x=45, y=140)
                        rb24=Button(MenuInicio, text="24")
                        rb24.place(x=85, y=140)
                        rb25=Button(MenuInicio, text="25")
                        rb25.place(x=125, y=140)
                        rb26=Button(MenuInicio, text="26")
                        rb26.place(x=165, y=140)
                        rb27=Button(MenuInicio, text="27")
                        rb27.place(x=205, y=140)
                        rb28=Button(MenuInicio, text="28")
                        rb28.place(x=245, y=140)
                        rb29=Button(MenuInicio, text="29")
                        rb29.place(x=5, y=180)
                        rb30=Button(MenuInicio, text="30")
                        rb30.place(x=45, y=180)

                        avisoCita = Label(MenuInicio)
                        avisoCita.place(x=200, y=40)
                        solicitarBoton=Button(MenuInicio)
                        def cita():
                            horarios=[]
                            for k in citasMensuales[dia]:
                                if k[0] == False:
                                       horarios.append(k[1])
                            horarioCitas.config(values=horarios)
                            horarioCitas.place(x=500,y=220)
                            solicitarBoton.config(text="Solicitar cita")
                            solicitarBoton.place(x=500, y=250)
                        
                        def numero1():
                            global dia
                            dia = 1
                            MenuInicio.after(500, cita())

                        def numero2():
                            global dia
                            dia = 2
                            MenuInicio.after(500, cita())

                        def numero3():
                            global dia
                            dia = 3
                            MenuInicio.after(500, cita())

                        def numero4():
                            global dia
                            dia = 4
                            MenuInicio.after(500, cita())

                        def numero5():
                            global dia
                            dia = 5
                            MenuInicio.after(500, cita())

                        def numero6():
                            global dia
                            dia = 6
                            MenuInicio.after(500, cita())
                        
                        def numero7():
                            global dia
                            dia = 7
                            MenuInicio.after(500, cita())

                        def numero8():
                            global dia
                            dia = 8
                            MenuInicio.after(500, cita())

                        def numero9():
                            global dia
                            dia = 9
                            MenuInicio.after(500, cita())

                        def numero10():
                            global dia
                            dia = 10
                            MenuInicio.after(500, cita())

                        def numero11():
                            global dia
                            dia = 11
                            MenuInicio.after(500, cita())

                        def numero12():
                            global dia
                            dia = 12
                            MenuInicio.after(500, cita())

                        def numero13():
                            global dia
                            dia = 13
                            MenuInicio.after(500, cita())

                        def numero14():
                            global dia
                            dia = 14
                            MenuInicio.after(500, cita())  

                        def numero15():
                            global dia
                            dia = 15
                            MenuInicio.after(500, cita())

                        def numero16():
                            global dia
                            dia = 16
                            MenuInicio.after(500, cita())

                        def numero17():
                            global dia
                            dia = 17
                            MenuInicio.after(500, cita())

                        def numero18():
                            global dia
                            dia = 18
                            MenuInicio.after(500, cita())
                            
                        def numero19():
                            global dia
                            dia = 19
                            MenuInicio.after(500, cita())
                        
                        def numero20():
                            global dia
                            dia = 20
                            MenuInicio.after(500, cita())

                        def numero21():
                            global dia
                            dia = 21
                            MenuInicio.after(500, cita())

                        def numero22():
                            global dia
                            dia = 22
                            MenuInicio.after(500, cita())

                        def numero23():
                            global dia
                            dia = 23
                            MenuInicio.after(500, cita())

                        def numero24():
                            global dia
                            dia = 24
                            MenuInicio.after(500, cita())

                        def numero25():
                            global dia
                            dia = 25
                            MenuInicio.after(500, cita())

                        def numero26():
                            global dia
                            dia = 26
                            MenuInicio.after(500, cita())

                        def numero27():
                            global dia
                            dia = 27
                            MenuInicio.after(500, cita())

                        def numero28():
                            global dia
                            dia = 28
                            MenuInicio.after(500, cita())

                        def numero29():
                            global dia
                            dia = 29
                            MenuInicio.after(500, cita())

                        def numero30():
                            global dia
                            dia = 30
                            MenuInicio.after(500, cita())

                        def procesoCita():
                            for k in citasMensuales[dia]:
                                if k[1] == horarioCitas.get():
                                    k[0] = True

                                    for i in expedientesPacientes:
                                        if i[0] == cedulaLogIn:
                                            nombrePaciente = i[1]
                                    k[3]=nombrePaciente

                                    hayCitas.config(text="Su cita ha sido anotada para el dia ",font=("Arial",12), justify=CENTER)
                                    diaCita.config(text=str(dia),font=("Arial",12), justify=CENTER)##
                                    doctorCitas.config(text="con el doctor/a",font=("Arial",12), justify=CENTER)
                                    nombreDoctor.config(text=k[2],font=("Arial",12), justify=CENTER)##
                                    horario1.config(text="a las ",font=("Arial",12), justify=CENTER)
                                    horario2.config(text=k[1],font=("Arial",12), justify=CENTER)##
                                    break
                            
                            
                        def volver():
                            rb1.place_forget()
                            rb2.place_forget()
                            rb3.place_forget()
                            rb4.place_forget()
                            rb5.place_forget()
                            rb6.place_forget()
                            rb7.place_forget()
                            rb8.place_forget()
                            rb9.place_forget()
                            rb10.place_forget()
                            rb11.place_forget()
                            rb12.place_forget()
                            rb13.place_forget()
                            rb14.place_forget()
                            rb15.place_forget()
                            rb16.place_forget()
                            rb17.place_forget()
                            rb18.place_forget()
                            rb19.place_forget()
                            rb20.place_forget()
                            rb21.place_forget()
                            rb22.place_forget()
                            rb23.place_forget()
                            rb24.place_forget()
                            rb25.place_forget()
                            rb26.place_forget()
                            rb27.place_forget()
                            rb28.place_forget()
                            rb29.place_forget()
                            rb30.place_forget()

                            botonVolver.place_forget()
                            horarioCitas.place_forget()
                            hayCitas.place_forget()
                            diaCita.place_forget()
                            solicitarBoton.place_forget()
                            doctorCitas.place_forget()
                            nombreDoctor.place_forget()
                            horario1.place_forget()
                            horario2.place_forget()
                            inicioDeSesion()

                        rb1.config(command=numero1, width = 4, height = 2)
                        rb2.config(command=numero2, width = 4, height = 2)
                        rb3.config(command=numero3, width = 4, height = 2)
                        rb4.config(command=numero4, width = 4, height = 2)
                        rb5.config(command=numero5, width = 4, height = 2)
                        rb6.config(command=numero6, width = 4, height = 2)
                        rb7.config(command=numero7, width = 4, height = 2)
                        rb8.config(command=numero8, width = 4, height = 2)
                        rb9.config(command=numero9, width = 4, height = 2)
                        rb10.config(command=numero10, width = 4, height = 2)
                        rb11.config(command=numero11, width = 4, height = 2)
                        rb12.config(command=numero12, width = 4, height = 2)
                        rb13.config(command=numero13, width = 4, height = 2)
                        rb14.config(command=numero14, width = 4, height = 2)
                        rb15.config(command=numero15, width = 4, height = 2)
                        rb16.config(command=numero16, width = 4, height = 2)
                        rb17.config(command=numero17, width = 4, height = 2)
                        rb18.config(command=numero18, width = 4, height = 2)
                        rb19.config(command=numero19, width = 4, height = 2)
                        rb20.config(command=numero20, width = 4, height = 2)
                        rb21.config(command=numero21, width = 4, height = 2)
                        rb22.config(command=numero22, width = 4, height = 2)
                        rb23.config(command=numero23, width = 4, height = 2)
                        rb24.config(command=numero24, width = 4, height = 2)
                        rb25.config(command=numero25, width = 4, height = 2)
                        rb26.config(command=numero26, width = 4, height = 2)
                        rb27.config(command=numero27, width = 4, height = 2)
                        rb28.config(command=numero28, width = 4, height = 2)
                        rb29.config(command=numero29, width = 4, height = 2)
                        rb30.config(command=numero30, width = 4, height = 2)

                        solicitarBoton.config(command=procesoCita)
                        botonVolver=Button(MenuInicio,text="Volver al menu de pacientes",command=volver)
                        botonVolver.place(x=510,y=300)


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
                        diaCita.place(x=460,y=150) ##
                        doctorCitas = Label(MenuInicio)
                        doctorCitas.place(x=490,y=150)
                        nombreDoctor = Label(MenuInicio)
                        nombreDoctor.place(x=85,y=170)##
                        horario1 = Label(MenuInicio)
                        horario1.place(x=228,y=170)
                        horario2 = Label(MenuInicio)
                        horario2.place(x=265,y=170)##
                        NohayCitas = Label(MenuInicio)
                        NohayCitas.place(x=105,y=150)
                        for i in expedientesPacientes:
                            if i[0] == cedulaLogIn:
                                nombrePaciente = i[1]

                        for i in citasMensuales.keys():
                            for k in citasMensuales[i]:
                                if nombrePaciente in k:
                                    hayCitas.config(text="Segun nuestros registros usted tiene cita el dia ",font=("Arial",12), justify=CENTER)
                                    diaCita.config(text=str(i),font=("Arial",12), justify=CENTER)##
                                    doctorCitas.config(text="con el doctor/a",font=("Arial",12), justify=CENTER)
                                    nombreDoctor.config(text=k[2],font=("Arial",12), justify=CENTER)##
                                    horario1.config(text="a las ",font=("Arial",12), justify=CENTER)
                                    horario2.config(text=k[1],font=("Arial",12), justify=CENTER)##
                                    NohayCitas.place_forget()    
                                else:
                                    NohayCitas.config(text="Segun nuestros registros usted no tiene citas pendientes ",font=("Arial",12), justify=CENTER)
                                    

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

                    
                    solicitudCita=Button(MenuInicio,text="Solicitar una cita", command=solicitarCita)
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
                errorInicio.Label(text="Datos incorrectos, intente de nuevo").place(x=0, y=500)
            else:
                errorInicio.config(text="Lo sentimos no se encuentra en nuestra base de datos").place(x=100, y=500)
    boton=Button(MenuInicio,text="Iniciar sesión",command=inicioDeSesion)
    boton.place(x=360,y=310)

menuPrincipal()
MenuInicio.mainloop()