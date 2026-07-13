# Proyecto Segundo Parcial - GUI con Base de Datos
# Asignatura: Programación Orientada a Objetos
# Jornada: Vespertina
# Grupo:
# Integrantes:
# -
# -
# -
# -

class ClienteEvento:
    """Clase que representa a un cliente del sistema."""
    def __init__(self, cedula, nombre, correo, telefono, tipo_sala):
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.tipo_sala = tipo_sala

    @property
    def tipo_sala(self):
        return self._tipo_sala

    @tipo_sala.setter
    def tipo_sala(self, valor):
        if valor == "" or valor == "Seleccionar":
            self._tipo_sala = "Sin asignar"
        else:
            self._tipo_sala = valor

    def __str__(self):
        return (f"Cliente: {self.nombre} | Cédula: {self.cedula} | "
                f"Correo: {self.correo} | Teléfono: {self.telefono} | "
                f"Sala: {self.tipo_sala}")