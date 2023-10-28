import { useState, useEffect } from 'react';
import { createPet, deletePet, editPet, getPet } from '../api/pets.api';
import { useNavigate, useParams } from 'react-router-dom';
import { TextField, Button, Select, MenuItem, FormControl, InputLabel } from '@mui/material';

export function PetFormPage() {
    const [name, setName] = useState('');
    const [race, setRace] = useState('');
    const [errors, setErrors] = useState({});
    const navigate = useNavigate();
    const params = useParams();

    useEffect(() => {
        async function loadPet() {
            if (params.id) {
                const { data } = await getPet(params.id);
                setName(data.name);
                setRace(data.race);
            }
        }
        loadPet();
    }, []);

    const onSubmit = async (event) => {
        event.preventDefault();
        const data = { name, race };
        if (params.id) {
            console.log(data);
            await editPet(params.id, data);
        } else {
            const res = await createPet(data);
            console.log(res);
        }
        // Auto redireccionamiento
        navigate('/pets');
    };

    const onDelete = async () => {
        const accepted = window.confirm('seguro?');
        if (accepted) {
            await deletePet(params.id);
        }
    };

    return (
        <div>
            <form onSubmit={onSubmit}>
                <TextField
                    label="Nombre"
                    variant="outlined"
                    value={name}
                    onChange={(event) => setName(event.target.value)}
                />
                {errors.name && <span>el nombre es requerido</span>}
                <FormControl variant="outlined">
                    <InputLabel id="race-label">Raza</InputLabel>
                    <Select
                        labelId="race-label"
                        id="race"
                        value={race}
                        onChange={(event) => setRace(event.target.value)}
                        label="Raza"
                    >
                        <MenuItem value="Gato">Gato</MenuItem>
                        <MenuItem value="Perro">Perro</MenuItem>
                    </Select>
                </FormControl>
                {errors.race && <span>la raza es requerida</span>}
                <Button variant="contained" type="submit">Crear</Button>
            </form>
            {params.id && <Button variant="contained" onClick={onDelete}>Delete</Button>}
        </div>
    );
}

