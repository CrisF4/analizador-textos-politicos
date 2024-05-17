import tkinter as tk
from tkinter import ttk

from PantallaCargarInforme import PantallaCargarInforme
from PantallaMostrarEstadisticasGenerales import PantallaMostrarEstadisticasGenerales
from PantallaMostra_CompararGraficas import PantallaMostrar_CompararGraficas

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Pantalla Principal')

        # Centrar la ventana
        window_width = 500
        window_height = 500

        # Obtener las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular la posición de la ventana
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Posicionar la ventana
        self.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        self.resizable(False, False)

        self.button1 = ttk.Button(self, text="Cargar informe", command=self.ir_pantalla_cargar_informe)
        self.button1.pack(pady=20)

        self.button2 = ttk.Button(self, text="Mostrar estadisticas generales", command=self.ir_pantalla_mostrar_estadisticas_generales)
        self.button2.pack(pady=20)

        self.button3 = ttk.Button(self, text="Mostra/Comparar graficas", command=self.ir_pantalla_mostrar_comparar_graficas)
        self.button3.pack(pady=20)

        self.quit_button = ttk.Button(self, text="Salir", command=self.quit)
        self.quit_button.pack(pady=20)
        
    def ir_pantalla_cargar_informe(self):
        self.new_window = PantallaCargarInforme(self)

    def ir_pantalla_mostrar_estadisticas_generales(self):
        self.new_window = PantallaMostrarEstadisticasGenerales(self)

    def ir_pantalla_mostrar_comparar_graficas(self):
        self.new_window = PantallaMostrar_CompararGraficas(self)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()