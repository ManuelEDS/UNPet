
import { useState } from 'react';
import { register } from '../api/accounts.api'
import { Link } from 'react-router-dom'
// import { Fragment } from 'react';
import { FaCheckCircle, FaLock } from 'react-icons/fa';
import { localidades } from './RegisterOrg';

export function Register() {

  const [tipoDocumento, setTipoDocumento] = useState('');
  const [sexo, setSexo] = useState('');
  const [localidad, setLocalidad] = useState('');
  const [errorUsername, setErrorUsername] = useState('');
  const [errorEmail, setErrorEmail] = useState('');
  const [errorPassword, setErrorPassword] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const usernameRegex = /^[a-zA-Z0-9_]+$/;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$/;

    try {
      const resp = await register(data);
      navigate('/home');

    } catch (error) {
      setError(true);
      console.log('Login failed: ', error);
    }

  };

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
            <form className="space-y-6" action="#" method="POST">
              <input type="hidden" name="remember" value="true" />
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
                    Photo file
                  </label>
                  <input
                    id="photo_file"
                    name="photo_file"
                    type="file"
                    accept="image/*"
                    className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                  />
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
