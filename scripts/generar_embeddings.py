import os
import numpy as np
import re
from laser_encoders import LaserEncoderPipeline


def read_file(file_name):
    """Función para leer un archivo y devolver una lista de oraciones."""
    with open(file_name, 'r', encoding='utf-8') as file:
        sentences = [line.strip() for line in file if line.strip()]
    return sentences

def generate_embeddings(file_name, lang, output_dir):
    """Generar y guardar embeddings para un archivo dado, en el directorio especificado, con el idioma especificado por el usuario."""
    sentences = read_file(file_name)
    encoder = LaserEncoderPipeline(lang=lang)
    embeddings = encoder.encode_sentences(sentences, normalize_embeddings=True)
    
    # Crear el directorio si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Construir la ruta de salida completa para guardar el archivo
    output_file_path = os.path.join(output_dir, f'embeddings_{os.path.basename(file_name)}.npy')
    np.save(output_file_path, embeddings)
    print(f"Embeddings saved to {output_file_path}")

# Solicitar al usuario que introduzca el nombre del archivo, el idioma y el directorio de salida
file_name = input("Por favor, introduce el nombre del archivo overlap: ")
lang = input("Por favor, introduce el código de idioma para este archivo (e.g., 'spanish', 'english', 'french'): ")
output_dir = input("Introduce el directorio de salida para los embeddings: ")

# Generar embeddings para el archivo especificado y guardarlos en el directorio especificado
generate_embeddings(file_name, lang, output_dir)