import tkinter as tk

class PantallaMostrarEstadisticasGenerales(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.title('Mostrar Estadísticas Generales')
        self.parent = parent
        self.parent.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
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
        
    def on_close(self):
        self.destroy()
        self.parent.deiconify()