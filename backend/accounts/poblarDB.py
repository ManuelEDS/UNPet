def poblar_db(sender, **kwargs):
    agregar_grupos()
    agregar_localidades()
    agregar_personas()
    agregar_organizaciones()
    agregar_publicaciones()
    agregar_mascotas()
    # agregar_comentarios()


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
            "titulo": "Mr",
            "descripcion": "Integer ac leo. Pellentesque ultrices mattis odio. Donec vitae nisi.",
            "n_mascotas": 8,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 25,
            "estado": "Adoptados",
            "titulo": "Ms",
            "descripcion": "Quisque id justo sit amet sapien dignissim vestibulum sollicitudin ut, suscipit a, feugiat et, eros.",
            "n_mascotas": 2,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 27,
            "estado": "Disponibles",
            "titulo": "Dr",
            "descripcion": "Morbi porttitor lorem id ligula. Suspendisse ornare consequat lectus. In est risus, auctor sed, tristique in, tempus sit amet, sem.",
            "n_mascotas": 7,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 28,
            "estado": "Disponibles",
            "titulo": "Dr",
            "descripcion": "Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.",
            "n_mascotas": 6,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 24,
            "estado": "Adoptados",
            "titulo": "Dr",
            "descripcion": "Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.",
            "n_mascotas": 9,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 28,
            "estado": "Adoptados",
            "titulo": "Ms",
            "descripcion": "Pellentesque at nulla. Suspendisse potenti. Cras in purus eu magna vulputate luctus.",
            "n_mascotas": 0,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 27,
            "estado": "Disponibles",
            "titulo": "Honorable",
            "descripcion": "Phasellus sit amet erat. Nulla tempus. Vivamus in felis eu sapien cursus vestibulum.",
            "n_mascotas": 2,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 26,
            "estado": "Adoptados",
            "titulo": "Ms",
            "descripcion": "Fusce consequat. Nulla nisl. Nunc nisl.",
            "n_mascotas": 1,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 26,
            "estado": "Disponibles",
            "titulo": "Dr",
            "descripcion": "Nullam porttitor lacus at turpis. Donec posuere metus vitae ipsum. Aliquam non mauris.",
            "n_mascotas": 9,
            "n_mascotas_adoptadas": 0,
        },
        {
            "idorganizacion": 26,
            "estado": "Adoptados",
            "titulo": "Dr",
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
        }
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
    comentarios = [  # id organizaciones: [24 - 29] | id personas: [1 - 23] | id publicaciones [1 - 40]
        {
            "autor_persona": Persona.objects.get(id=1),
            "contenido": "Esta publicacion me gustó",
            "publicacion": Publicacion.objects.get(id=40),
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
                Publicacion.objects.filter(id__in=publicaciones_ids)
            )

    print("\nComentarios ficticios agregados correctamente.")
