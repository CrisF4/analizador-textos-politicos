import tkinter as tk
import sys
import os
# Añadir el directorio raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Control.MostrarEstadisticasGenerales import obtener_datos

class PantallaMostrarEstadisticasGenerales(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Mostrar Estadísticas Generales')
        self.parent = parent
        self.parent.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        window_width = 500
        window_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        self.resizable(False, False)

        self.resultados_texto = tk.Text(self, wrap="word")
        self.resultados_texto.pack(expand=True, fill="both")
        
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
            self.resultados_texto.insert(tk.END, f"Presidente: {resultado['Presidente']}\n")
            self.resultados_texto.insert(tk.END, f"Total de palabras encontradas: {resultado['TotalPalabras']}\n")
            self.resultados_texto.insert(tk.END, f"Promedio de palabras por documento: {resultado['PromedioPalabras']:.2f}\n")
            self.resultados_texto.insert(tk.END, f"Total de palabras diferentes: {resultado['TotalDiferentes']}\n")
            self.resultados_texto.insert(tk.END, f"Conteo de palabras clave encontradas: {resultado['TotalClave']}\n")
            self.resultados_texto.insert(tk.END, f"Ruta del archivo de conteo de palabras: {resultado['RutaPalabras']}\n")
            self.resultados_texto.insert(tk.END, f"Ruta del archivo de conteo de palabras clave: {resultado['RutaClave']}\n")
            self.resultados_texto.insert(tk.END, "---------------------------------------\n")
            
        # Botón para volver a la pantalla principal
        self.volver_button = tk.Button(self, text="Volver", command=self.volver_a_principal)
        self.volver_button.pack(pady=20)

    def volver_a_principal(self):
        self.destroy()
        self.parent.deiconify()

    def on_close(self):
        self.destroy()
        self.parent.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Ventana Principal')
    root.geometry('300x200')

    def abrir_estadisticas():
        PantallaMostrarEstadisticasGenerales(root)

    boton = tk.Button(root, text="Mostrar Estadísticas", command=abrir_estadisticas)
    boton.pack(pady=20)

    root.mainloop()