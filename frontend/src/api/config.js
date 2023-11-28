import axios from "axios";

//===============================================//
// --> SOLO UNA PUEDE SER TRUE <-- //
export const DEBUG = false;
export const DOCKER_MODE = false;
export const RENDER_MODE = true;
//===============================================//

let URL = "";

if (DEBUG) {
    URL = "http://localhost:8000/api";
} else if (DOCKER_MODE) {
    URL = "";
} else if (RENDER_MODE) {
    URL = "https://unpet-api-rest.onrender.com/api";
} else {
    // Test each URL with a simple GET request to "accounts/api/test/"
    const urls = [
        "http://127.0.0.1:8000/api",
        "",
        "https://unpet-api-rest.onrender.com/api"
    ];

    for (let testURL of urls) {
        try {
            await fetch(testURL + "/accounts/api/test");
            // If the request is successful, set the URL and break the loop
            URL = testURL;
            break;
        } catch (error) {
            // console.log('ERROR, EL HOST ES:' + testURL, error);
        }
    }
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

// const sessionId = getCookie('sessionid');
// console.log('sessionid COOKIE: ', sessionId);
// const X_CDRFToken = getCookie('csrftoken');
// console.log('csrftoken COOKIE: ', X_CDRFToken);
/**
 * La URL base del host.
 * @type {string}
 */
export const BASE_URL = URL;
export const CREDENTIALS = 'same-origin';

export const getCSRF = async () => {
    return fetch(BASE_URL + "/accounts/api/csrf/", {
        credentials: CREDENTIALS,
    })
    .then(response => response.json())
    .then(data => {
        console.log('crsfToken para el nuevo getCSRF(): ', data.csrfToken);
        return data.csrfToken;
    })
    .catch((err) => {
        //console.log(err);
    });
}
// Wrap getSession function inside a self-invoking function
// (function() {
//     const getSession = () => {
//         fetch(BASE_URL + "/accounts/api/session/", {
//             credentials: CREDENTIALS,
//         })
//             .then((res) => res.json())
//             .then((data) => {
//                // console.log(data);
//                 if (data.isAuthenticated) {

//                 } else {

//                     getCSRF();
//                 }
//             })
//             .catch((err) => {
//                 //console.log(err);
//             });
//     }

//     getSession(); // Call getSession function when the JavaScript file is loaded
// })();

export class UNPetAxios {
    constructor(base_ruta = '') {
        this.BASE_URL = BASE_URL;
        this.BASE_URL_RUTA = BASE_URL + base_ruta;
        this.CREDENTIALS = CREDENTIALS;
        
    }
    init() {
    }

   
    async fetchWithHeaders(url, options = {}, moreHeaders) {
        //'url: ', url, 'options: ', options, 'moreHeaders: ', moreHeaders);
        let contenttype = moreHeaders ? moreHeaders["Content-Type"] : "application/json";
        
        const allOptions = {
            headers: {
                "Content-Type": contenttype,
               "X-CSRFToken": this.csrfToken,
            },
            withCredentials: true,
            credentials: 'include',
            ...options,
        };

        console.log('JUSTO ANTES DEL FETCH: fetchWithHeaders, allOptions: ', allOptions, 'URL: ', this.BASE_URL_RUTA + url);

        return axios(this.BASE_URL_RUTA + url, allOptions);
    }

    get(url, options = {}) {
        return this.fetchWithHeaders(url, options);
    }

    post(url, body = {}, options = {}, headers = {}) {
        //console.log('UNPETAXIOS, post, body: ', body, 'headers: ', headers);
        return this.fetchWithHeaders(url, {
            method: "post",
            data: body, // axios usa 'data' en lugar de 'body'
            ...options,
        }, headers);
    }

    put(url, body = {}, options = {}, headers = {}) {
        return this.fetchWithHeaders(url, {
            method: "put",
            data: body, // axios usa 'data' en lugar de 'body'
            ...options,
        }, headers);
    }

    delete(url, options = {}) {
        return this.fetchWithHeaders(url, {
            method: "delete",
            ...options,
        });
    }
}