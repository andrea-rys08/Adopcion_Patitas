# 🐾 Sistema de Gestión de Adopciones "Patitas de Amor"
## 📝 Descripción del Proyecto
Este proyecto es una aplicación web dinámica diseñada para digitalizar y optimizar el proceso de adopción en refugios de animales. El sistema permite gestionar un catálogo de mascotas, registrar adoptantes y generar un historial de transacciones mediante una arquitectura de base de datos relacional normalizada.

## 🛠️ Stack Tecnológico
* [cite_start]**Lenguaje:** Python 3.12 [cite: 134]
* [cite_start]**Framework Web:** Flask (Arquitectura MVC simplificada) [cite: 120]
* [cite_start]**Base de Datos:** MariaDB / MySQL [cite: 131]
* [cite_start]**Interfaz:** HTML5, CSS3 (Diseño responsivo basado en Cards) [cite: 174, 175]
* [cite_start]**Entorno:** Ubuntu Linux / VS Code [cite: 140]

## 🗄️ Arquitectura de la Base de Datos
El sistema utiliza una estructura de 4 tablas para garantizar la integridad referencial y cumplir con las formas normales de bases de datos:
1.  [cite_start]**Person:** Almacena datos de identidad (Nombre, Apellido, Cédula)[cite: 48, 50, 52].
2.  [cite_start]**Adopter:** Relaciona a una persona con su información de domicilio[cite: 54].
3.  [cite_start]**Dog:** Contiene el catálogo de mascotas (Raza, Edad, Estado de Adopción)[cite: 25, 26].
4.  [cite_start]**Adoption:** Tabla de hechos que vincula al adoptante con la mascota y la fecha del proceso[cite: 71].

## 🤖 Log de Desarrollo con Asistencia de IA
Durante la fase de construcción, se utilizó Inteligencia Artificial para resolver desafíos técnicos específicos:
* [cite_start]**Debugging de Conexión:** Resolución del error `Access denied for user root` mediante la creación de un usuario específico con privilegios en MariaDB[cite: 131, 164, 165].
* [cite_start]**Optimización SQL:** Implementación de consultas con **Triple INNER JOIN** para mostrar nombres legibles en lugar de IDs numéricos en el historial[cite: 170, 171].

## 🚀 Guía de Instalación
1.  **Entorno Virtual:** Activar el entorno con `source venv/bin/activate`.
2.  **Base de Datos:** Importar el script SQL adjunto en MariaDB.
3.  **Ejecución:** Iniciar el servidor con `python main.py`.
<img width="1365" height="765" alt="GitHub_Readme" src="https://github.com/user-attachments/assets/8cd7ec22-666f-42ee-acd3-13b4b39edd40" />
<img width="1366" height="524" alt="GitHUbReadme" src="https://github.com/user-attachments/assets/c489dc8d-a591-4d97-977a-163518666532" />

