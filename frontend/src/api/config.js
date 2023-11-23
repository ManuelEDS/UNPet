import axios from "axios";



//===============================================//
// --> SOLO UNA PUEDE SER TRUE <-- //
export const DEBUG = true;
export const DOCKER_MODE = false;
export const RENDER_MODE = false;
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
        console.log('ERROR, EL HOST ES:' + testURL, error);
      }
    }
}



/**
 * La URL base del host.
 * @type {string}
 */
export const BASE_URL = URL;
export const CREDENTIALS = 'include';

let csrfToken;

fetch(BASE_URL + "/accounts/api/csrf/")
  .then(response => response.json())
  .then(data => {
    csrfToken = data.csrfToken;
    console.log('CSRF TOKEN real: ', csrfToken);
  })
  .catch(error => {
    console.error('Error al obtener el token CSRF:', error);
  });

export class UNPetAxios {
  constructor(base_ruta='') {
    this.BASE_URL = BASE_URL
    this.BASE_URL_RUTA = BASE_URL + base_ruta
    this.CREDENTIALS = CREDENTIALS
    this.init()
  }

  async init() {
    this.csrfToken = csrfToken
  }

  async getCSRFToken() {
    const response = await fetch(this.BASE_URL + "/accounts/api/csrf/", { credentials: this.CREDENTIALS });
    const csrfToken = response.headers.get("X-CSRFToken");
    console.log('CSRF TOKEN: ', csrfToken);
    return csrfToken;
  }


  fetchWithHeaders(url, options = {}) {
    const allOptions = {
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": this.csrfToken,
      },
      credentials: this.CREDENTIALS,
      ...options,
    };
    return fetch(this.BASE_URL_RUTA + url, allOptions);
  }

  get(url, options = {}) {
    return this.fetchWithHeaders(url, options);
  }

  post(url, body = {}, options = {}) {
    return this.fetchWithHeaders(url, {
      method: "POST",
      body: JSON.stringify(body),
      ...options,
    });
  }

  put(url, body = {}, options = {}) {
    return this.fetchWithHeaders(url, {
      method: "PUT",
      body: JSON.stringify(body),
      ...options,
    });
  }

  delete(url, options = {}) {
    return this.fetchWithHeaders(url, {
      method: "DELETE",
      ...options,
    });
  }
}
