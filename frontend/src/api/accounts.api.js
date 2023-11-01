import axios from 'axios';
import { BASE_URL } from './config'

const ACCOUNTS = axios.create({
    baseURL: BASE_URL + 'accounts/api/',
})

/**
 * Función que realiza una petición POST al endpoint 'login/' del API de cuentas.
 * @param {Object} formData - Objeto con los datos del formulario de inicio de sesión.
 * @returns {Promise} - Promesa que resuelve con la respuesta de la petición.
 */
export const login = async (formData) => {
    const response = await ACCOUNTS.post('login/', formData);
    return response;
};

/**
 * Función que realiza una petición POST al endpoint 'register/' del API de cuentas.
 * @param {Object} formData - Objeto con los datos del formulario de registro.
 * @returns {Promise} - Promesa que resuelve con la respuesta de la petición.
 */
export const register = async (formData) => {
    const response = await ACCOUNTS.post('register/', formData);
    return response;
};

/**
 * Función que realiza una petición POST al endpoint 'org_register/' del API de cuentas.
 * @param {Object} formData - Objeto con los datos del formulario de registro de organización.
 * @returns {Promise} - Promesa que resuelve con la respuesta de la petición.
 */
export const orgRegister = async (formData) => {
    const response = await ACCOUNTS.post('org_register/', formData);
    return response;
};


/**
 * Función que realiza una petición POST al endpoint 'logout/' del API de cuentas para cerrar sesión.
 * @returns {Promise} - Promesa que resuelve con la respuesta de la petición.
 */
export const logout = async () => {
    const response = await ACCOUNTS.post('logout/');
    return response;
};


/**
 * Función que realiza una petición GET al endpoint 'user/:username/' del API de cuentas.
 * @param {string} username - Nombre de usuario del usuario a obtener.
 * @returns {Promise} - Promesa que resuelve con la respuesta de la petición.
 */
export const getUser = async (username) => {
    const response = await ACCOUNTS.get(`user/${username}/`);
    return response;
};

/**
 * Función que realiza una petición GET al endpoint 'profile/' del API de cuentas.
 * @returns {Promise} - Promesa que resuelve con la respuesta de la petición.
 */
export const getProfile = async () => {
    const response = await ACCOUNTS.get('profile/');
    return response;
};

/**
 * Función que realiza una petición GET al endpoint 'legal/:filename.md' del API de cuentas para obtener un archivo legal.
 * @param {string} filename - Nombre del archivo legal a obtener.
 * @returns {Promise} - Promesa que resuelve con el contenido del archivo legal.
 * @throws {Error} - Error que se lanza si la petición no se realiza correctamente.
 */
export const getMD = async (filename) => {
    try {
        console.log('nombre de archivo: '+filename);
        const response = await ACCOUNTS.get('legal/'+filename);

        if (response.status === 200) {
            return response.data;
        } else {
            throw new Error(response.data.message);
        }
    } catch (error) {
        console.log(error.message);
        throw new Error(error.message);
    }
};

