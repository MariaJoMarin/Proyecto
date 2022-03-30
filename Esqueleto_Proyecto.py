import os
import random
randList=[]

credencialesDoctores = [[113409787,"Angelica Perez","AnP104"],[112652354,"Roberto Bermudez","Bz190955"],[119336712,"Evangelina Barcelo","435Be88"],[1104504382,"Luis Lopez","lL437636"]]
credencialesPacientes = [[112345678,"Pedro Sanchez","Pedr0"]]
cedulaLogIn = 0
contraseniaLogIn = ""
intentos = 3

expedientesPacientes = [[112345678,"Pedro Sanchez",32]]
cedula = 0 
edad = 0
nombreCompleto = ""

citasMensuales={}
for i in range(0,30):
    for k in range(0,10):
        a=random.randint(0,3)
        randList.append(a)
    citasMensuales[i+1] = [[False,"7:00 am",credencialesDoctores[randList[0]][1],"Paciente"],[False,"8:00 am",credencialesDoctores[randList[1]][1],"Paciente"],[False,"9:00 am",credencialesDoctores[randList[2]][1],"Paciente"],[False,"10:00 am",credencialesDoctores[randList[3]][1],"Paciente"],[False,"11:00 am",credencialesDoctores[randList[4]][1],"Paciente"],[False,"12:00 pm",credencialesDoctores[randList[5]][1],"Paciente"],[False,"1:00 pm",credencialesDoctores[randList[6]][1],"Paciente"],[False,"2:00 pm",credencialesDoctores[randList[7]][1],"Paciente"],[False,"3:00 pm",credencialesDoctores[randList[8]][1],"Paciente"],[False,"4:00 pm",credencialesDoctores[randList[9]][1],"Paciente"]]

while True:
    opcion = 0
    print("\t Bienvenido al inicio de sesión del hospital ")
    cedulaLogIn = int(input("Ingrese su numero de cedula \n"))
    contraseniaLogIn = input("Digite su contraseña \n ")

    #Inicio sesion doctores
    for i in range(len(credencialesDoctores)):
        if cedulaLogIn in credencialesDoctores[i] and contraseniaLogIn in credencialesDoctores[i]:
            os.system("cls")
            #Menú para doctores
            while opcion == 0:
                opcion=int(input("Bienvenido doctor que desea hacer: \n 1.Crear un expediente \n 2.Consultar un expediente \n 3.Modificar un expediente \n 4.Cerrar sesión \n"))

                while opcion == 1:
                    cedula = int(input("Ingrese el numero de cedula del paciente para crear el expediente "))
                    nombreCompleto = input("Ingrese el nombre completo del paciente ")
                    nombreCompleto = nombreCompleto.title()
                    nombreCompleto = nombreCompleto.rstrip()
                    nombreCompleto = nombreCompleto.lstrip()
                    edad = int(input("Ingrese la edad del paciente "))

                    expedientesPacientes.append([cedula, nombreCompleto, edad])

                    print(expedientesPacientes)

                    opcion = int(input("¿Desea crear otro expediente? \n 1.Si \n 2.No \n"))
                    if opcion != 1:
                        opcion = 0
                    os.system("cls")

                if opcion == 2:
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
                                            os.system("cls")
                                else:
                                    opcion = 0 
                                    os.system("cls")

                if opcion == 3:
                    cedula = int(input("Ingrese el numero de cedula del paciente "))
                    for i in range(len(expedientesPacientes)):
                        for k in range(len(expedientesPacientes[i])):
                            if expedientesPacientes[i][k] == cedula:
                                print(expedientesPacientes[i])
                                opcion = 1
                                while opcion == 1:
                                    os.system("cls")
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
                                    if opcion != 1:
                                        opcion = 0 
                                        os.system("cls")
                if opcion == 4:
                    break
        
    else:
        #Inicio sesion pacientes
        for i in range(len(credencialesPacientes)):
            if cedulaLogIn in credencialesPacientes[i] and contraseniaLogIn in credencialesPacientes[i]:
                os.system("cls")
                while True:
                    print("Bienvenido al sistema del hospital ¿Qué desea hacer?")
                    print ("A: Solicitar cita \nB: Ver información de las citas \nC: Ver información de recetas \nD: Ver información del centro médico \nE:Cerrar Sesión")
                    opcion = str(input())
                    opcion = opcion.lower()
                    os.system("cls")
                    if (opcion == "solicitar cita" or opcion == "a"):
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


                    else:
                         if (opcion == "ver informacion de las citas" or opcion == "b"):
                            for i in expedientesPacientes:
                                if i[0] == cedulaLogIn:
                                    nombrePaciente = i[1]

                            for i in citasMensuales.keys():
                                for k in citasMensuales[i]:
                                    if nombrePaciente in k:
                                        print(f"Usted tiene cita el día {i} con el doctor/a {k[2]} a las {k[1]}")
                                    else:
                                        print("Usted no tiene citas pendientes")
                            os.system("cls")
                         else:
                             if (opcion == "Ver información de recetas" or opcion == "c"):
                                for i in expedientesPacientes:
                                    if cedulaLogIn in i:
                                        try:
                                            print("Su receta es",i[6])
                                        except:
                                            print("Usted no tiene recetas pendientes")
                             else:
                                if (opcion == "ver información del centro médico" or opcion == "d"):
                                    print ("El día de hoy el servicio de medicamententos no se encuentra disponible \n Gracias por su atencion")
                                    os.system("cls")

                                else:
                                    if (opcion == "cerrar sesion" or opcion == "e"):
                                        opcion = 4
                                        break

    if opcion != 4:
        intentos = intentos - 1
        if intentos > 0:
            print("Datos incorrectos, intente de nuevo")
        else:
            print("Lo sentimos no se encuentra en nuestra base de datos")
            break


