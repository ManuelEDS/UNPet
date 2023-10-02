
def poblar_db(sender, **kwargs):
    agregar_grupos()
    agregar_localidades()
    agregar_personas()
    agregar_organizaciones()
    agregar_pulicaciones()

def agregar_grupos():
    from django.contrib.auth.models import Group

    grupos = ["Persona", "Organizacion"]
    lista = [g.name for g in Group.objects.all()]
    print("\n\n\n\n", lista, "\n\n\n\n")
    for grupo in grupos:
        if grupo not in lista:
            Group.objects.create(name=grupo)


def agregar_localidades():
    from .models import Localidad
    # Define una lista de localidades de Bogotá
    localidades_bogota = [
        {"idlocalidad": 1, "nombre": "Usaquén"},
        {"idlocalidad": 2, "nombre": "Chapinero"},
        {"idlocalidad": 3, "nombre": "Santa Fe"},
        {"idlocalidad": 4, "nombre": "San Cristóbal"},
        {"idlocalidad": 5, "nombre": "Usme"},
        {"idlocalidad": 6, "nombre": "Tunjuelito"},
        {"idlocalidad": 7, "nombre": "Bosa"},
        {"idlocalidad": 8, "nombre": "Kennedy"},
        {"idlocalidad": 9, "nombre": "Fontibón"},
        {"idlocalidad": 10, "nombre": "Engativá"},
        {"idlocalidad": 11, "nombre": "Suba"},
        {"idlocalidad": 12, "nombre": "Barrios Unidos"},
        {"idlocalidad": 13, "nombre": "Teusaquillo"},
        {"idlocalidad": 14, "nombre": "Los Mártires"},
        {"idlocalidad": 15, "nombre": "Antonio Nariño"},
        {"idlocalidad": 16, "nombre": "Puente Aranda"},
        {"idlocalidad": 17, "nombre": "La Candelaria"},
        {"idlocalidad": 18, "nombre": "Rafael Uribe Uribe"},
        {"idlocalidad": 19, "nombre": "Ciudad Bolívar"},
        {"idlocalidad": 20, "nombre": "Sumapaz"},
    ]

    # Itera sobre la lista de localidades y agrégalas a la base de datos
    for localidad_data in localidades_bogota:
        localidad = Localidad(**localidad_data)
        localidad.save()

    print("\nLocalidades de Bogotá agregadas correctamente.")


def agregar_organizaciones():
    #from .models import Organizacion
    from django.contrib.auth import get_user_model

    # Obtiene una localidad de Bogotá de la base de datos (puedes ajustar esto)
    user = get_user_model()
    # localidad_bogota = Localidad.objects.get(idlocalidad=1)

    # Define una lista de organizaciones ficticias
    organizaciones_ficticias = [
        {
            "username": "organizacion1",
            "email": "org1@example.com",
            "direccion": "Calle 123",
            "nit": "123456785-15",
            "descripcion": "Organización 1",
            "telefono": "1234567890",
            "urlfoto": "https://example.com/org1.jpg",
            "idlocalidad": 4,
            "password": "contraseñaorganizacion1",
        },
        {
            "username": "organizacion2",
            "email": "org2@example.com",
            "direccion": "Avenida 456",
            "nit": "98765421-28",
            "descripcion": "Organización 2",
            "telefono": "9876543210",
            "urlfoto": "https://example.com/org2.jpg",
            "idlocalidad": 2,
            "password": "contraseñaorganizacion2",
        },
        {
            "username": "organizacion3",
            "email": "org3@example.com",
            "direccion": "Carrera 789",
            "nit": "56789123-37",
            "descripcion": "Organización 3",
            "telefono": "5678901230",
            "urlfoto": "https://example.com/org3.jpg",
            "idlocalidad": 1,
            "password": "contraseñaorganizacion3",
        },
    ]

    # Itera sobre la lista de organizaciones y agrégalas a la base de datos
    for data in organizaciones_ficticias:
        extra_fields = {
            key: value
            for key, value in data.items()
            if key not in ["email", "username", "nit", "password"]
        }
        # print('estos son los extafields- poblar db--->', extra_fields)
        user.objects.create_Organization(
            email=data["email"],
            username=data["username"],
            nit=data["nit"],
            password=data["password"],
            **extra_fields
        )

    print("\nOrganizaciones ficticias agregadas correctamente.")


def agregar_personas():
    from django.contrib.auth import get_user_model

    user = get_user_model()
    # localidad_bogota = Localidad.objects.get(idlocalidad=2)
    personas_data = [
        {
            "username": "persona1",
            "email": "persona1@example.com",
            "tipo_doc": "CC",
            "n_doc": "1234567890",
            "descripcion": "Persona 1",
            "telefono": "1234567890",
            "urlfoto": "https://example.com/persona1.jpg",
            "idlocalidad": 5,  # ID de la localidad correspondiente
            "first_name": "Nombre1",
            "last_name": "Apellido1",
            "date_joined": "2023-09-29T10:00:00Z",
            "sexo": "M",
            "password": "contraseñapersona1",
        },
        {
            "username": "persona2",
            "email": "persona2@example.com",
            "tipo_doc": "TI",
            "n_doc": "0987654321",
            "descripcion": "Persona 2",
            "telefono": "9876543210",
            "urlfoto": "https://example.com/persona2.jpg",
            "idlocalidad": 4,  # ID de la localidad correspondiente
            "first_name": "Nombre2",
            "last_name": "Apellido2",
            "date_joined": "2023-09-30T11:00:00Z",
            "sexo": "F",
            "password": "contraseñapersona2",
        },
    ]
    # Agrega más diccionarios según sea necesario

    # Para crear usuarios a partir de la lista
    for data in personas_data:
        extra_fields = {
            key: value
            for key, value in data.items()
            if key not in ["email", "username", "password"]
        }
        user.objects.create_Persona(
            email=data["email"],
            username=data["username"],
            password=data["password"],
            **extra_fields
        )
    print("\nPersonas ficticias agregadas correctamente.")


def agregar_pulicaciones():
    from posts.models import Publicacion
    from .models import Persona, Organizacion
    # localidad_bogota = Localidad.objects.get(idlocalidad=2)
    #from random import Random as r
    
    publicaciones = [
        {
            "idpublicacion": 1,
            "estado": "disponible",
            "titulo": "Se dan en adopción estos hermosos gatitos",
            "descripcion": "Cinco gatitos adorables en busca de un nuevo hogar.",
            "fechapublicacion": "2023-09-30T14:30:00Z",
            "idorganizacion": 4,  # ID de la organización que publica
            "idpersona": 2,  # No asociado a un usuario individual
        },
        {
            "idpublicacion": 2,
            "estado": "vendido",
            "titulo": "Cachorros de Golden Retriever en adopción",
            "descripcion": "Tres cachorros de Golden Retriever ya encontraron un hogar.",
            "fechapublicacion": "2023-09-28T10:15:00Z",
            "idorganizacion": 3,  # ID de otra organización que publica
            "idpersona": 2,  # No asociado a un usuario individual
        },
        {
            "idpublicacion": 3,
            "estado": "disponible",
            "titulo": "Buscando un hogar para este perrito",
            "descripcion": "Perrito de raza mixta en busca de una familia cariñosa.",
            "fechapublicacion": "2023-09-25T16:45:00Z",
            "idorganizacion": 5,  # No asociado a una organización
            "idpersona": 1,  # ID de un usuario individual que publica
        },
        {
            "idpublicacion": 4,
            "estado": "disponible",
            "titulo": "Dos gatos juguetones necesitan un nuevo hogar",
            "descripcion": "Gatos hermanos que desean encontrar un hogar juntos.",
            "fechapublicacion": "2023-09-22T09:00:00Z",
            "idorganizacion": 3,  # No asociado a una organización
            "idpersona": 2,  # ID de otro usuario individual que publica
        },
    ]
    # Agrega más diccionarios según sea necesario

    # Para crear usuarios a partir de la lista
    for data in publicaciones:
        extra_fields = {
            key: value
            for key, value in data.items()
            if key not in ["idpublicacion", "estado", "descripcion", "titulo", 'idorganizacion', 'idpersona']
        }
        pers = Persona.objects.get(id= data['idpersona'])
        org =Organizacion.objects.get(id= data['idorganizacion'])
        Publicacion(
            idpublicacion=data["idpublicacion"],
            estado=data["estado"],
            descripcion=data["descripcion"],
            titulo=data["titulo"],
            idorganizacion= org,
            idpersona=pers,
            **extra_fields
        )

    print("\nPublicaciones ficticias agregadas correctamente.")
