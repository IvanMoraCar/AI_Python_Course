import shutil

# Definimos la ruta (en Windows usamos "C:")
path = "C:/"

# Obtenemos las estadísticas en bytes
total, used, free = shutil.disk_usage(path)

# Convertimos a Gigabytes para que sea legible (1 GB = 1024^3 bytes)
print(f"--- Reporte de Disco ({path}) ---")
print(f"Total: {total // (2**30)} GB")
print(f"Usado: {used // (2**30)} GB")
print(f"Libre: {free // (2**30)} GB")
print(f"Porcentaje de uso: {100 * used // total}%")
