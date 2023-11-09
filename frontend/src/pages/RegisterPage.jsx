
import  { useState } from 'react';
import {register} from '../api/accounts.api'
// import { Fragment } from 'react';
import { FaCheckCircle } from 'react-icons/fa';

const tiposDocumento = [
  { id: 'CC', nombre: 'Cédula de Ciudadanía (CC)' },
  { id: 'TI', nombre: 'Tarjeta de Identidad (TI)' },
  { id: 'CE', nombre: 'Cédula de Extranjería (CE)' },
  { id: 'Pasaporte', nombre: 'Pasaporte' },
  // Agrega más tipos de documento según sea necesario
];
const sexoOptions = [
  { id: 'M', nombre: 'Masculino' },
  { id: 'F', nombre: 'Femenino' },
  { id: 'O', nombre: 'Otro' },
];
export const localidades = [
  { id: '1', nombre: 'Usaquén' },
  { id: '2', nombre: 'Chapinero' },
  { id: '3', nombre: 'Santa Fe' },
  { id: '4', nombre: 'San Cristóbal' },
  { id: '5', nombre: 'Usme' },
  { id: '6', nombre: 'Tunjuelito' },
  { id: '7', nombre: 'Bosa' },
  { id: '8', nombre: 'Kennedy' },
  { id: '9', nombre: 'Fontibón' },
  { id: '10', nombre: 'Engativá' },
  { id: '11', nombre: 'Suba' },
  { id: '12', nombre: 'Barrios Unidos' },
  { id: '13', nombre: 'Teusaquillo' },
  { id: '14', nombre: 'Los Mártires' },
  { id: '15', nombre: 'Antonio Nariño' },
  { id: '16', nombre: 'Puente Aranda' },
  { id: '17', nombre: 'La Candelaria' },
  { id: '18', nombre: 'Rafael Uribe Uribe' },
  { id: '19', nombre: 'Ciudad Bolívar' },
  { id: '20', nombre: 'Sumapaz' },
  // Agrega más localidades según sea necesario
];

export function Register() {

  const [tipoDocumento, setTipoDocumento] = useState('');
  const [sexo, setSexo] = useState('');
  const [localidad, setLocalidad] = useState('');
  const [errorUsername, setErrorUsername] = useState('');
  const [errorEmail, setErrorEmail] = useState('');
  const [errorPassword, setErrorPassword] = useState('');

  const  handleSubmit = async (event) => {
    event.preventDefault();
    console.log('handlesubmit--->', event.currentTarget);
    const data = new FormData(event.currentTarget);
    const usernameRegex = /^[a-zA-Z0-9_]+$/;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    console.log('data', data);


    try {
      const resp = await register(data);
    //console.log(resp.data, resp);
    
      navigate('/home');
      
    } catch (error) {
      setError(true);
      console.log('Register failed: ', error);
    }
    
  };

    return (
      <div className="min-h-screen bg-gray-100 py-6 flex flex-col justify-center sm:py-12">
        <div className="relative py-3 sm:max-w-xl sm:mx-auto">
          <div className="absolute inset-0 bg-gradient-to-r from-cyan-400 to-light-blue-500 shadow-lg transform -skew-y-6 sm:skew-y-0 sm:-rotate-3 sm:rounded-3xl"></div>
          <div className="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl sm:p-20">
            <div className="max-w-md mx-auto">
              <div>
              <FaCheckCircle className="h-12 w-12 text-green-500 mx-auto" />
                <h1 className="text-2xl font-semibold text-gray-900 mt-6 text-center">Registrarse</h1>
              </div>
              <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
                <input type="hidden" name="remember" value="true" />
                <div className="rounded-md shadow-sm space-y-4">
                  <div>
                    <label htmlFor="first_name" className="sr-only">
                      Nombres
                    </label>
                    <input
                      id="first_name"
                      name="first_name"
                      type="text"
                      autoComplete="given-name"
                      required
                      className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-cyan-500 focus:border-cyan-500 focus:z-10 sm:text-sm"
                      placeholder="Nombres"
                    />
                    {errorUsername && <p>{errorUsername}</p>}
                  </div>
                  <div>
                    <label htmlFor="last_name" className="sr-only">
Apellidos                    </label>
                    <input
                      id="last_name"
                      name="last_name"
                      type="text"
                      autoComplete="family-name"
                      required
                      className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-cyan-500 focus:border-cyan-500 focus:z-10 sm:text-sm"
                      placeholder="Apellidos"
                    />
                    {errorUsername && <p>{errorUsername}</p>}
                  </div>
                  <div>
                    <label htmlFor="tipo_doc" className="sr-only">
                      Tipo de Documento
                    </label>
                    <select
                      id="tipo_doc"
                      name="tipo_doc"
                      autoComplete="tipo_doc"
                      required
                      className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-cyan-500 focus:border-cyan-500 focus:z-10 sm:text-sm"
                      value={tipoDocumento}
                      onChange={(e) => setTipoDocumento(e.target.value)}
                    >
                      {tiposDocumento.map((item) => (
                        <option key={item.id} value={item.id}>
                          {item.nombre}
                        </option>
                      ))}
                    </select>
                  </div>
                  <div>
                    <label htmlFor="n_doc" className="sr-only">
                      Número de documento
                    </label>
                    <input
                      id="n_doc"
                      name="n_doc"
                      type="text"
                      autoComplete="n_doc"
                      required
                      
                      className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-cyan-500 focus:border-cyan-500 focus:z-10 sm:text-sm"
                      placeholder="Número de documento"
                    />
                    {errorUsername && <p>{errorUsername}</p>}
                  </div>
                  <div>
                    <label htmlFor="sexo" className="sr-only">
                      Sexo
                    </label>
                    <select
                      id="sexo"
                      name="sexo"
                      autoComplete="sexo"
                      required
                      className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-cyan-500 focus:border-cyan-500 focus:z-10 sm:text-sm"
                      value={sexo}
                      onChange={(e) => setSexo(e.target.value)}
                    >
                      <option value="">Sexo</option>
                      {sexoOptions.map((option) => (
                        <option key={option.id} value={option.id}>
                          {option.nombre}
                        </option>
                      ))}
                    </select>
                  </div>
                  <div>
                    <label htmlFor="telefono" className="sr-only">
                      Teléfono
                    </label>
                    <input
                      id="telefono"
                      name="telefono"
                      type="text"
                      autoComplete="telefono"
                      required
                      className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-cyan-500 focus:border-cyan-500 focus:z-10 sm:text-sm"
                      placeholder="Teléfono"
                    />
                    {errorUsername && <p>{errorUsername}</p>}
                  </div>
                  <div>
                    <label htmlFor="idlocalidad" className="sr-only">
                      Localidad
                    </label>
                    <select
                      id="idlocalidad"
                      name="idlocalidad"
                      autoComplete="idlocalidad"
                      required
                      className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-cyan-500 focus:border-cyan-500 focus:z-10 sm:text-sm"
                      value={localidad}
                      onChange={(e) => setLocalidad(e.target.value)}
                    >
                      <option value="">Localidad</option>
                      {localidades.map((localidad) => (
                        <option key={localidad.id} value={localidad.id}>
                          {localidad.nombre}
                        </option>
                      ))}
                    </select>
                  </div>
                  <div>
                    <label htmlFor="photo_file" className="sr-only">
                      Photo file
                    </label>
                    <input
                      id="photo_file"
                      name="photo_file"
                      type="file"
                      accept="image/*"
                      className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-cyan-500 focus:border-cyan-500 focus:z-10 sm:text-sm"
                    />
                    {errorUsername && <p>{errorUsername}</p>}
                  </div>
                  <div>
                    <label htmlFor="email" className="sr-only">
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
                    {errorUsername && <p>{errorUsername}</p>}
                  </div>
                  <div>
                    <label htmlFor="username" className="sr-only">
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
                    {errorUsername && <p>{errorUsername}</p>}
                  </div>
                  <div>
                    <label htmlFor="password" className="sr-only">
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

                

                <div className="flex items-center">
                <input
                  id="terms"
                  name="terms"
                  type="checkbox"
                  required
                  className="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
                />
                {errorUsername && <p>{errorUsername}</p>}
                <label htmlFor="terms" className="ml-2 block text-sm text-gray-900">
                  Estoy de acuerdo con los{' '}
                  <a href="/legal/terms-and-conditions" className="font-medium text-indigo-600 hover:text-indigo-500">
                    términos y condiciones
                  </a>{' '}
                  del servicio
                </label>
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
            </div>
          </div>
        </div>
      </div>
    );
  }

  export default Register;
