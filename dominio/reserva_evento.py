"""
========================================================
PROYECTO_PRIMER_PARCIAL_POO_GRUPO_3
--------------------------------------------------------
Archivo: reserva_evento.py

Descripción:
Clase hija de ServicioEvento.
Representa una reserva para eventos especiales
como conciertos, festivales, obras de teatro
u otros espectáculos.

Esta clase implementa:
- Herencia
- Encapsulamiento
- Polimorfismo
- Validaciones mediante propiedades
- Sobrescritura de métodos

Autor: Grupo 3
Materia: Programación Orientada a Objetos
========================================================
"""

from servicio_evento import ServicioEvento


# from clase_base import ServicioEvento

class ReservaEvento(ServicioEvento):

    """
    Clase que representa una reserva de evento.
    Hereda de ServicioEvento.
    """

    def __init__(self, codigo, nombre, num_personas, ubicacion, servicio_incluido):

        """
        Constructor de la clase.

        Parámetros:
        codigo             -> Código identificador de la reserva.
        nombre             -> Nombre del evento.
        num_personas       -> Cantidad de personas.
        ubicacion          -> Tipo de ubicación del evento.
        servicio_incluido  -> Servicio adicional incluido.
        """

        super().__init__(codigo, nombre, f"Reserva de evento - {nombre}")

        self._num_personas = None
        self._ubicacion = None
        self._servicio_incluido = None

        self.num_personas = num_personas
        self.ubicacion = ubicacion
        self.servicio_incluido = servicio_incluido

    # ====================================================
    # PROPIEDAD NUM_PERSONAS
    # ====================================================

    @property
    def num_personas(self):

        """
        Obtiene la cantidad de personas.
        """

        return self._num_personas

    @num_personas.setter
    def num_personas(self, valor):

        """
        Valida la cantidad de personas.
        Si el valor es menor o igual a cero,
        asigna 1 por defecto.
        """

        if valor <= 0:
            self._num_personas = 1
        else:
            self._num_personas = valor

    # ====================================================
    # PROPIEDAD UBICACION
    # ====================================================

    @property
    def ubicacion(self):

        """
        Obtiene la ubicación seleccionada.
        """

        return self._ubicacion

    @ubicacion.setter
    def ubicacion(self, valor):

        """
        Valida la ubicación y asigna
        automáticamente el precio correspondiente.
        """

        if valor == "general":
            self._ubicacion = "general"
            self._precio_ubicacion = 15.00

        elif valor == "preferencial":
            self._ubicacion = "preferencial"
            self._precio_ubicacion = 25.00

        elif valor == "vip":
            self._ubicacion = "vip"
            self._precio_ubicacion = 50.00

        elif valor == "palco":
            self._ubicacion = "palco"
            self._precio_ubicacion = 80.00

        else:
            self._ubicacion = "general"
            self._precio_ubicacion = 15.00

    # ====================================================
    # PROPIEDAD SERVICIO_INCLUIDO
    # ====================================================

    @property
    def servicio_incluido(self):

        """
        Obtiene el servicio incluido.
        """

        return self._servicio_incluido

    @servicio_incluido.setter
    def servicio_incluido(self, valor):

        """
        Valida el servicio incluido y asigna
        automáticamente el costo correspondiente.
        """

        if valor == "ninguno":
            self._servicio_incluido = "ninguno"
            self._costo_servicio = 0.00

        elif valor == "buffet":
            self._servicio_incluido = "buffet"
            self._costo_servicio = 12.00

        elif valor == "cena":
            self._servicio_incluido = "cena"
            self._costo_servicio = 20.00

        elif valor == "bebidas":
            self._servicio_incluido = "bebidas"
            self._costo_servicio = 8.00

        else:
            self._servicio_incluido = "ninguno"
            self._costo_servicio = 0.00

    # ====================================================
    # METODOS SOBRESCRITOS
    # ====================================================

    def calcular_total(self):

        """
        Calcula el total a pagar.

        Fórmula:
        (precio ubicación + costo servicio)
        multiplicado por el número de personas.
        """

        total = (
            self._precio_ubicacion +
            self._costo_servicio
        ) * self._num_personas

        return round(total, 2)

    def mostrar_info(self):

        """
        Retorna la información detallada
        de la reserva del evento.
        """

        return (
            f"RESERVA EVENTO | Codigo: {self._codigo}\n"
            f"  Evento           : {self._nombre}\n"
            f"  Numero personas  : {self._num_personas}\n"
            f"  Ubicacion        : {self._ubicacion.capitalize()}\n"
            f"  Servicio incluido: {self._servicio_incluido.capitalize()}\n"
            f"  Total a pagar    : ${self.calcular_total():.2f}"
        )

    def __str__(self):

        """
        Representación textual del objeto.
        """

        return (
            f"ReservaEvento | {self._nombre} | Personas: {self._num_personas} | "
            f"Ubicacion: {self._ubicacion} | Servicio: {self._servicio_incluido} | "
            f"Total: ${self.calcular_total():.2f}"
        )

    # ====================================================
    # PRUEBAS
    # ====================================================

if __name__ == "__main__":
        print("=== PRUEBA 1 ===")

        reserva1 = ReservaEvento(
            "RE-001",
            "Concierto Rock",
            4,
            "vip",
            "cena"
        )

        print(reserva1.mostrar_info())
        print(reserva1)

        print("\n=== PRUEBA 2 ===")

        reserva2 = ReservaEvento(
            "",
            "",
            0,
            "zona_invalida",
            "servicio_invalido"
        )

        print(reserva2.mostrar_info())
        print(reserva2)