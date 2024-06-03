# webscrpaing
## README.md for Funeral Announcement Scraper

**Objetivo:**

* Extraer los enlaces a los avisos fúnebres del sitio web La Arena ([https://www.laarena.com.ar/](https://www.laarena.com.ar/))
* Aprender a utilizar Beautiful Soup para parsear el árbol HTML

**Creado por:** Diego Hirschfeld

**Última vez editado:** 1 de junio de 2024

**Requisitos:**

* Tener Python instalado
* Tener la biblioteca `beautifulsoup4` instalada (ejecutar `pip install beautifulsoup4`)

**Descripción:**

Este script utiliza la biblioteca Beautiful Soup para extraer los enlaces a los avisos fúnebres del sitio web La Arena. El script recorre las páginas de anuncios fúnebres del año 2023 (páginas 23 a 85) y extrae los enlaces a cada publicación individual. Luego, para cada publicación, el script descarga la página completa y extrae el texto del anuncio fúnebre. 

**Uso:**

1. Asegúrese de tener las bibliotecas necesarias instaladas (Python y Beautiful Soup).
2. Guarde el script como un archivo Python (por ejemplo, `funeral_scraper.py`).
3. Ejecute el script desde la línea de comandos:

```bash
python funeral_scraper.py
```

**Archivos de salida:**

* `anuncios.txt`: Contiene el HTML de cada página de anuncios fúnebres.
* `publicaciones.txt`: Contiene el texto de cada anuncio fúnebre.

**Consideraciones:**

* El script está diseñado para extraer anuncios fúnebres del año 2023. Si desea extraer anuncios de otros años, deberá modificar el código para cambiar el rango de páginas que se recorren.
* El script realiza una espera de 5 segundos entre cada solicitud para evitar ser bloqueado por el sitio web.
* Es importante utilizar este script de manera responsable y respetuosa con los términos de servicio del sitio web La Arena.

**Contribuciones:**

Si desea contribuir a este script, puede hacerlo creando un pull request en el repositorio de GitHub donde se aloja el código.

**Agradecimientos:**

A la comunidad de desarrollo de Python por las bibliotecas y herramientas que hacen posible este tipo de scripts.
