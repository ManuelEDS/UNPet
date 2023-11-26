import { UNPetAxios } from './config'


const BASE_RUTA = '/accounts/api/'
const ACCOUNTS = new UNPetAxios(BASE_RUTA)
ACCOUNTS.init()


/**
 * Función que realiza una petición POST al endpoint 'login/' del API de cuentas.
 * @param {Object} formData - Objeto con los datos del formulario de inicio de sesión.
 * @returns {Promise} - Promesa que resuelve con la respuesta de la petición.
 */
export const login = async (formData) => {
    
    console.log('login, body: ', formData)
    try {
        const response = await ACCOUNTS.post('login/', formData);
        if (response.status === 200) {
            return { isAuthenticated: true, error: "" };
        } else {
            throw new Error("Wrong username or password.");
        }
    } catch (error) {
        console.log(error);
        return { isAuthenticated: false, error: "server error." };
    }
};

/**
 * Función que realiza una petición POST al endpoint 'register/' del API de cuentas.
 * @param {Object} formData - Objeto con los datos del formulario de registro.
 * @returns {Promise} - Promesa que resuelve con la respuesta de la petición.
 */
export const register = async (formData) => {
    try {
        const response = await ACCOUNTS.post('register/', formData, {}, {"Content-Type": 'multipart/form-data'});
        if (response.status === 200) {
            return { isAuthenticated: true, error: "" };
        } else {
            throw new Error("error de usuario.");
        }
    } catch (error) {
        console.log(error);
        return { isAuthenticated: false, error: error };
    }
};

/**
 * Función que realiza una petición POST al endpoint 'org_register/' del API de cuentas.
 * @param {Object} formData - Objeto con los datos del formulario de registro de organización.
 * @returns {Promise} - Promesa que resuelve con la respuesta de la petición.
 */
export const orgRegister = async (formData) => {
    try {
        const response = await ACCOUNTS.post('org_register/', formData, {}, {"Content-Type": 'multipart/form-data'});
        if (response.status === 200) {
            return { isAuthenticated: true, error: "" };
        } else {
            throw new Error("error de usuario.");
        }
    } catch (error) {
        console.log(error);
        return { isAuthenticated: false, error: error };
    }
};


/**
 * Función que realiza una petición POST al endpoint 'logout/' del API de cuentas para cerrar sesión.
 * @returns {Promise} - Promesa que resuelve con la respuesta de la petición.
 */
export const logout = async () => {
   
    try {
        const response = await ACCOUNTS.get('logout/');

        return { isAuthenticated: false, error: "" };
    } catch (error) {
        console.log(error);
        return { isAuthenticated: true, error: error };
        
    }
};


/**
 * Función que realiza una petición GET al endpoint 'user/:username/' del API de cuentas.
 * @param {string} username - Nombre de usuario del usuario a obtener.
 * @returns {Promise} - Promesa que resuelve con la respuesta de la petición.
 */
export const getUser = async (username) => {
    const response = await ACCOUNTS.get(`user/${username}/`);
    const data = response.data
    console.log(data);
    return data;
};
/**
 * Función que realiza una petición GET al endpoint 'profile/' del API de cuentas.
 * @returns {Promise} - Promesa que resuelve con la respuesta de la petición.
 */
export const getProfile = async () => {
    const response = await ACCOUNTS.get('profile/');
    const data = response
    console.log(data);
    return data;
};

export const updateProfile = async (formData) => {
    const response = await ACCOUNTS.put('profile/', formData);
    return response;
}

/**
 * Función que realiza una petición GET al endpoint 'legal/:filename.md' del API de cuentas para obtener un archivo legal.
 * @param {string} filename - Nombre del archivo legal a obtener.
 * @returns {Promise} - Promesa que resuelve con el contenido del archivo legal.
 * @throws {Error} - Error que se lanza si la petición no se realiza correctamente.
 */
export const getHTML = async (filename) => {
    try {
        const response = await ACCOUNTS.get('legal/'+filename);

        if (response.status === 200) {
            return response.text();
        } else {
            throw new Error(response.data.message);
        }
    } catch (error) {
        console.log(error.message);
        throw new Error(error.message);
    }
};

