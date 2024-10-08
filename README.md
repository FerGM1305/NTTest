# NTTest
# Proceso ETL y API de Números Naturales

Este proyecto está dividido en dos secciones principales. La **Sección 1** trata sobre la carga, extracción y transformación de datos utilizando FastAPI y MySQL, mientras que la **Sección 2** consiste en una API para trabajar con números naturales.

## Sección 1: Proceso ETL

Este proyecto utiliza **FastAPI** y **MySQL** para cargar datos desde un archivo CSV, transformarlos y almacenarlos en una base de datos relacional. 

### Tecnologías utilizadas:
- **FastAPI**: Framework web rápido y moderno para crear APIs con Python.
- **MySQL**: Base de datos relacional utilizada para almacenar los datos estructurados.
  
### Requisitos previos

1. Clonar este repositorio.
2. Instalar las dependencias necesarias ejecutando:
## Instalación de Librerías

Para instalar todas las librerías necesarias para correr el proyecto, utiliza el archivo `requirements.txt`. Ejecuta el siguiente comando en la terminal:

pip install -r requirements.txt

Asegurarse de tener un servidor MySQL corriendo y configurar la conexión en el archivo .env.

Crear la base de datos ejecutando el script SQL que se encuentra en el archivo files/query.sql.

Cómo ejecutar el proyecto
Ejecutar el servidor de FastAPI:

En la carpeta Seccion1ProcesoETL, correr el siguiente comando:

uvicorn app.main:app --reload
Configurar la conexión a la base de datos:

En el archivo .env, escribe tu cadena de conexión a MySQL. Ejemplo:

DATABASE_URL=mysql+pymysql://<usuario>:<contraseña>@<host>/<nombre_de_base_de_datos>
Subir los datos a la base de datos:

Utilizando la interfaz de Swagger que viene integrada con FastAPI, abre tu navegador y accede a:

http://127.0.0.1:8000/docs
Luego, sigue estos pasos:

Subir el archivo CSV:

Haz clic en el botón Try it out en la ruta /upload_csv/.
Selecciona el archivo CSV que está en la carpeta files/ del proyecto y presiona Execute para cargar los datos.
Transformar y cargar los datos:

En la ruta /transform/, haz clic en Try it out y selecciona el archivo con los datos.
Presiona Execute para realizar la transformación y cargar los datos procesados a la base de datos.
Detalles del proceso de transformación
Durante el proceso de transformación, se abordan algunos retos clave:

IDs nulos: Si una fila tiene un company_id nulo y el nombre de la compañía coincide con un registro existente, se asigna el company_id correcto.
Nombres de compañías coincidentes: Si el nombre contiene "MiP", automáticamente se ajusta a "MiPasajefy".
Manejo de valores grandes: Para cantidades extremadamente grandes (amount), se ajusta el valor dividiéndolo entre sí mismo.
Sección 2: API para Números Naturales
Este es un API que opera sobre números naturales, donde se puede extraer un número y obtener el faltante.

Cómo ejecutar el proyecto
En la carpeta Seccion2APINaturales, ejecuta el siguiente comando:


uvicorn ApiNumerosNaturales:app --reload
Abre el navegador y accede a:


http://127.0.0.1:8000/docs
Para probar las funciones:

Extraer número:
En la ruta /extraer_numero, haz clic en Try it out.
Ingresa el número en el request body y presiona Execute para obtener el resultado.
Número faltante:
En la ruta /numero_faltante, presiona Try it out y luego Execute para obtener el número faltante.
