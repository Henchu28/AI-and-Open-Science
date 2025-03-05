#!/bin/bash

apt update -qq && apt install -y curl -qq

INPUT_DIR="/opt/grobid/input"
OUTPUT_DIR="/opt/grobid/output"

mkdir -p "$OUTPUT_DIR"

for file in "$INPUT_DIR"/*.pdf; do
  echo "Procesando: $file"
  curl -X POST "http://localhost:8070/api/processFulltextDocument" \
       -F "input=@$file" \
       -F "consolidateHeader=1" \
       -F "consolidateCitations=1" \
       -F "outputFormat=tei" \
       -o "$OUTPUT_DIR/$(basename "$file" .pdf).tei.xml"
done

echo "Procesamiento completado. Archivos guardados en $OUTPUT_DIR"


