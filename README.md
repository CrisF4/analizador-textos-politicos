# Analizador de textos políticos

Este es una version funcional del analizador de textos politicos hecho en python utilizando las siguientes librerias:
1. MyMUPdf
2. pandas
3. matplotlib
4. nltk
5. Counter
6. string
7. numpy
8. re
9. Image
10. WordCloud

En caso de no tener alguna de las librerias, instalar de la siguiente forma:

1. Se recomienda hacer un enviroment (aqui se utilzo anaconda3)
2. Abrir la terminal de vsc
3. escribir "pip install NombreDeLaLibreria
4. Presionar Enter y esperar a que se instale dicha libreria

IMPORTANTE: Al momento de utlizar el sistema, ABRA LA CARPETA 'analizador-textos-politicos' COMO CARPETA RAIZ DENTRO DE VISUAL STUDIO CODE.De esta forma, no tendra ningun inconveniente con respecto a las rutas relaitvas de los documentos utilizados.

<h2>Funcionalidaes</h2>
Este sistema permite ingresar documentos en formato pdf (en este caso, informes presidenciales) para su respectivo procesamiento de datos. Este nos dara:
1. Estadisticas generales, como el número total de palabras, total de palabras distintas, palabras clave y promedio de palabras por documento.
2. Ver gráficas tales como de Dispersión lexica, WordClouds, Gráficas de barras y series de tiempo.
De esta forma, se podra hacer un analisis mas profundo sobre cada presidente y tambien da la posibilidad de comparar tendencias, patrones y tematicas que hay entre presidentes.
