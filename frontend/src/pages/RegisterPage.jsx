
import { useState } from 'react';
import { register } from '../api/accounts.api'
import { Link, useNavigate } from 'react-router-dom'
// import { Fragment } from 'react';
import { FaCheckCircle, FaLock } from 'react-icons/fa';
import { localidades } from './RegisterOrg';
import { UserContext } from '../context/UserContext';
import { useContext, useEffect } from 'react';


export function Register() {
  const { user } = useContext(UserContext);
  const navigate = useNavigate();
  const [localidad, setLocalidad] = useState('');
  const [errorUsername, setErrorUsername] = useState('');
  const [error, setError] = useState(false);
  const [errorTerms, setErrorTerms] = useState(false);
  const [errorEmail, setErrorEmail] = useState('');
  const [errorPassword, setErrorPassword] = useState('');
  const [errorID, setErrorID] = useState(false);
  const {errorPhone, setErrorPhone} = useState(false);
  const [errorFile, setErrorFile] = useState(false);
  const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const regexUsername = /^(?!.*\.\.)(?!.*\.$)[a-zA-Z0-9][\w.]{0,29}$/
  const regexPassword = /^(?=.*[0-9])(?=.*[a-zA-Z])[0-9a-zA-Z]{8,}$/;
  const regexID = /^[a-zA-Z0-9]{8,10}$/;
  const regexPhone = /^[0-9]{7,10}$/;
  // Función para verificar la contraseña
  const checkPassword = (contraseña) => {
    return regexPassword.test(contraseña);
  };

  // Función para verificar el formato del correo electrónico
  const checkEmail = (correo) => {
    return regexEmail.test(correo);
  };
  const checkUsername = (username) => {
    return regexUsername.test(username);
  }
  // Función para verificar el número de teléfono
  const checkPhone = (phone) => {
    return regexPhone.test(phone);
  };

  // Función para verificar el formato del ID
  const checkID = (id) => {
    return regexID.test(id);
  };
  const checkFile = (file) => {
    if (file && file.type.includes('image')) {
      return true;
    }
    return false;
  }
  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    console.log('este es el form data', Object.fromEntries(data));
    const termsIsChecked = data.get('terms');
    const imgFile = data.get('photo_file');
    console.log('este es el img file', imgFile);
    if (!termsIsChecked) {
      setErrorTerms(true);
      return;
    }
    // if(!checkEmail(data.get('email'))) {
    //   setErrorEmail(true);
    //   return;
    // }
    // if(!checkUsername(data.get('username'))) {
    //   setErrorUsername(true);
    //   return;
    // }
    // if(!checkPassword(data.get('password'))) {
    //   setErrorPassword(true);
    //   return;
    // }
    // if(!checkID(data.get('n_doc'))) {
    //   setErrorID(true);
    //   return;
    // }
    // if(!checkPhone(data.get('telefono'))) {
    //   setErrorPhone(true);
    //   return;
    // }
    // if(!checkFile(imgFile)) {
    //   setErrorFile(true);
    //   return;
    // }
    try {
      const resp = await register(data);
      user.checkAuth() // Refresh the page
      navigate('/home');
    } catch (error) {
      setError(true);
      console.log('Login failed: ', error);
    }
  };
  useEffect(() => {
    if(user.isAuthenticated){
      navigate('/home');
    }
}, []);

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
      <div className="sm:mx-auto sm:w-full sm:max-w-md">
        <div className="text-center"></div>
        <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
          <div className="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
            <div>
              <FaCheckCircle className="h-12 w-12 text-green-500 mx-auto" />
              <h1 className="text-2xl font-semibold text-gray-900 mt-6 text-center">Registrarse</h1>
            </div>
            
            <form className="space-y-6" method="POST" encType="multipart/form-data" onSubmit={handleSubmit}>

              <div className="rounded-md shadow-sm -space-y-px">
                <div>
                  <label htmlFor="first_name" className="block text-sm font-medium text-gray-700 py-2 py-2">
                    Nombres
                  </label>
                  <input
                    id="first_name"
                    name="first_name"
                    type="text"
                    autoComplete="given-name"
                    required
                    className="ppearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    placeholder="Nombres"
                  />
                </div>
                <div>
                  <label htmlFor="last_name" className="block text-sm font-medium text-gray-700 py-2">
                    Apellidos                    </label>
                  <input
                    id="last_name"
                    name="last_name"
                    type="text"
                    autoComplete="family-name"
                    required
                    className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    placeholder="Apellidos"
                  />
                </div>
                <div>
                  <label htmlFor="tipo_doc" className="block text-sm font-medium text-gray-700 py-2">
                    Tipo de Documento
                  </label>
                  <select
                    id="tipo_doc"
                    name="tipo_doc"
                    autoComplete="tipo_doc"
                    required
                    className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                  >
                    <option value="">Tipo de Documento</option>
                    <option value="1">Cédula de ciudadanía</option>
                    <option value="2">Cédula de extranjería</option>
                    <option value="3">Pasaporte</option>
                  </select>
                </div>
                <div>
                  <label htmlFor="n_doc" className="block text-sm font-medium text-gray-700 py-2">
                    Número de documento
                  </label>
                  <input
                    id="n_doc"
                    name="n_doc"
                    type="text"
                    autoComplete="n_doc"
                    required
                    className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    placeholder="Número de documento"
                  />
                  {errorID && <p className="mt-2 text-sm text-red-600">
                  El numero de documento no es válido</p>
                  }
                </div>
                <div>
                  <label htmlFor="sexo" className="block text-sm font-medium text-gray-700 py-2">
                    Sexo
                  </label>
                  <select
                    id="sexo"
                    name="sexo"
                    autoComplete="sexo"
                    required
                    className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                  >
                    <option value="">Sexo</option>
                    <option value="M">Masculino</option>
                    <option value="F">Femenino</option>
                    <option value="O">No binario</option>
                  </select>
                </div>
                <div>
                  <label htmlFor="telefono" className="block text-sm font-medium text-gray-700 py-2">
                    Teléfono
                  </label>
                  <input
                    id="telefono"
                    name="telefono"
                    type="text"
                    autoComplete="telefono"
                    required
                    className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    placeholder="Teléfono"
                  />
                  {errorPhone &&
                  
                  <p className="mt-2 text-sm text-red-600">
                  El numero de telefono no es válido</p>
                  }
                </div>
                <div>
                <label htmlFor="idlocalidad" className="block text-sm font-medium text-gray-700">
                  Localidad
                </label>
                <div className="mt-1">
                  <select
                    id="idlocalidad"
                    name="idlocalidad"
                    autoComplete="family-name"
                    required
                    className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                    value={localidad}
                    onChange={(e) => setLocalidad(e.target.value)}
                  >
                    <option value="">Seleccione una localidad</option>
                    {localidades.map((loc) => (
                      <option key={'k-loc' + loc.id} value={loc.id}>
                        {loc.name}
                      </option>
                    ))}
                  </select>
                </div>
              </div>
                <div>
                  <label htmlFor="photo_file" className="block text-sm font-medium text-gray-700 py-2">
                    Foto de perfil
                  </label>
                  <input
                    id="photo_file"
                    name="photo_file"
                    type="file"
                    accept="image/*"
                    className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                  />
                  {errorFile &&
                  
                  <p className="mt-2 text-sm text-red-600">
                  El archivo no es de tipo imagen</p>
                  }
                </div>
                <div>
                  <label htmlFor="email" className="block text-sm font-medium text-gray-700 py-2">
                    Correo electrónico
                  </label>
                  <input
                    id="email"
                    name="email"
                    type="email"
                    autoComplete="email"
                    required
                    className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-cyan-500 focus:border-cyan-500 focus:z-10 sm:text-sm"
                    placeholder="Correo electrónico"
                  />
                  {errorEmail &&
                  
                  <p className="mt-2 text-sm text-red-600">
                  El coreo electrónico no es válido</p>
                  }
                </div>
                <div>
                  <label htmlFor="username" className="block text-sm font-medium text-gray-700 py-2">
                    Nombre de usuario
                  </label>
                  <input
                    id="username"
                    name="username"
                    type="text"
                    autoComplete="username"
                    required
                    className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-cyan-500 focus:border-cyan-500 focus:z-10 sm:text-sm"
                    placeholder="Nombre de usuario"
                  />
                  
                  {errorUsername &&
                  
                  <p className="mt-2 text-sm text-red-600">
                  El username no es válido</p>
                  }
                </div>
                <div>
                  <label htmlFor="password" className="block text-sm font-medium text-gray-700 py-2">
                    Contraseña
                  </label>
                  <input
                    id="password"
                    name="password"
                    type="password"
                    autoComplete="current-password"
                    required
                    className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-cyan-500 focus:border-cyan-500 focus:z-10 sm:text-sm"
                    placeholder="Contraseña"
                  />
                  {errorPassword &&
                  
                  <p className="mt-2 text-sm text-red-600">
                  La contraseña debe ser de almenos 8 caracteres, con numeros y letras</p>
                  }
                </div>
              </div>

              <div className="flex items-center justify-between">
                <div className="flex items-center">
                  <input
                    id="terms"
                    name="terms"
                    type="checkbox"
                    className="h-4 w-4 text-cyan-600 focus:ring-cyan-500 border-gray-300 rounded"
                  />
                  <label htmlFor="terms" className="ml-2 block text-sm text-gray-900">
                    Estoy de acuerdo con los <Link
                      to="/legal/terms-and-conditions"
                      className="font-medium text-indigo-600 hover:text-indigo-500"
                    >
                      términos y condiciones del servicio
                    </Link>
                  </label>
                  {errorTerms &&
                  
                  <p className="mt-2 text-sm text-red-600">
                  Debes aceptar los terminos y condiciones</p>
                  }
                </div>
              </div>

              <div>
                <button
                  type="submit"
                  className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                >
                  <span className="absolute left-0 inset-y-0 flex items-center pl-3">
                    <FaCheckCircle className="h-5 w-5 text-indigo-500 group-hover:text-indigo-400" aria-hidden="true" />
                  </span>
                  Registrarse
                </button>
              </div>
              <div className="mt-6">
                <div className="relative">
                  <div className="absolute inset-0 flex items-center" aria-hidden="true">
                    <div className="w-full border-t border-gray-300" />
                  </div>
                  <div className="relative flex justify-center text-sm">
                    <span className="px-2 bg-white text-gray-500">¿Ya tienes una cuenta?</span>
                  </div>
                </div>
                <div className="mt-3">
                  <Link
                    to="/login"
                    className="group relative w-full flex justify-center py-2 px-4 border border-gray-300 text-sm font-medium rounded-md text-gray-700 py-2 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                  >
                    <span className="absolute left-0 inset-y-0 flex items-center pl-3">
                      <FaLock className="h-5 w-5 text-gray-500 group-hover:text-gray-400" aria-hidden="true" />
                    </span>
                    Ingresa
                  </Link>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Register;
