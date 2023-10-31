import axios from 'axios';
import { BASE_URL } from './config'
const ACCOUNTS = axios.create({
    baseURL: BASE_URL + 'accounts/api/',
})

export const login = async (formData) => {
    const response = await ACCOUNTS.post('login/', formData);
    return response;
};

export const register = async (formData) => {
    const response = await ACCOUNTS.post('register/', formData);
    return response;
};

export const orgRegister = async (formData) => {
    const response = await ACCOUNTS.post('org_register/', formData);
    return response;
};

export const logout = async () => {
    const response = await ACCOUNTS.post('logout/');
    return response;
};

export const getUser = async (username) => {
    const response = await ACCOUNTS.get(`user/${username}/`);
    return response;
};

export const getProfile = async () => {
    const response = await ACCOUNTS.get('profile/');
    return response;
};


export const getMD = async (filename) => {
    try {
        console.log('nopmbre de archivo: '+filename);
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

