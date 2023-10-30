
def poblar_db(sender, **kwargs):
    agregar_grupos()
    agregar_localidades()
    agregar_personas()
    agregar_organizaciones()
    agregar_publicaciones()
    agregar_comentarios()

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
  "urlfoto": "http://pbs.org/viverra/eget.xml?quisque=ac&ut=enim&erat=in&curabitur=tempor&gravida=turpis&nisi=nec&at=euismod&nibh=scelerisque&in=quam&hac=turpis&habitasse=adipiscing&platea=lorem&dictumst=vitae&aliquam=mattis&augue=nibh&quam=ligula&sollicitudin=nec&vitae=sem&consectetuer=duis&eget=aliquam&rutrum=convallis&at=nunc&lorem=proin&integer=at&tincidunt=turpis&ante=a&vel=pede&ipsum=posuere&praesent=nonummy&blandit=integer&lacinia=non&erat=velit&vestibulum=donec&sed=diam&magna=neque&at=vestibulum&nunc=eget&commodo=vulputate&placerat=ut&praesent=ultrices&blandit=vel&nam=augue&nulla=vestibulum&integer=ante&pede=ipsum&justo=primis&lacinia=in&eget=faucibus&tincidunt=orci&eget=luctus&tempus=et&vel=ultrices&pede=posuere&morbi=cubilia&porttitor=curae&lorem=donec&id=pharetra&ligula=magna&suspendisse=vestibulum&ornare=aliquet&consequat=ultrices&lectus=erat&in=tortor&est=sollicitudin&risus=mi&auctor=sit&sed=amet&tristique=lobortis&in=sapien&tempus=sapien&sit=non&amet=mi&sem=integer&fusce=ac&consequat=neque&nulla=duis&nisl=bibendum&nunc=morbi&nisl=non&duis=quam&bibendum=nec&felis=dui&sed=luctus&interdum=rutrum&venenatis=nulla&turpis=tellus&enim=in&blandit=sagittis&mi=dui&in=vel&porttitor=nisl&pede=duis&justo=ac&eu=nibh&massa=fusce&donec=lacus",
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
  "urlfoto": "https://squidoo.com/maecenas/rhoncus/aliquam/lacus.jpg?lobortis=molestie&sapien=lorem&sapien=quisque&non=ut&mi=erat&integer=curabitur&ac=gravida&neque=nisi&duis=at&bibendum=nibh&morbi=in&non=hac&quam=habitasse&nec=platea&dui=dictumst&luctus=aliquam&rutrum=augue&nulla=quam&tellus=sollicitudin&in=vitae&sagittis=consectetuer&dui=eget&vel=rutrum&nisl=at&duis=lorem&ac=integer&nibh=tincidunt&fusce=ante&lacus=vel&purus=ipsum&aliquet=praesent&at=blandit&feugiat=lacinia&non=erat&pretium=vestibulum&quis=sed&lectus=magna&suspendisse=at&potenti=nunc&in=commodo&eleifend=placerat&quam=praesent&a=blandit&odio=nam&in=nulla&hac=integer&habitasse=pede&platea=justo",
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
  "urlfoto": "https://dell.com/felis/donec/semper/sapien/a.jsp?faucibus=luctus&orci=rutrum&luctus=nulla&et=tellus&ultrices=in&posuere=sagittis&cubilia=dui&curae=vel&donec=nisl&pharetra=duis",
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
  "urlfoto": "https://mlb.com/leo/maecenas/pulvinar.js?ut=faucibus&tellus=cursus&nulla=urna&ut=ut&erat=tellus&id=nulla&mauris=ut&vulputate=erat&elementum=id&nullam=mauris&varius=vulputate&nulla=elementum&facilisi=nullam&cras=varius&non=nulla&velit=facilisi&nec=cras&nisi=non&vulputate=velit&nonummy=nec&maecenas=nisi&tincidunt=vulputate&lacus=nonummy&at=maecenas&velit=tincidunt&vivamus=lacus&vel=at&nulla=velit",
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
  "urlfoto": "https://nasa.gov/viverra/diam/vitae/quam/suspendisse/potenti/nullam.js?mus=sem&etiam=duis&vel=aliquam&augue=convallis&vestibulum=nunc&rutrum=proin&rutrum=at&neque=turpis&aenean=a&auctor=pede&gravida=posuere&sem=nonummy&praesent=integer&id=non&massa=velit&id=donec&nisl=diam&venenatis=neque&lacinia=vestibulum&aenean=eget&sit=vulputate&amet=ut&justo=ultrices&morbi=vel&ut=augue&odio=vestibulum&cras=ante&mi=ipsum&pede=primis&malesuada=in&in=faucibus&imperdiet=orci&et=luctus&commodo=et&vulputate=ultrices&justo=posuere&in=cubilia&blandit=curae&ultrices=donec&enim=pharetra&lorem=magna&ipsum=vestibulum&dolor=aliquet&sit=ultrices&amet=erat&consectetuer=tortor&adipiscing=sollicitudin&elit=mi&proin=sit&interdum=amet&mauris=lobortis&non=sapien&ligula=sapien&pellentesque=non&ultrices=mi&phasellus=integer&id=ac&sapien=neque&in=duis&sapien=bibendum&iaculis=morbi&congue=non&vivamus=quam&metus=nec&arcu=dui&adipiscing=luctus&molestie=rutrum&hendrerit=nulla&at=tellus&vulputate=in&vitae=sagittis&nisl=dui&aenean=vel&lectus=nisl&pellentesque=duis&eget=ac&nunc=nibh&donec=fusce&quis=lacus&orci=purus&eget=aliquet&orci=at&vehicula=feugiat&condimentum=non&curabitur=pretium&in=quis&libero=lectus&ut=suspendisse&massa=potenti&volutpat=in&convallis=eleifend&morbi=quam&odio=a&odio=odio",
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
  "urlfoto": "http://nifty.com/adipiscing/elit/proin/risus/praesent/lectus/vestibulum.jsp?interdum=a&mauris=ipsum&ullamcorper=integer&purus=a&sit=nibh&amet=in&nulla=quis&quisque=justo&arcu=maecenas&libero=rhoncus&rutrum=aliquam&ac=lacus&lobortis=morbi&vel=quis&dapibus=tortor&at=id&diam=nulla&nam=ultrices&tristique=aliquet&tortor=maecenas",
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
  "urlfoto": "https://themeforest.net/turpis/enim/blandit/mi.xml?habitasse=in&platea=hac&dictumst=habitasse&aliquam=platea&augue=dictumst&quam=aliquam&sollicitudin=augue&vitae=quam&consectetuer=sollicitudin&eget=vitae&rutrum=consectetuer&at=eget&lorem=rutrum&integer=at&tincidunt=lorem&ante=integer&vel=tincidunt&ipsum=ante&praesent=vel&blandit=ipsum&lacinia=praesent&erat=blandit&vestibulum=lacinia&sed=erat&magna=vestibulum&at=sed&nunc=magna&commodo=at&placerat=nunc&praesent=commodo&blandit=placerat&nam=praesent&nulla=blandit&integer=nam&pede=nulla&justo=integer&lacinia=pede&eget=justo&tincidunt=lacinia&eget=eget&tempus=tincidunt&vel=eget&pede=tempus&morbi=vel&porttitor=pede&lorem=morbi&id=porttitor&ligula=lorem&suspendisse=id&ornare=ligula&consequat=suspendisse&lectus=ornare&in=consequat&est=lectus&risus=in&auctor=est&sed=risus&tristique=auctor&in=sed&tempus=tristique&sit=in&amet=tempus&sem=sit&fusce=amet&consequat=sem&nulla=fusce&nisl=consequat&nunc=nulla&nisl=nisl&duis=nunc&bibendum=nisl&felis=duis&sed=bibendum&interdum=felis&venenatis=sed&turpis=interdum&enim=venenatis&blandit=turpis",
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
  "urlfoto": "https://chicagotribune.com/sapien/non/mi/integer/ac/neque.js?ridiculus=praesent&mus=lectus&etiam=vestibulum&vel=quam&augue=sapien&vestibulum=varius&rutrum=ut&rutrum=blandit&neque=non&aenean=interdum&auctor=in&gravida=ante&sem=vestibulum&praesent=ante&id=ipsum&massa=primis&id=in&nisl=faucibus&venenatis=orci&lacinia=luctus&aenean=et&sit=ultrices&amet=posuere&justo=cubilia&morbi=curae&ut=duis&odio=faucibus&cras=accumsan&mi=odio&pede=curabitur&malesuada=convallis&in=duis&imperdiet=consequat&et=dui&commodo=nec&vulputate=nisi&justo=volutpat&in=eleifend&blandit=donec&ultrices=ut&enim=dolor&lorem=morbi&ipsum=vel&dolor=lectus&sit=in&amet=quam&consectetuer=fringilla&adipiscing=rhoncus&elit=mauris&proin=enim&interdum=leo&mauris=rhoncus&non=sed&ligula=vestibulum&pellentesque=sit&ultrices=amet&phasellus=cursus&id=id&sapien=turpis&in=integer&sapien=aliquet&iaculis=massa&congue=id&vivamus=lobortis&metus=convallis&arcu=tortor",
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
  "urlfoto": "https://examiner.com/morbi.xml?velit=lacus&id=purus&pretium=aliquet&iaculis=at&diam=feugiat&erat=non&fermentum=pretium&justo=quis&nec=lectus&condimentum=suspendisse&neque=potenti&sapien=in&placerat=eleifend&ante=quam",
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
  "urlfoto": "https://fotki.com/orci/vehicula/condimentum/curabitur/in.jpg?vel=ipsum&sem=dolor&sed=sit&sagittis=amet&nam=consectetuer&congue=adipiscing&risus=elit&semper=proin&porta=risus&volutpat=praesent&quam=lectus&pede=vestibulum&lobortis=quam&ligula=sapien&sit=varius&amet=ut&eleifend=blandit&pede=non&libero=interdum&quis=in&orci=ante&nullam=vestibulum&molestie=ante&nibh=ipsum&in=primis&lectus=in&pellentesque=faucibus&at=orci&nulla=luctus&suspendisse=et&potenti=ultrices&cras=posuere&in=cubilia&purus=curae&eu=duis&magna=faucibus&vulputate=accumsan&luctus=odio&cum=curabitur&sociis=convallis&natoque=duis&penatibus=consequat&et=dui&magnis=nec&dis=nisi&parturient=volutpat&montes=eleifend&nascetur=donec&ridiculus=ut",
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
  "urlfoto": "https://cbslocal.com/velit/id/pretium/iaculis/diam/erat/fermentum.jsp?ante=augue&vivamus=vestibulum&tortor=ante&duis=ipsum&mattis=primis&egestas=in&metus=faucibus&aenean=orci&fermentum=luctus&donec=et&ut=ultrices&mauris=posuere&eget=cubilia&massa=curae&tempor=donec&convallis=pharetra&nulla=magna&neque=vestibulum&libero=aliquet&convallis=ultrices&eget=erat&eleifend=tortor&luctus=sollicitudin&ultricies=mi&eu=sit&nibh=amet&quisque=lobortis&id=sapien&justo=sapien&sit=non&amet=mi&sapien=integer&dignissim=ac&vestibulum=neque&vestibulum=duis&ante=bibendum&ipsum=morbi&primis=non&in=quam&faucibus=nec&orci=dui&luctus=luctus&et=rutrum&ultrices=nulla&posuere=tellus&cubilia=in&curae=sagittis&nulla=dui&dapibus=vel&dolor=nisl&vel=duis&est=ac&donec=nibh&odio=fusce&justo=lacus&sollicitudin=purus&ut=aliquet&suscipit=at&a=feugiat&feugiat=non&et=pretium&eros=quis&vestibulum=lectus&ac=suspendisse&est=potenti&lacinia=in&nisi=eleifend&venenatis=quam&tristique=a&fusce=odio&congue=in&diam=hac&id=habitasse&ornare=platea&imperdiet=dictumst&sapien=maecenas&urna=ut",
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
  "urlfoto": "https://soundcloud.com/quam/sapien/varius/ut/blandit/non/interdum.png?nisl=amet&duis=diam&bibendum=in&felis=magna&sed=bibendum&interdum=imperdiet&venenatis=nullam&turpis=orci&enim=pede&blandit=venenatis&mi=non&in=sodales&porttitor=sed&pede=tincidunt&justo=eu&eu=felis&massa=fusce&donec=posuere&dapibus=felis&duis=sed&at=lacus&velit=morbi&eu=sem&est=mauris&congue=laoreet&elementum=ut&in=rhoncus&hac=aliquet&habitasse=pulvinar&platea=sed&dictumst=nisl&morbi=nunc&vestibulum=rhoncus&velit=dui&id=vel&pretium=sem&iaculis=sed&diam=sagittis&erat=nam&fermentum=congue&justo=risus&nec=semper&condimentum=porta&neque=volutpat&sapien=quam&placerat=pede&ante=lobortis&nulla=ligula&justo=sit&aliquam=amet&quis=eleifend&turpis=pede&eget=libero&elit=quis&sodales=orci&scelerisque=nullam&mauris=molestie&sit=nibh&amet=in&eros=lectus&suspendisse=pellentesque&accumsan=at&tortor=nulla&quis=suspendisse&turpis=potenti&sed=cras&ante=in&vivamus=purus&tortor=eu&duis=magna&mattis=vulputate&egestas=luctus&metus=cum&aenean=sociis&fermentum=natoque&donec=penatibus&ut=et&mauris=magnis&eget=dis&massa=parturient&tempor=montes&convallis=nascetur&nulla=ridiculus&neque=mus&libero=vivamus&convallis=vestibulum&eget=sagittis&eleifend=sapien&luctus=cum&ultricies=sociis&eu=natoque&nibh=penatibus&quisque=et&id=magnis",
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
  "urlfoto": "http://hc360.com/natoque/penatibus/et/magnis/dis/parturient/montes.js?et=cras&ultrices=mi&posuere=pede&cubilia=malesuada&curae=in&mauris=imperdiet&viverra=et&diam=commodo&vitae=vulputate&quam=justo&suspendisse=in&potenti=blandit&nullam=ultrices&porttitor=enim&lacus=lorem&at=ipsum&turpis=dolor&donec=sit&posuere=amet&metus=consectetuer&vitae=adipiscing&ipsum=elit&aliquam=proin&non=interdum&mauris=mauris&morbi=non&non=ligula&lectus=pellentesque&aliquam=ultrices&sit=phasellus&amet=id&diam=sapien&in=in&magna=sapien&bibendum=iaculis&imperdiet=congue&nullam=vivamus&orci=metus",
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
  "urlfoto": "https://rambler.ru/faucibus/orci.aspx?dictumst=suspendisse&maecenas=potenti&ut=nullam&massa=porttitor&quis=lacus&augue=at&luctus=turpis&tincidunt=donec&nulla=posuere&mollis=metus&molestie=vitae&lorem=ipsum&quisque=aliquam&ut=non&erat=mauris&curabitur=morbi&gravida=non&nisi=lectus&at=aliquam&nibh=sit&in=amet&hac=diam&habitasse=in&platea=magna&dictumst=bibendum&aliquam=imperdiet&augue=nullam&quam=orci&sollicitudin=pede&vitae=venenatis&consectetuer=non&eget=sodales&rutrum=sed&at=tincidunt&lorem=eu&integer=felis&tincidunt=fusce&ante=posuere&vel=felis&ipsum=sed&praesent=lacus&blandit=morbi&lacinia=sem&erat=mauris&vestibulum=laoreet&sed=ut&magna=rhoncus&at=aliquet&nunc=pulvinar&commodo=sed&placerat=nisl&praesent=nunc&blandit=rhoncus&nam=dui&nulla=vel&integer=sem",
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
  "urlfoto": "http://fema.gov/elit/ac.json?dapibus=quam&dolor=sapien&vel=varius&est=ut&donec=blandit&odio=non&justo=interdum&sollicitudin=in&ut=ante&suscipit=vestibulum&a=ante&feugiat=ipsum&et=primis",
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
  "urlfoto": "http://t.co/metus/aenean/fermentum/donec/ut/mauris/eget.jpg?odio=sit&in=amet&hac=cursus&habitasse=id&platea=turpis&dictumst=integer&maecenas=aliquet&ut=massa&massa=id&quis=lobortis&augue=convallis&luctus=tortor&tincidunt=risus&nulla=dapibus&mollis=augue&molestie=vel&lorem=accumsan&quisque=tellus&ut=nisi&erat=eu&curabitur=orci&gravida=mauris&nisi=lacinia&at=sapien&nibh=quis&in=libero&hac=nullam&habitasse=sit&platea=amet&dictumst=turpis&aliquam=elementum&augue=ligula&quam=vehicula&sollicitudin=consequat&vitae=morbi&consectetuer=a&eget=ipsum&rutrum=integer&at=a&lorem=nibh&integer=in&tincidunt=quis&ante=justo&vel=maecenas&ipsum=rhoncus&praesent=aliquam&blandit=lacus&lacinia=morbi&erat=quis&vestibulum=tortor",
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
  "urlfoto": "http://ibm.com/luctus.xml?vulputate=tortor&elementum=sollicitudin&nullam=mi&varius=sit&nulla=amet&facilisi=lobortis&cras=sapien&non=sapien&velit=non&nec=mi&nisi=integer&vulputate=ac&nonummy=neque&maecenas=duis&tincidunt=bibendum&lacus=morbi&at=non&velit=quam&vivamus=nec&vel=dui&nulla=luctus&eget=rutrum&eros=nulla&elementum=tellus&pellentesque=in&quisque=sagittis&porta=dui&volutpat=vel&erat=nisl&quisque=duis&erat=ac&eros=nibh&viverra=fusce&eget=lacus&congue=purus&eget=aliquet&semper=at&rutrum=feugiat&nulla=non&nunc=pretium&purus=quis&phasellus=lectus&in=suspendisse&felis=potenti&donec=in&semper=eleifend&sapien=quam&a=a&libero=odio&nam=in&dui=hac&proin=habitasse&leo=platea&odio=dictumst&porttitor=maecenas&id=ut",
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
  "urlfoto": "http://paginegialle.it/non/velit/nec/nisi/vulputate.json?eleifend=faucibus&luctus=orci&ultricies=luctus&eu=et&nibh=ultrices&quisque=posuere&id=cubilia&justo=curae&sit=donec&amet=pharetra&sapien=magna&dignissim=vestibulum&vestibulum=aliquet&vestibulum=ultrices&ante=erat&ipsum=tortor&primis=sollicitudin&in=mi&faucibus=sit&orci=amet&luctus=lobortis&et=sapien&ultrices=sapien&posuere=non&cubilia=mi&curae=integer&nulla=ac&dapibus=neque&dolor=duis&vel=bibendum&est=morbi&donec=non&odio=quam&justo=nec&sollicitudin=dui&ut=luctus&suscipit=rutrum&a=nulla&feugiat=tellus&et=in&eros=sagittis&vestibulum=dui&ac=vel&est=nisl&lacinia=duis&nisi=ac&venenatis=nibh&tristique=fusce&fusce=lacus&congue=purus&diam=aliquet&id=at&ornare=feugiat&imperdiet=non&sapien=pretium&urna=quis&pretium=lectus&nisl=suspendisse&ut=potenti&volutpat=in&sapien=eleifend&arcu=quam&sed=a&augue=odio&aliquam=in&erat=hac&volutpat=habitasse&in=platea&congue=dictumst&etiam=maecenas&justo=ut&etiam=massa&pretium=quis&iaculis=augue&justo=luctus&in=tincidunt&hac=nulla&habitasse=mollis&platea=molestie&dictumst=lorem&etiam=quisque&faucibus=ut",
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
  "urlfoto": "http://amazon.de/lacinia/sapien.js?in=augue&porttitor=vestibulum&pede=ante&justo=ipsum&eu=primis&massa=in&donec=faucibus&dapibus=orci&duis=luctus&at=et&velit=ultrices&eu=posuere&est=cubilia&congue=curae&elementum=donec&in=pharetra&hac=magna&habitasse=vestibulum&platea=aliquet&dictumst=ultrices&morbi=erat&vestibulum=tortor&velit=sollicitudin&id=mi&pretium=sit&iaculis=amet&diam=lobortis&erat=sapien&fermentum=sapien&justo=non&nec=mi&condimentum=integer&neque=ac&sapien=neque&placerat=duis&ante=bibendum&nulla=morbi&justo=non&aliquam=quam&quis=nec&turpis=dui",
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
  "urlfoto": "https://geocities.com/in/eleifend/quam/a/odio/in/hac.js?ultrices=sapien&vel=placerat&augue=ante&vestibulum=nulla&ante=justo&ipsum=aliquam&primis=quis&in=turpis&faucibus=eget&orci=elit&luctus=sodales&et=scelerisque&ultrices=mauris&posuere=sit&cubilia=amet&curae=eros&donec=suspendisse&pharetra=accumsan&magna=tortor&vestibulum=quis&aliquet=turpis&ultrices=sed&erat=ante",
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
    #from random import Random as r
    
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
        pers = Persona.objects.get(id= data['idpersona'])
        org =Organizacion.objects.get(id= data['idorganizacion'])
        Publicacion(
            id=data["id"],
            estado=data["estado"],
            descripcion=data["descripcion"],
            titulo=data["titulo"],
            idorganizacion= org,
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
        },
        {
            "estado": "vendido",
            "titulo": "Cachorros de Golden Retriever en adopción",
            "descripcion": "Tres cachorros de Golden Retriever ya encontraron un hogar.",
            "fechapublicacion": "2023-09-28T10:15:00Z",
            "idorganizacion": 28,  # ID de otra organización que publica
            "idpersona": 2,  # No asociado a un usuario individual
        },
        {
            "estado": "disponible",
            "titulo": "Buscando un hogar para este perrito",
            "descripcion": "Perrito de raza mixta en busca de una familia cariñosa.",
            "fechapublicacion": "2023-09-25T16:45:00Z",
            "idorganizacion": 26,  # No asociado a una organización
            "idpersona": 1,  # ID de un usuario individual que publica
        },
        {
            "estado": "disponible",
            "titulo": "Dos gatos juguetones necesitan un nuevo hogar",
            "descripcion": "Gatos hermanos que desean encontrar un hogar juntos.",
            "fechapublicacion": "2023-09-22T09:00:00Z",
            "idorganizacion": 25,  # No asociado a una organización
            "idpersona": 2,  # ID de otro usuario individual que publica
        },
    ]
    print('vamos en posts: lista de ids de org:', [(org.id,org.username) for org in Organizacion.objects.all()])
    for data in publicaciones:
        extra_fields = {
            key: value
            for key, value in data.items()
            if key not in ["estado", "descripcion", "titulo", 'idorganizacion', 'idpersona']
        }
        pers = Persona.objects.get(id= data['idpersona'])
        org =Organizacion.objects.get(id= data['idorganizacion'])
        Publicacion.objects.create(
            estado=data["estado"],
            descripcion=data["descripcion"],
            titulo=data["titulo"],
            idorganizacion= org,
            idpersona=pers,
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
            comentario.publicaciones.set(Publicacion.objects.filter(id__in=publicaciones_ids))

    print("\nComentarios ficticios agregados correctamente.")


