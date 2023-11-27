import requests
import random
from datetime import datetime, timedelta
def obtener_urls_gatos_aleatorios(n, url):
    urls = []

    for _ in range(n):
        # Realizar solicitud HTTP a la URL base
        response = requests.get(url)

        # Obtener la URL redireccionada
        redirected_url = response.url

        # Agregar la URL a la lista
        urls.append(redirected_url)

    return urls



def generar_fecha_nacimiento():
    today = datetime.now()
    random_days_ago = random.randint(365, 3650)  # Entre 1 y 10 años atrás
    birth_date = today - timedelta(days=random_days_ago)
    return birth_date.strftime("%Y-%m-%d")

def crear_mascotas(url, n):
    mascotas = []

    # Lista de nombres aleatorios
    #nombres = ['Fido', 'Mittens', 'Whiskers', 'Fluffy', 'Shadow', 'Luna']
    nombres = ['Buddy', 'Max', 'Charlie', 'Rocky', 'Bailey', 'Luna', 'Lucy', 'Cooper', 'Daisy', 'Sadie']

    for i in range(1, n + 1):
        mascota = {
            "nombre": random.choice(nombres),
            "especie": "Perro",
            "raza": "Desconocida",
            "sexo": random.choice(["Macho", "Hembra"]),
            "fechanacimiento": generar_fecha_nacimiento(),
            "urlfoto": random.choice(obtener_urls_gatos_aleatorios(1, url)),
            "idorganizacion": random.randint(24, 29),
            "adoptada": random.choice([True, False]),
            "publicacion": random.randint(11, 15),
        }
        mascotas.append(mascota)

    return mascotas

# # Ejemplo de uso: obtener 5 mascotas aleatorias
# url_base = "https://source.unsplash.com/random/900x700/?cat"
# n_mascotas = 10
# mascotas_generadas = crear_mascotas(url_base, n_mascotas)

# # Imprimir las mascotas generadas
# print({"mascotas": mascotas_generadas})



import random
from faker import Faker

def crear_comentarios(n):
    fake = Faker()
    comentarios = []

    for _ in range(n):
        comentario = {
            "autor": random.randint(1, 29),
            "contenido": fake.paragraph(nb_sentences=3),
            "publicacion": random.randint(1, 15),
            "comentario_padre": None,
        }
        comentarios.append(comentario)

    return comentarios

# Ejemplo de uso: obtener 5 comentarios ficticios
n_comentarios = 100
comentarios_generados = crear_comentarios(n_comentarios)
print({"comentarios": comentarios_generados})
print(len(comentarios_generados))