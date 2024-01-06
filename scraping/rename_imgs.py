import os

# Ruta al directorio que contiene las imágenes
directorio = 'imgs'

# Obtén una lista de nombres de archivo en el directorio
archivos = os.listdir(directorio)

# Itera sobre cada archivo en el directorio
for archivo in archivos:
    # Verifica si el archivo es una imagen (puedes ajustar esto según tus extensiones de archivo)
    if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        nuevo_nombre = archivo[2:]
        # Construye las rutas completas para el archivo antiguo y el nuevo
        ruta_antigua = os.path.join(directorio, archivo)
        ruta_nueva = os.path.join(directorio, nuevo_nombre)

        # Renombra el archivo
        os.rename(ruta_antigua, ruta_nueva)

        print(f"Renombrado: {archivo} -> {nuevo_nombre}")
