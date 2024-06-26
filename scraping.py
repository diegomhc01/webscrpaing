"""
OBJETIVO: 
  - Extraer los enlaces a los avisos fúnebres
  - Aprender a utilizar Beautiful Soup para parsear el arbol HTML
CREADO POR: DIEGO HIRSCHFELD
ULTIMA VEZ EDITADO: 01 DE JUNIO DE 2024
"""
import requests
from bs4 import BeautifulSoup # pip install beautifulsoup4
from time import sleep

# USER AGENT PARA PROTEGERNOS DE BANEOS
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


file = open("anuncios.txt","w") #ARCHIVO PARA GUARDAR LOS ANUNCIOS QUE TIENEN EL ENLACE A LA PUBLICACION
fileo = open("publicaciones.txt","w") #ARCHIVO PARA GUARDAR CADA PUBLICACION
#EL RANGO A LA FECHA DEL DESARROLLO DE ESTE SCRAPING SOLO TOMA LOS SEPELIOS DEL AÑO 2023
#QUE VA DESDE LA PAGINA 23 A LA 85
for i in range(23,85): 
    url = 'https://www.laarena.com.ar/servicios/funebres/'
    #VA TOMANDO LA URL DE LOS ANUNCIOS POR PAGINA
    url = url + str(i)
    
    respuesta = requests.get(url, headers=headers)

    # PARSEO DEL ARBOL CON BEAUTIFUL SOUP
    soup = BeautifulSoup(respuesta.text,features="lxml")
    #EN LA ETIQUETA DIV CON LA CLASE columns ESTÁN LOS ANUNCIOS
    contenedor = soup.find(class_="columns") # ENCONTRAR UN ELEMENTO POR CLASS
    #EN LA ETIQUETA DIV CON LA CLASE item is-4 ESTÁ CADA ANUNCIO
    anuncios = contenedor.find_all('div', class_="item is-4") 
    #ESCRIBO EN EL ARCHIVO anuncios.txt
    file.writelines(str(contenedor)+"\n")
    
    for anuncio in anuncios: # ITERAR POR LOS ANUNCIOS DE CADA PAGINA
        #TOMAR SOLO LAS PUBLICACIONES DE SEPELIOS, NO LAS PARTICIPACIONES
        if anuncio.find('a').text.find('Sepe') > 0: 
            # DENTRO DE CADA ELEMENTO ITERADO ENCONTRAR UN TAG a EL ATRIBUTO href
            url_publicacion = anuncio.find('a').get('href') 
            
            urlo = 'https://www.laarena.com.ar' + url_publicacion

            respuesta_publicacion = requests.get(urlo, headers=headers)

            # PARSEO DEL ARBOL CON BEAUTIFUL SOUP
            soupo = BeautifulSoup(respuesta_publicacion.text,features="lxml")
            # ENCONTRAR UN ELEMENTO POR CLASS DE LA PUBLICACION
            publicacion = soupo.find(class_="container") 
            # ENCONTRAR EL TEXTO DE LA PUBLICACION
            textos = publicacion.find_all('div', class_="funebre__body") 
            for texto in textos:
                #ESCRIBO EL ARCHIVO publicaciones.txt
                fileo.writelines(texto.text+"\n")
            #HAGO UNA ESPERA DE 5 SEGUNDOS PARA QUE NO ME AGREGUE A LA LISTA NEGRA
            #POR LAS PETICIONES REALIZADAS
            sleep(5)
file.close()
fileo.close()