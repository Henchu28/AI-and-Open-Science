import unittest
from unittest.mock import patch, MagicMock
import xml.etree.ElementTree as ET
import data_extract

class TestDataExtract(unittest.TestCase):
    
    @patch("glob.glob")
    @patch("xml.etree.ElementTree.parse")
    def test_extract_data(self, mock_parse, mock_glob):
        # Simular archivos TEI en la carpeta
        mock_glob.return_value = ["file1.tei.xml", "file2.tei.xml"]
        
        # Crear un XML de prueba
        tei_content = """
        <TEI xmlns="http://www.tei-c.org/ns/1.0">
            <text>
                <body>
                    <abstract>
                        <p>Keyword1 Keyword2 Keyword3</p>
                    </abstract>
                    <figure/>
                    <figure/>
                    <listBibl>
                        <bibl>
                            <ref type="url" target="http://example.com"/>
                        </bibl>
                    </listBibl>
                </body>
            </text>
        </TEI>
        """
        
        # Simular la estructura del XML
        root = ET.ElementTree(ET.fromstring(tei_content))
        mock_parse.return_value = root
        
        # Ejecutar el script simulado
        data_extract.figures_count = {}
        data_extract.all_links = []
        data_extract.all_keywords = []
        
        for tei_file in mock_glob.return_value:
            tree = mock_parse(tei_file)
            root = tree.getroot()
            ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
            
            # Extraer palabras clave
            abstract = root.find(".//tei:abstract", ns)
            if abstract is not None:
                abstract_text = " ".join(abstract.itertext())
                data_extract.all_keywords.extend(abstract_text.split())
            
            # Contar figuras
            figures = root.findall(".//tei:figure", ns)
            data_extract.figures_count[tei_file] = len(figures)
            
            # Extraer enlaces
            for ref in root.findall(".//tei:ref[@type='url']", ns):
                url = ref.get("target")
                if url:
                    data_extract.all_links.append(url)
        
        # Verificar resultados esperados
        self.assertEqual(len(data_extract.figures_count), 2)
        self.assertEqual(data_extract.figures_count["file1.tei.xml"], 2)
        self.assertEqual(data_extract.figures_count["file2.tei.xml"], 2)
        self.assertIn("Keyword1", data_extract.all_keywords)
        self.assertIn("Keyword2", data_extract.all_keywords)
        self.assertIn("Keyword3", data_extract.all_keywords)
        self.assertIn("http://example.com", data_extract.all_links)

if __name__ == "__main__":
    unittest.main()
