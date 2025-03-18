import zipfile
import os

def zip_file(path: str, file: str) -> str:

    file_path = os.path.join(path, file)

    if os.path.exists(file_path):

        file_zip = f"{file}.zip"
        zip_path = os.path.join(path, file_zip)

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.write(file_path, file)
            print(f"Archivo {file} comprimido como {file_zip}")
            return file_zip
    else:
        print(f"El archivo {file} no existe en el directorio {path}")

def unzip_file(path: str, file: str):

    file_path = os.path.join(path, file)

    if os.path.exists(file_path):
        with zipfile.ZipFile(file_path) as zipf:
            zipf.extractall(path)
            print(f"Archivo {file} descomprimido en {path}")

    else:
        print(f"El archivo {file} no existe en el directorio {path}")
    return None


path = os.path.dirname(os.path.abspath(__file__))
file = "messi.png"

zip = zip_file(path, file)

if zip != None:

    #Borro el file (en este ejemplo es messi.png) para que en vez de sobreescribir, lo descargue desde el .zip
    os.remove(os.path.join(path, file))
    
    unzip_file(path, zip)