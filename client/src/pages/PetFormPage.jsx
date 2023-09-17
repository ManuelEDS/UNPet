import { useForm, } from 'react-hook-form'
import { createPet, deletePet, editPet, getPet } from '../api/pets.api'
import { useNavigate, useParams } from 'react-router-dom';
import { useEffect } from 'react';

export function PetFormPage() {

    const { register, handleSubmit,
        formState: { errors },
        setValue
    } = useForm();

    const navigate = useNavigate();

    const params = useParams();

    const onSubmit = handleSubmit(async data => {
        if (params.id) {
            console.log(data)
            await editPet(params.id, data)
        } else {
            const res = await createPet(data);
            console.log(res)
        }

        // Auto redireccionamiento
        navigate("/pets");

    })

    useEffect(() => {
        async function loadPet() {
            if (params.id) {
                const { data } = await getPet(params.id);
                setValue('name', data.name);
                setValue('race', data.race)
                console.log(data)
            }
        }
        loadPet()
    }, [])


    return (
        <div>
            <form onSubmit={onSubmit}>
                <input type="text" placeholder="Nombre" {...register("name", { required: true })} />                {errors.name && <span>el nombre es requerido</span>}
                <select name="race" id="race" {...register("race", { required: true })}>
                    <option value="Gato">Gato</option>
                    <option value="Perro">Perro</option>
                </select>
                {errors.race && <span>la raza es requerida</span>}
                <button>Crear</button>
            </form>
            {params.id && <button onClick={async () => {
                const accepted = window.confirm('seguro?')
                if (accepted) {
                    await deletePet(params.id)
                }
            }
            }>Delete</button>}

        </div>
    )
}