# Práctica 1


Este repositorio de Github contiene los ficheros necesarios para replicar el análisis de artículos de investigación realizados en mi máquina mediante GROBID.

Este análisis se realiza dentro de un contenedor Docker y, posteriormente, se realiza el análisis con un script de Python.

Por consiguiente, para poder realizar el proyecto es necesario tener instaladas las siguientes herramientas:
- Docker Desktop ---> https://docs.docker.com/desktop/setup/install/windows-install/
- Anaconda ---> https://www.anaconda.com/download/success
- 

## Contenedor GROBID

Para poder realizar la práctica, primero se levanta el contenedor utilizando los archivos `Dockerfile` y `docker-compose.yml`. Primero, nos situamos en la carpeta `Prac 1` al clonar el repositorio y usamos los comandos:

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
