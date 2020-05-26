#Menu Chido para el pia osi osi 

print("»"*60)

loop= True
while loop == True:
    accion=int(input("Dime a que archivo deseas entrar:\n Curso=1:\n Empleado=2:\n Video=3:\n Tema=4:\n Curso_Tema=5:\n Curso_Tema_Video=6:\n"))
    if accion == 1:
         opcion = int(input("Dime que deseas hacer en este archivo:\n Agregar= 1:\n Borrar=2:\n Modificar=3:\n Consultar todo=4:\n Ver detalles de algun curso=5:\n"))
         
             
             

        
    
             
         
        
             


             
        

             
             
              
             
             
             
            
            

            
    if accion == 2:
        opcion = int(input("Dime que deseas hacer en este archivo:\n Agregar= 1:\n Borrar=2:\n Modificar=3:\n Consultar todo=4:\n Ver detalles de algun empleado=5:\n"))
        if opcion == 1:
           #AGREGAR EMPLEADO OSI OSI
           archivo = open("./archivos/empleados.txt","a",encoding='utf8')
           idEmpleado = int(input("Dame el id del empleado crack: \n"))  
           nombre = input("Dame el nombre: \n")   
           direccion = input("Dame la direccion del empleado: \n")
         
           archivo.write( str(idEmpleado) + '!' + nombre + '!' + str(direccion))
           archivo.write("\n")
             

        
            
           archivo.close
        if opcion ==2:
            #BORRAR DATOS DE EMPLEADOS UWU
            listaborrado=[]
            borrado=input("Dime que dato deseas borrar de este archivo: \n")
            archivoread= open("./archivos/empleados.txt",encoding='utf8')
            print(archivoread.read())
            archivoread.close()



             












    