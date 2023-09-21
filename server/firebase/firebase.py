import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage as fstorage
from google.cloud import storage as gstorage
import os

# Establece la variable de entorno GOOGLE_APPLICATION_CREDENTIALS
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./server/firebase/serviceAccountKey.json"

def uploadUserIMG():
    pass

def getUserIMG():
    pass

def deleteUserIMG():
    pass

def __isJPG(url: str):
    return url.lower.endswith('.jpg')

cred = credentials.Certificate(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])

app = firebase_admin.initialize_app(cred, {'storageBucket': 'unpet-f599b.appspot.com'})


bucket = fstorage.bucket()
NOMBRE_IMG_PARA_DB = "nuevoGato.jpg"
blob = bucket.blob("nuevoGato.jpg")  # Cambia el nombre de acuerdo a tu preferencia
blob.upload_from_filename('./server/public/img/gato.jpg')

# Obtiene la URL de descarga de la imagen
url_imagen = blob.public_url


# Crea una instancia del cliente de almacenamiento
storage_client = gstorage.Client()
# Nombre del bucket de Firebase Storage
bucket_name = "unpet-f599b.appspot.com"
# Nombre del objeto de almacenamiento que deseas firmar
object_name = "b01.jpg"
# Obtén una referencia al objeto de almacenamiento
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(object_name)
# Genera una URL firmada para el objeto de almacenamiento sin tiempo de expiración
url_imagen = blob.generate_signed_url(expiration=3153600000)  # Sin tiempo de expiración

# Imprime la URL firmada o utilízala según tus necesidades
print("URL de la imagen firmada:", url_imagen)

