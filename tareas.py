
# Definimos la clase Tarea
class Tarea:
    def __init__(self, descripcion:str, completada=False):
        self.__descripcion = descripcion
        self.__completada = completada
        
    def set_completada(self, completada:bool):
        self.__completada = completada
        
    def get_completada(self)->bool:
        return self.__completada
    
    def set_descripcion(self, descripcion: str):
        self.__descripcion = descripcion
        
    def get_descripcion(self)->str: 
        return self.__descripcion

# Definimos una clase que va a ser una lista de objetos de la clase Tarea
class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion:str):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)

    def marcar_completada(self, indice):
        # Controlamos la excepcion de que el indice pasado por parametro no esté en el rango de tareas
        try:
            self.tareas[indice].set_completada(True)
        except IndexError:
            print("El número de la tarea para marcar como completada no existe. (Error: Índice fuera de rango)")
            
    # Muestra el listado de las tareas, devuelve False sin no tiene nada que mostrar, True en caso contrario
    def mostrar_tareas(self):
        # Preguntamos a la lista si es vacia
        if not self.tareas:
            print("No hay tareas en el listado de tareas.")
        else:
            for i, tarea in enumerate(self.tareas):
                estado = "Completada" if tarea.get_completada() else "Pendiente"
                print(f"{i + 1}.- {tarea.get_descripcion()} - {estado}")
        return self.tareas

    def eliminar_tarea(self, indice):
        try:
            del self.tareas[indice]
        except IndexError:
            print("El número de la tarea a eliminar no existe (Error: Índice fuera de rango)")
        except ValueError:
            print("No ha introducido un numero correcto")

# Función principal del programa
def main():
    listado_de_tareas = ListaTareas()

    while True:
        print("\n***** GESTIÓN DE TAREAS *****")
        print("***** Listado de opciones *****")
        print()
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Listar todas las tareas")
        print("4. Borrar tarea")
        print("5. Salir")
        print()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descripcion = input("Escriba la descripción de la tarea: ")
            listado_de_tareas.agregar_tarea(descripcion)
        elif opcion == "2":
            if listado_de_tareas.mostrar_tareas():
                indice = int(input("Escriba el número de la tarea a marcar como completada: ")) - 1
                listado_de_tareas.marcar_completada(indice)
        elif opcion == "3":
            listado_de_tareas.mostrar_tareas()
        elif opcion == "4":
            while listado_de_tareas.mostrar_tareas():
                try:
                    indice = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
                    listado_de_tareas.eliminar_tarea(indice)
                    break
                except ValueError:
                    print("No ha introducido un numero")
        elif opcion == "5":
            print("¡Gracias por usar este programa!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción correcta.")

# Usamos un entry point
if __name__ == "__main__":
    main()
    