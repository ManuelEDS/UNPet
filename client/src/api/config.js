import axios from "axios";

const isDevelopment = process.env.NODE_ENV === 'development';

const BASE_URL = isDevelopment
    ? 'http://127.0.0.1:8000/' : 'https://unpet.onrender.com/accounts/api';
var d =''
try {
    d=axios.get(BASE_URL+'accounts/api/test/');
} catch (error) {
    console.log('ERROR, EL HOST ES:' + BASE_URL, d)
    if (isDevelopment) {
        BASE_URL = 'http://localhost:8000/'
    }
    
}

export { BASE_URL };