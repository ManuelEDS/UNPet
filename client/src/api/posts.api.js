import axios from 'axios';
import { BASE_URL } from './config'
const POSTS = axios.create({
    baseURL: BASE_URL + 'posts/api/'
})

export const getposts = async (page) => {
    const response = await POSTS.get(`posts/page/${page}/`);
    return response.data;
};

export const getPublicacion = async (id) => {
    const response = await POSTS.get(`posts/${id}/`);
    return response.data;
};

export const createPublicacion = async (publicacion) => {
    const response = await POSTS.post(`posts/`, publicacion);
    return response.data;
};

export const updatePublicacion = async (id, publicacion) => {
    const response = await POSTS.put(`posts/${id}/`, publicacion);
    return response.data;
};

export const deletePublicacion = async (id) => {
    const response = await POSTS.delete(`posts/${id}/`);
    return response.status === 204;
};

export const searchposts = async (query) => {
    const encodedQuery = encodeURIComponent(query);
    const response = await POSTS.get(`posts/search/?q=${encodedQuery}`);
    return response.data;
};