import { useEffect, useState } from "react"
import {getAllPets} from '../api/pets.api'
import {PetCard} from './PetCard'

export function PetList() {

    const [pets, setPets] = useState([]);

    useEffect(() => {     
        async function loadPets(){
            const res = await getAllPets();
            setPets(res.data)
        }
        loadPets();
      }, [])
      
    return (
      <div>
        {pets.map(pet => (
            <PetCard key={pet.id} pet={pet} />
        ))}
      </div>
    )
  }