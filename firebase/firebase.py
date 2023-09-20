import pyrebase
import os

# Obtén el directorio actual del archivo Python
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Define el nombre del archivo JSON
nombre_archivo_json = "serviceAccountKey.json"

# Construye la ruta completa al archivo JSON
ruta_completa = os.path.join(directorio_actual, "firebase", nombre_archivo_json)

firebaseConfig = {
  "apiKey": "AIzaSyBOmXu25JmUFakC8d-SaRQoH6u8NyyVJLw",
  "authDomain": "unpet-f599b.firebaseapp.com",
  "projectId": "unpet-f599b",
  "storageBucket": "unpet-f599b.appspot.com",
  "messagingSenderId": "780334025549",
  "appId": "1:780334025549:web:a0f11c0f3fcbd8c84e8504",
  #"serviceAccount": f"{ruta_completa}",
  "databaseURL": "https://unpet-f599b-default-rtdb.firebaseio.com/"
};

firebase = pyrebase.initialize_app(firebaseConfig)


storage = firebase.storage()
imgUrl= "public/img/gato.jpg"

storage.child(imgUrl).put(imgUrl)

db = firebase.database()

auth = firebase.auth()
print('SUBIDA EXITOSA')