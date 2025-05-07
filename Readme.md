# 📁 listar_archivos

Un script en Python para explorar de manera recursiva una carpeta seleccionada por el usuario y generar un archivo `.csv` con información detallada de cada archivo encontrado.

---

## 🚀 Características

- Selección de carpeta mediante interfaz gráfica (`Tkinter`)
- Exploración recursiva de todos los archivos dentro de la carpeta
- Exportación de resultados a un archivo CSV con:
  - Nombre del archivo
  - Ruta completa
  - Carpeta contenedora

---

## 🛠️ Requisitos

- Python 3.6 o superior
- Bibliotecas estándar:
  - `os`
  - `csv`
  - `tkinter`

> No se requiere instalar paquetes externos adicionales.

---

## ▶️ Cómo usarlo

1. Clona este repositorio:

```bash
git clone https://github.com/tuusuario/FileLister.git
cd FileLister

2. Crea un entorno virtual y actívalo:
python -m venv env
# En Windows
env\Scripts\activate
# En macOS/Linux
source env/bin/activate

3. Instala las dependencias:
pip install -r requirements.txt

4. Ejecuta el script:
python listar_archivos.py
