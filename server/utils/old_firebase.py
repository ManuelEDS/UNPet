import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage as fstorage
import os

# Establece la variable de entorno GOOGLE_APPLICATION_CREDENTIALS
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./server/firebase/serviceAccountKey.json"
serviceAccount = "./serviceAccountKey.json"

def uploadUserIMG():
    pass

def getUserIMG():
    pass

def deleteUserIMG():
    pass

def __isJPG(url: str):
    return url.lower.endswith('.jpg')

cred = credentials.Certificate(serviceAccount)

app = firebase_admin.initialize_app(cred, {'storageBucket': 'unpet-f599b.appspot.com'})

bucket = fstorage.bucket()
blob = bucket.blob("nuevoGato2")  # Cambia el nombre de acuerdo a tu preferencia
#blob.upload_from_file()
blob.upload_from_filename('../public/img/gato.jpg')

# Obtiene la URL de descarga de la imagen
url_imagen = blob.public_url

# Imprime la URL o utilízala según tus necesidades
print("URL de la imagen:", url_imagen)

# Genera una URL firmada para el objeto de almacenamiento sin tiempo de expiración
url_firmada = blob.generate_signed_url(expiration=3153600000)  #100 años, basicamente infinito

# Imprime la URL firmada o utilízala según tus necesidades
print("URL de la imagen firmada:", url_firmada, '\n\nLongitud: ', len(url_firmada))

