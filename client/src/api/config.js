import axios from "axios";
import process from "process";

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

export const BASE_URL = URL;

