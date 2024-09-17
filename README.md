# TFM-MasterIA: Explotación de corpus pequeños para la incorporación de nuevos idiomas de pocos recursos a modelos de lenguaje masivos
Este proyecto se basa en la explotación de corpus pequeños de idiomas de bajos recursos (Aragonés, Asturiano, Aranés) para su incorporación en modelos de traducción automática. El proyecto utiliza herramientas como Vecalign para la alineación de oraciones, LASER para generar embeddings multilingües, y la API de OpenAI para realizar prompting.
## Descripción General

Este proyecto tiene los siguientes objetivos principales:

1. **Digitalización y extracción de textos multilingües utilizando "El Principito"** en varios idiomas (Aragonés, Asturiano, Aranés y Español).
2. **Alineación de oraciones entre pares de idiomas** utilizando `Vecalign`.
3. **Generación de embeddings multilingües** con LASER.
4. **Ajuste fino (fine-tuning)** de un modelo de traducción automática preentrenado de Hugging Face.
5. **Traducción y evaluación con GPT-4o mediante prompting** utilizando la API de OpenAI.


## Estructura de los scripts
### 1. `preprocesar_texto_extraido.py`
Este script toma el texto extraído de los archivos escaneados y lo preprocesa para eliminar ruido y normalizar el formato de las oraciones.
**Uso**: 
  ```bash

python preprocesar_texto_extraido.py
```
 *  **Input:** Archivos de texto en crudo (e.g., `extracted_texts(aranes).txt`).
 * **Output:** Archivos procesados con las oraciones limpias y listas para la alineación. (e.g. , `extracted_texts(aranes)_procesado.txt`)


### 2. `generar_embeddings.py`
Este script utiliza LASER para generar embeddings multilingües a partir de los textos preprocesados.

**Uso**: 

  ```bash

python python generar_embeddings.py
```
 * **Input:** Archivo overlap (e.g.,  `overlaps_aranes`) , Idioma (e.g., ` spa`, `cat`..), carpeta de salida (e.g., `../overlaps`)
 * **Output:** Archivo `.npy` que contienen los embeddings generados para cada idioma. (e.g., `embeddings_overlaps_español.npy`)

## Estructura notebooks
### 1. `extraccion_texto.ipynb.ipynb`
Este notebook extrae el texto de los documentos escaneados.
* **Input:** Cuentos escaneados "El Principito".
* **Output:** Archivo con el texto extraído de los documentos en PDF (e.g. `extracted_texts.txt).

### 2. `fine_tunning_transform.ipynb`   
Este notebook  crea los datasets (train, dev, test), y realiza fine-tunnig con el modelo de lengua `Helsinki-NLP/opus-mt-ca-es`, 
* **Input:** Archivos con el texto procesado una vez extraído de los documentos PDF (e.g. `extracted_texts(aranes)_procesado.txt`) y archivo con los índices de los pares de oraciones alineadas.
* **Output:** Corpus bilingües procesados para realizar prompting (e.g. `train_dataset.txt`,`test_dataset.txt`..) y corpus monolingüe procesado para prompting (e.g.`test_sources.txt`) , y  resultado puntuación BLEU 
  
### 3. `prompting_gpt4o_aranes.ipynb`
Este notebbok realiza el análisis del traducciones del modelo GPT-4o antes y después de introducir en el prompt todo el dataset de entrenamiento
 * **Input:** Archivos corpus procesado para prompting GPT-4o (e.g. , `train_dataset.txt`, `test_sources.txt`)
 * **Output:** Puntuación BLUE traducciones : sin train en el prompt y  con train en el prompt.

## Herramientas Externas

Este proyecto utiliza las siguientes herramientas externas para la alineación de oraciones y la generación de embeddings:

1. **Vecalign**: 
   - Vecalign se utiliza para la alineación de oraciones entre los textos de diferentes idiomas. Las instrucciones completas para utilizar los scripts `overlap.py` y `vecalign.py` están disponibles en su [repositorio oficial de GitHub](https://github.com/thompsonb/vecalign/).
   
2. **LASER**:
   - LASER (Language-Agnostic SEntence Representations) se utiliza para generar embeddings multilingües en este proyecto. Las instrucciones detalladas para utilizar `generar_embeddings.py` están disponibles en su [repositorio oficial de GitHub](https://github.com/facebookresearch/LASER/).

# Estructura de Directorios

El proyecto está organizado en los siguientes directorios, cada uno contiene archivos clave necesarios para las diferentes fases del proceso de traducción automática:

- **/alineaciones**:
  -   Contiene los arhivos con el resultado de las alineaciones de oraciones  de los idiomas aranés y español
- **/texto_extraido**: 
  Contiene los archivos de texto preprocesados en los diferentes idiomas.
  - `extracted_texts_*`: Archivos de texto extraido de los cuentos (sin porcesar y procesados) de cada idioma (por ejemplo, `extracted_texts(español).txt` o `extracted_texts(español)_procesado.txt` ).

- **/embeddings**: 
  Contiene los archivos `.npy` que almacenan los embeddings generados por LASER.
  - `embeddings_*`: Archivos `.npy` de embeddings generados para cada idioma (por ejemplo, `embeddings_aragones.npy`).
    
- **/overlaps**: 
  Almacena los archivos generados por el script `overlap.py`, que combina oraciones consecutivas para la alineación.
  - `overlaps_*`: Archivos de combinaciones de oraciones para alineación (por ejemplo, `overlaps_aragones.txt`).

- **/openai_api**: 
  Incluye los archivos relacionados con el prompting y las evaluaciones utilizando la API de OpenAI.
  - `train_dataset.txt`: Conjunto de entrenamiento utilizado para el prompting con la API.
  - `test_sources.txt`: Conjunto de prueba con las oraciones sin traducir.
  - `completed_test_sources.txt`: Traducciones generadas por GPT-4 sin "entrenamiento" previo.
  - `completed_test_sources_with_train.txt`: Traducciones generadas por GPT-4o con el dataset de entrenemiento enviado previamente en el prompt
 
 - **/noteboks**: 
  Incluye los notebooks para la correcta ejecución de la extraaciónb del texto de los documentos escaneados, realizar fine-tunnig y prompting.
  

## Cómo usar este proyecto.
 **1. Extracción de texto de documentos PDF** . Ejecutar el notebook `extraccion_texto.ipynb`
 
 **2. Generar archivos overlaps**.  En entorno **Vecalign** preprocesar textos `preprocesar_texto_extraido.py`  y generar combinaciones de oraciones `overlap.py`
 
 **3. Generar embeddings**  En entorno **LASER** .`generar_embeddings.py`
 
 **4. Fine-tunnig (`Helsinki-NLP/opus-mt-ca-es`)** . Notebook `fine_tunning_transform.ipynb`
 
 **5. Prompting GPT-4o**.  Notebook `prompting_gpt4o_aranes.ipynb`

 ## Uso de Material con Derechos de Autor

En este proyecto se han utilizado textos escaneados del cuento **"El Principito"** y otras obras con derechos de autor, exclusivamente para **fines de investigación** en el ámbito de la **traducción automática y el procesamiento del lenguaje natural**.

### Importante:

- **Los archivos de texto escaneados no se han subido a este repositorio** debido a las restricciones legales impuestas por los derechos de autor.
- **Todo el contenido protegido por derechos de autor se ha empleado únicamente para experimentos controlados y con fines académicos**.
- Si deseas replicar este proyecto, necesitarás utilizar tus propios textos de dominio público o con los permisos correspondientes.

Este proyecto sigue los principios del uso justo (*fair use*) para fines educativos y de investigación.

Si tienes preguntas o inquietudes sobre el uso de este material, no dudes en contactarnos.

 
## Contribuciones

Si encuentras errores o tienes sugerencias de mejora, no dudes en abrir un issue o enviar un pull request. ¡Toda contribución es bienvenida!

---

### Explicación:

1. **Uso de secciones claras**: Cada script tiene su propia sección con una breve descripción y su formato de entrada/salida.
2. **Código destacado**: Las secciones de uso del código están envueltas en bloques de código utilizando backticks (` ``` `) para que se visualicen correctamente en Markdown.
3. **Archivos importantes**: Se proporciona una lista clara de los archivos que forman parte del proyecto, con una breve descripción de su función.
4. **Cómo usar el proyecto**: Se ofrece una guía clara de los pasos a seguir para ejecutar los scripts en orden.
