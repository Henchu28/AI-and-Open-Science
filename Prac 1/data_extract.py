import os
import glob
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# Ruta donde están los archivos TEI
tei_folder = "grobid_data/output"

# Listas para almacenar los datos
figures_count = {}
all_links = []
all_keywords = []

for tei_file in glob.glob(os.path.join(tei_folder, "*.tei.xml")):
    tree = ET.parse(tei_file)
    root = tree.getroot()
    
    # Espacio de nombres del TEI
    ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
    
    # Obtener nombre del archivo para referencias
    file_name = os.path.basename(tei_file)
    
    # Extraer palabras clave del abstract
    abstract = root.find(".//tei:abstract", ns)
    if abstract is not None:
        abstract_text = " ".join(abstract.itertext())
        all_keywords.extend(abstract_text.split())

    # Contar número de figuras en el documento
    figures = root.findall(".//tei:figure", ns)
    figures_count[file_name] = len(figures)

    # Extraer todos los enlaces (URLs)
    for ref in root.findall(".//tei:ref[@type='url']", ns):
        url = ref.get("target")
        if url:
            all_links.append(url)

# Mostrar los enlaces extraídos
print("\n Lista de enlaces encontrados en los artículos:")
for link in all_links:
    print(link)

# Generar la nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(all_keywords))
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Nube de palabras del Abstract")
print('-'*70)

# Visualizar el número de figuras por artículo
file_labels = [f"archivo {i+1}" for i in range(len(figures_count))]

plt.figure(figsize=(10, 5))
plt.bar(file_labels, figures_count.values(), color="skyblue")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Número de Figuras")
plt.title("Número de Figuras por Artículo")
plt.show()
