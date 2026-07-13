# Proyecto Segundo Parcial - GUI con Base de Datos
# Asignatura: Programación Orientada a Objetos
# Jornada: Vespertina
# Grupo:
# Integrantes:
# -
# -
# -
# -

from PySide6.QtWidgets import QMainWindow, QMessageBox
from GUI.vtn_principal import Ui_vtn_principal
from datos.cliente_eventoDAO import ClienteEventoDAO
from dominio.cliente_evento import ClienteEvento


class PersonaServicio(QMainWindow):
    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)

        # Conexión de eventos
        self.ui.btn_agregar.clicked.connect(self.guardar)
        self.ui.btn_limpiar.clicked.connect(self.limpiar)
        self.ui.btn_buscar.clicked.connect(self.buscar)
        self.ui.btn_actualizar.clicked.connect(self.actualizar)
        self.ui.btn_eliminar.clicked.connect(self.eliminar)

    def guardar(self):
        nombre = self.ui.txt_nombre.text().strip()
        cedula = self.ui.txt_cedula.text().strip()
        telefono = self.ui.txt_telefono.text().strip()
        correo = self.ui.txt_correo.text().strip()
        tipo_sala = self.ui.cb_tipo_sala.currentText()

        # Validación de campos de texto
        if nombre == '' or cedula == '' or telefono == '' or correo == '':
            QMessageBox.warning(self, "Advertencia", "Por favor, complete todos los campos obligatorios.")
            return

        # Validación del ComboBox
        if tipo_sala == "Seleccionar":
            QMessageBox.warning(self, "Advertencia", "Por favor, seleccione un Tipo de Sala válido.")
            return

        if '@' not in correo or '.' not in correo:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese un correo electrónico válido.")
            return

        try:
            cliente = ClienteEvento(cedula=cedula, nombre=nombre, correo=correo,
                                    telefono=telefono, tipo_sala=tipo_sala)
            if ClienteEventoDAO.insertar(cliente) > 0:
                self.ui.statusbar.showMessage('Cliente guardado correctamente', 3000)
                self.limpiar()
            else:
                QMessageBox.critical(self, 'Error', 'Error al guardar el registro en la base de datos.')
        except Exception as e:
            QMessageBox.critical(self, 'Excepción', f'Error inesperado: {e}')

    def buscar(self):
        cedula_buscar = self.ui.txt_buscar_cedula.text().strip()
        if cedula_buscar == '':
            QMessageBox.information(self, "Advertencia", "Ingrese una cédula en el campo de búsqueda.")
            return

        cliente = ClienteEventoDAO.seleccionar_x_cedula(cedula_buscar)
        if cliente:
            self.ui.txt_cedula.setText(cliente.cedula)
            self.ui.txt_nombre.setText(cliente.nombre)
            self.ui.txt_telefono.setText(cliente.telefono)
            self.ui.txt_correo.setText(cliente.correo)

            # Asigna la sala encontrada al ComboBox
            self.ui.cb_tipo_sala.setCurrentText(cliente.tipo_sala)

            self.ui.statusbar.showMessage('Registro cargado exitosamente', 3000)
        else:
            QMessageBox.information(self, "Información", "No se encontró ningún registro con esa cédula.")

    def actualizar(self):
        nombre = self.ui.txt_nombre.text().strip()
        cedula = self.ui.txt_cedula.text().strip()
        telefono = self.ui.txt_telefono.text().strip()
        correo = self.ui.txt_correo.text().strip()
        tipo_sala = self.ui.cb_tipo_sala.currentText()

        if nombre == '' or cedula == '' or telefono == '' or correo == '':
            QMessageBox.warning(self, "Advertencia", "Complete todos los campos del formulario para actualizar.")
            return

        if tipo_sala == "Seleccionar":
            QMessageBox.warning(self, "Advertencia", "Por favor, seleccione un Tipo de Sala válido.")
            return

        try:
            cliente = ClienteEvento(cedula=cedula, nombre=nombre, correo=correo,
                                    telefono=telefono, tipo_sala=tipo_sala)
            if ClienteEventoDAO.actualizar(cliente) > 0:
                self.ui.statusbar.showMessage('Registro actualizado correctamente', 3000)
                self.limpiar()
            else:
                QMessageBox.critical(self, 'Error', 'No se pudo actualizar el registro. Verifique la cédula.')
        except Exception as e:
            QMessageBox.critical(self, 'Excepción', f'Error: {e}')

    def eliminar(self):
        cedula_buscar = self.ui.txt_buscar_cedula.text().strip()
        if cedula_buscar == '':
            QMessageBox.information(self, "Advertencia", "Ingrese la cédula del registro que desea eliminar.")
            return

        try:
            if ClienteEventoDAO.eliminar(cedula_buscar) > 0:
                self.ui.statusbar.showMessage('Registro eliminado correctamente', 3000)
                self.limpiar()
            else:
                QMessageBox.critical(self, 'Error', 'No se encontró el registro para eliminar.')
        except Exception as e:
            QMessageBox.critical(self, 'Excepción', f'Error: {e}')

    def limpiar(self):
        self.ui.txt_nombre.clear()
        self.ui.txt_cedula.clear()
        self.ui.txt_telefono.clear()
        self.ui.txt_correo.clear()
        self.ui.txt_buscar_cedula.clear()

        # Devuelve el ComboBox a la opción inicial
        self.ui.cb_tipo_sala.setCurrentIndex(0)

        self.ui.txt_nombre.setFocus()