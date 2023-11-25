// eslint-disable-next-line no-unused-vars
import { Link } from 'react-router-dom'
import { useNavigate } from "react-router-dom";
import { useState, useContext, useEffect } from 'react';
import {UserContext} from '../context/UserContext'
import { login } from '../api/accounts.api';
import { FaLock } from 'react-icons/fa';
import {getProfile, updateProfile} from '../api/accounts.api'
export function Profile() {
    const { user } = useContext(UserContext);
    const [profile, setProfile] = useState(null);
    const navigate = useNavigate();

    const [error, setError] = useState(false);
    useEffect(() => {
        const fetchProfile = async () => {
            try {
                console.log('peticion a : ', 'get profile ');
                const data = await getProfile()
                setProfile(data)
                console.log('data: ', data);
                
            } catch (error) {
                console.error('Error fetching user:', error);
            }
        };
        fetchProfile();
        
        
    }, [profile, user]);

    const handleSubmit = async (event) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);
        console.log({
            userID: data.get('userID'),
            password: data.get('password'),
        });
        try {
            const resp = await updateProfile(data);
            console.log('profile update successful, status: ', resp.status);

        } catch (error) {
            setError(true);
            console.log('profile update failed: ', error);
        }
    };

    return (
        
        <div className="max-h-screen bg-gray-50 flex flex-col justify-center py-36 sm:px-6 lg:px-8 h-full">
            <div className="sm:mx-auto sm:w-full sm:max-w-md">
                <img
                    className="mx-auto h-40 w-auto"
                    src={user.urlfoto}
                    alt={user.username}
                />
                <h3 className="mt-4 text-center text-2xl font-extrabold text-gray-900">
                    {user.username}
                </h3>
            </div>
            <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
                <div className="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
                    <form className="space-y-6" onSubmit={handleSubmit}>
                        <div>
                            <label
                                htmlFor="email"
                                className="block text-sm font-medium text-gray-700"
                            >
                                NIT
                            </label>
                            <div className="mt-1">
                                <input
                                    id="NIT"
                                    name="userID"
                                    type="text"
                                    autoComplete="username email"
                                    value="4567992-3"
                                    disabled="True"
                                    required
                                    className={`appearance-none rounded-md relative block w-full px-3 py-2 border ${error ? 'border-red-300' : 'border-gray-300'
                                        } placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm`}
                                />
                            </div>
                            <label
                                htmlFor="email"
                                className="block text-sm font-medium text-gray-700"
                            >
                                Dirección
                            </label>
                            <div className="mt-1">
                                <input
                                    id="NIT"
                                    name="userID"
                                    type="text"
                                    autoComplete="username email"
                                    value="Calle 76 #27-24"
                                    required
                                    className={`appearance-none rounded-md relative block w-full px-3 py-2 border ${error ? 'border-red-300' : 'border-gray-300'
                                        } placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm`}
                                />
                            </div>
                            <label
                                htmlFor="email"
                                className="block text-sm font-medium text-gray-700"
                            >
                                Localidad
                            </label>
                            <div className="mt-1">
                                <input
                                    id="NIT"
                                    name="userID"
                                    type="text"
                                    autoComplete="username email"
                                    value="Barrios Unidos"
                                    required
                                    className={`appearance-none rounded-md relative block w-full px-3 py-2 border ${error ? 'border-red-300' : 'border-gray-300'
                                        } placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm`}
                                />
                            </div>
                            <label
                                htmlFor="email"
                                className="block text-sm font-medium text-gray-700"
                            >
                                Correo Electrónico
                            </label>
                            <div className="mt-1">
                                <input
                                    id="NIT"
                                    name="userID"
                                    type="text"
                                    autoComplete="username email"
                                    value="adopcionescab@gmail.com"
                                    disabled="True"
                                    required
                                    className={`appearance-none rounded-md relative block w-full px-3 py-2 border ${error ? 'border-red-300' : 'border-gray-300'
                                        } placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm`}
                                />
                            </div>
                            <label
                                htmlFor="email"
                                className="block text-sm font-medium text-gray-700"
                            >
                                Teléfono
                            </label>
                            <div className="mt-1">
                                <input
                                    id="NIT"
                                    name="userID"
                                    type="text"
                                    autoComplete="username email"
                                    value="601 4340321"
                                    required
                                    className={`appearance-none rounded-md relative block w-full px-3 py-2 border ${error ? 'border-red-300' : 'border-gray-300'
                                        } placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm`}
                                />
                            </div>

                            {error && (
                                <p className="mt-2 text-sm text-red-600">
                                    Información incorrecta
                                </p>
                            )}
                        </div>

                        <div>
                            <label
                                htmlFor="password"
                                className="block text-sm font-medium text-gray-700"
                            >
                                Contraseña
                            </label>
                            <div className="mt-1">
                                <input
                                    id="password"
                                    name="password"
                                    type="password"
                                    autoComplete="current-password"
                                    value="******************"
                                    disabled="True"
                                    required
                                    className={`appearance-none rounded-md relative block w-full px-3 py-2 border ${error ? 'border-red-300' : 'border-gray-300'
                                        } placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm`}
                                />
                            </div>
                            {error && (
                                <p className="mt-2 text-sm text-red-600">
                                    Información incorrecta
                                </p>
                            )}
                        </div>
                        <div>
                            <button
                                type="submit"
                                className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                            >
                                <span className="absolute left-0 inset-y-0 flex items-center pl-3">
                                    <FaLock className="h-5 w-5 text-indigo-500 group-hover:text-indigo-400" aria-hidden="true" />

                                </span>
                                Modificar
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
}
