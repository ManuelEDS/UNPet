import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage as fstorage
from django.core.files.uploadedfile import UploadedFile

# Establece la variable de entorno GOOGLE_APPLICATION_CREDENTIALS
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./server/firebase/serviceAccountKey.json"
#serviceAccount = "./serviceAccountKey.json"

def uploadUserIMG():
    pass

def getUserIMG():
    pass

def deleteUserIMG():
    pass

def __isJPG(url: str):
    return url.lower.endswith('.jpg')

# bucket = fstorage.bucket()
# blob = bucket.blob("nuevoGato2")  # Cambia el nombre de acuerdo a tu preferencia
# #blob.upload_from_file()
# blob.upload_from_filename('../public/img/gato.jpg')

# # Obtiene la URL de descarga de la imagen
# url_imagen = blob.public_url

# # Imprime la URL o utilízala según tus necesidades
# print("URL de la imagen:", url_imagen)

# # Genera una URL firmada para el objeto de almacenamiento sin tiempo de expiración
# url_firmada = blob.generate_signed_url(expiration=3153600000)  #100 años, basicamente infinito

# # Imprime la URL firmada o utilízala según tus necesidades
# print("URL de la imagen firmada:", url_firmada, '\n\nLongitud: ', len(url_firmada))


def uploadUserIMG(foto:UploadedFile, nombre:str):
    try:
        photo_data=None
        # Lee los datos binarios de la foto
        if not isinstance(foto, UploadedFile) and not isinstance(foto, bytes):
            raise ValueError("El parámetro 'foto' debe ser un objeto UploadedFile o de tipo bytes.")
        elif isinstance(foto, UploadedFile) and foto.size > 1024 * 1024 * 5: #---> 5 MB, si pesa mas que eso se rechaza
            raise ValueError("La foto no debe pesar mas de 5 MegaBytes.")
        else:
            photo_data = photo_data if isinstance(foto, bytes) else foto.read()

        # Inicializa Firebase Storage y obtén el blob
        bucket = fstorage.bucket()
        blob = bucket.blob(nombre)

        # Sube la foto a Firebase Storage
        blob.upload_from_string(photo_data)

        # Genera una URL firmada con una expiración de 100 años (3153600000 segundos)
        url_firmada = blob.generate_signed_url(expiration=3153600000)

        # Devuelve la URL firmada
        return url_firmada
    except Exception as e:
        # Maneja cualquier error que pueda ocurrir durante la carga
        print(f"Error al cargar la foto en Firebase Storage: {str(e)}")
        return None
    

def obtener_url_de_imagen(nombre_archivo_en_storage, ruta=None):
    try:
        # Inicializa Firebase Storage y obtén el blob
        bucket = fstorage.bucket()
        blob = bucket.blob(ruta + '/' + nombre_archivo_en_storage) if ruta else bucket.blob(nombre_archivo_en_storage)

        # Devuelve la URL pública del archivo en Firebase Storage
        return blob.public_url
    except Exception as e:
        # Maneja cualquier error que pueda ocurrir durante la obtención de la URL
        print(f"Error al obtener la URL de la imagen en Firebase Storage: {str(e)}")
        return None