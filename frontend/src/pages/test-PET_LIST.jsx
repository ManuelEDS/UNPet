import React, { useEffect, useState } from 'react';
import { getOrganizationPets } from '../api/pets.api';

export const PetList = () => {
    const [pets, setPets] = useState([]);

    useEffect(() => {
        const fetchPets = async () => {
            console.log('EL FETCH CON FNCION: ');
            const data = await getOrganizationPets();
            console.log('EL DATA con unpetaxios: ',data)
            setPets(data);
        }
        fetchPets();
    }, []);

    return (
        <div>
            {pets.map((pet, index) => (
                <div key={pet.id + index}>
                    <h2>{pet.nombre}</h2>
                    <img src={pet.urlfoto} alt="" />

                    {/* Add more fields as necessary */}
                </div>
            ))}
        </div>
    );
};