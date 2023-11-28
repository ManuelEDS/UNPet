import { useState, useContext, useEffect } from 'react';
import { UserContext } from '../context/UserContext';
import { Link } from 'react-router-dom';
import { FaCheckCircle, FaLock } from 'react-icons/fa';
import { orgRegister } from '../api/accounts.api'
import { useNavigate } from "react-router-dom"


export const localidades = [
  { id: '1', name: 'Usaquén' },
  { id: '2', name: 'Chapinero' },
  { id: '3', name: 'Santa Fe' },
  { id: '4', name: 'San Cristóbal' },
  { id: '5', name: 'Usme' },
  { id: '6', name: 'Tunjuelito' },
  { id: '7', name: 'Bosa' },
  { id: '8', name: 'Kennedy' },
  { id: '9', name: 'Fontibón' },
  { id: '10', name: 'Engativá' },
  { id: '11', name: 'Suba' },
  { id: '12', name: 'Barrios Unidos' },
  { id: '13', name: 'Teusaquillo' },
  { id: '14', name: 'Los Mártires' },
  { id: '15', name: 'Antonio Nariño' },
  { id: '16', name: 'Puente Aranda' },
  { id: '17', name: 'La Candelaria' },
  { id: '18', name: 'Rafael Uribe Uribe' },
  { id: '19', name: 'Ciudad Bolívar' },
  { id: '20', name: 'Sumapaz' },
  // Agrega más localidades según sea necesario
];

export function RegisterOrg() {
  const navigate = useNavigate();
  const [localidad, setLocalidad] = useState('');
  const { user } = useContext(UserContext);
  const [nitError, setNitError] = useState(false);
  const [errorPassword, setErrorPassword] = useState('');
  const [errorEmail, setErrorEmail] = useState('');
  const [errorTerms, setErrorTerms] = useState(false);
  const [errorFile, setErrorFile] = useState(false);
  const { errorPhone, setErrorPhone } = useState(false);
  const [errorUsername, setErrorUsername] = useState('');
  const [loading, setLoading] = useState(false);

  const regexNIT = /^[0-9]{8,11}-[0-9]{1}$/;
  const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
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

  const checkNIT = (nit) => {
    return regexNIT.test(nit);
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
    // if (!checkNIT(data.get('nit'))) {
    //   setNitError(true)
    //   return;
    // }
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
      setLoading(true);
      const resp = await orgRegister(data);
      user.checkAuth() // Refresh the page
      navigate('/home');
      setLoading(false);

    } catch (error) {
      setError(true);
      console.log('register org failed: ', error);
    }
  };
  useEffect(() => {
    if (user.isAuthenticated) {
      navigate('/home');
    }
  }, []);
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
      {loading && <div className="fixed top-0 left-0 z-50 w-screen h-screen flex items-center justify-center bg-black bg-opacity-50">
        <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-white"></div>
      </div>}
      <div className="sm:mx-auto sm:w-full sm:max-w-md">
        <div className="text-center">
          <FaLock className="mx-auto h-12 w-auto text-indigo-600" />
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Registrarse como organización
          </h2>
          <p className="mt-2 text-center text-sm text-gray-600">
            O{' '}
            <Link
              to="/register"
              className="font-medium text-indigo-600 hover:text-indigo-500"
            >
              regístrate como adoptante
            </Link>
          </p>
        </div>
        <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
          <div className="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
            <form className="space-y-6" method="POST" encType="multipart/form-data" onSubmit={handleSubmit}>
              <div>
                <label htmlFor="name" className="block text-sm font-medium text-gray-700">
                  Nombre de la organización
                </label>
                <div className="mt-1">
                  <input
                    id="name"
                    name="name"
                    type="text"
                    autoComplete="given-name"
                    placeholder="Nombre de la organización"
                    required
                    className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                  />
                </div>
              </div>

              <div>
                <label htmlFor="nit" className="block text-sm font-medium text-gray-700">
                  NIT
                </label>
                <div className="mt-1">
                  <input
                    id="nit"
                    name="nit"
                    type="number"
                    placeholder="NIT"
                    min="11111111"
                    max="99999999999"
                    pattern="[0-9]+@[-]+[0-9]$"
                    required
                    className={`appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm`}
                  />

                </div>
                {nitError &&

                  <p className="mt-2 text-sm text-red-600">
                    El formato para NIT son de 8 a 10 numeros, seguido de un guión para finalizar con un numero</p>
                }
              </div>

              <div>
                <label htmlFor="telefono" className="block text-sm font-medium text-gray-700">
                  Teléfono
                </label>
                <div className="mt-1">
                  <input
                    id="telefono"
                    name="telefono"
                    type="number"
                    autoComplete="family-name"
                    placeholder="Teléfono"
                    min="1111111111"
                    max="3311111111"
                    required
                    className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                  />
                </div>
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
                <label htmlFor="email" className="block text-sm font-medium text-gray-700">
                  Correo electrónico
                </label>
                <div className="mt-1">
                  <input
                    id="email"
                    name="email"
                    type="email"
                    autoComplete="email"
                    placeholder="organizacion@mail.com"
                    pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"
                    required
                    className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                  />
                </div>
                {errorEmail &&

                  <p className="mt-2 text-sm text-red-600">
                    El coreo electrónico no es válido</p>
                }
              </div>
              <div>
                <label htmlFor="username" className="block text-sm font-medium text-gray-700 py-2">
                  Username de la Organización
                </label>
                <input
                  id="username"
                  name="username"
                  type="text"
                  autoComplete="username"
                  minLength="6"
                  maxLength="16"
                  required
                  className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-cyan-500 focus:border-cyan-500 focus:z-10 sm:text-sm"
                  placeholder=" Username de la Organizacion"
                />
                {errorUsername &&

                  <p className="mt-2 text-sm text-red-600">
                    El username no es válido, debe tener mínimo 5 caracteres, máximo 16</p>
                }
              </div>
              <div>
                <label htmlFor="password" className="block text-sm font-medium text-gray-700">
                  Contraseña
                </label>
                <div className="mt-1">
                  <input
                    id="password"
                    name="password"
                    type="password"
                    autoComplete="new-password"
                    minLength="8"
                    maxLength="16"
                    required
                    className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                  />
                </div>
                {errorPassword &&

                  <p className="mt-2 text-sm text-red-600">
                    La contraseña debe ser de almenos 8 caracteres, máximo 16</p>
                }
              </div>

              <div className="flex items-center">
                <input
                  id="terms"
                  name="terms"
                  type="checkbox"

                  className="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
                />
                <label htmlFor="terms" className="ml-2 block text-sm text-gray-900">
                  Estoy de acuerdo con los{' '}
                  <Link to="/legal/terms-and-conditions" className="font-medium text-indigo-600 hover:text-indigo-500">
                    términos y condiciones
                  </Link>{' '}
                  del servicio
                </label>
                {errorTerms &&

                  <p className="mt-2 text-sm text-red-600">
                    Debes aceptar los terminos y condiciones</p>
                }
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
            </form>
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
                  className="group relative w-full flex justify-center py-2 px-4 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                >
                  <span className="absolute left-0 inset-y-0 flex items-center pl-3">
                    <FaLock className="h-5 w-5 text-gray-500 group-hover:text-gray-400" aria-hidden="true" />
                  </span>
                  Ingresa
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );

}
