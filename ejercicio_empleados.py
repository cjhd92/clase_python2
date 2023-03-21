"""
Ejercicio 1 POO

Está realizado de forma simplificada centrado en POO, no se realizan muchas comprobaciones y entradas
de datos del usuario pero debería hacerse en un caso de aplicación real y siempre que lo pida el enunciado del ejercicio.
"""


from model.empleado_fijo import EmpleadoFijo
from model.empleado_temporal import EmpleadoTemporal


class GestionEmpleados(object):
    def __init__(self):
        self.empleados = {}
        self.menu = """
Menú de opciones

(1) Añadir empleado
(2) Borrar empleado
(3) Mostrar lista empleados
(4) Mostrar detalle de un empleado
(5) Mostrar empleados cumpleaños
(6) Terminar

Elige una opción: """
        
    def add_test_data(self):
        emp1 = EmpleadoFijo(nif = "32.234.234M", 
            nombre = "Pedro Rodríguez Martínez", 
            fecha_nacimiento="12/05/1985", 
            sueldo=2000, complemento=200, anho_alta=2010)

        emp2 = EmpleadoTemporal(nif="33.345.879Z", 
            nombre="Lucía López Rodríguez", 
            fecha_nacimiento="02/01/1990",
            sueldo=2000, 
            fecha_alta="02/01/2021",
            fecha_baja="31/12/2021")

        self.empleados["32.234.234M"] = emp1
        self.empleados["33.345.879Z"] = emp2

    def borrar_empleado(self):
        nif = input("Introduce el nif del empleado que quieres borrar: ")
        empleado = self.empleados.get(nif)
        if empleado == None:
            print("No existe ningún empleado con ese nif")
        else:
            del self.empleados[nif]

    def add_empleado(self):
        print("Introduce los datos del empleado:")
        tipo = input("Tipo de empleado (fijo/temporal): ")
        while (tipo not in ["fijo", "temporal"]):
            print("Tipo incorrecto.")
            tipo = input("Tipo de empleado (fijo/temporal): ")

        empleado = self.pedir_datos_empleado(tipo)
        self.empleados[empleado.nif] = empleado

    def pedir_datos_empleado(self, tipo):
        if tipo == "fijo":
            empleado = self.pedir_datos_emp_fijo()
        else:
            empleado = self.pedir_datos_emp_temporal()

        return empleado

    def pedir_datos_comunes(self, empleado):
        nombre = input("Introduce el nombre: ")
        nif = input("Introduce el nif: ")
        fecha_nacimiento = input("Introduce la fecha de nacimiento (dd/mm/aaaa): ")
        sueldo = int(input("Introduce el sueldo mensual: " ))
        empleado.nombre = nombre
        empleado.nif = nif
        empleado.fecha_nacimiento = fecha_nacimiento
        empleado.sueldo = sueldo

    def pedir_datos_emp_fijo(self):
        empleado = EmpleadoFijo()
        self.pedir_datos_comunes(empleado)
        anho = int(input("Introduce el año de alta en la empresa: "))
        comp = int(input("Introduce el complemento anual: "))
        empleado.anho_alta = anho
        empleado.complemento = comp
        return empleado

    def pedir_datos_emp_temporal(self):
        empleado = EmpleadoTemporal()
        self.pedir_datos_emp_temporal()
        fecha_alta = input("Introduce la fecha de alta (dd/mm/aaaa): ")
        fecha_baja = input("Introduce la fecha de baja (dd/mm/aaaa): ")
        # En un caso real, se tendría que comprobar que la fecha es correcta
        empleado.fecha_alta = fecha_alta
        empleado.fecha_baja = fecha_baja
        return empleado

    def listar_empleados(self):
        print()
        for empleado in self.empleados.values():
            print(empleado)

    def mostrar_detalle_empleado(self):
        nif = input("Introduce el nif del empleado que quieres consultar: ")
        empleado = self.empleados.get(nif)
        if empleado == None:
            print("No existe ningún empleado con ese nif")
        else:
            empleado.mostrar_datos()

    def mostrar_empleados_cumple(self):
        mes = int(input("\nIntroduce un mes (1 - 12): "))
        emp_cumples = [emp for emp in self.empleados.values() if emp.es_mes_cumpleanhos(mes)]
        if (len(emp_cumples)>0):
            print("\nEstán de cumpleaños: ")
            for emp in emp_cumples:
                print(f"{emp.nombre}, {emp.fecha_nacimiento}")
        else:
            print("\nNo hay ningún cumpleaños")
        print()

    def ejecutar_programa(self):
        option = 1
        while option != 6:
            option = int(input(self.menu))
            if option == 1:
                self.add_empleado()
            elif option == 2:
                self.borrar_empleado()
            elif option == 3:
                self.listar_empleados()
            elif option == 4:
                self.mostrar_detalle_empleado()
            elif option == 5:
                self.mostrar_empleados_cumple()


if __name__ == "__main__":
    gestion = GestionEmpleados()
    gestion.add_test_data()
    gestion.ejecutar_programa()
