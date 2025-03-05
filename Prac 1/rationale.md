# Rationale Prac 1


Este repositorio de Github contiene los ficheros necesarios para replicar el análisis de artículos de investigación realizados en mi máquina mediante GROBID.

Este análisis se realiza dentro de un contenedor Docker y, posteriormente, se realiza el análisis con un script de Python.

Por consiguiente, para poder realizar el proyecto es necesario tener instaladas las siguientes herramientas:
- Docker Desktop ---> https://docs.docker.com/desktop/setup/install/windows-install/
- Anaconda ---> https://www.anaconda.com/download/success

## Archivos del repositorio


En este repositorio se tienen varios archivos, unos para levantar el contenedor de GROBID en Docker y realizar el análisis y otros para preparar el entorno Conda y extraer información de los archivos procesados.

Los árticulos que se analizan se encuentran en la carpeta `grobid_data/input`. En caso de querer analizar otros archivos diferentes, basta con cambiar los ficheros contenidos en la carpeta y volver a levantar el contenedor.

En caso de querer editar la configuración de GROBID para que funcione mejor en tu máquina, puedes modificar el archivo de configuración contenido en la carpeta `grobid_data/config`.

Los archivos `Dockerfile` y `docker-compose.yml` permiten levantar el contenedor, mientras que el archivo `process.sh` se encarga de comenzar el proceso de análisis de los archivos en GROBID.

El archivo `environment.yml` sirve para crear el entorno "grobid_analysis" con Conda, donde se puede ejecutar el script `data_extract.py` para obtener los datos pedidos en la práctica: nube de palabras del Abstract, número de figuras por artículo y lista de links.

## Contenedor GROBID


Como se ha mencionado, para poder levantar el contenedor se utilizan los archivos `Dockerfile` y `docker-compose.yml`. Primero, nos situamos en la carpeta `Prac 1` al clonar el repositorio y usamos los comandos:

```
docker-compose build  #creamos la imagen con el Dockerfile
docker-compose up -d  #levantamos el contenedor con el archivo docker-compose.yml
```
Con esto, tendríamos GROBID ya funcionando en el Docker. Para que comience a procesar los artículos, ejecutamos el comando:

```
docker exec -it bash /opt/grobid/process.sh
```

Esto manda los artículos a procesarse y los guarda en la carpeta del ordenador `grobid_data/output`, conectada al volumen del contenedor.

## Análisis en Conda


Una vez los archivos ya están en la carpeta `grobid_data/output`, se continúa con la creación del entorno Conda.

```
conda env create -f environment.yml
```

Una vez creado, activamos el entorno y ejecutamos el script de extracción de datos.

```
conda activate -n grobid_analysis
python data_extract.py
```

Se mostraran la lista de enlaces de los artículos en el símbolo del sistema (CMD) y se generarán dos pestañas con la nube de palabras y el número de figuras por artículo.
