## README.md

## Extracción de datos de Publicaciones de funerales

**Objetivo:**

Este script extrae los enlaces a los avisos fúnebres publicados en el diario La Arena ([https://www.laarena.com.ar/](https://www.laarena.com.ar/)) y guarda el texto de cada publicación en un archivo de texto.

**Librerías utilizadas:**

- `requests`: Para realizar solicitudes HTTP a la página web.
- `BeautifulSoup`: Para parsear el HTML de las páginas y extraer los datos relevantes.
- `time`: Para introducir un retardo entre solicitudes para evitar ser bloqueado.

**Creado por:**

Diego Hirschfeld

**Última vez editado:**

01 de junio de 2024

**Descripción del código:**

1.  **Importación de librerías:**

    Se importan las librerías necesarias para el funcionamiento del script: `requests`, `BeautifulSoup` y `time`.

2.  **Definición de variables:**

    - `headers`: Diccionario que contiene el user-agent para evitar ser bloqueado por la página web.
    - `file`: Archivo de texto para guardar los enlaces a los avisos fúnebres.
    - `fileo`: Archivo de texto para guardar el texto de cada publicación.
    - `url`: URL base de la sección de avisos fúnebres en La Arena.
    - `i`: Variable para iterar por las páginas de avisos fúnebres.

3.  **Bucle principal:**

    El script recorre un rango de páginas (de la 23 a la 85) para extraer los avisos fúnebres del año 2023.

    Para cada página:

    a. **Solicitud HTTP:**

    Se realiza una solicitud HTTP a la URL de la página actual utilizando la librería `requests`.

    b. **Parseo del HTML:**

    Se parsea el HTML de la página utilizando la librería `BeautifulSoup`.

    c. **Extracción de enlaces:**

    Se extraen los enlaces a los avisos fúnebres de la página actual y se escriben en el archivo `anuncios.txt`.

    d. **Extracción del texto de las publicaciones:**

    Se itera por cada enlace a un aviso fúnebre:

    i. **Solicitud HTTP:**

          Se realiza una solicitud HTTP a la URL del aviso fúnebre.

    ii. **Parseo del HTML:**

          Se parsea el HTML del aviso fúnebre.

    iii. **Extracción del texto:**

          Se extrae el texto de la publicación y se escribe en el archivo `publicaciones.txt`.

    iv. **Retardo:**

          Se introduce un retardo de 5 segundos entre solicitudes para evitar ser bloqueado por la página web.

4.  **Cierre de archivos:**

    Se cierran los archivos `anuncios.txt` y `publicaciones.txt`.

**Ejecución del script:**

Para ejecutar el script, guarde el código como un archivo `.py` y ejecútelo desde la línea de comandos utilizando el siguiente comando:

```bash
python scraping.py
```

**Consideraciones:**

- El script está diseñado para extraer avisos fúnebres del año 2023. Si desea extraer avisos de otros años, deberá modificar el rango de páginas utilizado en el bucle principal.
- Es importante utilizar el script de manera responsable y evitar realizar solicitudes excesivas a la página web, ya que esto podría generar problemas para el funcionamiento del script y para la página web en sí.

## README.md Extracción de las edades de las publicaciones

**Objetivo:**

Este script extrae las edades de los fallecidos a partir de los anuncios fúnebres del archivo `anuncios.txt` y las guarda en un archivo CSV llamado `edades_fallecimiento.csv`. Este archivo puede ser utilizado posteriormente para calcular la edad promedio de los fallecidos.

**Librerías utilizadas:**

- No se utilizan librerías externas en este script.

**Entrada:**

- El script espera un archivo de texto llamado `anuncios.txt` que contiene los avisos fúnebres extraídos de la página web (presumiblemente generado por el script `scraping.py`).

**Proceso:**

1. **Lectura del archivo:**

   - Se utiliza `open()` para abrir el archivo `anuncios.txt` en modo lectura (`'r'`).
   - Se leen las líneas del archivo y se almacenan en una lista.

2. **Búsqueda de la edad:**

   - Se itera por cada línea del archivo.
   - Se busca la palabra "años" dentro de un rango específico de palabras (entre la quinta y la decimosexta, asumiendo un formato estándar de las publicaciones).
   - Si se encuentra la palabra "años", se extrae la palabra anterior (asumiendo que representa la edad).

3. **Escritura en el archivo CSV:**

   - Se abre un archivo de texto llamado `edades_fallecimiento.csv` en modo escritura (`'w'`).
   - Se escribe la edad extraída en cada línea del archivo CSV.

4. **Manejo de errores:**

   - Se incluye un bloque `try-except` para capturar posibles excepciones durante la lectura del archivo.

5. **Cierre del archivo:**
   - Se cierra el archivo de texto `edades_fallecimiento.csv` para liberar recursos.

**Salida:**

- Se genera un archivo CSV llamado `edades_fallecimiento.csv` que contiene una columna con las edades de los fallecidos extraídas de los avisos fúnebres.

**Ejecución del script:**

Para ejecutar el script, guarde el código como un archivo `.py` y ejecútelo desde la línea de comandos utilizando el siguiente comando:

```bash
python sepelio.py
```

**Consideraciones:**

- El script asume un formato estándar para las publicaciones fúnebres en el archivo `anuncios.txt`. Si el formato cambia, es posible que sea necesario modificar el script para extraer correctamente las edades.
- Este script solo extrae las edades, no calcula la media. Se recomienda utilizar otro script que lea el archivo `edades_fallecimiento.csv` y realice el cálculo del promedio.

## README.md Análisis de edades (Data Visualization)

**Objetivo:**

Este script analiza los datos de las edades de fallecidos extraídos del archivo `edades_fallecimiento.csv` (presumiblemente generado por el script `sepelio.py`) y genera un histograma para visualizar la distribución de las edades.

**Librerías utilizadas:**

- Pandas (`pandas`): Para lectura y manipulación de datos en DataFrames.
- Statistics (`statistics`): Para cálculo de media, desviación estándar y cuartiles (no utilizado en esta versión).
- Matplotlib (`matplotlib.pyplot`): Para creación de gráficos.
- NumPy (`numpy`): Para operaciones numéricas con arrays.

**Entrada:**

- El script espera un archivo CSV llamado `edades_fallecimiento.csv` que contiene una columna con las edades de los fallecidos.

**Proceso:**

1. **Lectura del archivo:**

   - Se utiliza `pandas.read_csv` para leer los datos del archivo CSV, especificando la codificación `latin-1` para manejar correctamente el texto en el archivo.

2. **Cálculo de estadísticas:**

   - Se calcula la media de las edades utilizando el método `mean` del DataFrame.
   - Se calcula la desviación estándar de las edades utilizando el método `std` del DataFrame.

3. **Generación del histograma:**

   - Se utiliza `matplotlib.pyplot.hist` para crear un histograma de las edades.
   - Se configura el ancho de las barras, el color, el borde, la transparencia y el etiquetado del eje X y Y.
   - Se muestra el título del histograma incluyendo la media y la desviación estándar calculadas.

4. **Visualización del gráfico:**
   - El script utiliza `matplotlib.pyplot.show` para mostrar el histograma generado.

**Salida:**

- Se genera un histograma que muestra la distribución de las edades de los fallecidos.

**Contribuciones:**

Si desea contribuir a este script, puede hacerlo creando un pull request en el repositorio de GitHub donde se aloja el código.

**Agradecimientos:**

A la comunidad de desarrollo de Python por las librerías y herramientas que hacen posible este tipo de scripts de scraping.
