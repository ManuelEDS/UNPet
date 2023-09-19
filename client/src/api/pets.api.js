import axios from 'axios'

const petApi = axios.create({
    baseURL: 'https://unpet_api.onrender.com/pets/api/v1/'
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