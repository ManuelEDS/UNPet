// eslint-disable-next-line no-unused-vars
import { Link } from 'react-router-dom'
import { useNavigate } from "react-router-dom";
import { useState } from 'react';
import { createPost } from '../api/posts.api';
import { FaPaw } from 'react-icons/fa';

export function CreatePost() {
    const navigate = useNavigate();
    const [error, setError] = useState(false);
    const [file, setFile] = useState();
    const handleSubmit = async (event) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);
        
        try {
            const resp = await createPost(data);
            console.log('Login successful: ', resp);
            navigate('/home');

        } catch (error) {
            setError(true);
            console.log('Login failed: ', error);
        }
    };
    return (
        <div className="max-h-screen bg-gray-50 flex flex-col justify-left py-36 sm:px-6 lg:px-8 h-full">
            <div className="sm:mx-auto sm:w-full sm:max-w-md">
                <FaPaw className="mx-auto h-12 w-auto" />
                <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
                    Crea una post
                </h2>
                <p className="mt-2 text-center text-sm text-gray-600">
                    Recuerda nuestros{' '}
                    <Link
                        to="/legal/terms-and-conditions"
                        className="font-medium text-indigo-600 hover:text-indigo-500"
                    >
                        Términos del servicio
                    </Link>
                </p>
            </div>
            <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
                <div className="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
                    <form className="space-y-6" onSubmit={handleSubmit}>
                        <div>
                            <label
                                htmlFor="email"
                                className="block text-sm font-medium text-gray-700">
                                Título de tu publicación
                            </label>
                            <div className="mt-1">
                                <input
                                    id="title"
                                    name="title"
                                    type="text"
                                    placeholder='Título de tu publicación'
                                    autoComplete="username email"
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
                                Descripción
                            </label>
                            <div className="mt-1">
                                <textarea
                                    id="description"
                                    name="description"
                                    type="long-text"
                                    placeholder='Cuéntanos sobre la oportunidad que vas a brindar'
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
                                    <FaPaw className="h-5 w-5 text-indigo-500 group-hover:text-indigo-400" aria-hidden="true" />
                                </span>
                                Crear Post
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
}