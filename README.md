# TFM-MasterIA: Explotación de corpus pequeños para la incorporación de nuevos idiomas de pocos recursos a modelos de lenguaje masivos
Este proyecto se centra en la explotación de corpus pequeños de idiomas de bajos recursos (Aragonés, Asturiano, Aranés) para su incorporación en modelos de traducción automática. El proyecto utiliza herramientas como Vecalign para la alineación de oraciones, LASER para generar embeddings multilingües, y la API de OpenAI para realizar prompting.
## Descripción General

Este proyecto tiene los siguientes objetivos principales:

1. **Digitalización y extracción de textos multilingües utilizando "El Principito"** en varios idiomas (Aragonés, Asturiano, Aranés y Español).
2. **Alineación de oraciones entre pares de idiomas** utilizando `Vecalign`.
3. **Generación de embeddings multilingües** con LASER.
4. **Ajuste fino (fine-tuning)** de un modelo de traducción automática preentrenado de Hugging Face.
5. **Traducción y evaluación con GPT-4o mediante prompting** utilizando la API de OpenAI.


## Estructura de los scripts
### `preprocesar_texto_extraido.py`
Este script toma el texto extraído de los archivos escaneados y lo preprocesa para eliminar ruido y normalizar el formato de las oraciones.
**Uso**: 
  ```bash
python preprocesar_texto_extraido.py
- **Input** : Archivos de texto en crudo (e.g., extracted_texts(aranes).txt).
- **Output** : Archivos procesados con las oraciones limpias y listas para la alineación. (e.g. , extracted_texts(aranes)_procesado.txt)
