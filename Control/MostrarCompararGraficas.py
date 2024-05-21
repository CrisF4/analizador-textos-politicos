import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re
import os
from collections import Counter
from PIL import Image
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from nltk.draw.dispersion import dispersion_plot
from Control.CargarInforme import tokenizar_texto_pdf, obtener_texto, contar_palabras_clave
from Control.MostrarEstadisticasGenerales import exportar_a_csv

def combinar_tokens(rutas_pdf):
    tokens_combinados = []
    for ruta_pdf in rutas_pdf:
        texto_pdf = obtener_texto(ruta_pdf)
        tokens_pdf = tokenizar_texto_pdf(texto_pdf)
        tokens_combinados.extend(tokens_pdf)
    return tokens_combinados

def graficar_dispersion(presidente, palabras_clave):
    rutas_pdf = obtener_rutas_pdf(presidente)
    tokens_combinados = combinar_tokens(rutas_pdf)
    dispersion_plot(tokens_combinados, palabras_clave, ignore_case=True, title=f'Gráfica de Dispersión Léxica - {presidente}')
    plt.gcf().set_size_inches(11, 5)  # Establecer tamaño de la figura
    plt.xlabel("Desplazamiento de palabra")
    plt.ylabel("Palabras clave")
    plt.grid(True)
    #plt.show()

def obtener_rutas_pdf(presidente):
    ruta_directorio = "Persistencia\Presidentes"
    rutas_pdf = []
    for filename in os.listdir(ruta_directorio):
        if filename.endswith(".txt"):
            with open(os.path.join(ruta_directorio, filename), 'r') as file:
                for line in file:
                    if presidente in line:
                        rutas_pdf.append(line.strip())
    return rutas_pdf

def graficar_barras(ruta_archivo_csv):
    df_clave = pd.read_csv(ruta_archivo_csv, encoding='latin1')
    plt.figure(figsize=(11,5))
    plt.bar(df_clave['Palabra'], df_clave['Conteo'])
    plt.xlabel('Palabra clave')
    plt.ylabel('Conteo')
    plt.title('Conteo de palabras clave en informes presidenciales')
    plt.grid(True)
    plt.xticks(rotation='vertical')
    #plt.show()

def graficar_wordcloud(ruta_archivo_csv, ruta_png):
    def transformar_png(png_path):
        mapa_mascara = np.array(Image.open(png_path))
        def transform_format(val):
            return np.where(val == 0, 255, val)
        return transform_format(mapa_mascara)
    
    df = pd.read_csv(ruta_archivo_csv, encoding='latin1')
    png_path = ruta_png
    palabras_dicc = dict(zip(df['Palabra'], df['Conteo']))
    mapa_mascara = transformar_png(png_path)
    wordcloud = WordCloud(width=800, height=400, mask=mapa_mascara, contour_width=1.0, contour_color='black', background_color='white').generate_from_frequencies(palabras_dicc)
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    #plt.show()

def graficar_serie_tiempo(df_tiempo, palabras_st):
    plt.figure(figsize=(10, 6))
    for palabra in palabras_st:
        plt.plot(df_tiempo.index, df_tiempo[palabra], label=palabra)
    plt.title('Evolución del Conteo de Palabras Clave')
    plt.xlabel('Año')
    plt.ylabel('Conteo')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def procesar_pdf(presidente, palabras_st):
    rutas_pdf = obtener_rutas_pdf(presidente)
    contador_total = Counter()
    fechas = []
    conteos = {palabra: [] for palabra in palabras_st}

    for ruta_pdf in rutas_pdf:
        match = re.findall(r'_(\d{4})_', ruta_pdf)
        año = match[0] if match else 'Desconocido'
        
        texto_pdf = obtener_texto(ruta_pdf)
        contador_actual = contar_palabras_clave(texto_pdf, palabras_st)
        contador_total.update(contador_actual)
        nombre_archivo = f'Tablas_conteo\conteo_palabras_clave_{año}.csv'
        exportar_a_csv(contador_actual, nombre_archivo)
        
        fechas.append(año)
        for palabra in palabras_st:
            conteos[palabra].append(contador_actual[palabra])

    df_tiempo = pd.DataFrame(conteos, index=fechas)
    return df_tiempo