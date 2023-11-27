
# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Publicacion
from pets.models import Mascota
from .serializer import PublicacionSerializer
from accounts.models import Organizacion, User
from pets.serializer import MascotaSerializer


class PublicacionViewTest(TestCase):


    def setUp(self):

        agregar_grupos()
        agregar_localidades()
        self.client = Client()
        self.url = reverse('publicacion-create')
        user , org = User.objects.create_Organization(email='org1@gmail.com',username='organizacion1', nit='123456789', password='contraseñaorganizacion1', name='Organizacion1 huellitas', direccion='Calle 1', telefono='1234567890', idlocalidad=1)
        self.client.login(username='organizacion1', password='contraseñaorganizacion1')

        # Crea algunas mascotas para la prueba
        common_data= {'idorganizacion': user.id, 'publicacion':None, 'raza':'Desconocida', 'sexo':'Macho', 'especie':'Perro'}
        m1= {'nombre': 'Wisky', 'fechanacimiento':'2020-11-13', "urlfoto": "https://images.unsplash.com/photo-1530991671072-ac4f81c2c3c1?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MTQ1MA&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900"}
        m2= {'nombre': 'Rex', 'fechanacimiento':'2020-03-13', "urlfoto": "https://images.unsplash.com/photo-1545249390-6bdfa286032f?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=700&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2F0fHx8fHx8MTcwMDk2MTQ1Mg&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=900"}
        self.mascota1 = MascotaSerializer(data={**common_data, **m1})
        self.mascota1.is_valid(raise_exception=True)
        self.mascota1= self.mascota1.save()

        self.mascota2 = MascotaSerializer(data={**common_data, **m2})
        self.mascota2.is_valid(raise_exception=True)
        self.mascota2=  self.mascota2.save()

        # Datos para la solicitud POST
        self.data = {
            'post': {
                "idorganizacion": user.id,
                "estado": "Disponibles",
                'titulo': 'Titulo de prueba',
                'descripcion': 'Contenido de prueba',
                "n_mascotas": 2,
                "n_mascotas_adoptadas": 0,
                "mascotas": [{'id': self.mascota1.id}, {'id': self.mascota2.id}],
            }
        }

    def test_create_publicacion(self):
        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        publicacion = Publicacion.objects.get(id=response.data['id'])
        self.assertEqual(publicacion.titulo, self.data['post']['titulo'])
        self.assertEqual(publicacion.descripcion, self.data['post']['descripcion'])

        mascotas = publicacion.mascotas.all()
        self.assertEqual(len(mascotas), 2)
        self.assertEqual(mascotas[0].id, self.mascota1.id)
        self.assertEqual(mascotas[1].id, self.mascota2.id)




def agregar_grupos():
    from django.contrib.auth.models import Group

    grupos = ["Persona", "Organizacion"]
    lista = [g.name for g in Group.objects.all()]
    print("\n\n\n\n", lista, "\n\n\n\n")
    for grupo in grupos:
        if grupo not in lista:
            Group.objects.create(name=grupo)

def agregar_localidades():
    from accounts.models import Localidad

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