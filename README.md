# Jump2Digital - Entrega Hackaton

Aquí está mi entrega para el hackaton de Jump2Digital. La tarea consistía en crear una API que permitiera a los usuarios consultar, adquirir, modificar y eliminar skins.

## Instalación

Para ejecutar el proyecto, se recomienda crear un entorno virtual. Si prefieres no utilizar un entorno virtual, puedes saltarte este paso y, en ese caso, ten en cuenta que las dependencias se instalarán en todo el sistema.

### Crear un entorno virtual
Si quieres más información del entorno virtual, visita la [documentación de Python](https://docs.python.org/es/3/tutorial/venv.html) 
1. Para crear un entorno virtual, asegúrate de tener Python instalado y, dentro de la carpeta donde hayas descargado el proyecto, ejecuta el siguiente comando:
```bash
   python -m venv jump2Digital-env
```
En este ejemplo, el entorno virtual se llama jump2Digital-env. Puedes elegir otro nombre si lo deseas.

2. Activa el entorno virtual. En Windows, puedes hacerlo con el siguiente comando:
```bash
   jump2Digital-env\Scripts\activate
```
Para desactivar el entorno virtual en Windows: 
```bash
   deactivate
```

### Instalar las dependencias

Una vez creado y activado el entorno virtual (o si has decidido no usar uno), instala las dependencias del proyecto. El proyecto proporciona un archivo requirements.txt con todas las dependencias necesarias. Ejecuta el siguiente comando:
```bash
   pip install -r requirements.txt
```

## Ejecución

Ahora que tienes todas las dependencias instaladas, puedes iniciar el servidor. Desde la carpeta del proyecto, ejecuta el siguiente comando:
```bash
   uvicorn main:app --reload
```
Si todo ha ido bien, el servidor FastAPI debería iniciarse y proporcionarte la URL a la que puedes acceder localmente (por defecto, http://127.0.0.1:8000).

## Nota sobre la Base de Datos
Para inicializar la base de datos he dejado un script en la carpeta 'extra', que contiene toda la estructura y dos inserts en la tabla usuarios para poder utilizarlos en las pruebas.

Es importante destacar que la base de datos en este proyecto es muy básica. No se han implementado sistemas de autenticación ni se han realizado comprobaciones avanzadas. Este proyecto se centra en cumplir con las cuatro funcionalidades requeridas en el hackaton.

## Carga de Datos

Se proporciona un script llamado leerJson.py que lee skins desde un archivo JSON y las almacena en la base de datos. Puedes encontrar un archivo JSON de ejemplo con varias skins. Si deseas agregar más skins, simplemente agrega las entradas al archivo JSON. Si intentas agregar una skin con un ID que ya existe, sobrescribirá la anterior. + Asegúrate de que el nombre sea único.

## Documentación de la API

Una vez que el servidor esté en funcionamiento, puedes acceder a la documentación de la API en http://127.0.0.1:8000/docs#/. Esta documentación, además, te permitirá probar los endpoints directamente desde tu navegador.


