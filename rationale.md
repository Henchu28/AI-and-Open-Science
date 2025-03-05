# Rationale Prac 1


## Archivos del repositorio


En este repositorio se tienen varios archivos, unos para levantar el contenedor de GROBID en Docker y realizar el análisis y otros para preparar el entorno Conda y extraer información de los archivos procesados.

Los árticulos que se analizan se encuentran en la carpeta `grobid_data/input`. En caso de querer analizar otros archivos diferentes, basta con cambiar los ficheros contenidos en la carpeta y volver a levantar el contenedor.

En caso de querer editar la configuración de GROBID para que funcione mejor en tu máquina, puedes modificar el archivo de configuración contenido en la carpeta `grobid_data/config`.

Los archivos `Dockerfile` y `docker-compose.yml` permiten levantar el contenedor, mientras que el archivo `process.sh` se encarga de comenzar el proceso de análisis de los archivos en GROBID.

El archivo `environment.yml` sirve para crear el entorno "grobid_analysis" con Conda, donde se puede ejecutar el script `data_extract.py` para obtener los datos pedidos en la práctica: nube de palabras del Abstract, número de figuras por artículo y lista de links.
