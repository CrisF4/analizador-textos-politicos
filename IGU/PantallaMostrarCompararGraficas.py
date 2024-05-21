import tkinter as tk
from tkinter import ttk
import os
import sys
# Añadir el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Control.MostrarCompararGraficas import *

class PantallaMostrarCompararGraficas(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Mostrar y Comparar Gráficas')
        self.parent = parent
        self.parent.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.presidente1 = tk.StringVar()
        self.presidente2 = tk.StringVar()

        self.frame_presidentes = tk.Frame(self)
        self.frame_presidentes.pack(pady=10)

        tk.Label(self.frame_presidentes, text="Presidente 1:").grid(row=0, column=0, padx=5)
        self.entry_presidente1 = tk.Entry(self.frame_presidentes, textvariable=self.presidente1)
        self.entry_presidente1.grid(row=0, column=1, padx=5)

        tk.Label(self.frame_presidentes, text="Presidente 2:").grid(row=1, column=0, padx=5)
        self.entry_presidente2 = tk.Entry(self.frame_presidentes, textvariable=self.presidente2)
        self.entry_presidente2.grid(row=1, column=1, padx=5)

        self.frame_botones = tk.Frame(self)
        self.frame_botones.pack(pady=10)

        self.boton_dispersion = tk.Button(self.frame_botones, text="Gráfica de Dispersión", command=self.generar_grafica_dispersion)
        self.boton_dispersion.grid(row=0, column=0, padx=5)

        self.boton_barras = tk.Button(self.frame_botones, text="Gráfica de Barras", command=self.generar_grafica_barras)
        self.boton_barras.grid(row=0, column=1, padx=5)

        self.boton_wordcloud = tk.Button(self.frame_botones, text="WordCloud", command=self.generar_wordcloud)
        self.boton_wordcloud.grid(row=0, column=2, padx=5)

        self.boton_serie_tiempo = tk.Button(self.frame_botones, text="Serie de Tiempo", command=self.generar_serie_tiempo)
        self.boton_serie_tiempo.grid(row=0, column=3, padx=5)

    def generar_grafica_dispersion(self):
        presidente1 = self.presidente1.get()
        presidente2 = self.presidente2.get()
        palabras_clave = ['modernizacion', 'respeto', 'justicia', 'reforma', 'revolución', 'empresas', 'seguridad', 'compromiso', 'inversión',
                          'económica', 'trabajadores', 'trabajo', 'deuda', 'externa', 'concertación', 'estabilidad', 'solidaridad', 'democracia',
                          'medio', 'ambiente', 'campesinos', 'salud', 'inflación', 'impuesto', 'salarios']
        graficar_dispersion(presidente1, palabras_clave)
        graficar_dispersion(presidente2, palabras_clave)
        plt.show()

    def generar_grafica_barras(self):
        presidente1 = self.presidente1.get()
        presidente2 = self.presidente2.get()
        ruta_archivo_csv1 = 'Persistencia\Tablas_conteo\{}_conteo_palabras_clave.csv'.format(presidente1)
        ruta_archivo_csv2 = 'Persistencia\Tablas_conteo\{}_conteo_palabras_clave.csv'.format(presidente2)
        graficar_barras(ruta_archivo_csv1)
        graficar_barras(ruta_archivo_csv2)
        plt.show()

    def generar_wordcloud(self):
        presidente1 = self.presidente1.get()
        presidente2 = self.presidente2.get()
        ruta_archivo_csv1 = 'Persistencia\Tablas_conteo\{}_conteo_palabras_clave.csv'.format(presidente1)
        ruta_archivo_csv2 = 'Persistencia\Tablas_conteo\{}_conteo_palabras_clave.csv'.format(presidente2)
        ruta_png = 'Recursos\mapa_mexico_2.1.png'
        graficar_wordcloud(ruta_archivo_csv1, ruta_png)
        graficar_wordcloud(ruta_archivo_csv2, ruta_png)
        plt.show()

    def generar_serie_tiempo(self):
        presidente1 = self.presidente1.get()
        presidente2 = self.presidente2.get()
        ruta_archivo_csv1 = 'Persistencia\Tablas_conteo\{}_conteo_palabras_clave.csv'.format(presidente1)
        ruta_archivo_csv2 = 'Persistencia\Tablas_conteo\{}_conteo_palabras_clave.csv'.format(presidente2)
        palabras_st = ['inflación', 'deuda', 'impuesto', 'salarios', 'gasolina', 'educación', 'corrupción']
        df_tiempo1 = generar_df_tiempo(ruta_archivo_csv1, palabras_st)
        df_tiempo2 = generar_df_tiempo(ruta_archivo_csv2, palabras_st)
        graficar_serie_tiempo(df_tiempo1, palabras_st)
        graficar_serie_tiempo(df_tiempo2, palabras_st)

    def on_close(self):
        self.destroy()
        self.parent.deiconify()

def generar_df_tiempo(ruta_archivo_csv, palabras_st):
    df = pd.read_csv(ruta_archivo_csv, encoding='latin1')
    fechas = sorted(set(df['Año']))  # Obtener fechas únicas y ordenarlas
    conteos = {palabra: [] for palabra in palabras_st}
    
    for fecha in fechas:
        df_fecha = df[df['Año'] == fecha]
        for palabra in palabras_st:
            conteo_total = df_fecha[df_fecha['Palabra'] == palabra]['Conteo'].sum()
            conteos[palabra].append(conteo_total)
    
    df_tiempo = pd.DataFrame(conteos, index=fechas)
    return df_tiempo

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Ventana Principal')
    root.geometry('300x200')

    def abrir_comparar_graficas():
        PantallaMostrarCompararGraficas(root)

    boton = tk.Button(root, text="Mostrar y Comparar Gráficas", command=abrir_comparar_graficas)
    boton.pack(pady=20)

    root.mainloop()