def poblar_db(sender, **kwargs):
    agregar_grupos()
    agregar_localidades()
    agregar_personas()
    agregar_organizaciones()
    agregar_publicaciones()
    agregar_mascotas()
    agregar_comentarios()
    agregar_respuestas()


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
            "name": "Fundacion huellitas alegres",
            "email": "org1@example.com",
            "direccion": "Calle 123",
            "nit": "123456785-15",
            "descripcion": "Organización 1",
            "telefono": "1234567890",
            "urlfoto": "https://images.unsplash.com/photo-1598888831641-72b238bc5bae?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8cGV0cyxsb2dvfHx8fHx8MTcwMDMzNjAyMQ&ixlib=rb-4.0.3&q=80&w=900",
            "idlocalidad": 4,
            "password": "contraseñaorganizacion1",
        },
        {
            "username": "organizacion2",
            "name": "Fundacion Mascotas felices",
            "email": "org2@example.com",
            "direccion": "Avenida 456",
            "nit": "98765421-28",
            "descripcion": "Organización 2",
            "telefono": "9876543210",
            "urlfoto": "https://images.unsplash.com/photo-1626012303270-9b3ad43ee13b?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8cGV0cyxsb2dvfHx8fHx8MTcwMDMzNjA1NA&ixlib=rb-4.0.3&q=80&w=900",
            "idlocalidad": 2,
            "password": "contraseñaorganizacion2",
        },
        {
            "username": "organizacion3",
            "name": "Adopta Ya!: Fundacion de mascotas (Chapinero)",
            "email": "org3@example.com",
            "direccion": "Carrera 789",
            "nit": "56789123-37",
            "descripcion": "Organización 3",
            "telefono": "5678901230",
            "urlfoto": "https://images.unsplash.com/photo-1535294533130-c1a6b771aa9e?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8cGV0cyxsb2dvfHx8fHx8MTcwMDMzNjA2OA&ixlib=rb-4.0.3&q=80&w=900",
            "idlocalidad": 1,
            "password": "contraseñaorganizacion3",
        },
        {
            "username": "organizacion4",
            "name": "LovePets (Sede Teusaquillo)",
            "email": "org4@example.com",
            "direccion": "Calle 123",
            "nit": "12345678-90",
            "descripcion": "Organización 4",
            "telefono": "1234567890",
            "urlfoto": "https://images.unsplash.com/photo-1573625585535-44f12e52f1d7?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8cGV0cyxsb2dvfHx8fHx8MTcwMDMzNjExOQ&ixlib=rb-4.0.3&q=80&w=900",
            "idlocalidad": 2,
            "password": "contraseñaorganizacion4",
        },
        {
            "username": "organizacion5",
            "name": "Mascotas OnLinePet (Adopciones en línea)",
            "email": "org5@example.com",
            "direccion": "Avenida 456",
            "nit": "23456789-01",
            "descripcion": "Organización 5",
            "telefono": "2345678901",
            "urlfoto": "https://images.unsplash.com/photo-1495953852792-8b6722cbd195?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8cGV0cyxsb2dvfHx8fHx8MTcwMDMzNjEyOA&ixlib=rb-4.0.3&q=80&w=900",
            "idlocalidad": 3,
            "password": "contraseñaorganizacion5",
        },
        {
            "username": "organizacion6",
            "name": "Tu Mundo Mascota  (Bosa)",
            "email": "org6@example.com",
            "direccion": "Carrera 789",
            "nit": "34567890-12",
            "descripcion": "Organización 6",
            "telefono": "3456789012",
            "urlfoto": "https://images.unsplash.com/photo-1618774658704-e7f58f3ff260?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8cGV0cyxsb2dvfHx8fHx8MTcwMDMzNjE3MA&ixlib=rb-4.0.3&q=80&w=900",
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
            "urlfoto": "https://images.unsplash.com/photo-1520271348391-049dd132bb7c?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=400&ixid=MnwxfDB8MXxyYW5kb218MHx8cHJvZmlsZXx8fHx8fDE3MDAzMzc3MTU&ixlib=rb-4.0.3&q=80&w=400",
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
            "urlfoto": "https://images.unsplash.com/photo-1516767784670-cfc730ed0f87?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=400&ixid=MnwxfDB8MXxyYW5kb218MHx8cHJvZmlsZXx8fHx8fDE3MDAzMzc2Nzc&ixlib=rb-4.0.3&q=80&w=400",
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
            "urlfoto": "https://images.unsplash.com/photo-1556157382-97eda2d62296?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=400&ixid=MnwxfDB8MXxyYW5kb218MHx8cHJvZmlsZXx8fHx8fDE3MDAzMzc3MzY&ixlib=rb-4.0.3&q=80&w=400",
            "idlocalidad": 12,
            "first_name": "Fiann",
            "last_name": "Pattenden",
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "F",
            "password": "google.cn",
        },
        {
            "username": "rpatemore22",
            "email": "rpatemore22@time.com",
            "tipo_doc": "TI",
            "n_doc": 6625336450,
            "descripcion": "Team-oriented impactful database",
            "telefono": 1221519301,
            "urlfoto": "https://images.unsplash.com/photo-1579783901467-31b604eac7a8?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=400&ixid=MnwxfDB8MXxyYW5kb218MHx8cHJvZmlsZXx8fHx8fDE3MDAzMzc3NDk&ixlib=rb-4.0.3&q=80&w=400",
            "idlocalidad": 19,
            "first_name": "Ronni",
            "last_name": "Patemore",
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "F",
            "password": "illinois.edu",
        },
        {
            "username": "ecropton23",
            "email": "ecropton23@mysql.com",
            "tipo_doc": "TI",
            "n_doc": 8976258918,
            "descripcion": "Versatile multimedia challenge",
            "telefono": 3005880788,
            "urlfoto": "https://images.unsplash.com/photo-1522778147829-047360bdc7f6?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=400&ixid=MnwxfDB8MXxyYW5kb218MHx8cHJvZmlsZXx8fHx8fDE3MDAzMzc3NjA&ixlib=rb-4.0.3&q=80&w=400",
            "idlocalidad": 12,
            "first_name": "Erhard",
            "last_name": "Cropton",
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "M",
            "password": "marketwatch.com",
        },
        {
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
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "M",
            "password": "google.ru",
        },
        {
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
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "M",
            "password": "shop-pro.jp",
        },
        {
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
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "M",
            "password": "360.cn",
        },
        {
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
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "F",
            "password": "exblog.jp",
        },
        {
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
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "M",
            "password": "free.fr",
        },
        {
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
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "F",
            "password": "epa.gov",
        },
        {
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
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "F",
            "password": "comcast.net",
        },
        {
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
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "F",
            "password": "stanford.edu",
        },
        {
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
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "F",
            "password": "mediafire.com",
        },
        {
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
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "M",
            "password": "theatlantic.com",
        },
        {
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
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "M",
            "password": "free.fr",
        },
        {
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
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "M",
            "password": "addthis.com",
        },
        {
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
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "M",
            "password": "facebook.com",
        },
        {
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
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "F",
            "password": "deviantart.com",
        },
        {
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
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "F",
            "password": "jigsy.com",
        },
        {
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
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "M",
            "password": "ask.com",
        },
        {
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
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "M",
            "password": "kickstarter.com",
        },
        {
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
            "date_joined": 'error: invalid date "2023-09-29T10:00:00Z"',
            "sexo": "F",
            "password": "merriam-webster.com",
        },
    ]

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


def agregar_publicaciones():
    from posts.models import Publicacion
    from .models import Persona, Organizacion

    publicaciones = [
        # GATOS:
        {
            "idorganizacion": 24,
            "estado": "Disponibles",
            "titulo": "Se da en adopción este hermoso gato de dos meses de edad",
            "descripcion": "Su nombre es Tom y es un gato muy juguetón y cariñoso.",
            "n_mascotas": 1,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 27,
            "estado": "Adoptados",
            "titulo": "Gatos en adopción esperando que los adoptes",
            "descripcion": "Estos gatos esperan a su nuevo dueño el cual puede ser tú.",
            "n_mascotas": 2,
            "n_mascotas_adoptadas": 1,
        },
        {
            "idorganizacion": 26,
            "estado": "Disponibles",
            "titulo": "Mr 4 meses de nacido, gatos en adopcion, perros en adopcion, perros ",
            "descripcion": "Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi.",
            "n_mascotas": 8,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 25,
            "estado": "Adoptados",
            "titulo": "Ms chapinero suba, gatos cariñosos, gatos en adopcion, gatos en adopcion bogota",
            "descripcion": "Quisque id justo sit amet sapien dignissim vestibulum sollicitudin ut, suscipit a, feugiat et, eros.",
            "n_mascotas": 2,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 27,
            "estado": "Disponibles",
            "titulo": "Dr gatos raza persa, gatos en adopcion, gatos en adopcion bogota, gatos en adopcion chapinero, gatos en adopcion suba",
            "descripcion": "Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem.",
            "n_mascotas": 7,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 28,
            "estado": "Disponibles",
            "titulo": "Dr perros raza labrador, raza criolla perros en adopcion, perros en adopcion bogota,  suba",
            "descripcion": "Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.",
            "n_mascotas": 6,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 24,
            "estado": "Adoptados",
            "titulo": "Dr perros raza labrador, raza criolla perros en adopcion, parkway en adopcion bogota,  suba",
            "descripcion": "Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.",
            "n_mascotas": 9,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 28,
            "estado": "Adoptados",
            "titulo": "Ms animalitos recien nacidos en adopcion, gatos en adopcion, perros en adopcion",
            "descripcion": "Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus.",
            "n_mascotas": 0,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 27,
            "estado": "Disponibles",
            "titulo": "Hermosos gatos en adopción esperando que los adoptes y les des un hogar, parkway",
            "descripcion": "Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.",
            "n_mascotas": 2,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 26,
            "estado": "Adoptados",
            "titulo": "Ms gatos en adopcion, perros en adopcion, perros en adopcion bogota, gatos en adopcion bogota",
            "descripcion": "Fusce consequat. Nulla nisl. Nunc nisl., Nos ubicamos en el parkway",
            "n_mascotas": 1,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 26,
            "estado": "Disponibles",
            "titulo": "Dr perros gatos en adopcion engativa, perros gatos en adopcion suba, perros gatos en adopcion chapinero",
            "descripcion": "Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.",
            "n_mascotas": 9,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 26,
            "estado": "Adoptados",
            "titulo": "Dr mascotas adopcion perro salchicha, gato, perro labrador, perro callejero",
            "descripcion": "In hac habitasse platea dictumst. Morbi vestibulum, velit idmentum neque sapien placerat ante. Nulla justo.",
            "n_mascotas": 7,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 24,
            "estado": "Disponibles",
            "titulo": "Se dan en adopción estos hermosos gatitos",
            "descripcion": "In hac habitasse platea dictumst. Morbi vestibulum, ondimentum neque sapien placerat ante. Nulla justo.",
            "n_mascotas": 7,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 24,
            "estado": "Disponibles",
            "titulo": "Estamos dando en adopción estos perros callejeros",
            "descripcion": "Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris, felix, perro, labrador.",
            "n_mascotas": 9,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 24,
            "estado": "Adoptados",
            "titulo": "Estamos dando en adopción estos perros raza labrador",
            "descripcion": "Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus.",
            "n_mascotas": 9,
            "n_mascotas_adoptadas": 9,
        },
    ]
    # print('vamos en posts: lista de ids de org:', [ f'({org.id}, {org.username})\n' for org in Organizacion.objects.all()])
    # print('vamos en posts: lista de ids de personas:', [
    #       (org.id, org.username) for org in Persona.objects.all()])
    print("numero de publicaciones", len(publicaciones))
    for data in publicaciones:

        extra_fields = {
            key: value for key, value in data.items() if key not in ["idorganizacion"]
        }
        org = None
        try:
            org = Organizacion.objects.get(id=data["idorganizacion"])
            # print('org es:', org)
            data["idorganizacion"] = org
            # print('data es:', data.items(), '\n', type(data["idorganizacion"]))
        except Exception as e:
            print("error: org es None, se salta este ingreso de post, error--> ", e)
            continue
        Publicacion.objects.create(**data)

    print("\nPublicaciones ficticias agregadas correctamente.")


def agregar_mascotas():
    from pets.models import Mascota
    from posts.models import Publicacion
    from accounts.models import Organizacion

    pets = [
        # GATOS:
        {
            "nombre": "Fido",
            "especie": "Gato",
            "raza": "",
            "sexo": "Macho",
            "fechanacimiento": "2015-07-01",
            "urlfoto": "https://images.unsplash.com/photo-1572582683267-2874e6c5678d?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Z2F0b3x8fHx8fDE3MDAzNTUwNDA&ixlib=rb-4.0.3&q=80&w=900",
            "idorganizacion": 24,
            "adoptada": False,
            "publicacion": 1,
        },
        {
            "nombre": "nikky",
            "especie": "Hembra",
            "raza": "",
            "sexo": "Macho",
            "fechanacimiento": "2018-07-01",
            "urlfoto": "https://previews.123rf.com/images/serkucher/serkucher1708/serkucher170800338/84265017-gato-joven-y-gatito-concepto-gatito-peque%C3%B1o-sobre-un-fondo-de-madera.jpg",
            "idorganizacion": 24,
            "adoptada": False,
            "publicacion": 2,
        },
        {
            "nombre": "Chita",
            "especie": "Gato",
            "raza": "",
            "sexo": "Hembra",
            "fechanacimiento": "2015-07-01",
            "urlfoto": "https://images.unsplash.com/photo-1580784355694-0d5295dcc007?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDIzNzk4NA&ixlib=rb-4.0.3&q=80&w=900",
            "idorganizacion": 24,
            "adoptada": False,
            "publicacion": 2,
        },
        {
            "nombre": "Shadow",
            "especie": "Gato",
            "raza": "Desconocida",
            "sexo": "Hembra",
            "fechanacimiento": "2021-09-24",
            "urlfoto": "https://images.unsplash.com/photo-1618424160135-fe3b7680af1e?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MDY3Ng&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 26,
            "adoptada": True,
            "publicacion": 7,
        },
        {
            "nombre": "Fluffy",
            "especie": "Gato",
            "raza": "Desconocida",
            "sexo": "Hembra",
            "fechanacimiento": "2020-02-08",
            "urlfoto": "https://images.unsplash.com/photo-1568152950566-c1bf43f4ab28?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MDY3OA&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 27,
            "adoptada": False,
            "publicacion": 9,
        },
        {
            "nombre": "Shadow",
            "especie": "Gato",
            "raza": "Desconocida",
            "sexo": "Hembra",
            "fechanacimiento": "2021-08-22",
            "urlfoto": "https://images.unsplash.com/photo-1493548578639-b0c241186eb0?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MDY3OQ&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 24,
            "adoptada": False,
            "publicacion": 5,
        },
        {
            "nombre": "Mittens",
            "especie": "Gato",
            "raza": "Desconocida",
            "sexo": "Hembra",
            "fechanacimiento": "2014-08-06",
            "urlfoto": "https://images.unsplash.com/photo-1612532276780-14ed318a03e0?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MDY4Mg&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 25,
            "adoptada": False,
            "publicacion": 7,
        },
        {
            "nombre": "Shadow",
            "especie": "Gato",
            "raza": "Desconocida",
            "sexo": "Macho",
            "fechanacimiento": "2013-12-09",
            "urlfoto": "https://images.unsplash.com/photo-1606509769472-7660d4a478ac?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MDY4OA&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 26,
            "adoptada": False,
            "publicacion": 5,
        },
        {
            "nombre": "Luna",
            "especie": "Gato",
            "raza": "Desconocida",
            "sexo": "Macho",
            "fechanacimiento": "2015-11-08",
            "urlfoto": "https://images.unsplash.com/photo-1549545931-59bf067af9ab?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MDY5MQ&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 29,
            "adoptada": False,
            "publicacion": 3,
        },
        {
            "nombre": "Mittens",
            "especie": "Gato",
            "raza": "Desconocida",
            "sexo": "Hembra",
            "fechanacimiento": "2015-09-11",
            "urlfoto": "https://images.unsplash.com/photo-1566847438217-76e82d383f84?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MDY5Mg&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 25,
            "adoptada": True,
            "publicacion": 5,
        },
        {
            "nombre": "Fido",
            "especie": "Gato",
            "raza": "Desconocida",
            "sexo": "Hembra",
            "fechanacimiento": "2016-12-20",
            "urlfoto": "https://images.unsplash.com/photo-1566513317351-c6d7be11505e?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MDY5NA&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 29,
            "adoptada": False,
            "publicacion": 3,
        },
        {
            "nombre": "Shadow",
            "especie": "Gato",
            "raza": "Desconocida",
            "sexo": "Hembra",
            "fechanacimiento": "2015-03-11",
            "urlfoto": "https://images.unsplash.com/photo-1501820488136-72669149e0d4?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MDY5Ng&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 24,
            "adoptada": False,
            "publicacion": 8,
        },
        {
            "nombre": "Fluffy",
            "especie": "Gato",
            "raza": "Desconocida",
            "sexo": "Hembra",
            "fechanacimiento": "2020-06-02",
            "urlfoto": "https://images.unsplash.com/photo-1545249390-6bdfa286032f?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MDY5OA&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 27,
            "adoptada": False,
            "publicacion": 7,
        },
        # PERROS:
        {
            "nombre": "Rocky",
            "especie": "Perro",
            "raza": "Desconocida",
            "sexo": "Macho",
            "fechanacimiento": "2020-05-08",
            "urlfoto": "https://images.unsplash.com/photo-1571566882372-1598d88abd90?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MTQyNw&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 28,
            "adoptada": False,
            "publicacion": 14,
        },
        {
            "nombre": "Lucy",
            "especie": "Perro",
            "raza": "Desconocida",
            "sexo": "Hembra",
            "fechanacimiento": "2014-11-19",
            "urlfoto": "https://images.unsplash.com/photo-1618924217601-502b99239681?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MTQyOQ&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 25,
            "adoptada": False,
            "publicacion": 11,
        },
        {
            "nombre": "Cooper",
            "especie": "Perro",
            "raza": "Desconocida",
            "sexo": "Macho",
            "fechanacimiento": "2015-05-12",
            "urlfoto": "https://images.unsplash.com/photo-1546180572-28e937c8128b?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MTQzNw&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 26,
            "adoptada": False,
            "publicacion": 12,
        },
        {
            "nombre": "Cooper",
            "especie": "Perro",
            "raza": "Desconocida",
            "sexo": "Hembra",
            "fechanacimiento": "2016-06-09",
            "urlfoto": "https://images.unsplash.com/photo-1536589961747-e239b2abbec2?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MTQ0MA&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 25,
            "adoptada": True,
            "publicacion": 12,
        },
        {
            "nombre": "Daisy",
            "especie": "Perro",
            "raza": "Desconocida",
            "sexo": "Hembra",
            "fechanacimiento": "2016-01-20",
            "urlfoto": "https://images.unsplash.com/photo-1560114928-40f1f1eb26a0?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MTQ0Mw&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 27,
            "adoptada": True,
            "publicacion": 12,
        },
        {
            "nombre": "Buddy",
            "especie": "Perro",
            "raza": "Desconocida",
            "sexo": "Macho",
            "fechanacimiento": "2019-10-03",
            "urlfoto": "https://images.unsplash.com/photo-1617112513579-d8755a2c4693?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MTQ0NA&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 28,
            "adoptada": False,
            "publicacion": 4,
        },
        {
            "nombre": "Buddy",
            "especie": "Perro",
            "raza": "Desconocida",
            "sexo": "Hembra",
            "fechanacimiento": "2021-06-01",
            "urlfoto": "https://images.unsplash.com/photo-1618826411640-d6df44dd3f7a?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MTQ0Ng&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 27,
            "adoptada": False,
            "publicacion": 6,
        },
        {
            "nombre": "Charlie",
            "especie": "Perro",
            "raza": "Desconocida",
            "sexo": "Hembra",
            "fechanacimiento": "2017-05-08",
            "urlfoto": "https://images.unsplash.com/photo-1612532276780-14ed318a03e0?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MTQ0OA&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 28,
            "adoptada": False,
            "publicacion": 10,
        },
        {
            "nombre": "Luna",
            "especie": "Perro",
            "raza": "Desconocida",
            "sexo": "Hembra",
            "fechanacimiento": "2015-02-18",
            "urlfoto": "https://images.unsplash.com/photo-1530991671072-ac4f81c2c3c1?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MTQ1MA&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 24,
            "adoptada": True,
            "publicacion": 13,
        },
        {
            "nombre": "Cooper",
            "especie": "Perro",
            "raza": "Desconocida",
            "sexo": "Hembra",
            "fechanacimiento": "2020-11-13",
            "urlfoto": "https://images.unsplash.com/photo-1545249390-6bdfa286032f?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MTQ1Mg&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900",
            "idorganizacion": 27,
            "adoptada": True,
            "publicacion": 15,
        },
    ]

    print("vamos en pets: ")
    # print('vamos en posts: lista de ids de personas:', [
    #       (org.id, org.username) for org in Persona.objects.all()])
    print("numero de pets", len(pets))

    for data in pets:
        org = None
        post = None
        try:
            # id organizaciones: [24 - 29] | is personas: [1 - 23]
            org = Organizacion.objects.get(id=data["idorganizacion"])

            post = (
                Publicacion.objects.get(id=data["publicacion"])
                if data["publicacion"] is not None
                else None
            )
            print("org es:", org)
            data["idorganizacion"] = org
            data["publicacion"] = post

        except Exception as e:
            print(
                "error: org o post es None, se salta este ingreso de post|org, error--> ",
                e,
            )
            continue
        Mascota.objects.create(**data)

    print("\Mascotas ficticias agregadas correctamente.")


def agregar_comentarios():
    from posts.models import Comentario, Publicacion
    from accounts.models import Persona, Organizacion
    from django.contrib.auth import get_user_model

    User = get_user_model()
    # id organizaciones: [24 - 29] | is personas: [1 - 23]

    # autor_persona = models.ForeignKey(
    #         'accounts.Persona', on_delete=models.CASCADE, related_name='comentarios', blank=True, null=True)
    #     autor_organizacion = models.ForeignKey(
    #         'accounts.Organizacion', on_delete=models.CASCADE, related_name='comentarios', blank=True, null=True)
    #     contenido = models.CharField(max_length=300)
    #     publicacion = models.ForeignKey(
    #         Publicacion, on_delete=models.CASCADE, related_name='comentarios', blank=True, null=True)
    #     comentario_padre = models.ForeignKey(
    #         'self', on_delete=models.CASCADE, related_name='respuestas', blank=True, null=True)
    #     fechapublicacion = models.DateTimeField(auto_now_add=True)
    comentarios = [
        {
            "autor": 14,
            "contenido": "Recently week leader make anything such mind. Upon several between take feel fear fine. National than control long particular they during hit. Effort senior score.",
            "publicacion": 7,
            "comentario_padre": None,
        },
        {
            "autor": 20,
            "contenido": "Price arm defense bank after far live. Eight most represent view drop else wear.",
            "publicacion": 3,
            "comentario_padre": None,
        },
        {
            "autor": 14,
            "contenido": "Only together star machine main us interesting. His life direction law.",
            "publicacion": 13,
            "comentario_padre": None,
        },
        {
            "autor": 21,
            "contenido": "Easy walk manage guess. Inside thus pick.",
            "publicacion": 1,
            "comentario_padre": None,
        },
        {
            "autor": 1,
            "contenido": "Happen list mention economy. Success around fall sound list former woman better. Drive way view sit start sometimes.",
            "publicacion": 10,
            "comentario_padre": None,
        },
        {
            "autor": 14,
            "contenido": "Finish carry much only course maybe. Machine science spring serious yes particular with. Once company wall picture model already.",
            "publicacion": 6,
            "comentario_padre": None,
        },
        {
            "autor": 5,
            "contenido": "Energy hot buy blood store rate couple. Involve be data concern whatever. Build hundred standard down friend.",
            "publicacion": 5,
            "comentario_padre": None,
        },
        {
            "autor": 24,
            "contenido": "Surface him must part yes end. Central fund make kid join.",
            "publicacion": 15,
            "comentario_padre": None,
        },
        {
            "autor": 18,
            "contenido": "Put energy goal without plan admit to resource.",
            "publicacion": 5,
            "comentario_padre": None,
        },
        {
            "autor": 13,
            "contenido": "Compare way draw develop indicate. Most agency somebody player. Brother different pass them firm smile discuss.",
            "publicacion": 5,
            "comentario_padre": None,
        },
        {
            "autor": 13,
            "contenido": "Step finish beautiful thus little majority. Scene painting full central bit.",
            "publicacion": 7,
            "comentario_padre": None,
        },
        {
            "autor": 22,
            "contenido": "Stay thousand yes sport year while college north. Score never usually whole experience never.",
            "publicacion": 3,
            "comentario_padre": None,
        },
        {
            "autor": 1,
            "contenido": "Ever onto impact miss bar discuss. Whose me move either.",
            "publicacion": 8,
            "comentario_padre": None,
        },
        {
            "autor": 11,
            "contenido": "Plant dinner board station. Perform future home dark church student. Serious only strong majority its much.",
            "publicacion": 8,
            "comentario_padre": None,
        },
        {
            "autor": 9,
            "contenido": "Final operation executive moment. Could inside occur true even her seven leg. Really artist cultural.",
            "publicacion": 7,
            "comentario_padre": None,
        },
        {
            "autor": 5,
            "contenido": "Let nature bank degree professor cultural build. Approach bit center visit end. Officer computer buy result us line discussion can.",
            "publicacion": 14,
            "comentario_padre": None,
        },
        {
            "autor": 5,
            "contenido": "Leave single information.",
            "publicacion": 2,
            "comentario_padre": None,
        },
        {
            "autor": 2,
            "contenido": "Oil pretty take film. Under president cut together institution leave seem discuss.",
            "publicacion": 8,
            "comentario_padre": None,
        },
        {
            "autor": 11,
            "contenido": "See radio keep draw class push. Real thing again third special nice. Decision she site same total white. Floor who space hospital weight soldier.",
            "publicacion": 7,
            "comentario_padre": None,
        },
        {
            "autor": 27,
            "contenido": "Fall since simple material.",
            "publicacion": 9,
            "comentario_padre": None,
        },
        {
            "autor": 24,
            "contenido": "Able attention teacher step senior professional measure. Discussion find fire feeling crime concern each.",
            "publicacion": 5,
            "comentario_padre": None,
        },
        {
            "autor": 23,
            "contenido": "Yard opportunity somebody his.",
            "publicacion": 11,
            "comentario_padre": None,
        },
        {
            "autor": 18,
            "contenido": "So today case decide. Drug term store child.",
            "publicacion": 6,
            "comentario_padre": None,
        },
        {
            "autor": 10,
            "contenido": "Sort ok paper just. Our new soon argue which.",
            "publicacion": 2,
            "comentario_padre": None,
        },
        {
            "autor": 25,
            "contenido": "Perhaps skill by now price medical successful determine. Too agency another book key.",
            "publicacion": 13,
            "comentario_padre": None,
        },
        {
            "autor": 15,
            "contenido": "Really finally dog himself often. Next wish personal after wrong. Street require person wife whether kitchen cause evidence.",
            "publicacion": 10,
            "comentario_padre": None,
        },
        {
            "autor": 12,
            "contenido": "Certain environment every east. Herself garden green treatment national among prepare. Democratic smile page run.",
            "publicacion": 10,
            "comentario_padre": None,
        },
        {
            "autor": 29,
            "contenido": "Capital point hair out ground low. Lawyer family action sing analysis. Add decade mouth control economy whole. Experience purpose forget current beyond bar direction adult.",
            "publicacion": 5,
            "comentario_padre": None,
        },
        {
            "autor": 17,
            "contenido": "Stock value us. Guy particularly ten direction green.",
            "publicacion": 12,
            "comentario_padre": None,
        },
        {
            "autor": 14,
            "contenido": "Evening change large. Ever lose seek.",
            "publicacion": 14,
            "comentario_padre": None,
        },
        {
            "autor": 21,
            "contenido": "Fast rule reality.",
            "publicacion": 2,
            "comentario_padre": None,
        },
        {
            "autor": 18,
            "contenido": "Option national meet decide seven own among. May piece purpose material almost. Name employee science issue beyond.",
            "publicacion": 5,
            "comentario_padre": None,
        },
        {
            "autor": 2,
            "contenido": "Material loss beyond ahead ground police plant deal. Do can follow act. Scene data employee item. Explain yourself former key.",
            "publicacion": 12,
            "comentario_padre": None,
        },
        {
            "autor": 14,
            "contenido": "Defense ten medical often out simple. Reveal fund agent range property above could none.",
            "publicacion": 4,
            "comentario_padre": None,
        },
        {
            "autor": 12,
            "contenido": "Of bar production give heart scientist.",
            "publicacion": 3,
            "comentario_padre": None,
        },
        {
            "autor": 10,
            "contenido": "Early garden war serious me add. Deep your their feel type. Nature poor contain stuff build fly.",
            "publicacion": 2,
            "comentario_padre": None,
        },
        {
            "autor": 24,
            "contenido": "Painting travel stuff use would particularly. Such whole heart spring ago over.",
            "publicacion": 6,
            "comentario_padre": None,
        },
        {
            "autor": 21,
            "contenido": "Into hit style window middle. Leg or friend Republican. House nature nature drug.",
            "publicacion": 7,
            "comentario_padre": None,
        },
        {
            "autor": 27,
            "contenido": "Article husband that approach organization. Reach then majority.",
            "publicacion": 8,
            "comentario_padre": None,
        },
        {
            "autor": 8,
            "contenido": "When contain meeting mean thing. Land nature them pattern add.",
            "publicacion": 4,
            "comentario_padre": None,
        },
        {
            "autor": 11,
            "contenido": "A in minute large five technology.",
            "publicacion": 2,
            "comentario_padre": None,
        },
        {
            "autor": 17,
            "contenido": "President far so space away this forget. Piece month better.",
            "publicacion": 14,
            "comentario_padre": None,
        },
        {
            "autor": 19,
            "contenido": "Wrong huge including wonder it. Start rich cut everyone meet.",
            "publicacion": 2,
            "comentario_padre": None,
        },
        {
            "autor": 4,
            "contenido": "Draw total nice do suffer billion. Run board enough employee positive recognize.",
            "publicacion": 9,
            "comentario_padre": None,
        },
        {
            "autor": 19,
            "contenido": "Full medical small. Idea stage chair political process. Already program best.",
            "publicacion": 4,
            "comentario_padre": None,
        },
        {
            "autor": 11,
            "contenido": "Turn his against whose group serious forget. Unit car not to PM front. Drive information maintain.",
            "publicacion": 1,
            "comentario_padre": None,
        },
        {
            "autor": 21,
            "contenido": "Can artist worry establish task as tax. Agent project system rock machine.",
            "publicacion": 8,
            "comentario_padre": None,
        },
        {
            "autor": 21,
            "contenido": "Skin throughout discuss myself. Heart decade focus none city of.",
            "publicacion": 15,
            "comentario_padre": None,
        },
        {
            "autor": 1,
            "contenido": "Method her first always. Human drop letter focus culture environment. Rest example behind particularly avoid myself may.",
            "publicacion": 10,
            "comentario_padre": None,
        },
        {
            "autor": 1,
            "contenido": "Work company account east break all smile forward. Thank through reason color nearly rock term field.",
            "publicacion": 3,
            "comentario_padre": None,
        },
        {
            "autor": 25,
            "contenido": "Later to site attention improve able arm.",
            "publicacion": 2,
            "comentario_padre": None,
        },
        {
            "autor": 25,
            "contenido": "Research note imagine already suffer role. Under thought represent risk against message management.",
            "publicacion": 9,
            "comentario_padre": None,
        },
        {
            "autor": 8,
            "contenido": "Kid fact on our. Art chair local office tough week week.",
            "publicacion": 11,
            "comentario_padre": None,
        },
        {
            "autor": 14,
            "contenido": "Direction industry meeting phone focus poor serious. Direction hit important next. Drop president like address around nearly.",
            "publicacion": 11,
            "comentario_padre": None,
        },
        {
            "autor": 12,
            "contenido": "Officer throw free west record. Carry public support fall system knowledge. Front prepare set agree week leader man.",
            "publicacion": 15,
            "comentario_padre": None,
        },
        {
            "autor": 28,
            "contenido": "Break unit another natural positive medical can expert. Not discussion poor benefit go end.",
            "publicacion": 3,
            "comentario_padre": None,
        },
        {
            "autor": 14,
            "contenido": "True pass particularly seek according technology customer agreement. Decision hour resource like can road. House institution or green order.",
            "publicacion": 15,
            "comentario_padre": None,
        },
        {
            "autor": 12,
            "contenido": "Generation what civil PM. Offer method language someone week. Your book man run cell degree throw.",
            "publicacion": 14,
            "comentario_padre": None,
        },
        {
            "autor": 8,
            "contenido": "General quickly trial side close put. Song guess other effort leave.",
            "publicacion": 4,
            "comentario_padre": None,
        },
        {
            "autor": 14,
            "contenido": "Social event money economy drive subject study sign. Home building expert two people drug sure. Value support foreign.",
            "publicacion": 1,
            "comentario_padre": None,
        },
        {
            "autor": 9,
            "contenido": "Case consider win allow program three main. Owner child outside argue stock. However speech tend only though.",
            "publicacion": 15,
            "comentario_padre": None,
        },
        {
            "autor": 6,
            "contenido": "Blood truth table source beyond manager truth. Kid quickly both increase fact word mean. Far worry through find girl situation current. Method popular career candidate change Republican peace.",
            "publicacion": 13,
            "comentario_padre": None,
        },
        {
            "autor": 26,
            "contenido": "Help here fund book. Star too standard.",
            "publicacion": 14,
            "comentario_padre": None,
        },
        {
            "autor": 25,
            "contenido": "Size agent director consumer or state computer order. Recent memory movement. Position never one safe fly. Single among which hope more our.",
            "publicacion": 9,
            "comentario_padre": None,
        },
        {
            "autor": 20,
            "contenido": "Boy institution total design card program. Wonder have field support firm. Relate difference provide heart send next this.",
            "publicacion": 12,
            "comentario_padre": None,
        },
        {
            "autor": 4,
            "contenido": "Record security wind manager first response. Mention offer model mention I his.",
            "publicacion": 6,
            "comentario_padre": None,
        },
        {
            "autor": 23,
            "contenido": "Poor carry five evening music share. Air ask protect describe someone executive.",
            "publicacion": 2,
            "comentario_padre": None,
        },
        {
            "autor": 14,
            "contenido": "I during wrong serious trip draw anyone upon. Heavy pattern candidate get sign would.",
            "publicacion": 11,
            "comentario_padre": None,
        },
        {
            "autor": 11,
            "contenido": "Community ahead though class well recently. Year training best team.",
            "publicacion": 8,
            "comentario_padre": None,
        },
        {
            "autor": 4,
            "contenido": "Group husband once realize like. Able almost increase. True yeah box.",
            "publicacion": 7,
            "comentario_padre": None,
        },
        {
            "autor": 26,
            "contenido": "Figure age realize American myself between fund ability. Executive center bad institution issue.",
            "publicacion": 14,
            "comentario_padre": None,
        },
        {
            "autor": 18,
            "contenido": "Side similar actually share.",
            "publicacion": 12,
            "comentario_padre": None,
        },
        {
            "autor": 13,
            "contenido": "Benefit administration bill sort. Fire while authority perform such event send nothing. So institution early.",
            "publicacion": 6,
            "comentario_padre": None,
        },
        {
            "autor": 7,
            "contenido": "Something money again hundred popular seek state you. Marriage way would imagine man determine lot career. Sit at weight special office main.",
            "publicacion": 9,
            "comentario_padre": None,
        },
        {
            "autor": 26,
            "contenido": "Bank interest along report. Republican goal yeah avoid explain. Write somebody physical education sign.",
            "publicacion": 10,
            "comentario_padre": None,
        },
        {
            "autor": 11,
            "contenido": "Realize partner culture woman south. Employee wife organization which art whether source. Operation they which but deep particular seven.",
            "publicacion": 5,
            "comentario_padre": None,
        },
        {
            "autor": 14,
            "contenido": "They someone cut term Democrat. Law compare blue city continue.",
            "publicacion": 6,
            "comentario_padre": None,
        },
        {
            "autor": 27,
            "contenido": "Challenge type more difference. Again again goal.",
            "publicacion": 10,
            "comentario_padre": None,
        },
        {
            "autor": 18,
            "contenido": "Film structure father leg each main claim environment. Wish so determine single word real. Environmental space individual. Safe foot once eight under issue again student.",
            "publicacion": 3,
            "comentario_padre": None,
        },
        {
            "autor": 22,
            "contenido": "Value husband truth reach win not. Send impact notice administration culture. Store laugh single color stage.",
            "publicacion": 4,
            "comentario_padre": None,
        },
        {
            "autor": 26,
            "contenido": "Southern cause through great. Music wonder dinner today claim expert improve. Step between enter through list according different.",
            "publicacion": 11,
            "comentario_padre": None,
        },
        {
            "autor": 5,
            "contenido": "Collection pattern general production listen. Wall anyone mind brother receive.",
            "publicacion": 13,
            "comentario_padre": None,
        },
        {
            "autor": 2,
            "contenido": "Where central fine think. Magazine might agent star entire all ago. Network hold theory myself walk trouble.",
            "publicacion": 9,
            "comentario_padre": None,
        },
        {
            "autor": 3,
            "contenido": "Yet office position structure. Cold play table network large claim range.",
            "publicacion": 15,
            "comentario_padre": None,
        },
        {
            "autor": 26,
            "contenido": "Seek mouth also teach tell any type.",
            "publicacion": 3,
            "comentario_padre": None,
        },
        {
            "autor": 24,
            "contenido": "Black another of. Nor write stand affect five. There direction find maybe western.",
            "publicacion": 2,
            "comentario_padre": None,
        },
        {
            "autor": 22,
            "contenido": "Increase among piece word. Moment media consider simple. Support especially public relationship skill science consider. Mind affect result still walk improve war.",
            "publicacion": 7,
            "comentario_padre": None,
        },
        {
            "autor": 15,
            "contenido": "Network sea give low attention particularly perform analysis. Feel this him.",
            "publicacion": 2,
            "comentario_padre": None,
        },
        {
            "autor": 2,
            "contenido": "Glass among catch customer result story. Level federal paper again black. Stop describe win improve enjoy forward family nor. Boy last whom trade stuff.",
            "publicacion": 12,
            "comentario_padre": None,
        },
        {
            "autor": 7,
            "contenido": "Indicate phone indicate community why paper serve. Republican walk approach now while. Yeah also matter soldier usually hard our.",
            "publicacion": 9,
            "comentario_padre": None,
        },
        {
            "autor": 16,
            "contenido": "Artist much television think tree treat care. Explain generation your quickly. Write husband article group better factor difference.",
            "publicacion": 11,
            "comentario_padre": None,
        },
        {
            "autor": 24,
            "contenido": "Become sea leg. Sell challenge last employee anything.",
            "publicacion": 4,
            "comentario_padre": None,
        },
        {
            "autor": 17,
            "contenido": "Clearly do drug ahead ready radio free. Example economic so effect.",
            "publicacion": 6,
            "comentario_padre": None,
        },
        {
            "autor": 24,
            "contenido": "Whatever whether under fund realize science. Six newspaper production size window television partner book.",
            "publicacion": 9,
            "comentario_padre": None,
        },
        {
            "autor": 11,
            "contenido": "Opportunity star high bring similar new our art. Future control operation finish. Day involve bring condition.",
            "publicacion": 7,
            "comentario_padre": None,
        },
        {
            "autor": 5,
            "contenido": "Right sometimes time. Size what activity four low nothing spring much.",
            "publicacion": 10,
            "comentario_padre": None,
        },
        {
            "autor": 7,
            "contenido": "Those discuss film street tax art. Sport TV yes attack.",
            "publicacion": 5,
            "comentario_padre": None,
        },
        {
            "autor": 22,
            "contenido": "Best wide piece hot. College throughout evening so raise yeah. With economy show sit party identify.",
            "publicacion": 4,
            "comentario_padre": None,
        },
        {
            "autor": 3,
            "contenido": "Hot once rise relationship speak. Practice more relationship level analysis particularly arm thing. Modern commercial poor bank remember for. Tonight picture fish reality.",
            "publicacion": 10,
            "comentario_padre": None,
        },
        {
            "autor": 12,
            "contenido": "History entire fall box idea let reach. Animal night attorney difference. Case place strategy serious tonight a.",
            "publicacion": 11,
            "comentario_padre": None,
        },
    ]
    print("\nagregando cometarios")
    for comentario_data in comentarios:
        comentario_data["autor"] = User.objects.get(id=comentario_data["autor"])
        comentario_data["publicacion"] = Publicacion.objects.get(
            id=comentario_data["publicacion"]
        )
        # Crear la instancia de Comentario sin asignar publicaciones
        comentario = Comentario.objects.create(**comentario_data)
        print('creado:',comentario)

        # Obtener las IDs de las publicaciones y asignarlas

    print("\nComentarios ficticios agregados correctamente.")


def agregar_respuestas():
    from posts.models import Comentario, Publicacion
    from accounts.models import Persona, Organizacion
    from django.contrib.auth import get_user_model

    User = get_user_model()
    # id organizaciones: [24 - 29] | is personas: [1 - 23]

    # autor_persona = models.ForeignKey(
    #         'accounts.Persona', on_delete=models.CASCADE, related_name='comentarios', blank=True, null=True)
    #     autor_organizacion = models.ForeignKey(
    #         'accounts.Organizacion', on_delete=models.CASCADE, related_name='comentarios', blank=True, null=True)
    #     contenido = models.CharField(max_length=300)
    #     publicacion = models.ForeignKey(
    #         Publicacion, on_delete=models.CASCADE, related_name='comentarios', blank=True, null=True)
    #     comentario_padre = models.ForeignKey(
    #         'self', on_delete=models.CASCADE, related_name='respuestas', blank=True, null=True)
    #     fechapublicacion = models.DateTimeField(auto_now_add=True)
    comentarios = [  # id organizaciones: [24 - 29] | id personas: [1 - 23] | id publicaciones [1 - 40]
        {
            "autor": 7,
            "contenido": "Type station cell well. Along reality finish market big.",
            "publicacion": 6,
            "comentario_padre": 66,
        },
        {
            "autor": 29,
            "contenido": "Beat moment since material lead buy prevent. Scientist prevent simple pull drug over.",
            "publicacion": 14,
            "comentario_padre": 66,
        },
        {
            "autor": 18,
            "contenido": "He writer expect. Teach establish represent discover network without. Fine mind whose finally. Care brother produce cold together.",
            "publicacion": 15,
            "comentario_padre": 33,
        },
        {
            "autor": 10,
            "contenido": "Ten actually yet believe. Trade item my stage choose energy happen effect.",
            "publicacion": 9,
            "comentario_padre": 75,
        },
        {
            "autor": 20,
            "contenido": "Condition source reach price within pass. Radio sit day just rich they.",
            "publicacion": 8,
            "comentario_padre": 30,
        },
        {
            "autor": 5,
            "contenido": "Buy idea heavy view push. Executive once senior prove away.",
            "publicacion": 11,
            "comentario_padre": 83,
        },
        {
            "autor": 19,
            "contenido": "Main film outside degree. Behavior attack as total expert want. Stay political consumer audience high produce campaign.",
            "publicacion": 15,
            "comentario_padre": 36,
        },
        {
            "autor": 17,
            "contenido": "Physical choose sing group. Again place mother interesting actually imagine shake. Him condition section full still ball.",
            "publicacion": 8,
            "comentario_padre": 66,
        },
        {
            "autor": 28,
            "contenido": "Color live billion raise may what expect. Perform sometimes authority many subject it record. Sister laugh figure mother share four.",
            "publicacion": 13,
            "comentario_padre": 86,
        },
        {
            "autor": 22,
            "contenido": "Light instead become civil information deal theory. Shake across opportunity. Once hour apply understand.",
            "publicacion": 14,
            "comentario_padre": 85,
        },
        {
            "autor": 22,
            "contenido": "Room level shoulder very. Message agree though people. Billion image individual spring protect address baby.",
            "publicacion": 13,
            "comentario_padre": 95,
        },
        {
            "autor": 4,
            "contenido": "Special state data list.",
            "publicacion": 1,
            "comentario_padre": 81,
        },
        {
            "autor": 9,
            "contenido": "Environment receive quickly animal training education. Like shoulder degree nearly fear new.",
            "publicacion": 9,
            "comentario_padre": 20,
        },
        {
            "autor": 14,
            "contenido": "Particularly create guy attorney certainly argue condition now. Everything official may mother enjoy. Bit fish garden teacher road.",
            "publicacion": 15,
            "comentario_padre": 34,
        },
        {
            "autor": 14,
            "contenido": "Stage tree return education dinner course blood. Pick window character town before.",
            "publicacion": 3,
            "comentario_padre": 95,
        },
        {
            "autor": 10,
            "contenido": "Executive card information onto drop bring.",
            "publicacion": 4,
            "comentario_padre": 16,
        },
        {
            "autor": 18,
            "contenido": "Attack listen can part property population. Blood resource school rise. Couple sister impact hospital.",
            "publicacion": 15,
            "comentario_padre": 67,
        },
        {
            "autor": 4,
            "contenido": "Happen instead result college ok. Tough between conference direction prepare understand better campaign. Professor treatment talk personal think.",
            "publicacion": 6,
            "comentario_padre": 24,
        },
        {
            "autor": 19,
            "contenido": "Both never entire pick. Interesting majority usually high too. Weight reduce series task theory.",
            "publicacion": 3,
            "comentario_padre": 2,
        },
        {
            "autor": 18,
            "contenido": "Final majority say rest.",
            "publicacion": 6,
            "comentario_padre": 3,
        },
        {
            "autor": 2,
            "contenido": "Subject move because mouth however attack. Which debate much call they responsibility. After coach first church.",
            "publicacion": 4,
            "comentario_padre": 44,
        },
        {
            "autor": 1,
            "contenido": "Quite close offer. News business her field. How executive modern her up.",
            "publicacion": 2,
            "comentario_padre": 74,
        },
        {
            "autor": 15,
            "contenido": "Figure suffer wish. Player why reflect environmental after back know.",
            "publicacion": 4,
            "comentario_padre": 64,
        },
        {
            "autor": 5,
            "contenido": "Wall central color light already. Imagine evidence issue all level.",
            "publicacion": 8,
            "comentario_padre": 67,
        },
        {
            "autor": 12,
            "contenido": "Role month card month speak. Middle draw whatever customer very second cold. Care meeting notice ready ground behavior thousand.",
            "publicacion": 15,
            "comentario_padre": 25,
        },
        {
            "autor": 26,
            "contenido": "Election history scene huge.",
            "publicacion": 2,
            "comentario_padre": 84,
        },
        {
            "autor": 12,
            "contenido": "Represent explain foot maintain instead worker. Begin parent whether market manager act.",
            "publicacion": 15,
            "comentario_padre": 66,
        },
        {
            "autor": 12,
            "contenido": "Language fire sometimes huge dark democratic tax. Go building job month.",
            "publicacion": 2,
            "comentario_padre": 49,
        },
        {
            "autor": 24,
            "contenido": "Name capital those child end. Fall civil authority president. Stuff far admit Mr.",
            "publicacion": 10,
            "comentario_padre": 99,
        },
        {
            "autor": 28,
            "contenido": "Attorney modern yeah concern. Science body without area door. Want create power wish.",
            "publicacion": 15,
            "comentario_padre": 41,
        },
        {
            "autor": 4,
            "contenido": "Management usually small despite. List seem standard. Religious line deal financial prevent also.",
            "publicacion": 13,
            "comentario_padre": 78,
        },
        {
            "autor": 23,
            "contenido": "Animal state group. Practice yes easy perform avoid so. Clearly maybe oil fear require pull. Together important paper break give street left.",
            "publicacion": 13,
            "comentario_padre": 43,
        },
        {
            "autor": 25,
            "contenido": "Music fear section. Everything skin successful.",
            "publicacion": 15,
            "comentario_padre": 77,
        },
        {
            "autor": 26,
            "contenido": "Describe feeling state clearly. Per real certainly despite woman.",
            "publicacion": 6,
            "comentario_padre": 16,
        },
        {
            "autor": 2,
            "contenido": "Image center old. Card learn night still subject feeling. Feeling toward approach Republican pick study thing.",
            "publicacion": 14,
            "comentario_padre": 5,
        },
        {
            "autor": 29,
            "contenido": "Cultural travel single during trouble any role. Itself country staff policy bring join. To prevent deal school media view cold exist. Only along reality successful world manager.",
            "publicacion": 14,
            "comentario_padre": 60,
        },
        {
            "autor": 22,
            "contenido": "Or lot wrong animal reason which war open.",
            "publicacion": 12,
            "comentario_padre": 27,
        },
        {
            "autor": 20,
            "contenido": "Form discussion economy use. Only leader have early fear two movie enjoy. Boy kid middle then language.",
            "publicacion": 15,
            "comentario_padre": 20,
        },
        {
            "autor": 8,
            "contenido": "Free race guy. Role red someone sign. Hold mother assume this able vote.",
            "publicacion": 13,
            "comentario_padre": 86,
        },
        {
            "autor": 2,
            "contenido": "Away car part some cultural throw care. Particularly quite home box.",
            "publicacion": 10,
            "comentario_padre": 100,
        },
        {
            "autor": 25,
            "contenido": "Whole mouth deep you stop. Change old theory start interesting painting. Blood whom politics authority apply establish everyone age.",
            "publicacion": 3,
            "comentario_padre": 21,
        },
        {
            "autor": 13,
            "contenido": "Republican rock administration theory wonder boy. Likely home establish relate involve task room party.",
            "publicacion": 1,
            "comentario_padre": 3,
        },
        {
            "autor": 17,
            "contenido": "Economic special success debate economic. Phone PM mouth story. Song general industry shoulder season article system.",
            "publicacion": 8,
            "comentario_padre": 50,
        },
        {
            "autor": 5,
            "contenido": "Democratic might wrong arrive light. Film play often pretty. Return center produce score body entire. Particular blood scientist consider news.",
            "publicacion": 8,
            "comentario_padre": 36,
        },
        {
            "autor": 22,
            "contenido": "Science word everybody expect wide. Investment pattern deal. Wait live sea movement add size assume.",
            "publicacion": 9,
            "comentario_padre": 80,
        },
        {
            "autor": 4,
            "contenido": "Painting factor certain wall any. Officer history according.",
            "publicacion": 8,
            "comentario_padre": 62,
        },
        {
            "autor": 24,
            "contenido": "Lawyer benefit little this skin debate lot. Expert police give man.",
            "publicacion": 8,
            "comentario_padre": 97,
        },
        {
            "autor": 13,
            "contenido": "Campaign necessary staff social raise sea sign. Number newspaper agreement discover.",
            "publicacion": 1,
            "comentario_padre": 57,
        },
        {
            "autor": 14,
            "contenido": "Investment place plant sound often. Both dream today west. Once event across forward.",
            "publicacion": 4,
            "comentario_padre": 68,
        },
        {
            "autor": 25,
            "contenido": "According understand teacher field. Participant tough hair teacher record despite fly. History watch land walk.",
            "publicacion": 7,
            "comentario_padre": 50,
        },
        {
            "autor": 11,
            "contenido": "Rise mention never letter bag back. Identify night how common.",
            "publicacion": 1,
            "comentario_padre": 92,
        },
        {
            "autor": 14,
            "contenido": "Difference central admit painting learn almost skill. Myself more so talk.",
            "publicacion": 8,
            "comentario_padre": 99,
        },
        {
            "autor": 28,
            "contenido": "Forward last response window again whom front human. Contain walk meeting billion woman.",
            "publicacion": 9,
            "comentario_padre": 76,
        },
        {
            "autor": 6,
            "contenido": "Fact structure heavy source follow rest. Take admit side result commercial then get.",
            "publicacion": 10,
            "comentario_padre": 30,
        },
        {
            "autor": 19,
            "contenido": "Computer including hit article standard. Turn stuff air indeed keep skin.",
            "publicacion": 7,
            "comentario_padre": 55,
        },
        {
            "autor": 5,
            "contenido": "His when these easy. Of physical brother deal sound build. Whether near specific read.",
            "publicacion": 13,
            "comentario_padre": 84,
        },
        {
            "autor": 1,
            "contenido": "According feeling edge happen throw market say. Plant knowledge customer shake mission.",
            "publicacion": 4,
            "comentario_padre": 34,
        },
        {
            "autor": 8,
            "contenido": "Front company level financial note age realize. Successful his leave if tell imagine type. Painting build federal instead take better program push.",
            "publicacion": 15,
            "comentario_padre": 39,
        },
        {
            "autor": 15,
            "contenido": "Teacher fish benefit best season people Mr conference. Son across here describe such evidence.",
            "publicacion": 7,
            "comentario_padre": 42,
        },
        {
            "autor": 24,
            "contenido": "Rise together kid stand PM. Investment who though appear girl within voice fight.",
            "publicacion": 1,
            "comentario_padre": 30,
        },
        {
            "autor": 8,
            "contenido": "Visit exactly color Mr central computer pressure. Foreign later walk from brother thing. Glass billion speak movement floor her test. Our son magazine environment about suggest.",
            "publicacion": 3,
            "comentario_padre": 62,
        },
        {
            "autor": 8,
            "contenido": "Then significant country least all. Partner he technology cut stand role us. Bag add stage adult few. Production its policy anything.",
            "publicacion": 8,
            "comentario_padre": 56,
        },
        {
            "autor": 19,
            "contenido": "Hot military pattern beat later data. City exist great rise clear figure entire. Lawyer old prevent candidate.",
            "publicacion": 1,
            "comentario_padre": 56,
        },
        {
            "autor": 6,
            "contenido": "First stand law magazine voice. Last hit country.",
            "publicacion": 6,
            "comentario_padre": 87,
        },
        {
            "autor": 14,
            "contenido": "Wife production computer dinner. Five any generation not real young draw. With own reach I appear sense. Before Republican change do usually box.",
            "publicacion": 13,
            "comentario_padre": 25,
        },
        {
            "autor": 11,
            "contenido": "Ok song throw different. Lawyer fire coach card stay. Wish quality history grow wear then.",
            "publicacion": 7,
            "comentario_padre": 2,
        },
        {
            "autor": 12,
            "contenido": "Way rise red reflect. Job none none difficult. Article hear able.",
            "publicacion": 6,
            "comentario_padre": 58,
        },
        {
            "autor": 5,
            "contenido": "Situation international process determine. Table course tonight recognize plant system. Religious cold career cost. Sister institution last yeah.",
            "publicacion": 13,
            "comentario_padre": 10,
        },
        {
            "autor": 9,
            "contenido": "Foot score could laugh reason tax painting. Apply man training choose any participant score. Answer art wide drug career. Since before throw thank style.",
            "publicacion": 9,
            "comentario_padre": 31,
        },
        {
            "autor": 17,
            "contenido": "Most clearly year above benefit. Your war when beyond garden main. Entire civil call democratic economic store.",
            "publicacion": 4,
            "comentario_padre": 25,
        },
        {
            "autor": 16,
            "contenido": "Simply international data set foot political animal. Full child trip program.",
            "publicacion": 8,
            "comentario_padre": 55,
        },
        {
            "autor": 9,
            "contenido": "Knowledge outside of any should rest.",
            "publicacion": 12,
            "comentario_padre": 87,
        },
        {
            "autor": 6,
            "contenido": "Left the stage detail throw war adult view. Focus my join maintain national tree else.",
            "publicacion": 6,
            "comentario_padre": 85,
        },
        {
            "autor": 5,
            "contenido": "Treat scene give defense many. Reality avoid tend thought.",
            "publicacion": 10,
            "comentario_padre": 96,
        },
        {
            "autor": 21,
            "contenido": "Page usually son method wife here.",
            "publicacion": 1,
            "comentario_padre": 65,
        },
        {
            "autor": 5,
            "contenido": "Here treatment future.",
            "publicacion": 6,
            "comentario_padre": 71,
        },
        {
            "autor": 28,
            "contenido": "Begin store back possible church protect. Hard threat like what.",
            "publicacion": 4,
            "comentario_padre": 80,
        },
        {
            "autor": 9,
            "contenido": "Next develop plant product edge finally pressure little. Onto probably Republican eye dinner center stop. Field campaign art bar knowledge environment former church.",
            "publicacion": 7,
            "comentario_padre": 70,
        },
        {
            "autor": 8,
            "contenido": "Trade keep life particularly cell work. Hear act draw tell wear ready. In simply yeah next reason maybe magazine.",
            "publicacion": 2,
            "comentario_padre": 78,
        },
        {
            "autor": 13,
            "contenido": "Pick month in. Space energy contain program green trade trial.",
            "publicacion": 1,
            "comentario_padre": 72,
        },
        {
            "autor": 12,
            "contenido": "Decision state fine. Government common nice yes ok property.",
            "publicacion": 11,
            "comentario_padre": 26,
        },
        {
            "autor": 23,
            "contenido": "Lot not medical tell church behavior. Policy seek design.",
            "publicacion": 11,
            "comentario_padre": 70,
        },
        {
            "autor": 11,
            "contenido": "Voice deep newspaper a catch able sign. Behind clearly pull party less. Wife career civil policy machine.",
            "publicacion": 9,
            "comentario_padre": 21,
        },
        {
            "autor": 22,
            "contenido": "We site difficult others start point. Film clear southern let mother trade something.",
            "publicacion": 3,
            "comentario_padre": 68,
        },
        {
            "autor": 5,
            "contenido": "Brother mouth rise throughout. Small investment range hospital. Three possible election country inside thank.",
            "publicacion": 11,
            "comentario_padre": 98,
        },
        {
            "autor": 23,
            "contenido": "Degree animal instead next sometimes. Budget art true media add.",
            "publicacion": 3,
            "comentario_padre": 83,
        },
        {
            "autor": 14,
            "contenido": "Summer list speak whole small then. Admit if ten Mr peace government cut someone.",
            "publicacion": 4,
            "comentario_padre": 81,
        },
        {
            "autor": 14,
            "contenido": "Fight mouth series its. From west since feeling throw.",
            "publicacion": 2,
            "comentario_padre": 47,
        },
        {
            "autor": 14,
            "contenido": "Spring system program life prevent away eye. Car tend minute perform receive up wonder.",
            "publicacion": 9,
            "comentario_padre": 14,
        },
        {
            "autor": 18,
            "contenido": "Nice born easy head response. Scientist campaign of though response wall according security. Will design seek international skill economic inside.",
            "publicacion": 12,
            "comentario_padre": 92,
        },
        {
            "autor": 5,
            "contenido": "Pass degree avoid power operation tax nice. Expert hot create.",
            "publicacion": 12,
            "comentario_padre": 85,
        },
        {
            "autor": 24,
            "contenido": "Who thought message music second front friend. Indeed skin minute tree attention page spring. Year score even. Mission clear them style life.",
            "publicacion": 10,
            "comentario_padre": 77,
        },
        {
            "autor": 10,
            "contenido": "Trial speak pull at. Believe decision at foreign. Garden white read total however year factor.",
            "publicacion": 7,
            "comentario_padre": 53,
        },
        {
            "autor": 18,
            "contenido": "Nearly many carry. Win myself final director control particular.",
            "publicacion": 11,
            "comentario_padre": 48,
        },
        {
            "autor": 12,
            "contenido": "Prepare PM ask majority throw. During he some cell spend series machine including. Again another everybody.",
            "publicacion": 7,
            "comentario_padre": 84,
        },
        {
            "autor": 19,
            "contenido": "They into yes dinner reveal. Range wear data if civil remember. Leave data piece state people really central.",
            "publicacion": 4,
            "comentario_padre": 28,
        },
        {
            "autor": 22,
            "contenido": "Door subject relate. Simple upon easy the this.",
            "publicacion": 7,
            "comentario_padre": 2,
        },
        {
            "autor": 26,
            "contenido": "Professor age body pull reality message.",
            "publicacion": 12,
            "comentario_padre": 87,
        },
        {
            "autor": 20,
            "contenido": "Dark partner Mrs hotel rich easy expect. Institution responsibility owner your it ahead. Serious follow recently direction.",
            "publicacion": 12,
            "comentario_padre": 17,
        },
        {
            "autor": 20,
            "contenido": "Cup doctor college shake five Congress paper. Education play keep loss likely company into artist.",
            "publicacion": 11,
            "comentario_padre": 13,
        },

    ]

    print("\nagregando respuestas")
    for respuesta in comentarios:
        respuesta["autor"] = User.objects.get(id=respuesta["autor"])
        respuesta["publicacion"] = Publicacion.objects.get(
            id=respuesta["publicacion"]
        )
        respuesta["comentario_padre"] = Comentario.objects.get(
            id=respuesta["comentario_padre"]
        )
        # Crear la instancia de Comentario sin asignar publicaciones
        comentario = Comentario.objects.create(**respuesta)
        print('creado:',comentario)
        # Obtener las IDs de las publicaciones y asignarlas
        
    print("\Respuestas ficticias agregados correctamente.")
