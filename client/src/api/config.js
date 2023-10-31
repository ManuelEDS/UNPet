import axios from "axios";

const debug = true

let URL = 'http://127.0.0.1:8000/';

var d =''
try {
    d=axios.get(URL+'accounts/api/test/');
} catch (error) {
    console.log('ERROR, EL HOST ES:' + URL, d)
    if (debug) {
        URL = 'http://localhost:8000/'
    }
    
}

if (debug){
    URL = 'http://127.0.0.1:8000/'
}
/**
 * La URL base del host.
 * @type {string}
 */
export const BASE_URL = URL;

