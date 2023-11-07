
def poblar_db(sender, **kwargs):
    agregar_grupos()
    agregar_localidades()
    agregar_personas()
    agregar_organizaciones()
    agregar_publicaciones()
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

    publicaciones = [{
  "idorganizacion": 24,
  "estado": "Disponibles",
  "titulo": "Honorable",
  "descripcion": "Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst.",
  "n_mascotas": 3,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 27,
  "estado": "Adoptados",
  "titulo": "Mrs",
  "descripcion": "Curabitur at ipsum ac tellus semper interdum. Mauris ullamcorper purus sit amet nulla. Quisque arcu libero, rut",
  "n_mascotas": 3,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 25,
  "estado": "Disponibles",
  "titulo": "Rev",
  "descripcion": "Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.",
  "n_mascotas": 1,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 25,
  "estado": "Disponibles",
  "titulo": "Dr",
  "descripcion": "Aenean fermentum. Donec ut mauris eget massa tempor convallis. Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh.",
  "n_mascotas": 5,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 27,
  "estado": "Disponibles",
  "titulo": "Honorable",
  "descripcion": "Duis bibendum, felis sed interdum venenatis, turpis enim blandit mi, in porttitor pede justo eu massa. Donec dapelementum.",
  "n_mascotas": 1,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 26,
  "estado": "Disponibles",
  "titulo": "Rev",
  "descripcion": "Proin eu mi. Nulla ac enim. In tempor, turpis nec euismod scelerisque, quam tura nec sem.",
  "n_mascotas": 1,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 26,
  "estado": "Adoptados",
  "titulo": "Mr",
  "descripcion": "Vestibulum ac est lacinia nisi venenatis tristique. Fuscpien urna pretium nisl, ut volutpat sapienaugue. Aliquam erat volutpat.",
  "n_mascotas": 6,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 26,
  "estado": "Adoptados",
  "titulo": "Ms",
  "descripcion": "Integer tincidunt ante vel ipsum. Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat.",
  "n_mascotas": 8,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 26,
  "estado": "Adoptados",
  "titulo": "Rev",
  "descripcion": "Proin interdum mauris non ligula pellentesque ultrices. Phing molestie, hendrerit at, vulputate vitae, nisl.",
  "n_mascotas": 10,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 28,
  "estado": "Adoptados",
  "titulo": "Mr",
  "descripcion": "Morbi non lectus. Aliquam sit amet diam in magna bibendum imps sed, tincidunt eu, felis.",
  "n_mascotas": 4,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 25,
  "estado": "Disponibles",
  "titulo": "Honorable",
  "descripcion": "Mauris enim leo, rhoncus sed, vestibulum sit amet, curs augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.",
  "n_mascotas": 9,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 28,
  "estado": "Adoptados",
  "titulo": "Mrs",
  "descripcion": "In hac habitasse platea dictumst. Morbi vestibulum, velneque sapien placerat ante. Nulla justo.",
  "n_mascotas": 7,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 27,
  "estado": "Disponibles",
  "titulo": "Dr",
  "descripcion": "In congue. Etiam justo. Etiam pretium iaculis justo.",
  "n_mascotas": 7,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 27,
  "estado": "Adoptados",
  "titulo": "Ms",
  "descripcion": "Aliquam quis turpis eget elit sodales scelerisque. Mauris sit amet eros. Suspendisse accumsan tortor quis turpis.",
  "n_mascotas": 1,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 27,
  "estado": "Adoptados",
  "titulo": "Rev",
  "descripcion": "Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.",
  "n_mascotas": 5,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 26,
  "estado": "Disponibles",
  "titulo": "Ms",
  "descripcion": "Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.",
  "n_mascotas": 5,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 25,
  "estado": "Adoptados",
  "titulo": "Dr",
  "descripcion": "Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi.",
  "n_mascotas": 2,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 24,
  "estado": "Disponibles",
  "titulo": "Dr",
  "descripcion": "Vestibulum ac est lacinia nisi venenatis tristiquretium nisl, ut volutpat sapid augue. Aliquam erat volutpat.",
  "n_mascotas": 7,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 24,
  "estado": "Disponibles",
  "titulo": "Honorable",
  "descripcion": "Duis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.",
  "n_mascotas": 10,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 26,
  "estado": "Disponibles",
  "titulo": "Rev",
  "descripcion": "Aenean fermentum. Donec ut mauris eget massa temptus, ultricies eu, nibh.",
  "n_mascotas": 10,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 25,
  "estado": "Disponibles",
  "titulo": "Mrs",
  "descripcion": "Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus.",
  "n_mascotas": 4,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 25,
  "estado": "Disponibles",
  "titulo": "Mrs",
  "descripcion": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin risus. Praesent lectus.",
  "n_mascotas": 10,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 25,
  "estado": "Adoptados",
  "titulo": "Ms",
  "descripcion": "Vestibulum ac est lacinia nisi venenatis tristique. Fuscelutpat sapien arcu sed augue. Aliquam erat volutpat.",
  "n_mascotas": 7,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 25,
  "estado": "Adoptados",
  "titulo": "Honorable",
  "descripcion": "Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi.",
  "n_mascotas": 5,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 25,
  "estado": "Adoptados",
  "titulo": "Rev",
  "descripcion": "Morbi non lectus. Aliquam sit amet diam in magna bibendunatis non, sodales sed, tincidunt eu, felis.",
  "n_mascotas": 3,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 26,
  "estado": "Disponibles",
  "titulo": "Mrs",
  "descripcion": "Sed ante. Vivamus tortor. Duis mattis egestas metus.",
  "n_mascotas": 1,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 25,
  "estado": "Adoptados",
  "titulo": "Mr",
  "descripcion": "Cras mi pede, malesuada in, imperdiet et, commodo vulp. Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
  "n_mascotas": 1,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 26,
  "estado": "Disponibles",
  "titulo": "Mr",
  "descripcion": "Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi.",
  "n_mascotas": 8,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 25,
  "estado": "Adoptados",
  "titulo": "Ms",
  "descripcion": "Quisque id justo sit amet sapien dignissim vestibulum sollicitudin ut, suscipit a, feugiat et, eros.",
  "n_mascotas": 2,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 27,
  "estado": "Disponibles",
  "titulo": "Dr",
  "descripcion": "Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem.",
  "n_mascotas": 7,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 28,
  "estado": "Disponibles",
  "titulo": "Dr",
  "descripcion": "Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.",
  "n_mascotas": 6,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 24,
  "estado": "Adoptados",
  "titulo": "Dr",
  "descripcion": "Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.",
  "n_mascotas": 9,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 28,
  "estado": "Adoptados",
  "titulo": "Ms",
  "descripcion": "Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus.",
  "n_mascotas": 0,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 27,
  "estado": "Disponibles",
  "titulo": "Honorable",
  "descripcion": "Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.",
  "n_mascotas": 2,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 26,
  "estado": "Adoptados",
  "titulo": "Ms",
  "descripcion": "Fusce consequat. Nulla nisl. Nunc nisl.",
  "n_mascotas": 1,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 26,
  "estado": "Disponibles",
  "titulo": "Dr",
  "descripcion": "Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.",
  "n_mascotas": 9,
  "n_mascotas_adoptadas": 0
}, {
  "idorganizacion": 26,
  "estado": "Adoptados",
  "titulo": "Dr",
  "descripcion": "In hac habitasse platea dictumst. Morbi vestibulum, velit idmentum neque sapien placerat ante. Nulla justo.",
  "n_mascotas": 7,
  "n_mascotas_adoptadas": 0
},
{
  "idorganizacion": 24,
  "estado": "Disponibles",
  "titulo": "Se dan en adopción estos hermosos gatitos",
  "descripcion": "In hac habitasse platea dictumst. Morbi vestibulum, ondimentum neque sapien placerat ante. Nulla justo.",
  "n_mascotas": 7,
  "n_mascotas_adoptadas": 0
},
{
  "idorganizacion": 24,
  "estado": "Disponibles",
  "titulo": "Estamos dando en adopción estos perros callejeros",
  "descripcion": "Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris, felix, perro, labrador.",
  "n_mascotas": 9,
  "n_mascotas_adoptadas": 0
},
 {
  "idorganizacion": 24,
  "estado": "Adoptados",
  "titulo": "Estamos dando en adopción estos perros raza labrador",
  "descripcion": "Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus.",
  "n_mascotas": 9,
  "n_mascotas_adoptadas": 9
},
    ]
    print('vamos en posts: lista de ids de org:', [ f'({org.id}, {org.username})\n' for org in Organizacion.objects.all()])
    # print('vamos en posts: lista de ids de personas:', [
    #       (org.id, org.username) for org in Persona.objects.all()])
    print('numero de publicaciones', len(publicaciones))
    for data in publicaciones:
        extra_fields = {
            key: value
            for key, value in data.items()
            if key not in ['idorganizacion']
        }
        org=None
        try:
          org = Organizacion.objects.get(id=data['idorganizacion'])
          print('org es:', org)
          data['idorganizacion']=org
          print('data es:', data.items(), '\n', type(data["idorganizacion"]))
        except Exception as e:
          print('error: org es None, se salta este ingreso de post, error--> ', e)
          continue
        Publicacion.objects.create(
            **data
        )

    print("\nPublicaciones ficticias agregadas correctamente.")


def agregar_comentarios():
    from posts.models import Comentario, Publicacion
    from accounts.models import Persona, Organizacion
    from django.contrib.auth import get_user_model

    User = get_user_model()

    comentarios = [
        {
            "contenido": "Este es un comentario de prueba.1",
            "es_respuesta": False,
            "comentador": Persona.objects.get(id=2),
            "comentador_org": None,
            "comentario_padre": None,
        },
        {
            "contenido": "Este es otro comentario de prueba2.",
            "es_respuesta": False,
            "comentador": Persona.objects.get(id=3),
            "comentador_org": None,
            "comentario_padre": None,
        },
        {
            "contenido": "Este es un comentario de respuesta.1",
            "es_respuesta": True,
            "comentador": Persona.objects.get(id=4),
            "comentador_org": None,
            "comentario_padre": None,
        },
        {
            "contenido": "Este es otro comentario de respuesta.2",
            "es_respuesta": True,
            "comentador": Persona.objects.get(id=5),
            "comentador_org": None,
            "comentario_padre": None,
        },
        {
            "contenido": "Este es un comentario de una organización1.",
            "es_respuesta": False,
            "comentador_org": Organizacion.objects.get(id=24),
            "comentario_padre": None,
        },
        {
            "contenido": "Este es otro comentario de una organización2.",
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
