import os
import re

def process_text_file(file_path):
    # Abre el archivo original para lectura y crea uno nuevo para la escritura
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

        # Eliminar pies de página que contienen "Page" seguido estrictamente por números
        #content = re.sub(r'\ n.*Page\s+\d+.*\n', '\n', content)

        # Eliminar pies de página y números de página
        #content = re.sub(r'^[\*\-]*\**Page.*$', '', content, flags=re.MULTILINE | re.IGNORECASE)

        # Eliminar guiones y espacios al inicio de cada línea
        content = re.sub(r'^[\-\s–—]+', '', content, flags=re.MULTILINE)   

        # Eliminación de líneas que contienen solo caracteres especiales
        content = re.sub(r'^\W+$', '', content, flags=re.MULTILINE)

        # Eliminar líneas que contienen números de capítulos en formato romano entre asteriscos dobles
        #content = re.sub(r'^\*\*[IVXLCDM]+\*\*$', '', content, flags=re.MULTILINE)

        # Eliminación de líneas que contienen solo números o números romanos
        content = re.sub(r'^\d+$', '', content, flags=re.MULTILINE)
        content = re.sub(r'^[IVXLCDM]+$', '', content, flags=re.MULTILINE)

        # Unir líneas interrumpidas por guiones al final de la línea
        #content = re.sub(r'-\s*\n', '', content)

        # Mantener el texto en una línea hasta encontrar un punto
        #content = ' '.join(line.strip() for line in content.splitlines())

        # Insertar saltos de línea después de cada punto, ":", "?" y adecuadamente después de "»", excluyendo puntos suspensivos
        #content = re.sub(r'([.?:])(\s*[»"]?)', lambda m: '\n' if m.group(1) == '.' and m.group(0)[-3:] != '...' else m.group(0), content)
        #content = re.sub(r'([.?:])(\s*[»"]?)', lambda m: '\n' if m.group(1) in {'.', ':', '?'} and m.group(0)[-3:] != '...' else m.group(0), content)

        # Eliminar líneas vacías antes de escribir en el archivo
        content = '\n'.join(line for line in content.split('\n') if line.strip())
        
    # Guardar el contenido procesado en un nuevo archivo
    with open(file_path.replace('.txt', '_procesado.txt'), 'w', encoding='utf-8') as new_file:
        new_file.write(content)

def process_directory(directory):
    # Procesa cada archivo .txt en el directorio especificado
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            process_text_file(file_path)
            print(f"Procesado: {filename}")

# Directorio donde están los archivos .txt
directory_path = 'texto_extraido'
process_directory(directory_path)