# Sistema de Administración de Cine - Proyecto Segundo Parcial GUI con Base de Datos

**Asignatura:** Programación Orientada a Objetos  
**Universidad:** Universidad de Guayaquil  
**Grupo:** Grupo 3  

---

### 1. Título del proyecto
Sistema de Administración de Cine - Gestión de Clientes y Salas

### 2. Descripción general del sistema
Es una aplicación de escritorio con interfaz gráfica orientada a gestionar la asignación de clientes a diferentes salas de un cine. El sistema se conecta de forma directa a una base de datos relacional para garantizar la persistencia de los datos, permitiendo un manejo fluido del flujo de información.

### 3. Integrantes del grupo
* Bajaña Alexander
* Gonzalez Scarlet
* Guzmán Nasly
* Rabascall Raul
* Robins Emeli

### 4. Jornada
[Matutina / Vespertina - Reemplazar con tu jornada]

### 5. Funcionalidades implementadas
El sistema cumple estrictamente con las operaciones CRUD requeridas:
* **Ingreso (Create):** Permite registrar nuevos clientes con su cédula, nombre, teléfono, correo y tipo de sala asignada.
* **Visualización (Read):** Consulta los datos de un cliente en tiempo real desde la base de datos buscando por su número de cédula y los carga en la interfaz gráfica.
* **Actualización (Update):** Modifica la información, el contacto o el tipo de sala de un cliente previamente registrado y guarda los cambios permanentemente.
* **Eliminación (Delete):** Borra por completo el registro de un cliente en la base de datos mediante su número de cédula.
* **Limpieza Automática:** Vacía los campos de texto y restablece la selección de la interfaz para facilitar un nuevo flujo de trabajo.

### 6. Tecnologías utilizadas
* **Lenguaje:** Python 3.
* **Interfaz Gráfica (GUI):** PySide6 (compilado desde Qt Designer).
* **Base de Datos:** Microsoft SQL Server.
* **Conector de Base de Datos:** Librería `pyodbc`.
* **Patrón de Diseño:** Modelo-Vista-Controlador (MVC) y Data Access Object (DAO).

### 7. Instrucciones para ejecutar el proyecto
1.  Clonar el repositorio en tu máquina local.
2.  Asegurarse de tener instalado Python y ejecutar `pip install PySide6 pyodbc`.
3.  Abrir **SQL Server Management Studio (SSMS)**, comprobar que la Autenticación Mixta está habilitada y ejecutar el script SQL adjunto en el proyecto para generar la base de datos `SAP_VES`, el usuario `admin_VES` y la tabla `objeto`.
4.  Ejecutar el archivo `main.py` desde la raíz del proyecto para inicializar el sistema.

### 8. Estructura del proyecto
El código está organizado en las siguientes capas lógicas:
* `/datos/`: Contiene la lógica de persistencia (`conexion.py` y `cliente_eventoDAO.py`).
* `/dominio/`: Contiene las clases y entidades principales de negocio (`cliente_evento.py`, `entrada_cine.py`, `gestor_eventos.py`, `reserva_evento.py`, `servicio_evento.py`).
* `/GUI/`: Almacena el diseño visual y el archivo compilado de la ventana (`vtn_principal.ui` y `vtn_principal.py`).
* `/servicio/`: Contiene el controlador que enlaza la GUI con los datos (`persona.py`).
* `main.py`: Archivo principal de ejecución.

### 9. Descripción de la base de datos
Se utiliza la base de datos relacional **`SAP_VES`**. La información central se almacena en la tabla **`objeto`**, la cual cuenta con la siguiente estructura:
* `id`: (INT IDENTITY) Identificador único autoincremental de control interno.
* `cedula`: (VARCHAR 10) Llave Primaria (Primary Key). Evita duplicidad de clientes.
* `nombre`: (VARCHAR 50) Almacena el nombre del cliente (No Nulo).
* `telefono`: (VARCHAR 10) Número de contacto.
* `correo`: (VARCHAR 50) Email del cliente.
* `tipo_sala`: (VARCHAR 30) Almacena la sala asignada seleccionada desde la GUI.

Se creó un usuario específico `admin_VES` con roles restringidos para ejecutar únicamente transacciones seguras (Insert, Select, Update, Delete) sobre esta tabla.

### 10. Capturas de pantalla de la GUI
![Ventana Principal del Sistema](Ruta/A/Tu/Imagen_GUI.png)
*(Reemplaza el texto entre paréntesis con la ruta de tu captura de pantalla de la ventana)*

### 11. Evidencia de conexión a la base de datos
![Evidencia de registros en SQL Server](Ruta/A/Tu/Imagen_SQL.png)
*(Reemplaza el texto entre paréntesis con una captura de SQL Server donde se vean los registros guardados)*

### 12. Enlace al video demostrativo
[▶️ Clic aquí para ver el video demostrativo en YouTube / Drive]
*(Asegúrate de pegar el link real aquí, verificar que no supere los 3 minutos y que tenga permisos públicos)*

### 13. Explicación breve de las validaciones implementadas
Para garantizar la integridad de los datos antes de viajar a SQL Server, se implementaron las siguientes validaciones en la capa de servicios:
* **Campos Obligatorios:** Verificación lógica para asegurar que nombre, cédula, teléfono y correo no se envíen vacíos.
* **Validación de Formato:** El correo electrónico requiere forzosamente contener un símbolo `@` y un punto `.`.
* **Validación de Selección (ComboBox):** Se impide realizar el guardado o la actualización si el menú desplegable del Tipo de Sala se encuentra en su estado por defecto ("Seleccionar").
* **Límites Nativos:** Se aplicó el atributo `maxLength` directamente en PySide6 para truncar visualmente la cédula y teléfono a un máximo de 10 caracteres, y el correo y nombre a 50, coincidiendo a la perfección con las capacidades de la base de datos para evitar errores de almacenamiento.

### 14. Estado final del proyecto
**Finalizado y Completamente Funcional.** El sistema cumple con todos los requerimientos de la rúbrica, incluyendo el desarrollo de la GUI, integración total con base de datos externa y ejecución exitosa de todas las operaciones CRUD y validaciones restrictivas.
