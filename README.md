## 👋 ¡Bienvenidos usuarios a mi proyecto! sistema en autenticacion

<img src="imagen_presentacion.png" alt="Presentación" width="205" align="left" style="margin-right:20px; border-radius:5px;">  
<p style="text-align: justify;">

Este proyecto consiste en el desarrollo de un sistema de autenticación de usuarios utilizando Python. Las credenciales (usuario y contraseña) se almacenan en un diccionario, lo que permite una gestión sencilla y eficiente de la información. 

El sistema permite registrar nuevos usuarios, iniciar sesión y mostrar los usuarios registrados mediante un menú interactivo en consola. Cada operación de autenticación se realiza mediante funciones reutilizables, garantizando una estructura organizada y modular del código.

El programa valida que los usuarios ingresen correctamente su nombre de usuario y contraseña, proporcionando retroalimentación inmediata en caso de error o éxito. Esto permite simular un sistema básico de control de acceso. Esta estructura no solo simula un sistema básico de autenticación, sino que también refuerza la organización de la información y la experiencia del usuario.

#
### 🧑‍💻 Lenguaje de programacion
- Python

#
### 🎯 Objetivos del proyecto
- Implementar diccionarios para almacenar usuarios y contraseñas.
- Aplicar funciones reutilizables para modularizar la lógica del programa.
- Utilizar condicionales y operadores lógicos para validar credenciales.
- Crear un menú interactivo que permita registrar usuarios, iniciar sesión y consultar los registros.
- Validar entradas para evitar errores y accesos no autorizados.
- Simular un sistema básico de autenticación de usuarios.

#
### 🧠 Temas que se a aplicado
- Diccionarios
- Funciones
- Condicionales (`if`, `elif`, `else`)
- Operadores lógicos (`and`, `or`)
- Bucles `while` para menú interactivo
- Validación de existencia de claves en diccionarios
- Control de errores y mensajes de retroalimentación

#
### ⚙️ Funcionamiento
1. Se crea un diccionario llamado `usuarios` donde:
   - La clave es el nombre de usuario.
   - El valor es la contraseña asociada.

2. El menú principal permite:
   - Registrar un nuevo usuario.
   - Iniciar sesión validando usuario y contraseña.
   - Mostrar todos los usuarios registrados.
   - Salir del sistema.

3. Al registrar un usuario:
   - Se verifica que el usuario no exista previamente.
   - Se guarda la contraseña asociada.

4. Al iniciar sesión:
   - Se valida que el usuario exista en el diccionario.
   - Se compara la contraseña ingresada con la almacenada.
   - Se muestra un mensaje de éxito o error según corresponda.

5. El programa se ejecuta de manera continua hasta que el usuario selecciona salir.

#
### ▶️ Cómo usar el proyecto
Tienes dos opciones para obtener el código:
1. **Descargar directamente:**
   Haz clic en el botón verde code y selecciona download zip.

2. **Clonar con git:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   ```