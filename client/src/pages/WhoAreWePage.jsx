import React from 'react';
import DevCard from '../components/DevCard';
import Ex1 from './ex1';
import { Typography } from '@mui/material';
import Container from '@mui/material/Container';

import '../styles/WhoAreWePage.css';
const developers = [
    {
        name: 'César Fabián Rincón Robayo',
        role: 'Full Stack Developer',
        image: 'https://dummyimage.com/600x400/d1d1d1/5b62c7.jpg&text=John%20Doe',
        bio: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor.'
    },
    {
        name: 'David Mateo Ballesteros',
        role: 'Frontend Developer',
        image: 'https://dummyimage.com/600x400/d1d1d1/5b62c7.jpg&text=Jane%20Doe',
        bio: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor.'
    },
    {
        name: 'Juan David Ramírez T.',
        role: 'Backend Developer',
        image: 'https://dummyimage.com/600x400/d1d1d1/5b62c7.jpg&text=Bob%20Smith',
        bio: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor.'
    }
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
                <br />
                <Typography variant="body1" gutterBottom className="left-align">
                    En UNPet, somos un grupo de apasionados desarrolladores estudiantes de la Universidad Nacional con un objetivo claro: hacer una diferencia en la vida de las mascotas y las personas que desean darles un hogar amoroso.
                </Typography>
                <br />
                <Typography variant="h5" gutterBottom className="right-align">
                    Nuestra Misión
                </Typography>
                <br />
                <Typography variant="body1" gutterBottom className="right-align">
                    Nuestra misión en UNPet es simple pero poderosa: darle visibilidad a las fundaciones de adopción de mascotas y ayudar a los usuarios a encontrar la mascota perfecta que se adapte a su estilo de vida y necesidades. Creemos en el poder de la adopción responsable, y estamos comprometidos a conectar a personas cariñosas con las mascotas que necesitan un nuevo hogar.
                </Typography>
                <br />
                <Typography variant="h5" gutterBottom className="left-align">
                    Lo que nos impulsa
                </Typography>
                <br />
                <Typography variant="body1" gutterBottom className="left-align">
                    En UNPet, estamos impulsados por el amor por los animales y el deseo de hacer del mundo un lugar mejor para ellos. Entendemos que las fundaciones de adopción de mascotas son la voz de los que no pueden hablar, y nuestro objetivo es amplificar esa voz. Creemos que cada mascota merece un hogar lleno de amor y cuidado, y estamos decididos a hacer que esto sea una realidad para tantas mascotas como sea posible.
                </Typography>
                <br />
                <Typography variant="h5" gutterBottom className="right-align">
                    Nuestro Compromiso
                </Typography>
                <br />
                <Typography variant="body1" gutterBottom className="right-align">
                    Estamos comprometidos con la transparencia, la ética y la seguridad en todas nuestras interacciones. Trabajamos estrechamente con fundaciones y refugios de mascotas para garantizar que todos los perfiles de mascotas sean precisos y que los usuarios puedan confiar en la información que encuentren en nuestra plataforma.
                </Typography>
                <br />
                <Typography variant="h5" gutterBottom className="left-align">
                    Únete a la Comunidad UNPet
                </Typography>
                <br />
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
            <div className="dev-card-container" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '20px', margin: '20px' }}>
                {developers.map((developer, index) => (

                    <DevCard
                        key={index}
                        name={developer.name}
                        skills={developer.role + ', ' + developer.bio}
                        photo={developer.image}
                        fb='facebook.com'
                        twt='twitter.com'
                        inst='instagram.com'
                        style={{ width: '250px' }}
                    />

                ))}
            </div>
        </Container>


    </div>
        //<Ex1></Ex1>
    );
}

export default WhoAreWePage;
