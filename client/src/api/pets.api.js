import axios from 'axios';
import { BASE_URL } from './config'
const PETS = axios.create({
    baseURL: BASE_URL + 'pets/api/'
})

// Función para obtener una lista de mascotas
async function getPets() {
  try {
    const response = await PETS.get('pets/');
    return response.data;
  } catch (error) {
    throw error;
  }
}

// Función para crear una nueva mascota
async function createPet(petData) {
  try {
    const response = await PETS.post('pets/', petData);
    return response.data;
  } catch (error) {
    throw error;
  }
}

// Función para obtener los detalles de una mascota por ID
async function getPetById(id) {
  try {
    const response = await PETS.get(`pets/${id}/`);
    return response.data;
  } catch (error) {
    throw error;
  }
}

// Función para actualizar los detalles de una mascota por ID
async function updatePet(id, petData) {
  try {
    const response = await PETS.put(`pets/${id}/`, petData);
    return response.data;
  } catch (error) {
    throw error;
  }
}

// Función para eliminar una mascota por ID
async function deletePet(id) {
  try {
    const response = await PETS.delete(`pets/${id}/`);
    return response.data;
  } catch (error) {
    throw error;
  }
}

// Función para obtener una lista de mascotas de una organización
async function getOrganizationPets() {
  try {
    const response = await PETS.get('pets/organization/');
    return response.data;
  } catch (error) {
    throw error;
  }
}

export const recoverPassword = (email) => PETS.get('/recoverPassword/')

export const setNewPassword = (email) => PETS.get('/recoverPassword/')

export {
  getPets,
  createPet,
  getPetById,
  updatePet,
  deletePet,
  getOrganizationPets,
};
