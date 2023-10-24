import axios from 'axios'

// const petApi = axios.create({
//     baseURL: 'https://unpet.onrender.com/pets/api/v1/pets'
// })

const isDevelopment = process.env.NODE_ENV === 'development';

const petApi = isDevelopment
  ? axios.create({
      baseURL: 'http://127.0.0.1:8000/pets/api/v1/pets'
    })
  : axios.create({
      baseURL: 'https://unpet.onrender.com/pets/api/v1/pets'
    });

  // Resto del código para otros entornos



export const getPet = (id) =>
petApi.get(`/${id}/`)

export const getAllPets = () =>
petApi.get('/')

export const createPet = (pet) => {
    return petApi.post('/', pet)
}

export const deletePet = (id) => petApi.delete(`${id}`)

export const editPet = (id, pet) => petApi.put(`/${id}/`, pet)

export const recoverPassword = (email) => petApi.get(`/recoverPassword/`)

export const setNewPassword = (email) => petApi.get(`/recoverPassword/`)