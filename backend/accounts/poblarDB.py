
def poblar_db(sender, **kwargs):
    agregar_grupos()
    agregar_localidades()
    agregar_personas()
    agregar_organizaciones()
    #agregar_publicaciones()
    #agregar_comentarios()


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
    # from .models import Organizacion
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
        {
            "username": "organizacion4",
            "email": "org4@example.com",
            "direccion": "Calle 123",
            "nit": "12345678-90",
            "descripcion": "Organización 4",
            "telefono": "1234567890",
            "urlfoto": "https://example.com/org4.jpg",
            "idlocalidad": 2,
            "password": "contraseñaorganizacion4",
        },
        {
            "username": "organizacion5",
            "email": "org5@example.com",
            "direccion": "Avenida 456",
            "nit": "23456789-01",
            "descripcion": "Organización 5",
            "telefono": "2345678901",
            "urlfoto": "https://example.com/org5.jpg",
            "idlocalidad": 3,
            "password": "contraseñaorganizacion5",
        },
        {
            "username": "organizacion6",
            "email": "org6@example.com",
            "direccion": "Carrera 789",
            "nit": "34567890-12",
            "descripcion": "Organización 6",
            "telefono": "3456789012",
            "urlfoto": "https://example.com/org6.jpg",
            "idlocalidad": 4,
            "password": "contraseñaorganizacion6",
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
            "idlocalidad": 5,
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
            "idlocalidad": 4,
            "first_name": "Nombre2",
            "last_name": "Apellido2",
            "date_joined": "2023-09-30T11:00:00Z",
            "sexo": "F",
            "password": "contraseñapersona2",
        },
        {
            "username": "fpattenden21",
            "email": "fpattenden21@sun.com",
            "tipo_doc": "TI",
            "n_doc": 6100795522,
            "descripcion": "Programmable asynchronous knowledge user",
            "telefono": 2165536872,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 12,
            "first_name": "Fiann",
            "last_name": "Pattenden",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "F",
            "password": "google.cn"
        }, {
            "username": "rpatemore22",
            "email": "rpatemore22@time.com",
            "tipo_doc": "TI",
            "n_doc": 6625336450,
            "descripcion": "Team-oriented impactful database",
            "telefono": 1221519301,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 19,
            "first_name": "Ronni",
            "last_name": "Patemore",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "F",
            "password": "illinois.edu"
        }, {
            "username": "ecropton23",
            "email": "ecropton23@mysql.com",
            "tipo_doc": "TI",
            "n_doc": 8976258918,
            "descripcion": "Versatile multimedia challenge",
            "telefono": 3005880788,
            "urlfoto": "http://ibm.com/morbi/vel/lectus/in.json?tempus=pellentesque",
            "idlocalidad": 12,
            "first_name": "Erhard",
            "last_name": "Cropton",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "M",
            "password": "marketwatch.com"
        }, {
            "username": "iwallworth24",
            "email": "iwallworth24@hud.gov",
            "tipo_doc": "CC",
            "n_doc": 5558552047,
            "descripcion": "Visionary dedicated customer loyalty",
            "telefono": 5847173712,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 10,
            "first_name": "Isaiah",
            "last_name": "Wallworth",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "M",
            "password": "google.ru"
        }, {
            "username": "hfaulconbridge25",
            "email": "hfaulconbridge25@amazon.com",
            "tipo_doc": "TI",
            "n_doc": 7710717109,
            "descripcion": "Reactive background matrices",
            "telefono": 4643932295,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 8,
            "first_name": "Harley",
            "last_name": "Faulconbridge",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "M",
            "password": "shop-pro.jp"
        }, {
            "username": "fgrestie26",
            "email": "fgrestie26@ning.com",
            "tipo_doc": "CC",
            "n_doc": 1057750974,
            "descripcion": "Total intangible time-frame",
            "telefono": 9458765922,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 8,
            "first_name": "Frants",
            "last_name": "Grestie",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "M",
            "password": "360.cn"
        }, {
            "username": "ecrowcum27",
            "email": "ecrowcum27@nationalgeographic.com",
            "tipo_doc": "CC",
            "n_doc": 9784369274,
            "descripcion": "Multi-layered background strategy",
            "telefono": 9583437305,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 15,
            "first_name": "Edwina",
            "last_name": "Crowcum",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "F",
            "password": "exblog.jp"
        }, {
            "username": "rbutchard28",
            "email": "rbutchard28@lulu.com",
            "tipo_doc": "CC",
            "n_doc": 6795159636,
            "descripcion": "Progressive bifurcated focus group",
            "telefono": 3594958959,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 10,
            "first_name": "Rodolfo",
            "last_name": "Butchard",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "M",
            "password": "free.fr"
        }, {
            "username": "zreuther29",
            "email": "zreuther29@ovh.net",
            "tipo_doc": "TI",
            "n_doc": 2683195354,
            "descripcion": "Profound solution-oriented pricing structure",
            "telefono": 6004484424,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 5,
            "first_name": "Zola",
            "last_name": "Reuther",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "F",
            "password": "epa.gov"
        }, {
            "username": "svalenta2a",
            "email": "svalenta2a@japanpost.jp",
            "tipo_doc": "TI",
            "n_doc": 7518911889,
            "descripcion": "Stand-alone didactic model",
            "telefono": 695983588,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 13,
            "first_name": "Silva",
            "last_name": "Valenta",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "F",
            "password": "comcast.net"
        }, {
            "username": "mfortman2b",
            "email": "mfortman2b@sina.com.cn",
            "tipo_doc": "TI",
            "n_doc": 2122861482,
            "descripcion": "Realigned multimedia customer loyalty",
            "telefono": 2169249565,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 17,
            "first_name": "Marys",
            "last_name": "Fortman",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "F",
            "password": "stanford.edu"
        }, {
            "username": "bduer2c",
            "email": "bduer2c@people.com.cn",
            "tipo_doc": "TI",
            "n_doc": 9792418237,
            "descripcion": "Up-sized mobile orchestration",
            "telefono": 3292659089,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 11,
            "first_name": "Bobinette",
            "last_name": "Duer",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "F",
            "password": "mediafire.com"
        }, {
            "username": "hpaulino2d",
            "email": "hpaulino2d@t-online.de",
            "tipo_doc": "TI",
            "n_doc": 2452928630,
            "descripcion": "Grass-roots static toolset",
            "telefono": 3438275301,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 9,
            "first_name": "Hodge",
            "last_name": "Paulino",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "M",
            "password": "theatlantic.com"
        }, {
            "username": "rfladgate2e",
            "email": "rfladgate2e@github.io",
            "tipo_doc": "CC",
            "n_doc": 2335789740,
            "descripcion": "Persistent actuating matrices",
            "telefono": 6252889506,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 11,
            "first_name": "Raynard",
            "last_name": "Fladgate",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "M",
            "password": "free.fr"
        }, {
            "username": "fhillatt2f",
            "email": "fhillatt2f@zdnet.com",
            "tipo_doc": "TI",
            "n_doc": 5302083451,
            "descripcion": "Future-proofed bi-directional matrix",
            "telefono": 7968092546,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 19,
            "first_name": "Fleming",
            "last_name": "Hillatt",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "M",
            "password": "addthis.com"
        }, {
            "username": "tsullivan2g",
            "email": "tsullivan2g@fema.gov",
            "tipo_doc": "TI",
            "n_doc": 35490250,
            "descripcion": "Distributed fresh-thinking forecast",
            "telefono": 9022444757,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 6,
            "first_name": "Tris",
            "last_name": "Sullivan",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "M",
            "password": "facebook.com"
        }, {
            "username": "dpucknell2h",
            "email": "dpucknell2h@cpanel.net",
            "tipo_doc": "CC",
            "n_doc": 5366270657,
            "descripcion": "Horizontal user-facing portal",
            "telefono": 8443499187,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 1,
            "first_name": "Dorie",
            "last_name": "Pucknell",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "F",
            "password": "deviantart.com"
        }, {
            "username": "lduffin2i",
            "email": "lduffin2i@upenn.edu",
            "tipo_doc": "TI",
            "n_doc": 9580861476,
            "descripcion": "Sharable global alliance",
            "telefono": 6560565754,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 19,
            "first_name": "Leonora",
            "last_name": "Duffin",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "F",
            "password": "jigsy.com"
        }, {
            "username": "wkelsow2j",
            "email": "wkelsow2j@istockphoto.com",
            "tipo_doc": "TI",
            "n_doc": 4426103706,
            "descripcion": "Virtual heuristic approach",
            "telefono": 8823215813,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 7,
            "first_name": "Westbrooke",
            "last_name": "Kelsow",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "M",
            "password": "ask.com"
        }, {
            "username": "imart2k",
            "email": "imart2k@nifty.com",
            "tipo_doc": "CC",
            "n_doc": 7799146707,
            "descripcion": "Up-sized well-modulated productivity",
            "telefono": 5001440080,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 15,
            "first_name": "Isaak",
            "last_name": "Mart",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "M",
            "password": "kickstarter.com"
        }, {
            "username": "amcrill2l",
            "email": "amcrill2l@engadget.com",
            "tipo_doc": "CC",
            "n_doc": 8897711704,
            "descripcion": "Upgradable composite benchmark",
            "telefono": 7464834094,
            "urlfoto": "https://source.unsplash.com/random/600x600/?profile",
            "idlocalidad": 11,
            "first_name": "Ashli",
            "last_name": "McRill",
            "date_joined": "error: invalid date \"2023-09-29T10:00:00Z\"",
            "sexo": "F",
            "password": "merriam-webster.com"
        }, ]

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
    # from random import Random as r

    publicaciones = [
        {
            "id": 1,
            "estado": "disponible",
            "titulo": "Se dan en adopción estos hermosos gatitos",
            "descripcion": "Cinco gatitos adorables en busca de un nuevo hogar.",
            "fechapublicacion": "2023-09-30T14:30:00Z",
            "idorganizacion": 24,  # ID de la organización que publica
            "idpersona": 2,  # No asociado a un usuario individual
        },
        {
            "id": 2,
            "estado": "vendido",
            "titulo": "Cachorros de Golden Retriever en adopción",
            "descripcion": "Tres cachorros de Golden Retriever ya encontraron un hogar.",
            "fechapublicacion": "2023-09-28T10:15:00Z",
            "idorganizacion": 25,  # ID de otra organización que publica
            "idpersona": 2,  # No asociado a un usuario individual
        },
        {
            "id": 3,
            "estado": "disponible",
            "titulo": "Buscando un hogar para este perrito",
            "descripcion": "Perrito de raza mixta en busca de una familia cariñosa.",
            "fechapublicacion": "2023-09-25T16:45:00Z",
            "idorganizacion": 25,  # No asociado a una organización
            "idpersona": 1,  # ID de un usuario individual que publica
        },
        {
            "id": 4,
            "estado": "disponible",
            "titulo": "Dos gatos juguetones necesitan un nuevo hogar",
            "descripcion": "Gatos hermanos que desean encontrar un hogar juntos.",
            "fechapublicacion": "2023-09-22T09:00:00Z",
            "idorganizacion": 28,  # No asociado a una organización
            "idpersona": 2,  # ID de otro usuario individual que publica
        },
    ]
    # Agrega más diccionarios según sea necesario

    # Para crear usuarios a partir de la lista
    for data in publicaciones:
        extra_fields = {
            key: value
            for key, value in data.items()
            if key not in ["id", "estado", "descripcion", "titulo", 'idorganizacion', 'idpersona']
        }
        pers = Persona.objects.get(id=data['idpersona'])
        org = Organizacion.objects.get(id=data['idorganizacion'])
        Publicacion(
            id=data["id"],
            estado=data["estado"],
            descripcion=data["descripcion"],
            titulo=data["titulo"],
            idorganizacion=org,
            idpersona=pers,
            **extra_fields
        )

    print("\nPublicaciones ficticias agregadas correctamente.")


def agregar_publicaciones():
    from posts.models import Publicacion
    from .models import Persona, Organizacion

    publicaciones = [
        {
            "estado": "disponible",
            "titulo": "Se dan en adopción estos hermosos gatitos",
            "descripcion": "Cinco gatitos adorables en busca de un nuevo hogar.",
            "fechapublicacion": "2023-09-30T14:30:00Z",
            "idorganizacion": 24,  # ID de la organización que publica
            "idpersona": 2,  # No asociado a un usuario individual
            "likes": 10,
        },
        {
            "estado": "vendido",
            "titulo": "Cachorros de Golden Retriever en adopción",
            "descripcion": "Tres cachorros de Golden Retriever ya encontraron un hogar.",
            "fechapublicacion": "2023-09-28T10:15:00Z",
            "idorganizacion": 28,  # ID de otra organización que publica
            "idpersona": 2,  # No asociado a un usuario individual
            "likes": 5,
        },
        {
            "estado": "disponible",
            "titulo": "Buscando un hogar para este perrito",
            "descripcion": "Perrito de raza mixta en busca de una familia cariñosa.",
            "fechapublicacion": "2023-09-25T16:45:00Z",
            "idorganizacion": 26,  # No asociado a una organización
            "idpersona": 1,  # ID de un usuario individual que publica
            "likes": 20,
        },
        {
            "estado": "disponible",
            "titulo": "Dos gatos juguetones necesitan un nuevo hogar",
            "descripcion": "Gatos hermanos que desean encontrar un hogar juntos.",
            "fechapublicacion": "2023-09-22T09:00:00Z",
            "idorganizacion": 25,  # No asociado a una organización
            "idpersona": 2,  # ID de otro usuario individual que publica
            "likes": 15,
        },
        {
            "estado": "vendido",
            "titulo": "Honorable",
            "descripcion": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin risus. Praesent lectus.",
            "fechapublicacion": "2022-03-17T04:41:05Z",
            "idorganizacion": 27,
            "idpersona": 9,
            "likes": 2999
        }, {
            "estado": "disponible",
            "titulo": "Rev",
            "descripcion": "Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.",
            "fechapublicacion": "2023-06-22T11:20:34Z",
            "idorganizacion": 26,
            "idpersona": 14,
            "likes": 913
        }, {
            "estado": "vendido",
            "titulo": "Honorable",
            "descripcion": "Maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. Pellentesque viverra pede ac diam. Cras pellentesque volutpat dui.",
            "fechapublicacion": "2022-02-14T10:58:26Z",
            "idorganizacion": 27,
            "idpersona": 12,
            "likes": 1728
        }, {
            "estado": "disponible",
            "titulo": "Mrs",
            "descripcion": "Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
            "fechapublicacion": "2020-11-06T18:22:32Z",
            "idorganizacion": 25,
            "idpersona": 19,
            "likes": 2143
        }, {
            "estado": "disponible",
            "titulo": "Rev",
            "descripcion": "Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.",
            "fechapublicacion": "2023-08-11T15:10:23Z",
            "idorganizacion": 24,
            "idpersona": 13,
            "likes": 1698
        }, {
            "estado": "vendido",
            "titulo": "Dr",
            "descripcion": "Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.",
            "fechapublicacion": "2021-01-22T11:10:13Z",
            "idorganizacion": 24,
            "idpersona": 16,
            "likes": 2123
        }, {
            "estado": "disponible",
            "titulo": "Dr",
            "descripcion": "Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.",
            "fechapublicacion": "2022-01-13T16:59:02Z",
            "idorganizacion": 26,
            "idpersona": 1,
            "likes": 1162
        }, {
            "estado": "vendido",
            "titulo": "Dr",
            "descripcion": "Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.",
            "fechapublicacion": "2021-11-05T15:32:33Z",
            "idorganizacion": 24,
            "idpersona": 5,
            "likes": 757
        }, {
            "estado": "disponible",
            "titulo": "Mr",
            "descripcion": "Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius.",
            "fechapublicacion": "2021-03-24T22:08:08Z",
            "idorganizacion": 25,
            "idpersona": 15,
            "likes": 2699
        }, {
            "estado": "vendido",
            "titulo": "Ms",
            "descripcion": "Nulla ut erat id mauris vulputate elementum. Nullam varius. Nulla facilisi.",
            "fechapublicacion": "2022-02-18T05:54:20Z",
            "idorganizacion": 29,
            "idpersona": 19,
            "likes": 2130
        }, {
            "estado": "vendido",
            "titulo": "Mrs",
            "descripcion": "In hac habitasse platea dictumst. Morbi vestibulum, velit id pretium iaculis, diam erat fermentum justo, nec condimentum neque sapien placerat ante. Nulla justo.",
            "fechapublicacion": "2022-05-03T02:22:32Z",
            "idorganizacion": 29,
            "idpersona": 9,
            "likes": 1443
        }, {
            "estado": "vendido",
            "titulo": "Ms",
            "descripcion": "Maecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem. Quisque ut erat.",
            "fechapublicacion": "2021-04-21T10:28:11Z",
            "idorganizacion": 29,
            "idpersona": 2,
            "likes": 2492
        }, {
            "estado": "vendido",
            "titulo": "Mrs",
            "descripcion": "Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.",
            "fechapublicacion": "2021-02-28T14:27:46Z",
            "idorganizacion": 25,
            "idpersona": 10,
            "likes": 223
        }, {
            "estado": "vendido",
            "titulo": "Ms",
            "descripcion": "Proin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius.",
            "fechapublicacion": "2022-08-20T13:38:43Z",
            "idorganizacion": 24,
            "idpersona": 7,
            "likes": 321
        }, {
            "estado": "vendido",
            "titulo": "Mr",
            "descripcion": "Morbi non lectus. Aliquam sit amet diam in magna bibendum imperdiet. Nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis.",
            "fechapublicacion": "2022-06-30T08:09:57Z",
            "idorganizacion": 29,
            "idpersona": 1,
            "likes": 577
        }, {
            "estado": "disponible",
            "titulo": "Mr",
            "descripcion": "Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.",
            "fechapublicacion": "2021-05-06T04:23:51Z",
            "idorganizacion": 27,
            "idpersona": 6,
            "likes": 748
        }, {
            "estado": "disponible",
            "titulo": "Mr",
            "descripcion": "Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros. Suspendisse accumsan tortor quis turpis.",
            "fechapublicacion": "2022-04-02T07:35:12Z",
            "idorganizacion": 24,
            "idpersona": 19,
            "likes": 1150
        }, {
            "estado": "vendido",
            "titulo": "Ms",
            "descripcion": "Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.",
            "fechapublicacion": "2022-10-21T13:25:23Z",
            "idorganizacion": 27,
            "idpersona": 8,
            "likes": 1226
        }, {
            "estado": "vendido",
            "titulo": "Dr",
            "descripcion": "Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus vestibulum sagittis sapien. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.",
            "fechapublicacion": "2022-01-09T17:54:20Z",
            "idorganizacion": 29,
            "idpersona": 12,
            "likes": 1311
        }, {
            "estado": "disponible",
            "titulo": "Dr",
            "descripcion": "Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.",
            "fechapublicacion": "2023-04-15T06:22:55Z",
            "idorganizacion": 29,
            "idpersona": 13,
            "likes": 972
        }, {
            "estado": "disponible",
            "titulo": "Rev",
            "descripcion": "Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.",
            "fechapublicacion": "2022-04-12T05:37:16Z",
            "idorganizacion": 25,
            "idpersona": 21,
            "likes": 2732
        }, {
            "estado": "vendido",
            "titulo": "Dr",
            "descripcion": "Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.",
            "fechapublicacion": "2021-09-20T10:03:17Z",
            "idorganizacion": 29,
            "idpersona": 10,
            "likes": 1748
        }, {
            "estado": "vendido",
            "titulo": "Mr",
            "descripcion": "Proin interdum mauris non ligula pellentesque ultrices. Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.",
            "fechapublicacion": "2022-08-30T16:25:16Z",
            "idorganizacion": 27,
            "idpersona": 11,
            "likes": 52
        }, {
            "estado": "disponible",
            "titulo": "Rev",
            "descripcion": "Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.",
            "fechapublicacion": "2021-12-25T02:50:13Z",
            "idorganizacion": 28,
            "idpersona": 10,
            "likes": 2238
        }, {
            "estado": "vendido",
            "titulo": "Ms",
            "descripcion": "Curabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rutrum ac, lobortis vel, dapibus at, diam.",
            "fechapublicacion": "2022-07-16T17:37:44Z",
            "idorganizacion": 28,
            "idpersona": 5,
            "likes": 1750
        }, {
            "estado": "disponible",
            "titulo": "Dr",
            "descripcion": "Sed sagittis. Nam congue, risus semper porta volutpat, quam pede lobortis ligula, sit amet eleifend pede libero quis orci. Nullam molestie nibh in lectus.",
            "fechapublicacion": "2023-01-27T12:30:23Z",
            "idorganizacion": 27,
            "idpersona": 9,
            "likes": 932
        }, {
            "estado": "disponible",
            "titulo": "Rev",
            "descripcion": "Aenean lectus. Pellentesque eget nunc. Donec quis orci eget orci vehicula condimentum.",
            "fechapublicacion": "2023-01-16T13:35:30Z",
            "idorganizacion": 28,
            "idpersona": 11,
            "likes": 2227
        }, {
            "estado": "vendido",
            "titulo": "Honorable",
            "descripcion": "Cras non velit nec nisi vulputate nonummy. Maecenas tincidunt lacus at velit. Vivamus vel nulla eget eros elementum pellentesque.",
            "fechapublicacion": "2022-09-29T14:22:18Z",
            "idorganizacion": 24,
            "idpersona": 20,
            "likes": 2219
        }, {
            "estado": "disponible",
            "titulo": "Dr",
            "descripcion": "Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.",
            "fechapublicacion": "2023-03-01T22:56:33Z",
            "idorganizacion": 24,
            "idpersona": 11,
            "likes": 2180
        },
    ]
    print('vamos en posts: lista de ids de org:', [
          (org.id, org.username) for org in Organizacion.objects.all()])
    print('vamos en posts: lista de ids de personas:', [
          (org.id, org.username) for org in Persona.objects.all()])
    for data in publicaciones:
        extra_fields = {
            key: value
            for key, value in data.items()
            if key not in ["estado", "descripcion", "titulo", 'idorganizacion', 'idpersona', 'likes']
        }
        pers = Persona.objects.get(id=data['idpersona'])
        org = Organizacion.objects.get(id=data['idorganizacion'])
        Publicacion.objects.create(
            estado=data["estado"],
            descripcion=data["descripcion"],
            titulo=data["titulo"],
            idorganizacion=org,
            idpersona=pers,
            likes=data["likes"],
            **extra_fields
        )

    print("\nPublicaciones ficticias agregadas correctamente.")


def agregar_comentarios():
    from posts.models import Comentario, Publicacion
    from accounts.models import Persona, Organizacion
    from django.contrib.auth import get_user_model

    User = get_user_model()

    comentarios = [
        {
            "contenido": "Este es un comentario de prueba.",
            "es_respuesta": False,
            "comentador": Persona.objects.get(id=2),
            "comentador_org": None,
            "comentario_padre": None,
        },
        {
            "contenido": "Este es otro comentario de prueba.",
            "es_respuesta": False,
            "comentador": Persona.objects.get(id=3),
            "comentador_org": None,
            "comentario_padre": None,
        },
        {
            "contenido": "Este es un comentario de respuesta.",
            "es_respuesta": True,
            "comentador": Persona.objects.get(id=4),
            "comentador_org": None,
            "comentario_padre": None,
        },
        {
            "contenido": "Este es otro comentario de respuesta.",
            "es_respuesta": True,
            "comentador": Persona.objects.get(id=5),
            "comentador_org": None,
            "comentario_padre": None,
        },
        {
            "contenido": "Este es un comentario de una organización.",
            "es_respuesta": False,
            "comentador_org": Organizacion.objects.get(id=24),
            "comentario_padre": None,
        },
        {
            "contenido": "Este es otro comentario de una organización.",
            "es_respuesta": False,
            "comentador_org": Organizacion.objects.get(id=25),
            "comentario_padre": None,
        },
    ]

    for comentario_data in comentarios:
        # Crear la instancia de Comentario sin asignar publicaciones
        comentario = Comentario.objects.create(**comentario_data)

        # Obtener las IDs de las publicaciones y asignarlas
        publicaciones_ids = comentario_data.get("publicaciones")
        if publicaciones_ids:
            comentario.publicaciones.set(
                Publicacion.objects.filter(id__in=publicaciones_ids))

    print("\nComentarios ficticios agregados correctamente.")
