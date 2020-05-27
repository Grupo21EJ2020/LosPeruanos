#Menu Chido para el pia osi osi 
from Clasecurso import Curso
from Claseempleado import empleado
from Clasecurso_tema import Curso_Tema
from clase_temas import Tema
from clase_videos import Video

print("»"*60)

loop= True
limitador = 6
while loop == True:
    accion=int(input("Dime a que archivo deseas entrar:\n Curso=1:\n Empleado=2:\n Video=3:\n Tema=4:\n Curso_Tema=5:\n Curso_Tema_Video=6:\n"))
    if accion == 1:
         opcion = int(input("Dime que deseas hacer en este archivo:\n Agregar= 1:\n Borrar=2:\n Modificar=3:\n Consultar todo=4:\n Ver detalles de algun curso=5:\n"))
         if opcion == 1:
             idcurso = int(input("id de curso: \n"))  
             descripcion = input("nombre de curso: \n")   
             idempleado = int(input("Id de empleado: \n"))
             add = Curso(idcurso,descripcion,idempleado)
             add.Agregar()
             print("Se han agrgado")
         if opcion == 2:
             
             archivo = open("./archivos/curso.txt")
             print(archivo.read())
             
             archivo.close()
             idcurso = int(input("Elija el curso a eliminar:\n"))
             descripcion = input("Elija el nombre del curso a eliminar:\n")
             idempleado = int(input("Elija el id del empleado a eliminar:\n"))
             print("se ha eliminado el curso ")



             delete = Curso(idcurso,descripcion,idempleado)
             delete.Eliminar  
         if opcion == 3:
             
             f = open("./archivos/curso.txt")
             print(archivo.read())
             f.close()
             idcurso = int(input("Elija el curso a modificar:\n"))
             descripcion = input("Elija el nombre del curso a modificar:\n")
             idempleado = int(input("Elija el id del empleado a modificar:\n"))
             mod = Curso(idcurso,descripcion,idempleado)
             mod.Modificar
         if opcion == 4:
             print("Esta es toda la informacion en el archivo\n")
             f = open("./archivos/curso.txt")
             print(f.read())
             f.close()
         if opcion == 5:
             print("Esta es toda la informacion en el archivo\n")
             f = open("./archivos/curso.txt")
             print(f.read())
             f.close()
             linea = int(input("Escribe la linea que deseas ver"))
             f = open("./archivos/curso.txt")
             linea = f.readline()
             print(linea)
             f.close()

             

             
         



#EMPLEADOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOS
    if accion == 2:
        opcion = int(input("Dime que deseas hacer en este archivo:\n Agregar= 1:\n Borrar=2:\n Modificar=3:\n Consultar todo=4:\n Ver detalles de algun empleado=5:\n Salir=6:\n"))
        if opcion == 1:
             idempleado = int(input("Dame el id del empleado a agregar: \n"))  
             nombre = input("Dame el nombre del empleado: \n")   
             direccion = (input("Dame la direccion: \n"))
             add = empleado(idempleado,nombre,direccion)
             add.Agregar()
             print("Se han agrgado")
             

        
            
            
        if opcion ==2:
            #BORRAR DATOS DE EMPLEADOS UWU
            print("Estos son los empleados que han sido registrados")
            archivochido=open("./archivos/empleados.txt")
            print(archivochido.read())
            archivochido.close()
            #

            idempleado = input("Dame el id del empleado a borrar:\n")
            nombre= input("Dame el nombre del empleado a borrar:\n")
            direccion= input("Dame la direccion del empleado a borrar:\n")
            borrado= empleado(idempleado,nombre,direccion)
            borrado.borrarInfo()

           
            


        if opcion == 3:
             
             f = open("./archivos/empleados.txt")
             print(archivo.read())
             f.close()
             idempleado = int(input("Elija el idempleado a modificar:\n"))
             nombre = input("Elija el nombre a modificar:\n")
             direccion = (input("Elija la direccion a modificar:\n"))
             mod = Curso(idempleado,nombre,direccion)
             mod.Modificar



        if opcion == 4:
            print("Esta es toda la informacion en el archivo de empleados\n")
            f = open("./archivos/empleados.txt")
            print(f.read())
            f.close()



        if opcion == 5:
            print("Esta es toda la informacion en el archivo de empleados\n")
            f = open("./archivos/empleados.txt")
            print(f.read())
            f.close()
            linea = int(input("Escribe la linea que deseas ver"))
            f = open("./archivos/empleados.txt")
            linea = f.readline()
            print(linea)
            f.close()

        if opcion == 6:
            pass


    if accion == 5:
        opcion = int(input("Dime que deseas hacer en este archivo:\n Agregar= 1:\n Borrar=2:\n Modificar=3:\n Consultar todo=4:\n Ver detalles de algun curso=5:\n"))
        if opcion == 1:
            idcurso_tema = int(input("id de curso_tema: \n"))  
            idcurso = int(input("id del curso: \n"))   
            idtema = int(input("Id del tema: \n"))
            add = Curso_Tema(idcurso_tema,idcurso,idtema)
            add.Agregar()
            print("Se han agregado")
        if opcion == 2:
            archivo = open("./archivos/curso_tema.txt")
            print(archivo.read())
             
            archivo.close()
            idcurso_tema = int(input("Elija el curso a eliminar:\n"))
            idcurso = input("Elija el nombre del curso a eliminar:\n")
            idtema = int(input("Elija el id del empleado a eliminar:\n"))
            print("se ha eliminado el curso ")
            delete = Curso_Tema(idcurso_tema,idcurso,idtema)
            
            delete.Eliminar
        if opcion == 3:

            f = open("./archivos/curso_tema.txt")
            print(f.read())
            f.close()
            idcurso_tema = int(input("Elija el id curso_tema a modificar:\n"))
            idcurso = int(input("Elija el id del curso a modificar:\n"))
            idtema = int(input("Elija el id del tema a mmodificar:\n"))
            mod = Curso(idcurso_tema,idcurso,idtema)
            mod.Modificar
        if opcion == 4:
            print("Esta es toda la informacion en el archivo\n")
            f = open("./archivos/curso_tema.txt")
            print(f.read())
            f.close()
        if opcion == 5:
            print("Esta es toda la informacion en el archivo\n")
            f = open("./archivos/curso_tema.txt")
            print(f.read())
            f.close()
            linea = int(input("Escribe la linea que deseas ver"))
            f = open("./archivos/curso_tema.txt")
            linea = f.readline()
            print(linea)
            f.close()

            





#---Opcion de MENU para el apartado de Tema---
if accion == 4:
         opcion = int(input("Dime que deseas hacer en este archivo:\n Agregar= 1:\n Borrar=2:\n Modificar=3:\n Consultar todo=4:\n Ver detalles de algun curso=5:\n"))
         if opcion == 1:
             idtema = int(input("id del tema: \n"))  
             nombre = input("nombre del tema: \n")   
             add = Tema(idtema,nombre)
             add.Agregar()
             print("Se han agregado")
         
         if opcion == 2:    
             archivo_tema = open("./archivos/tema.txt")
             print(archivo_tema.read())
             
             archivo_tema.close()
             idtema = int(input("Elija el id del tema a eliminar:\n"))
             nombre = input("Elija el nombre del tema a eliminar:\n")
             print("Eliminacion confirmada ")
             delete = Tema(idtema,nombre)
             delete.Eliminar  
         
         if opcion == 3:    
             f = open("./archivos/tema.txt")
             print(archivo_tema.read())
             f.close()
             idtema = int(input("Elija el tema a modificar:\n"))
             nombre = input("Elija el nombre del tema a modificar:\n")
             mod = Tema(idtema,nombre)
             mod.Modificar
         
         if opcion == 4:
             print("Esta es toda la informacion en el archivo\n")
             f = open("./archivos/tema.txt")
             print(f.read())
             f.close()

         if opcion == 5:
             print("Estos son los detalles de los Temas:\n")
             f = open("./archivos/tema.txt")
             print(f.read())
             f.close()
             linea = int(input("Escribe la linea que deseas ver"))
             f = open("./archivos/tema.txt")
             linea = f.readline()
             print(linea)
             f.close()