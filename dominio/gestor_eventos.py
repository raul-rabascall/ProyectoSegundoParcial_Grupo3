"""
========================================================
PROYECTO_PRIMER_PARCIAL_POO_GRUPO_3
--------------------------------------------------------
Archivo: gestor_eventos.py

Descripción:
Clase encargada de administrar todos los
servicios registrados dentro del sistema.

Esta clase permite:
- Almacenar servicios
- Agregar nuevos servicios
- Calcular totales generales
- Mostrar reportes completos

La clase trabaja aplicando polimorfismo,
permitiendo manejar distintos tipos de
servicios mediante una sola colección.

Autor: Grupo 3
Materia: Programación Orientada a Objetos
========================================================
"""


class GestorEventos:

    """
    Clase encargada de gestionar
    los servicios del sistema.
    """

    def __init__(self):

        """
        Constructor de la clase.

        Inicializa una lista vacía
        para almacenar servicios.
        """

        self._servicios = []

    # ====================================================
    # AGREGAR SERVICIOS
    # ====================================================

    def agregar_servicio(self, servicio):

        """
        Agrega un nuevo servicio
        a la lista de servicios.

        Parámetros:
        servicio -> Objeto de cualquier clase
                    que implemente calcular_total()
                    y mostrar_info().
        """

        self._servicios.append(servicio)

    # ====================================================
    # CALCULAR TOTALES
    # ====================================================

    def calcular_totales(self):

        """
        Calcula el total acumulado
        de todos los servicios registrados.
        """

        total = 0

        for servicio in self._servicios:
            total += servicio.calcular_total()

        return total

    # ====================================================
    # MOSTRAR REPORTE
    # ====================================================

    def mostrar_reporte(self):

        """
        Muestra un reporte completo
        de todos los servicios registrados.
        """

        print("\n===== REPORTE DE SERVICIOS =====\n")

        for servicio in self._servicios:
            print(servicio.mostrar_info())

        print(f"\nTOTAL GENERAL: ${self.calcular_totales()}")


# =========================
# PRUEBAS
# =========================

if __name__ == "__main__":

    """
    Bloque de pruebas de ejecución directa.
    """

    class ServicioPrueba:

        """
        Clase auxiliar utilizada
        para probar GestorEventos.
        """

        def __init__(self, nombre, total):

            """
            Constructor de la clase.

            Parámetros:
            nombre -> Nombre del servicio.
            total  -> Valor total del servicio.
            """

            self.nombre = nombre
            self.total = total

        def calcular_total(self):

            """
            Retorna el total del servicio.
            """

            return self.total

        def mostrar_info(self):

            """
            Retorna información del servicio.
            """

            return f"Servicio: {self.nombre} | Total: ${self.total}"


    # ====================================================
    # CREACION DEL GESTOR
    # ====================================================

    gestor = GestorEventos()

    # ====================================================
    # CREACION DE SERVICIOS DE PRUEBA
    # ====================================================

    servicio1 = ServicioPrueba("Decoracion", 150.00)
    servicio2 = ServicioPrueba("Catering", 320.50)
    servicio3 = ServicioPrueba("Sonido", 200.00)

    # ====================================================
    # AGREGAR SERVICIOS AL GESTOR
    # ====================================================

    gestor.agregar_servicio(servicio1)
    gestor.agregar_servicio(servicio2)
    gestor.agregar_servicio(servicio3)

    # ====================================================
    # MOSTRAR REPORTE FINAL
    # ====================================================

    gestor.mostrar_reporte()