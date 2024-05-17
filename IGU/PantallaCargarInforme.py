import tkinter as tk
from tkinter import filedialog
import os
import shutil

class PantallaCargarInforme(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.title('Ventana 1')
        self.parent = parent
        self.parent.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # Crear el directorio para almacenar los archivos de texto de cada presidente
        directorio_presidentes = "Persistencia\Informes presidenciales\Presidentes"
        os.makedirs(directorio_presidentes, exist_ok=True)

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

        # Campos de entrada para presidente y año de sexenio
        tk.Label(self, text="Nombre del Presidente:").pack(pady=10)
        self.presidente_entry = tk.Entry(self)
        self.presidente_entry.pack(pady=10)

        tk.Label(self, text="Año del Sexenio:").pack(pady=10)
        self.anio_entry = tk.Entry(self)
        self.anio_entry.pack(pady=10)

        # Botón para cargar archivo PDF
        self.cargar_pdf_button = tk.Button(self, text="Cargar PDF", command=self.cargar_pdf)
        self.cargar_pdf_button.pack(pady=20)

        # Etiqueta para mostrar el archivo cargado
        self.archivo_label = tk.Label(self, text="")
        self.archivo_label.pack(pady=10)

    def cargar_rutas_almacenadas(self):
        presidente = self.presidente_entry.get().strip()
        archivo_presidente = os.path.join("Presidentes", f"{presidente}.txt")

        if os.path.exists(archivo_presidente):
            with open(archivo_presidente, 'r') as file:
                return [line.strip() for line in file.readlines()]
        else:
            return []

    def guardar_rutas_almacenadas(self, presidente, rutas):
        archivo_presidente = os.path.join("Persistencia\Presidentes", f"{presidente}.txt")
        with open(archivo_presidente, 'w') as file:
            for ruta in rutas:
                file.write(f"{ruta}\n")

    def cargar_pdf(self):
        archivo = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf")],
            title="Seleccionar archivo PDF"
        )
        if archivo:
            presidente = self.presidente_entry.get().strip()
            anio = self.anio_entry.get().strip()

            if presidente and anio:
                iniciales = ''.join([nombre[0] for nombre in presidente.split()[:2]]).upper()
                nuevo_nombre = f"{anio}_informe_{iniciales}.pdf"

                # Directorio destino relativo
                directorio_destino = os.path.join(
                    "Persistencia",
                    "Informes presidenciales",
                    f"_{presidente.replace(' ', '_')}"
                )
                
                # Crear el directorio si no existe
                os.makedirs(directorio_destino, exist_ok=True)

                # Ruta completa del nuevo archivo
                nueva_ruta = os.path.join(directorio_destino, nuevo_nombre)

                # Mover el archivo
                try:
                    shutil.move(archivo, nueva_ruta)
                    self.archivo_label.config(text=f"Archivo renombrado y movido a: {nueva_ruta}")

                    # Cargar las rutas almacenadas para el presidente actual
                    rutas = self.cargar_rutas_almacenadas()
                    # Agregar la nueva ruta a la lista de rutas
                    rutas.append(nueva_ruta)
                    # Guardar las rutas actualizadas
                    self.guardar_rutas_almacenadas(presidente, rutas)
                except Exception as e:
                    self.archivo_label.config(text=f"Error al mover el archivo: {e}")
            else:
                self.archivo_label.config(text="Por favor, ingrese el nombre del presidente y el año del sexenio.")

    def on_close(self):
        self.destroy()
        self.parent.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = PantallaCargarInforme(root)
    root.mainloop()

