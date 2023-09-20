import axios from 'axios'

// const petApi = axios.create({
//     baseURL: 'https://unpet.onrender.com/pets/api/v1/pets'
// })


const petApi = axios.create({
    baseURL: 'http://127.0.0.1:8000/pets/api/v1/pets'
})

export const getPet = (id) =>
petApi.get(`/${id}/`)

export const getAllPets = () =>
petApi.get('/')

export const createPet = (pet) => {
    return petApi.post('/', pet)
}

export const deletePet = (id) => petApi.delete(`${id}`)

export const editPet = (id, pet) => petApi.put(`/${id}/`, pet)