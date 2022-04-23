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
citasMensuales={}
for i in range(0,31):
    for k in range(0,10):
        a=random.randint(0,3)
        randList.append(a)
    citasMensuales[i+1] = [[False,"7:00 am",credencialesDoctores[randList[0]][1],"Paciente"],[False,"8:00 am",credencialesDoctores[randList[1]][1],"Paciente"],[False,"9:00 am",credencialesDoctores[randList[2]][1],"Paciente"],[False,"10:00 am",credencialesDoctores[randList[3]][1],"Paciente"],[False,"11:00 am",credencialesDoctores[randList[4]][1],"Paciente"],[False,"12:00 pm",credencialesDoctores[randList[5]][1],"Paciente"],[False,"1:00 pm",credencialesDoctores[randList[6]][1],"Paciente"],[False,"2:00 pm",credencialesDoctores[randList[7]][1],"Paciente"],[False,"3:00 pm",credencialesDoctores[randList[8]][1],"Paciente"],[False,"4:00 pm",credencialesDoctores[randList[9]][1],"Paciente"]]

MenuInicio=Tk()
MenuInicio.title("Menu de Inicio")
MenuInicio.geometry("800x600")
MenuInicio.resizable(0,0)
MenuInicio['bg'] = 'AliceBlue'

#widgets menuPrincipal
errorInicio=Label(MenuInicio)
bienvenida = Label(MenuInicio,text="Bienvenido al inicio de sesión del hospital",font=("Times",16), justify=CENTER, bg="AliceBlue")
aviso = Label(MenuInicio,text="Por favor ingresar la información",font=("Times",14), justify=CENTER, bg="AliceBlue")
ingresoCedula = Label(MenuInicio,text="Identificación",font=("Times",14), bg="AliceBlue")
cedula=Entry(MenuInicio)
ingresoContrasenia = Label(MenuInicio,text="Contraseña",font=("Times",14), bg="AliceBlue")
contrasenia=Entry(MenuInicio,show="•")
boton=Button(MenuInicio,text="Iniciar sesión", height = 3, width = 13)

#widgets MenuDoctores
titulo1=Label(MenuInicio,text="Bienvenido Doctor",font=("Arial Bold",18), justify=CENTER, bg="AliceBlue")
titulo2=Label(MenuInicio,text="Que desea realizar ",font=("Arial Bold",12), justify=CENTER, bg="AliceBlue")
#widget crearExpediente
informacion=Label(MenuInicio,text="INFORMACION DEL NUEVO PACIENTE",font=("Arial",16,"bold","italic"), justify=CENTER, bg="AliceBlue")
ingresoCedulaNuevo = Label(MenuInicio,text="Ingrese el número de cédula del paciente del que se va a crear el expediente",font=(14), bg="AliceBlue")
nuevaCedula=Entry(MenuInicio)
ingresoNombreNuevo = Label(MenuInicio,text="Ingrese el nombre completo del paciente",font=(14), bg="AliceBlue")
nuevoNombre=Entry(MenuInicio)
ingresoEdad = Label(MenuInicio,text="Ingrese la edad del paciente",font=(14), bg="AliceBlue")
nuevaEdad=Entry(MenuInicio)
#widget registrar
registroInformacion=Label(MenuInicio,text="Información resgristrada",font=("Arial",16,"bold","italic"), justify=CENTER, bg="AliceBlue")
botonCrear=Button(MenuInicio,text="Crear expediente") 
#widget Volver
volverMenuRegistrar=Button(MenuInicio,text="Volver al Menu de doctores")
#widget consultarExpediente
registro=Label(MenuInicio,text="Registro de expedientes",font=("Arial",16,"bold","italic"),justify=CENTER, bg="AliceBlue")
ingresoCedulaConsulta = Label(MenuInicio,text="Ingrese el número de cédula del paciente",font=(14), bg="AliceBlue")
cedulaConsulta=Entry(MenuInicio)
expediente=Label(MenuInicio,text="Expediente del paciente",font=("Arial",16,"bold","italic"), justify=CENTER, bg="AliceBlue")
noCedula = Label(MenuInicio,text="Numero de cédula", bg="AliceBlue")
salidaCedula = Label(MenuInicio, bg="AliceBlue")
nombrePaciente=Label(MenuInicio, text="Nombre", bg="AliceBlue")
salidaNombre=Label(MenuInicio, bg="AliceBlue")
edadPaciente=Label(MenuInicio, text="Edad", bg="AliceBlue")
salidaEdad=Label(MenuInicio, bg="AliceBlue")
alturaPaciente=Label(MenuInicio, text="Altura", bg="AliceBlue")
salidaAltura=Label(MenuInicio, bg="AliceBlue")
pesoPaciente=Label(MenuInicio, text="Peso", bg="AliceBlue")
salidaPeso=Label(MenuInicio, bg="AliceBlue")
padecimientoPaciente=Label(MenuInicio, text="Padecimiento", bg="AliceBlue")
salidaPadecimiento=Label(MenuInicio, bg="AliceBlue")
recetaPaciente=Label(MenuInicio, text="Receta", bg="AliceBlue")
salidaReceta=Label(MenuInicio, bg="AliceBlue")
padecimientolbl = Label(MenuInicio, bg="AliceBlue")
agregarPadecimiento = Entry(MenuInicio)
recetalbl = Label(MenuInicio, bg="AliceBlue")
agregarReceta=Entry(MenuInicio)
alturalbl = Label(MenuInicio, bg="AliceBlue")
agregarAltura=Entry(MenuInicio)
pesolbl=Label(MenuInicio, bg="AliceBlue")
agregarPeso=Entry(MenuInicio)
modificarEx=Button(MenuInicio,text="Modificar expediente")
botonConsulta=Button(MenuInicio,text="Buscar expediente") 
#widget Volver
volverMenuConsulta=Button(MenuInicio,text="Volver al Menu de doctores")
#Widget Boton Crear & Consultar & Cerrar
botonCrear=Button(MenuInicio,text="Crear un expediente")
botonConsultar=Button(MenuInicio,text="Consultar un expediente")
terminarSesion=Button(MenuInicio,text="Cerrar sesión")
#widgets MenuPacientes
titulo3=Label(MenuInicio,text="Bienvenido Paciente",font=("Arial Bold",16), justify=CENTER, bg="AliceBlue")
titulo4=Label(MenuInicio,text="Que desea realizar ",font=("Arial Bold",12), justify=CENTER, bg="AliceBlue")
solicitudCita=Button(MenuInicio,text="Solicitar una cita")
consultaCita=Button(MenuInicio,text="Consultar sobre una cita")
consultaReceta=Button(MenuInicio,text="Consultar sobre una receta")
TerminarCerrarSecion=Button(MenuInicio,text="Cerrar sesión")
#widgets solicitarCita
hayCitas=Label(MenuInicio, bg="AliceBlue")
diaCita = Label(MenuInicio, bg="AliceBlue")
doctorCitas = Label(MenuInicio, bg="AliceBlue")
nombreDoctor = Label(MenuInicio, bg="AliceBlue")
horario1 = Label(MenuInicio, bg="AliceBlue")
horario2 = Label(MenuInicio, bg="AliceBlue")
horarioCitas = Combobox(state="readonly")
calendario=Label(MenuInicio,text="Calendario",font=("Arial",16),fg="RoyalBlue", bg="AliceBlue")
meses =("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
mesEscogido=Combobox(MenuInicio, state="readonly", values=meses)
rb1=Button(MenuInicio,text="1")
rb2=Button(MenuInicio, text="2")
rb3=Button(MenuInicio, text="3")
rb4=Button(MenuInicio, text="4")
rb5=Button(MenuInicio, text="5")
rb6=Button(MenuInicio, text="6")
rb7=Button(MenuInicio, text="7")
rb8=Button(MenuInicio, text="8")
rb9=Button(MenuInicio, text="9")
rb10=Button(MenuInicio, text="10")
rb11=Button(MenuInicio, text="11")
rb12=Button(MenuInicio, text="12")
rb13=Button(MenuInicio, text="13")
rb14=Button(MenuInicio, text="14")
rb15=Button(MenuInicio, text="15")
rb16=Button(MenuInicio, text="16")
rb17=Button(MenuInicio, text="17")
rb18=Button(MenuInicio, text="18")
rb19=Button(MenuInicio, text="19")
rb20=Button(MenuInicio, text="20")
rb21=Button(MenuInicio, text="21")
rb22=Button(MenuInicio, text="22")
rb23=Button(MenuInicio, text="23")
rb24=Button(MenuInicio, text="24")
rb25=Button(MenuInicio, text="25")
rb26=Button(MenuInicio, text="26")
rb27=Button(MenuInicio, text="27")
rb28=Button(MenuInicio, text="28")
rb29=Button(MenuInicio, text="29")
rb30=Button(MenuInicio, text="30")
rb31=Button(MenuInicio,text="31")
escogerMes = Button(MenuInicio, text="Escoger mes")
solicitarBoton=Button(MenuInicio)
volverSolicitudCitas=Button(MenuInicio,text="Volver al menu de pacientes")
#widgets consultarCitas
mensaje1 = Label(MenuInicio,text="Consulta de citas",font=("Arial Bold",16), justify=CENTER, bg="AliceBlue")
hayCitas = Label(MenuInicio, bg="AliceBlue")
diaCita = Label(MenuInicio, bg="AliceBlue")
doctorCitas = Label(MenuInicio, bg="AliceBlue")
nombreDoctor = Label(MenuInicio, bg="AliceBlue")
horario1 = Label(MenuInicio, bg="AliceBlue")
horario2 = Label(MenuInicio, bg="AliceBlue")
NohayCitas = Label(MenuInicio, bg="AliceBlue")
volverConsultarCitas=Button(MenuInicio,text="Volver al menu de pacientes")
mes = " "
citaEliminar = Button(MenuInicio, text = "Eliminar Cita")
citaModificar = Button(MenuInicio, text="Modificar Cita")
#widgets consultarReceta
mensaje1=Label(MenuInicio, bg="AliceBlue")
hayReceta=Label(MenuInicio, bg="AliceBlue")
receta=Label(MenuInicio, bg="AliceBlue")
NohayRecetas=Label(MenuInicio, bg="AliceBlue")
volverConsultarRecetas=Button(MenuInicio,text="Volver al menu de pacientes")

#Menu Doctores
def crearExpedientes():
        titulo1.place_forget()
        titulo2.place_forget()
        botonCrear.place_forget()
        botonConsultar.place_forget()
        terminarSesion.place_forget()

        informacion.place(x=210,y=55)
        ingresoCedulaNuevo.place(x=5,y=120)
        nuevaCedula.place(x=550,y=124)
        ingresoNombreNuevo.place(x=5,y=170)
        nuevoNombre.place(x=300,y=174)
        ingresoEdad.place(x=5,y=220)
        nuevaEdad.place(x=215,y=224)

                        
                        
        def registrar():
            global registroInformacion
            registroInformacion.place(x=260,y=310)
            cedula = int(nuevaCedula.get())
            nombreCompleto = str(nuevoNombre.get())
            nombreCompleto = nombreCompleto.title()
            nombreCompleto = nombreCompleto.rstrip()
            nombreCompleto = nombreCompleto.lstrip()
            edad = int(nuevaEdad.get())
            expedientesPacientes.append([cedula, nombreCompleto, edad])
        botonCrear.config(command=registrar)
        botonCrear.place(x=20,y=270)
        botonCrear['bg'] = 'AliceBlue'
        botonCrear['fg'] = 'SaddleBrown'

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
            volverMenuRegistrar.place_forget()
            inicioDeSesion()
        volverMenuRegistrar.config(command=volver)
        volverMenuRegistrar.place(x=634,y=510)
        volverMenuRegistrar['bg'] = 'azure'

def consultarExpediente():
        titulo1.place_forget()
        titulo2.place_forget()
        botonCrear.place_forget()
        botonConsultar.place_forget()
        terminarSesion.place_forget()
                        
        registro.place(x=280,y=55)
                        
        ingresoCedulaConsulta.place(x=5,y=120)
        cedulaConsulta.place(x=300,y=124)
        expediente.place(x=5,y=390)
        noCedula.place(x=5, y=420)
        salidaCedula.place(x=105, y=420)
        nombrePaciente.place(x=205, y=420)
        salidaNombre.place(x=255, y=420)
        edadPaciente.place(x=365, y=420)
        salidaEdad.place(x=405, y=420)
        alturaPaciente.place(x=5, y=470)
        salidaAltura.place(x=45, y=470)
        pesoPaciente.place(x=95, y=470)
        salidaPeso.place(x=125, y=470)
        padecimientoPaciente.place(x=200, y=470) 
        salidaPadecimiento.place(x=300, y=470)
        recetaPaciente.place(x=365,y=470)
        salidaReceta.place(x=405, y=470)
        padecimientolbl.place(x=5, y=200)
        recetalbl.place(x=300, y=200)
        alturalbl.place(x=550, y=200)
        pesolbl.place(x=5,y=240)
        modificarEx['bg'] = 'AliceBlue'
        modificarEx['fg'] = 'BlueViolet'
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
                        try:
                            salidaAltura.config(text=expedientesPacientes[i][3])
                        except:
                            salidaAltura.config(text="Sin datos")
                        try:
                            salidaPeso.config(text=expedientesPacientes[i][4])
                        except:
                            salidaPeso.config(text="Sin datos")
                        try:
                            salidaPadecimiento.config(text=expedientesPacientes[i][5])
                        except:
                            salidaPadecimiento.config(text="Sin datos")
                        try:
                            salidaReceta.config(text=expedientesPacientes[i][6])
                        except:
                            salidaReceta.config(text="Sin datos")
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
                salidaAltura.config(text=expedientesPacientes[posicionExpediente][3])

            if str(agregarPeso.get()) != "":
                try: 
                    expedientesPacientes[posicionExpediente][4] = str(agregarPeso.get())
                except:
                    expedientesPacientes[posicionExpediente].append(str(agregarPeso.get()))
                salidaPeso.config(text=expedientesPacientes[posicionExpediente][4])
                           
            if agregarPadecimiento.get() != "":
                try:
                    expedientesPacientes[posicionExpediente][5] = agregarPadecimiento.get()
                except:
                    expedientesPacientes[posicionExpediente].append(agregarPadecimiento.get())
                salidaPadecimiento.config(text=expedientesPacientes[posicionExpediente][5])

            if agregarReceta.get() != "":
                try:
                    expedientesPacientes[posicionExpediente][6] = agregarReceta.get()
                except:
                    expedientesPacientes[posicionExpediente].append(agregarReceta.get())
                salidaReceta.config(text=expedientesPacientes[posicionExpediente][6])

        botonConsulta.config(command = busqueda)                        
        botonConsulta.place(x=20,y=160)
        botonConsulta['bg'] = 'AliceBlue'
        botonConsulta['fg'] = 'BlueViolet'
        modificarEx.config(command=modficarExpediente)
                        
                        
        def volver():
            noCedula.place_forget()
            salidaCedula.place_forget()
            nombrePaciente.place_forget()
            salidaNombre.place_forget()
            edadPaciente.place_forget()
            salidaEdad.place_forget()
            alturaPaciente.place_forget()
            salidaAltura.place_forget()
            pesoPaciente.place_forget()
            salidaPeso.place_forget()
            padecimientoPaciente.place_forget()
            salidaPadecimiento.place_forget()
            recetaPaciente.place_forget()
            salidaReceta.place_forget()
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
            volverMenuConsulta.place_forget()
            inicioDeSesion()
        volverMenuConsulta.config(command=volver)
        volverMenuConsulta.place(x=634,y=510)
        volverMenuConsulta['bg'] = 'azure'

                        
def cerrarSesionDoctores():
    titulo1.place_forget()
    titulo2.place_forget()
    botonCrear.place_forget()
    botonConsultar.place_forget()
    terminarSesion.place_forget()
    menuPrincipal()

#Menu Pacientes
def solicitarCita():
    titulo3.place_forget()
    titulo4.place_forget()
    solicitudCita.place_forget()
    consultaCita.place_forget()
    consultaReceta.place_forget()
    TerminarCerrarSecion.place_forget()

    hayCitas.place(x=85,y=355)
    diaCita.place(x=340,y=355) ##
    doctorCitas.place(x=360,y=355)
    nombreDoctor.place(x=85,y=375)##
    horario1.place(x=228,y=375)
    horario2.place(x=265,y=375)
    calendario.place(x=350,y=20)
    mesEscogido.place(x=300,y=50)
    escogerMes.place(x=350, y=50)
    #mes.place(x=175,y=50)
    
    
    def cambiarMes():
        global mes
        mes = mesEscogido.get()
        if mesEscogido.get() == "Abril" or mesEscogido.get() == "Junio" or mesEscogido.get() == "Septiembre" or mesEscogido.get() == "Noviembre": 
            rb1.place(x=85, y=100)
            rb2.place(x=125, y=100)
            rb3.place(x=165, y=100)
            rb4.place(x=205, y=100)
            rb5.place(x=245, y=100)
            rb6.place(x=285, y=100)
            rb7.place(x=325, y=100)
            rb8.place(x=85, y=140)
            rb9.place(x=125, y=140)
            rb10.place(x=165, y=140)
            rb11.place(x=205, y=140)
            rb12.place(x=245, y=140)
            rb13.place(x=285, y=140)
            rb14.place(x=325, y=140)
            rb15.place(x=85, y=180)
            rb16.place(x=125, y=180)
            rb17.place(x=165, y=180)
            rb18.place(x=205, y=180)
            rb19.place(x=245, y=180)
            rb20.place(x=285, y=180)
            rb21.place(x=325, y=180)
            rb22.place(x=85, y=220)
            rb23.place(x=125, y=220)
            rb24.place(x=165, y=220)
            rb25.place(x=205, y=220)
            rb26.place(x=245, y=220)
            rb27.place(x=285, y=220)
            rb28.place(x=325, y=220)
            rb29.place(x=85, y=260)
            rb30.place(x=125, y=260)
        elif mesEscogido.get() == "Febrero":
            rb1.place(x=85, y=100)
            rb2.place(x=125, y=100)
            rb3.place(x=165, y=100)
            rb4.place(x=205, y=100)
            rb5.place(x=245, y=100)
            rb6.place(x=285, y=100)
            rb7.place(x=325, y=100)
            rb8.place(x=85, y=140)
            rb9.place(x=125, y=140)
            rb10.place(x=165, y=140)
            rb11.place(x=205, y=140)
            rb12.place(x=245, y=140)
            rb13.place(x=285, y=140)
            rb14.place(x=325, y=140)
            rb15.place(x=85, y=180)
            rb16.place(x=125, y=180)
            rb17.place(x=165, y=180)
            rb18.place(x=205, y=180)
            rb19.place(x=245, y=180)
            rb20.place(x=285, y=180)
            rb21.place(x=325, y=180)
            rb22.place(x=85, y=220)
            rb23.place(x=125, y=220)
            rb24.place(x=165, y=220)
            rb25.place(x=205, y=220)
            rb26.place(x=245, y=220)
            rb27.place(x=285, y=220)
            rb28.place(x=325, y=220)
        else:
            rb1.place(x=85, y=100)
            rb2.place(x=125, y=100)
            rb3.place(x=165, y=100)
            rb4.place(x=205, y=100)
            rb5.place(x=245, y=100)
            rb6.place(x=285, y=100)
            rb7.place(x=325, y=100)
            rb8.place(x=85, y=140)
            rb9.place(x=125, y=140)
            rb10.place(x=165, y=140)
            rb11.place(x=205, y=140)
            rb12.place(x=245, y=140)
            rb13.place(x=285, y=140)
            rb14.place(x=325, y=140)
            rb15.place(x=85, y=180)
            rb16.place(x=125, y=180)
            rb17.place(x=165, y=180)
            rb18.place(x=205, y=180)
            rb19.place(x=245, y=180)
            rb20.place(x=285, y=180)
            rb21.place(x=325, y=180)
            rb22.place(x=85, y=220)
            rb23.place(x=125, y=220)
            rb24.place(x=165, y=220)
            rb25.place(x=205, y=220)
            rb26.place(x=245, y=220)
            rb27.place(x=285, y=220)
            rb28.place(x=325, y=220)
            rb29.place(x=85, y=260)
            rb30.place(x=125, y=260)
            rb31.place(x=165,y=260)
    escogerMes.config(command=cambiarMes)                   
    solicitarBoton['bg'] = 'AliceBlue'
    def cita():
        horarios=[]
        for k in citasMensuales[dia]:
            if k[0] == False:
                    horarios.append(k[1])
        horarioCitas.config(values=horarios)
        horarioCitas.place(x=470,y=180)
        solicitarBoton.config(text="Solicitar cita")
        solicitarBoton.place(x=630, y=177)
        solicitarBoton['fg'] = 'BlueViolet'
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

    def numero31():
        global dia
        dia = 31
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
        rb31.place_forget()
        calendario.place_forget()
        escogerMes.place_forget()
        mesEscogido.place_forget()
        volverSolicitudCitas.place_forget()
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
    rb31.config(command=numero31, width = 4, height = 2)

    solicitarBoton.config(command=procesoCita)
    volverSolicitudCitas.config(command=volver)
    volverSolicitudCitas.place(x=617,y=547)
    volverSolicitudCitas['bg'] = 'azure'


def consultarCita():
    titulo3.place_forget()
    titulo4.place_forget()
    solicitudCita.place_forget()
    consultaCita.place_forget()
    consultaReceta.place_forget()
    TerminarCerrarSecion.place_forget()

    mensaje1.place(x=300,y=185)
    hayCitas.place(x=95,y=400)
    diaCita.place(x=95,y=435) ##
    doctorCitas.place(x=445,y=400)
    nombreDoctor.place(x=445,y=450)##
    horario1.place(x=500,y=400)
    horario2.place(x=500,y=435)##
    NohayCitas.place(x=195,y=435)
    hayCitas.config(text="Fecha",font=("Arial",12), justify=CENTER)
    doctorCitas.config(text="Doctor/a",font=("Arial",12), justify=CENTER)
    horario1.config(text="Hora",font=("Arial",12), justify=CENTER)
    for i in expedientesPacientes:
        if i[0] == cedulaLogIn:
            nombrePaciente = i[1]

    for i in citasMensuales.keys():
        for k in citasMensuales[i]:
            if nombrePaciente in k:
                fecha=str(i)
                fecha = fecha + " de " + mes
                diaCita.config(text=fecha,font=("Arial",12), justify=CENTER)##
                nombreDoctor.config(text=k[2],font=("Arial",12), justify=CENTER)##
                horario2.config(text=k[1],font=("Arial",12), justify=CENTER)##
                citaEliminar.place(x=225,y=500)
                citaModificar.place(x=275, y = 500)
                NohayCitas.place_forget()    
            else:
                NohayCitas.config(text="Segun nuestros registros usted no tiene citas pendientes ",font=("Arial",12), justify=CENTER)
    
    def modificarCita():
        for i in citasMensuales.keys():
            for k in citasMensuales[i]:
                if nombrePaciente in k:
                    doctor=k[2]
                    hora=k[1]
                    k[0]=False
                    k[3]="Paciente"
        for i in citasMensuales.keys():
            for k in citasMensuales[i]:
                if doctor in k and k[0] == False and k[1]!=hora:
                    k[0]=True
                    fecha=str(i)
                    fecha = fecha + " de " + mes
                    diaCita.config(text=fecha,font=("Arial",12), justify=CENTER)##
                    nombreDoctor.config(text=k[2],font=("Arial",12), justify=CENTER)##
                    horario2.config(text=k[1],font=("Arial",12), justify=CENTER)##
                    break
                else:
                    NohayCitas.config(text="El doctor no tiene más fechas disponibles")
                    break
            break
    citaModificar.config(command=modificarCita)           
                    
    def eliminarCita():
        for i in citasMensuales.keys():
            for k in citasMensuales[i]:
                if nombrePaciente in k:
                    k[3]="Paciente"
                    k[0]=False
                    MenuInicio.after(50, consultarCita)
                    diaCita.config(text=" ")
                    horario2.config(text=" ")
                    nombreDoctor.config(text=" ")
    citaEliminar.config(command=eliminarCita)
    def volver():
        mensaje1.place_forget()
        hayCitas.place_forget()
        diaCita.place_forget()
        doctorCitas.place_forget()
        nombreDoctor.place_forget()
        horario1.place_forget()
        horario2.place_forget()
        NohayCitas.place_forget()
        volverConsultarCitas.place_forget()
        inicioDeSesion()

    volverConsultarCitas.config(command=volver)
    volverConsultarCitas.place(x=617,y=547)
    volverConsultarCitas['bg'] = 'azure'

def consultarReceta():
    titulo3.place_forget()
    titulo4.place_forget()
    solicitudCita.place_forget()
    consultaCita.place_forget()
    consultaReceta.place_forget()
    TerminarCerrarSecion.place_forget()

    mensaje1.config(text="Consulta de Recetas",font=("Arial Bold",16), justify=CENTER)
    mensaje1.place(x=300,y=185)
                        
    hayReceta.place(x=205,y=300)
    NohayRecetas.place(x=195,y=300)
    receta.place(x=570,y=300) ##

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
        volverConsultarRecetas.place_forget()
        hayReceta.place_forget()
        receta.place_forget()
        NohayRecetas.place_forget()
        inicioDeSesion()
    volverConsultarRecetas.config(command=volver)
    volverConsultarRecetas.place(x=617,y=547)
    volverConsultarRecetas['bg'] = 'azure'
                        
def cerrarSesionPacientes():
    titulo3.place_forget()
    titulo4.place_forget()
    solicitudCita.place_forget()
    consultaCita.place_forget()
    consultaReceta.place_forget()
    TerminarCerrarSecion.place_forget()
    menuPrincipal()

def inicioDeSesion():
        global intentos
        global cedulaLogIn
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

                titulo1.place(x=301,y=105)
                titulo2.place(x=325,y=205)

                botonCrear.config(command = crearExpedientes)                
                botonCrear.place(x=150,y=325)
                botonCrear['bg'] = 'AliceBlue'
                botonCrear['fg'] = 'BlueViolet'
                botonConsultar.config(command = consultarExpediente)                
                botonConsultar.place(x=520,y=325)
                botonConsultar['bg'] = 'AliceBlue'
                botonConsultar['fg'] = 'BlueViolet'
                terminarSesion.config(command = cerrarSesionDoctores)                
                terminarSesion.place(x=687,y=547)
                terminarSesion['bg'] = 'azure'

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
                    
                    titulo3.place(x=301,y=105)
                    titulo4.place(x=327,y=200)

                    solicitudCita.config(command=solicitarCita)
                    solicitudCita.place(x=120,y=325)
                    solicitudCita['bg'] = 'AliceBlue'
                    solicitudCita['fg'] = 'BlueViolet'
                    consultaCita.config(command=consultarCita)
                    consultaCita.place(x=320,y=325)
                    consultaCita['bg'] = 'AliceBlue'
                    consultaCita['fg'] = 'BlueViolet'
                    consultaReceta.config(command=consultarReceta)
                    consultaReceta.place(x=520,y=325)
                    consultaReceta['bg'] = 'AliceBlue'
                    consultaReceta['fg'] = 'BlueViolet'
                    TerminarCerrarSecion.config(command=cerrarSesionPacientes)
                    TerminarCerrarSecion.place(x=687,y=547)
                    TerminarCerrarSecion['bg'] = 'azure'

        if comprobador == False:
            intentos = intentos - 1
            if intentos > 0:
                errorInicio.config(text="Datos incorrectos, intente de nuevo")
                errorInicio.place(x=0, y=500)
            else:
                errorInicio.config(text="Lo sentimos no se encuentra en nuestra base de datos")
                errorInicio.place(x=100, y=500)

def menuPrincipal():
    bienvenida.place(x=250,y=55)
    aviso.place(x=260,y=150)
    ingresoCedula.place(x=40,y=250)
    cedula.place(x=250,y=255)
    ingresoContrasenia.place(x=460,y=250)
    contrasenia.place(x=630,y=255)
    boton.config(command=inicioDeSesion)
    boton.place(x=350,y=310)
    boton['bg'] = 'AliceBlue'
    boton['fg'] = 'cyan4'

menuPrincipal()
MenuInicio.mainloop()
