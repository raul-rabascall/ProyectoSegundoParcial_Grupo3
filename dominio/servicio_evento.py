# Integrantes:
# - Bajaña Alexander
# - Gonzalez Scarlet# 
# - Guzmán Nasly
# - Rabascall Raul
# - Robins Emeli

"""
========================================================
PROYECTO_PRIMER_PARCIAL_POO_GRUPO_3
--------------------------------------------------------
Archivo: servicio_evento.py

Descripción:
Clase base del sistema de gestión de eventos.
Representa un servicio genérico del cual pueden
heredar otras clases especializadas.

Esta clase aplica:
- Encapsulamiento
- Propiedades (@property)
- Validaciones básicas
- Polimorfismo mediante calcular_total()

Autor: Grupo 3
Materia: Programación Orientada a Objetos
========================================================
"""


class ServicioEvento:

    """
    Clase base para representar servicios generales
    dentro del sistema.
    """

    def __init__(self, codigo, nombre, descripcion):

        """
        Constructor de la clase.

        Parámetros:
        codigo      -> Código identificador del servicio.
        nombre      -> Nombre del servicio.
        descripcion -> Descripción general del servicio.
        """

        self._codigo = None
        self._nombre = None
        self._descripcion = None

        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion

    # ====================================================
    # PROPIEDAD CODIGO
    # ====================================================

    @property
    def codigo(self):

        """
        Obtiene el código del servicio.
        """

        return self._codigo

    @codigo.setter
    def codigo(self, valor):

        """
        Valida y asigna el código.
        Si está vacío, asigna un valor por defecto.
        """

        if valor == "":
            self._codigo = "SIN-CODIGO"
        else:
            self._codigo = valor

    # ====================================================
    # PROPIEDAD NOMBRE
    # ====================================================

    @property
    def nombre(self):

        """
        Obtiene el nombre del servicio.
        """

        return self._nombre

    @nombre.setter
    def nombre(self, valor):

        """
        Valida y asigna el nombre.
        """

        if valor == "":
            self._nombre = "Sin nombre"
        else:
            self._nombre = valor

    # ====================================================
    # PROPIEDAD DESCRIPCION
    # ====================================================

    @property
    def descripcion(self):

        """
        Obtiene la descripción del servicio.
        """

        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):

        """
        Valida y asigna la descripción.
        """

        if valor == "":
            self._descripcion = "Sin descripcion"
        else:
            self._descripcion = valor

    # ====================================================
    # METODOS GENERALES
    # ====================================================

    def calcular_total(self):

        """
        Método polimórfico base.

        Retorna:
        0.0 por defecto.
        Las clases hijas deben sobrescribirlo.
        """

        return 0.0

    def mostrar_info(self):

        """
        Retorna información resumida del servicio.
        """

        return f"[{self._codigo}] {self._nombre} - {self._descripcion}"

    def __str__(self):

        """
        Representación textual del objeto.
        """

        return (
            f"ServicioEvento | Codigo: {self._codigo} | "
            f"Nombre: {self._nombre} | "
            f"Total: ${self.calcular_total():.2f}"
        )


# =========================
# PRUEBAS
# =========================

if __name__ == "__main__":

    """
    Bloque de pruebas de ejecución directa.
    """

    print("=== PRUEBA 1 ===")

    servicio1 = ServicioEvento(
        "EV001",
        "Decoracion",
        "Decoracion para boda"
    )

    print(servicio1.mostrar_info())
    print(servicio1)
    print("Total:", servicio1.calcular_total())

    print("\n=== PRUEBA 2 ===")

    servicio2 = ServicioEvento(
        "",
        "",
        ""
    )

    print(servicio2.mostrar_info())
    print(servicio2)

    print("Codigo:", servicio2.codigo)
    print("Nombre:", servicio2.nombre)
    print("Descripcion:", servicio2.descripcion)
