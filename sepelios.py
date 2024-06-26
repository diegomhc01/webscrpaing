#Hipótesis: 
#Determinar la edad promedio de los fallecimientos publicados en el diario La Arena
#durante el año 2023 

file = open("edades_fallecimiento.csv","w")
diccionario = []
k=0
arreglo = []
with open('anuncios.txt', 'r') as f:
    try:
        contenido = f.readlines()
        for k in range(len(contenido)):
            x = contenido[k]
            x = x.split()
            j=0
            texto = ''
            for i in x:
                if j > 4 and j < 16:                
                    if i == 'años':
                        texto = x[j-1]
                j = j + 1
            file.writelines(texto+"\n")
    except Exception as e:
        print(e.__str__())
file.close()    


