# AI and OP in RSE


Este repositorio contiene las prácticas realizadas para la asignatura Artificial Inteligence and Open Science in Research Software Engineering.

La carpeta `Prac 1` contiene los archivos que corresponden con la primera práctica, mientras que el resto de archivos `.md` permiten generar la documentación sobre la misma.

El objetivo de esta primera práctica es realizar el análisis de contenido de diferentes artículos científicos, procesados previamente con alguna herramienta (en mi caso GROBID).

## Funcionalidades
- Nube de Palabras de keywords:  
Genera una nube de palabras a partir de los abstracts de los artículos.
- Conteo de figuras:  
Crea una visualización con el número de figuras por artículo.
- Lista de links:  
 Genera una lista por artículo de los links que contiene.

## Requisitos
- Docker
- Docker Compose
- Anaconda

## Instalación y Ejecución
1. Clonar este repositorio y navegar a la aplicación:  
``` git clone https://github.com/Henchu28/AI-and-Open-Science ```  
``` cd AI-and-Open-Science/Prac 1 ```  
2. Introducir artículos a analizar en la carpeta `/grobid_data/input` de la práctica.
3. Construir y levantar contenedores (los scripts se ejecutan automáticamente):  
```docker compose up --build ```


## Otros Comandos

- Ejecutar GROBID manualmente: 
```docker exec grobid bash /opt/grobid/process.sh```

- Terminar GROBID:  
    - Eliminar contenedores (manteniendo el volumen creado):  
```docker compose down```
    - Eliminar contenedores y volumen:  
```docker compose down -v```

- Ejecutar Script:
    - Crear el entorno Conda:
```conda env create -f environment.yml```
    - Activar entorno:
```conda activate grobid_analysis```
    - Ejecutar Script:
```python data_extract.py```

## Citación del Repositorio
Díez Gómez, J.M. (2025). Henchu28/AI-and-Open-Science. https://github.com/Henchu28/AI-and-Open-Science

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
