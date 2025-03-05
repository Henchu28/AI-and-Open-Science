# Usar la imagen oficial de GROBID 0.8.1
FROM lfoppiano/grobid:0.8.1

# Copiar configuración personalizada si existe
COPY ./grobid_data/config/grobid.yaml /opt/grobid/config/grobid.yaml

# Crear carpetas de entrada y salida dentro del contenedor (en caso de que no existan)
RUN mkdir -p /opt/grobid/input /opt/grobid/output

COPY ./grobid_data/input /opt/grobid/input
COPY ./grobid_data/output /opt/grobid/output

# Ajustar permisos para evitar problemas de acceso a los volúmenes
RUN chmod -R 777 /opt/grobid/input /opt/grobid/output

# Copiar el script que procesará automáticamente los PDFs al iniciar el contenedor
RUN chmod +x ./process.sh
COPY ./process.sh /opt/grobid
