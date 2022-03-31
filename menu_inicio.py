#Las funciones están creadas de forma general, hace falta mucho trabajo
#presiento que vamos a tener que anidar funciones dentro de otras para mantener todo
#ordenado en variables locales y para pasar entre pantallas de forma más fácil
#cada menú va a tener que ser una funcion propia, hay algun detalle de logistica que hay que arreglar
#pero de momento hay que dejar listo lo minimo.
#Cada menu debe de tener un boton que permita volver al menu anterior
#

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
for i in range(0,30):
    for k in range(0,10):
        a=random.randint(0,3)
        randList.append(a)
    citasMensuales[i+1] = [[False,"7:00 am",credencialesDoctores[randList[0]][1],"Paciente"],[False,"8:00 am",credencialesDoctores[randList[1]][1],"Paciente"],[False,"9:00 am",credencialesDoctores[randList[2]][1],"Paciente"],[False,"10:00 am",credencialesDoctores[randList[3]][1],"Paciente"],[False,"11:00 am",credencialesDoctores[randList[4]][1],"Paciente"],[False,"12:00 pm",credencialesDoctores[randList[5]][1],"Paciente"],[False,"1:00 pm",credencialesDoctores[randList[6]][1],"Paciente"],[False,"2:00 pm",credencialesDoctores[randList[7]][1],"Paciente"],[False,"3:00 pm",credencialesDoctores[randList[8]][1],"Paciente"],[False,"4:00 pm",credencialesDoctores[randList[9]][1],"Paciente"]]


    

MenuInicio=Tk()
MenuInicio.title("Menu de Inicio")
MenuInicio.geometry("800x550")
MenuInicio.resizable(0,0)

# Opciones para el menu de doctor
def crearExpediente():
    cedula = int(input("Ingrese el numero de cedula del paciente para crear el expediente "))
    nombreCompleto = input("Ingrese el nombre completo del paciente ")
    nombreCompleto = nombreCompleto.title()
    nombreCompleto = nombreCompleto.rstrip()
    nombreCompleto = nombreCompleto.lstrip()
    edad = int(input("Ingrese la edad del paciente "))

    expedientesPacientes.append([cedula, nombreCompleto, edad])

    print(expedientesPacientes)

    opcion = int(input("¿Desea crear otro expediente? \n 1.Si \n 2.No \n"))

def consultaExpediente():
    cedula = int(input("Ingrese el numero de cedula del paciente "))
    for i in range(len(expedientesPacientes)):
        for k in range(len(expedientesPacientes[i])):
            if expedientesPacientes[i][k] == cedula:
                print(expedientesPacientes[i])
                opcion = int(input("Desea modificar el expediente? \n 1.Si \n 2.No \n"))
                if opcion == 1:
                    os.system("cls")
                    while opcion == 1:
                        opcion = int(input("Que desea modificar del expediente \n 1.Agregar padecimiento \n 2.Agregar receta \n 3.Cambiar altura o peso \n"))
                        if opcion == 1:
                            expedientesPacientes[i].append(input())
                        elif opcion == 2:
                            expedientesPacientes[i].append(input())
                        else:
                            opcion = int(input("Que desea cambiar \n 1.Altura \n 2.Peso \n"))
                            if opcion == 1:
                                try: 
                                    expedientesPacientes[i][3] = float(input("Digite la altura "))
                                except:
                                    expedientesPacientes[i].append(float(input("Digite la altura ")))
                            else:
                                try: 
                                    expedientesPacientes[i][4] = float(input("Digite el peso "))
                                except:
                                    expedientesPacientes[i].append(float(input("Digite el peso ")))
                        print(expedientesPacientes[i])
                        opcion = int(input("Desea modificar más el expediente? \n 1.Si \n 2.No \n"))
                        if opcion != 1:
                            opcion = 0
                        else:
                            opcion = 0

def modificarExpediente():
    #esta funcion puede ser opcional, se puede hacer que solo se pueda modificar el expediente desde la pantalla de consultarlo
    cedula = int(input("Ingrese el numero de cedula del paciente "))
    for i in range(len(expedientesPacientes)):
        for k in range(len(expedientesPacientes[i])):
            if expedientesPacientes[i][k] == cedula:
                print(expedientesPacientes[i])
                opcion = 1
                while opcion == 1:
                    opcion = int(input("Que desea modificar del expediente \n 1.Agregar padecimiento \n 2.Agregar receta \n 3.Cambiar altura o peso \n"))
                    if opcion == 1:
                        expedientesPacientes[i].append(input("Ingrese el padecimiento "))
                    elif opcion == 2:
                        expedientesPacientes[i].append(input("Ingrese la receta "))
                    else:
                        opcion = int(input("Que desea cambiar \n 1.Altura \n 2.Peso \n"))
                        if opcion == 1:
                            try: 
                                expedientesPacientes[i][3] = float(input("Digite la altura "))
                            except:
                                expedientesPacientes[i].append(float(input("Digite la altura ")))
                        else:
                            try: 
                                expedientesPacientes[i][4] = float(input("Digite el peso "))
                            except:
                                expedientesPacientes[i].append(float(input("Digite el peso ")))
                    opcion = int(input("Desea modificar más el expediente? \n 1.Si \n 2.No \n"))
       
#opciones pacientes
def solicitudCita():
    print("Los días dispoibles son: ")
    for j in citasMensuales.keys():
        for k in citasMensuales[j]:
            if False in k:
                print(j)
                break
    opcion = int(input("¿Que día desea solicitar su cita?"))
    print("Los horarios disponibles para ese día son: ")
    for k in citasMensuales[opcion]:
        if k[0] == False:
            print(k[1])
    hora = input("¿A qué hora desea su cita?")
    if hora == "7" or hora == "8" or  hora == "9" or hora == "10" or hora == "11" or hora == "12" or hora == "1" or hora == "2" or hora == "3" or hora == "4":
        hora = hora + ":00"
    if hora == "7:00" or hora == "8:00" or hora == "9:00" or hora == "10:00" or hora == "11:00":
        hora = hora + " am"
    else:
        hora = hora + " pm"
    for k in citasMensuales[opcion]:
        if k[1] == hora:
            k[0] = True

            for i in expedientesPacientes:
                if i[0] == cedulaLogIn:
                    nombrePaciente = i[1]
                    k[3]=nombrePaciente

                    print(f"Usted tiene cita el día {opcion} con el doctor/a {k[2]} a las {k[1]}")
                    break

def consultaCitas():
    for i in expedientesPacientes:
        if i[0] == cedulaLogIn:
            nombrePaciente = i[1]

            for i in citasMensuales.keys():
                for k in citasMensuales[i]:
                    if nombrePaciente in k:
                        print(f"Usted tiene cita el día {i} con el doctor/a {k[2]} a las {k[1]}")
                    else:
                        print("Usted no tiene citas pendientes")

def consultaRecetas():
    for i in expedientesPacientes:
        if cedulaLogIn in i:
            try:
                print("Su receta es",i[6])
            except:
                print("Usted no tiene recetas pendientes")

def cerrarSesion():
    #esta hace falta aún pensar el como cambiar entre pantallas, es universal para ambos menus 

    ""

def inicioDeSesion():
    global intentos
    cedulaLogIn = int(cedula.get())
    contraseniaLogIn = str(contrasenia.get())
    comprobador = False
    #Inicio sesion doctores
    for i in range(len(credencialesDoctores)):
        if cedulaLogIn in credencialesDoctores[i] and contraseniaLogIn in credencialesDoctores[i]:
            boton.place_forget() #.forget() elimina el widget para poder escribir más, hay que ir uno a uno
            comprobador = True
            menudoctor = Label(MenuInicio, text="Entró a los doctores").place(x=0, y=400)

           
    else:
        #Inicio sesion pacientes
        for i in range(len(credencialesPacientes)):
            if cedulaLogIn in credencialesPacientes[i] and contraseniaLogIn in credencialesPacientes[i]:
                comprobador = True
                menupaciente = Label(MenuInicio, text="Entró a los pacientes").place(x=0, y=400)
                

    if comprobador == False:
        intentos = intentos - 1
        if intentos > 0:
            Label(text="Datos incorrectos, intente de nuevo").place(x=0, y=500)
        else:
            Label(text="Lo sentimos no se encuentra en nuestra base de datos").place(x=100, y=500)


#widgets iniciales
bienvenida = Label(MenuInicio,text="Bienvenido al inicio de sesión del hospital",font=("Arial Bold",16), justify=CENTER).place(x=190,y=55)

aviso = Label(MenuInicio,text="Por favor ingresar lo siguiente",font=("Arial",14), justify=CENTER).place(x=255,y=150)

ingresoCedula = Label(MenuInicio,text="Ingrese su número de cédula",font=(16)).place(x=25,y=250)
cedula=Entry(MenuInicio)
cedula.place(x=250,y=255)

ingresoContrasenia = Label(MenuInicio,text="Digite su contraseña",font=(16)).place(x=460,y=250)
contrasenia=Entry(MenuInicio)
contrasenia.place(x=630,y=255)

boton=Button(MenuInicio,text="Haz click aquí",command=inicioDeSesion)
boton.place(x=360,y=310)
Label(MenuInicio,text="*Por favor darle al boton una vez haya terminado",font=("Arial Bold",14)).place(x=190,y=350)

MenuInicio.mainloop()