import axios from 'axios';
import { BASE_URL } from './config'
const ACCOUNTS = axios.create({
    baseURL: BASE_URL + 'accounts/api/'
})


export const login = async (formData) => {
    try {
        console.log(ACCOUNTS+'login/');
        const response = await ACCOUNTS.post('login/', formData);

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

export const register = async (formData) => {
    try {
        const response = await ACCOUNTS.post('register/', formData);

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


export const getUser = async (userID) => {
    try {
        const response = await ACCOUNTS.get('user/'+userID);

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
export const getprofile = async () => {
    try {
        const response = await ACCOUNTS.get('profile/');

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


