"""
========================================================
PROYECTO_PRIMER_PARCIAL_POO_GRUPO_3
--------------------------------------------------------
Archivo: entrada_cine.py

Descripción:
Clase hija de ServicioEvento.
Representa la compra de entradas de cine
dentro del sistema de entretenimiento.

Esta clase implementa:
- Herencia
- Encapsulamiento
- Validaciones mediante propiedades
- Polimorfismo
- Sobrescritura de métodos
- Cálculo automático de precios

Autor: Grupo 3
Materia: Programación Orientada a Objetos
========================================================
"""

from servicio_evento import ServicioEvento

# from clase_base import Servicioevento

class Entradacine(ServicioEvento):

    """
    Clase que representa una entrada de cine.
    Hereda de ServicioEvento.
    """

    def __init__(self, codigo, nombre, tipo_sala, horario, categoria, cantidad):

        """
        Constructor de la clase.

        Parámetros:
        codigo     -> Código identificador de la entrada.
        nombre     -> Nombre de la película o función.
        tipo_sala  -> Tipo de sala seleccionada.
        horario    -> Horario de la función.
        categoria  -> Categoría del cliente.
        cantidad   -> Cantidad de entradas.
        """

        super().__init__(codigo, nombre, f"Entrada de cine - Sala {tipo_sala}")

        self._tipo_sala = None
        self._horario = None
        self._categoria = None
        self._cantidad = None

        self.tipo_sala = tipo_sala
        self.horario = horario
        self.categoria = categoria
        self.cantidad = cantidad

    # ====================================================
    # PROPIEDAD TIPO_SALA
    # ====================================================

    @property
    def tipo_sala(self):

        """
        Obtiene el tipo de sala.
        """

        return self._tipo_sala

    @tipo_sala.setter
    def tipo_sala(self, valor):

        """
        Valida el tipo de sala y asigna
        automáticamente el precio correspondiente.
        """

        if valor == "2D":
            self._tipo_sala = "2D"
            self._precio_sala = 5.00

        elif valor == "3D":
            self._tipo_sala = "3D"
            self._precio_sala = 7.50

        elif valor == "IMAX":
            self._tipo_sala = "IMAX"
            self._precio_sala = 10.00

        elif valor == "4DX":
            self._tipo_sala = "4DX"
            self._precio_sala = 12.00

        else:
            self._tipo_sala = "2D"
            self._precio_sala = 5.00

    # ====================================================
    # PROPIEDAD HORARIO
    # ====================================================

    @property
    def horario(self):

        """
        Obtiene el horario seleccionado.
        """

        return self._horario

    @horario.setter
    def horario(self, valor):

        """
        Valida el horario y asigna
        automáticamente un multiplicador de precio.
        """

        if valor == "matinal":
            self._horario = "matinal"
            self._mult_horario = 0.80

        elif valor == "normal":
            self._horario = "normal"
            self._mult_horario = 1.00

        elif valor == "noche":
            self._horario = "noche"
            self._mult_horario = 1.20

        else:
            self._horario = "normal"
            self._mult_horario = 1.00

    # ====================================================
    # PROPIEDAD CATEGORIA
    # ====================================================

    @property
    def categoria(self):

        """
        Obtiene la categoría del cliente.
        """

        return self._categoria

    @categoria.setter
    def categoria(self, valor):

        """
        Valida la categoría y asigna
        automáticamente el descuento correspondiente.
        """

        if valor == "general":
            self._categoria = "general"
            self._descuento = 0.00

        elif valor == "estudiante":
            self._categoria = "estudiante"
            self._descuento = 0.15

        elif valor == "tercera_edad":
            self._categoria = "tercera_edad"
            self._descuento = 0.20

        elif valor == "nino":
            self._categoria = "nino"
            self._descuento = 0.25

        else:
            self._categoria = "general"
            self._descuento = 0.00

    # ====================================================
    # PROPIEDAD CANTIDAD
    # ====================================================

    @property
    def cantidad(self):

        """
        Obtiene la cantidad de entradas.
        """

        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):

        """
        Valida la cantidad de entradas.
        Si el valor es menor o igual a cero,
        asigna 1 por defecto.
        """

        if valor <= 0:
            self._cantidad = 1
        else:
            self._cantidad = valor

    # ====================================================
    # METODOS SOBRESCRITOS
    # ====================================================

    def calcular_total(self):

        """
        Calcula el total a pagar por las entradas.

        Fórmula:
        precio sala * multiplicador horario *
        (1 - descuento) * cantidad
        """

        precio_unitario = self._precio_sala * self._mult_horario * (1 - self._descuento)

        return round(precio_unitario * self._cantidad, 2)

    def mostrar_info(self):

        """
        Retorna información detallada
        de la entrada de cine.
        """

        return (
            f"ENTRADA CINE | Codigo: {self._codigo}\n"
            f"  Pelicula/Funcion : {self._nombre}\n"
            f"  Sala             : {self._tipo_sala}\n"
            f"  Horario          : {self._horario.capitalize()}\n"
            f"  Categoria        : {self._categoria.capitalize()}\n"
            f"  Cantidad         : {self._cantidad} entrada(s)\n"
            f"  Total a pagar    : ${self.calcular_total():.2f}"
        )

    def __str__(self):

        """
        Representación textual del objeto.
        """

        return (
            f"EntradaCine | {self._nombre} | Sala: {self._tipo_sala} | "
            f"Horario: {self._horario} | Categoria: {self._categoria} | "
            f"Cantidad: {self._cantidad} | Total: ${self.calcular_total():.2f}"
        )


class EntradaCine:
    pass


# =========================
# PRUEBAS
# =========================

if __name__ == "__main__":

    """
    Bloque de pruebas de ejecución directa.
    """

    print("=== PRUEBA 1 ===")

    entrada1 = Entradacine(
        "C001",
        "Avengers Endgame",
        "IMAX",
        "noche",
        "estudiante",
        3
    )

    print(entrada1.mostrar_info())
    print()
    print(entrada1)

    print("\n=== PRUEBA 2 ===")

    entrada2 = Entradacine(
        "",
        "",
        "XD",
        "mañana",
        "vip",
        -5
    )

    print(entrada2.mostrar_info())
    print()
    print(entrada2)