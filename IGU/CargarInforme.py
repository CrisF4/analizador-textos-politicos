import fitz
import nltk
import string
from collections import Counter
from nltk.tokenize import word_tokenize
import os

def validar_datos(nombre_presidente, anio_sexenio, ruta_pdf):
    # Validar que el nombre del presidente sea un string no vacío
    if not isinstance(nombre_presidente, str) or not nombre_presidente.strip():
        return False, "El nombre del presidente debe ser un string no vacío."

    # Validar que el año del sexenio sea un entero
    if not isinstance(anio_sexenio, int):
        try:
            anio_sexenio = int(anio_sexenio)
        except ValueError:
            return False, "El año del sexenio debe ser un número entero."

    # Validar que la ruta del PDF termine con la extensión ".pdf"
    if not ruta_pdf.endswith(".pdf"):
        return False, "El archivo seleccionado no es un PDF."

    # Validar que la ruta del PDF exista
    if not os.path.exists(ruta_pdf):
        return False, "El archivo seleccionado no existe en el sistema."
    
    mensaje = 'Entradas válidas.'

    return True, mensaje

def obtener_texto(pdf_path):
    texto = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        texto += page.get_text()  # Obtén el texto de la página
    doc.close()
    return texto

def contar_palabras(texto):
    contador = Counter()  # Inicializa un contador para contar las palabras
    tokens = nltk.word_tokenize(texto)
    palabras = [token.lower() for token in tokens if token.isalnum()]  # Se mantienen solo las palabras alfanuméricas
    contador.update(palabras)  # Actualiza el contador con las palabras
    
    return contador

def contar_palabras_clave(texto, palabras_clave):
    contador = Counter()
    for palabra_clave in palabras_clave:
        contador[palabra_clave] += texto.lower().count(palabra_clave.lower())  # Contabiliza las ocurrencias de la palabra clave en la página
    
    return contador

def tokenizar_texto_pdf(texto):
    tokens = nltk.word_tokenize(texto)
    tokens = [token for token in tokens if token not in string.punctuation]
    return tokens