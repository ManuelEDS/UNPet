import axios from 'axios';
import { BASE_URL } from './config'
const POSTS = axios.create({
    baseURL: BASE_URL + 'posts/api/'
})

export const getPublicaciones = async (page) => {
    const response = await POSTS.get(`publicaciones/page/${page}/`);
    return response.data;
};

export const getPublicacion = async (id) => {
    const response = await POSTS.get(`publicaciones/${id}/`);
    return response.data;
};

export const createPublicacion = async (publicacion) => {
    const response = await POSTS.post(`publicaciones/`, publicacion);
    return response.data;
};

export const updatePublicacion = async (id, publicacion) => {
    const response = await POSTS.put(`publicaciones/${id}/`, publicacion);
    return response.data;
};

export const deletePublicacion = async (id) => {
    const response = await POSTS.delete(`publicaciones/${id}/`);
    return response.status === 204;
};

export const searchPublicaciones = async (query) => {
    const encodedQuery = encodeURIComponent(query);
    const response = await POSTS.get(`publicaciones/search/?q=${encodedQuery}`);
    return response.data;
};