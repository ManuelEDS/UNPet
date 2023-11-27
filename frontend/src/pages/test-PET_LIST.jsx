import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {getOrganizationPets} from '../api/pets.api';
export const PetList = () => {
    const [pets, setPets] = useState([]);

    useEffect(() => {
        const fetchPets = async () => {
        const data =  await getOrganizationPets();
        console.log(pets)
        };
        fetchPets();
    }, []);

    return (
        <div>
            {pets.map((pet, index) => (
                <div key={pet.id + index}>
                    <h2>{pet.nombre}</h2>
                    
                    {/* Add more fields as necessary */}
                </div>
            ))}
        </div>
    );
};