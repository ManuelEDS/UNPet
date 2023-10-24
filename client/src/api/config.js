import axios from "axios";

const isDevelopment = process.env.NODE_ENV === 'development';

let URL = isDevelopment
    ? 'http://127.0.0.1:8000/' : 'https://unpet.onrender.com/accounts/api';
var d =''
try {
    d=axios.get(URL+'accounts/api/test/');
} catch (error) {
    console.log('ERROR, EL HOST ES:' + URL, d)
    if (isDevelopment) {
        URL = 'http://localhost:8000/'
    }
    
}
export const BASE_URL = URL;
