import React from 'react';
import DevCard from '../components/DevCard';
import Ex1 from './ex1';
import { Typography } from '@mui/material';
import Container from '@mui/material/Container';

import '../styles/WhoAreWePage.css';
const developers = [
    {
        name: 'César Fabián Rincón Robayo',
        role: 'Backend Developer',
        image: 'https://scontent.fbog3-1.fna.fbcdn.net/v/t39.30808-6/362633391_2315258502014590_7833701919667759161_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeHIIYGAB--o-TBnC5sjpBKWYAgBV71zsnJgCAFXvXOycpainCjxnxAjp8qCPVWn-rmSH9tM8XkClpd9tZ8P9ec1&_nc_ohc=l3AraDEgZNgAX900wVY&_nc_ht=scontent.fbog3-1.fna&oh=00_AfAsJMj7NBqT9-GhrGzOPEQ1-HTkabyPolJaIvzh-1QnRg&oe=65431E93',
        bio: 'Lorem ipsum dolor sit amet.',
        facebook: 'https://www.facebook.com/cesarfabian.rinconrobayo/',
        mail:'crinconro@unal.edu.co',
        instagram:'https://www.instagram.com/cesar343rincon/?next=%2F#',
        github:'https://github.com/CesarFRR/'
    },
    {
        name: 'David Mateo Ballesteros',
        role: 'Frontend Developer',
        image: 'https://scontent.fbog3-2.fna.fbcdn.net/v/t39.30808-6/273025259_3117086298621112_6950800873385306315_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeH19zdV0s7mOLtajQ1GJEaZsxCKRrm4jyCzEIpGubiPIBIeQhR04dxvbR1SLRJxUjYyeMa55syLW8i3HrA0Adkj&_nc_ohc=rmkOXqr1Os8AX8WqohZ&_nc_ht=scontent.fbog3-2.fna&oh=00_AfBk1oHLkze8QWDIo0QVnYkGmnjAAEnzkUy85foIi5UxZw&oe=654302F7',
        bio: 'Lorem ipsum dolor sit amet.'
    },
    {
        name: 'Juan David Ramírez Torres',
        role: 'Full Stack Developer',
        image: 'https://media.licdn.com/dms/image/C4E03AQFUXpq4V-LFdg/profile-displayphoto-shrink_800_800/0/1660250201603?e=1704326400&v=beta&t=rcue-vwOFf0qpJTiXjHP8QgZSanrz0zQMOpa2N9y6as',
        bio: 'Lorem ipsum dolor sit amet.'
    },
    {
        name: 'Manuel Eduardo Diaz Sabogal',
        role: 'Database Analyst',
        image: 'https://dummyimage.com/600x400/d1d1d1/5b62c7.jpg&text=Bob%20Smith',
        bio: 'Lorem ipsum dolor sit amet.'
    },
    {
        name: 'Carlos Javier Camacho Cely',
        role: 'Frontend Developer',
        image: 'https://dummyimage.com/600x400/d1d1d1/5b62c7.jpg&text=Bob%20Smith',
        bio: 'Lorem ipsum dolor sit amet.'
    },
];

function WhoAreWePage() {
    console.log(developers[0]);
    return (<div>
        <Container maxWidth="lg">

            <Container maxWidth="md">
            
                <Typography variant="h4" gutterBottom align="center">
                    ¿Quiénes somos?
                </Typography>
                <br />
                <br />
                

                <Typography variant="h5" gutterBottom className='h5-title'>
                    UNPet: Tu Compañero de Adopción de Mascotas
                </Typography>
               
                <Typography variant="body1" gutterBottom className="left-align">
                    En UNPet, somos un grupo de apasionados desarrolladores estudiantes de la Universidad Nacional con un objetivo claro: hacer una diferencia en la vida de las mascotas y las personas que desean darles un hogar amoroso.
                </Typography>
                <br />
                <Typography variant="h5" gutterBottom className="right-align">
                    Nuestra Misión
                </Typography>
               
                <Typography variant="body1" gutterBottom className="right-align">
                    Nuestra misión en UNPet es simple pero poderosa: darle visibilidad a las fundaciones de adopción de mascotas y ayudar a los usuarios a encontrar la mascota perfecta que se adapte a su estilo de vida y necesidades. Creemos en el poder de la adopción responsable, y estamos comprometidos a conectar a personas cariñosas con las mascotas que necesitan un nuevo hogar.
                </Typography>
                <br />
                <Typography variant="h5" gutterBottom className="left-align">
                    Lo que nos impulsa
                </Typography>
               
                <Typography variant="body1" gutterBottom className="left-align">
                    En UNPet, estamos impulsados por el amor por los animales y el deseo de hacer del mundo un lugar mejor para ellos. Entendemos que las fundaciones de adopción de mascotas son la voz de los que no pueden hablar, y nuestro objetivo es amplificar esa voz. Creemos que cada mascota merece un hogar lleno de amor y cuidado, y estamos decididos a hacer que esto sea una realidad para tantas mascotas como sea posible.
                </Typography>
                <br />
                <Typography variant="h5" gutterBottom className="right-align">
                    Nuestro Compromiso
                </Typography>
                
                <Typography variant="body1" gutterBottom className="right-align">
                    Estamos comprometidos con la transparencia, la ética y la seguridad en todas nuestras interacciones. Trabajamos estrechamente con fundaciones y refugios de mascotas para garantizar que todos los perfiles de mascotas sean precisos y que los usuarios puedan confiar en la información que encuentren en nuestra plataforma.
                </Typography>
                <br />
                <Typography variant="h5" gutterBottom className="left-align">
                    Únete a la Comunidad UNPet
                </Typography>
                
                <Typography variant="body1" gutterBottom className="left-align">
                    Si compartes nuestra pasión por los animales y crees en la adopción responsable, te invitamos a unirte a nuestra comunidad. Ya seas una fundación de adopción, un amante de las mascotas en busca de un nuevo compañero peludo o simplemente alguien interesado en apoyar nuestra causa, esperamos que te sientas inspirado por lo que hacemos en UNPet.
                </Typography>
                <br />
                <Typography variant="body1" gutterBottom className="left-align">
                    Juntos, podemos marcar la diferencia en la vida de las mascotas y hacer que el mundo sea un lugar más cálido y amoroso para todos. ¡Bienvenido a UNPet!
                </Typography>
                <br />
                <br />
                <br />
            </Container>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '60px', margin: '20px' }}>
                {developers.map((developer, index) => (

                    <DevCard
                        key={index}
                        name={developer.name}
                        skills={developer.role + ', ' + developer.bio}
                        photo={developer.image}
                        fb={developer.facebook}
                        mail={developer.mail}
                        inst={developer.instagram}
                        gh={developer.github}
                    />

                ))}
            </div>
        </Container>


    </div>
        //<Ex1></Ex1>
    );
}

export default WhoAreWePage;
