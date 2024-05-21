import nltk
import pandas as pd
from collections import Counter
from Control.CargarInforme import obtener_texto, contar_palabras, contar_palabras_clave
import os

# Descargar los recursos necesarios de NLTK
nltk.download('punkt')

def contar_palabras_pdfs(pdf_paths):
    contador_total = Counter()
    for pdf_path in pdf_paths:
        try:
            texto = obtener_texto(pdf_path)
            contador = contar_palabras(texto)
            contador_total.update(contador)
        except Exception as e:
            print(f"Error al procesar {pdf_path}: {e}")
    return contador_total

def contar_palabras_clave_pdfs(pdf_paths, palabras_clave):
    contador_total_clave = Counter()
    for pdf_path in pdf_paths:
        try:
            texto = obtener_texto(pdf_path)
            contador = contar_palabras_clave(texto, palabras_clave)
            contador_total_clave.update(contador)
        except Exception as e:
            print(f"Error al procesar {pdf_path}: {e}")
    return contador_total_clave

def exportar_a_csv(contador, nombre_archivo):
    df = pd.DataFrame.from_dict(contador, orient='index', columns=['Conteo']).reset_index()
    df.columns = ['Palabra', 'Conteo']
    df.to_csv(nombre_archivo, index=False)
    print(f"Conteo de palabras guardado en '{nombre_archivo}'")

def obtener_datos(rutas_archivos_txt, palabras_clave):
    resultados = []
    for ruta_archivo in rutas_archivos_txt:
        print(f"Procesando archivo: {ruta_archivo}")
        presidente = os.path.splitext(os.path.basename(ruta_archivo))[0]
        pdf_paths = []
        with open(ruta_archivo, "r") as file:
            for line in file:
                pdf_paths.append(line.strip())

        contadorPalabras = contar_palabras_pdfs(pdf_paths)
        contadorClave = contar_palabras_clave_pdfs(pdf_paths, palabras_clave)

        ruta_palabras = f'Persistencia\Tablas_conteo\{presidente}_conteo_palabras.csv'
        ruta_clave = f'Persistencia\Tablas_conteo\{presidente}_conteo_palabras_clave.csv'

        total_palabras = sum(contadorPalabras.values())
        promedio_palabras = total_palabras / len(pdf_paths)
        total_diferentes = len(contadorPalabras)
        total_clave = sum(contadorClave.values())

        resultados.append({
            "Presidente": presidente,
            "TotalPalabras": total_palabras,
            "PromedioPalabras": promedio_palabras,
            "TotalDiferentes": total_diferentes,
            "TotalClave": total_clave,
            "RutaPalabras": ruta_palabras,
            "RutaClave": ruta_clave
        })

        exportar_a_csv(contadorPalabras, ruta_palabras)
        exportar_a_csv(contadorClave, ruta_clave)

    return resultados

if __name__ == '__main__':
    ruta_directorio = "Persistencia\Presidentes"
    rutas_archivos_txt = []
    for filename in os.listdir(ruta_directorio):
        if filename.endswith(".txt"):
            rutas_archivos_txt.append(os.path.join(ruta_directorio, filename))

    palabras_clave = ['modernizacion', 'respeto', 'justicia', 'reforma', 'revolución', 'empresas', 'seguridad',
                      'compromiso', 'inversión', 'económica', 'trabajadores', 'trabajo', 'deuda', 'externa',
                      'concertación', 'estabilidad', 'solidaridad', 'democracia', 'medio', 'ambiente', 'campesinos',
                      'salud', 'inflación', 'impuesto', 'salarios']

    resultados = obtener_datos(rutas_archivos_txt, palabras_clave)
    for resultado in resultados:
        print(resultado)




