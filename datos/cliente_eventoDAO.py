from datos.conexion import Conexion
# Proyecto Segundo Parcial - GUI con Base de Datos
# Asignatura: Programación Orientada a Objetos
# Jornada: Vespertina
# Grupo:
# Integrantes:
# -
# -
# -
# -

from datos.conexion import Conexion
from dominio.cliente_evento import ClienteEvento


class ClienteEventoDAO:
    """DAO para las operaciones CRUD en la base de datos."""

    _INSERT = "INSERT INTO dbo.objeto (cedula, nombre, correo, telefono, tipo_sala) VALUES (?, ?, ?, ?, ?)"
    _SELECT = "SELECT cedula, nombre, correo, telefono, tipo_sala FROM dbo.objeto WHERE cedula = ?"
    _UPDATE = "UPDATE dbo.objeto SET nombre = ?, correo = ?, telefono = ?, tipo_sala = ? WHERE cedula = ?"
    _DELETE = "DELETE FROM dbo.objeto WHERE cedula = ?"

    @classmethod
    def insertar(cls, cliente):
        try:
            with Conexion.obtener_cursor() as cursor:
                datos = (cliente.cedula, cliente.nombre, cliente.correo, cliente.telefono, cliente.tipo_sala)
                cursor.execute(cls._INSERT, datos)
                Conexion.obtener_conexion().commit()
                return cursor.rowcount
        except Exception as e:
            print(f"Error en insertar: {e}")
            return -1

    @classmethod
    def seleccionar_x_cedula(cls, cedula):
        cliente = None
        try:
            with Conexion.obtener_cursor() as cursor:
                cursor.execute(cls._SELECT, (cedula,))
                rs = cursor.fetchone()
                if rs:
                    # Mapeamos los 5 campos retornados por la base de datos
                    cliente = ClienteEvento(cedula=rs[0], nombre=rs[1], correo=rs[2],
                                            telefono=rs[3], tipo_sala=rs[4])
        except Exception as e:
            print(f"Error en seleccionar_x_cedula: {e}")
        return cliente

    @classmethod
    def actualizar(cls, cliente):
        try:
            with Conexion.obtener_cursor() as cursor:
                datos = (cliente.nombre, cliente.correo, cliente.telefono, cliente.tipo_sala, cliente.cedula)
                cursor.execute(cls._UPDATE, datos)
                Conexion.obtener_conexion().commit()
                return cursor.rowcount
        except Exception as e:
            print(f"Error en actualizar: {e}")
            return -1

    @classmethod
    def eliminar(cls, cedula):
        try:
            with Conexion.obtener_cursor() as cursor:
                cursor.execute(cls._DELETE, (cedula,))
                Conexion.obtener_conexion().commit()
                return cursor.rowcount
        except Exception as e:
            print(f"Error en eliminar: {e}")
            return -1