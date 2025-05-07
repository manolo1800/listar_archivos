import os
import csv
from tkinter import Tk, filedialog

def seleccionar_carpeta():
    root = Tk()
    root.withdraw()
    return filedialog.askdirectory(title="Seleccione la carpeta a escanear")

def listar_archivos(carpeta_raiz):
    archivos = []
    for dirpath, dirnames, filenames in os.walk(carpeta_raiz):
        for filename in filenames:
            archivos.append({
                'nombre_archivo': filename,
                'ruta_completa': os.path.join(dirpath, filename),
                'carpeta_padre': dirpath
            })
    return archivos

def guardar_a_csv(archivos, nombre_csv='lista_archivos.csv'):
    campos = ['nombre_archivo', 'ruta_completa', 'carpeta_padre']
    try:
        with open(nombre_csv, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            writer.writeheader()
            writer.writerows(archivos)
        print(f"Se han guardado {len(archivos)} archivos en {nombre_csv}")
    except Exception as e:
        print(f"Error al guardar el CSV: {e}")

def main():
    print("Seleccione la carpeta a escanear...")
    carpeta = seleccionar_carpeta()
    if not carpeta:
        print("No se seleccionó ninguna carpeta. Saliendo...")
        return
    print(f"Escaneando {carpeta}...")
    archivos = listar_archivos(carpeta)
    if not archivos:
        print("No se encontraron archivos en la carpeta seleccionada.")
        return
    nombre_csv = input("Ingrese el nombre del archivo CSV a guardar (o presione Enter para usar el predeterminado): ").strip()
    if not nombre_csv:
        nombre_csv = 'lista_archivos.csv'
    guardar_a_csv(archivos, nombre_csv)

if __name__ == "__main__":
    main()
