import { useState, useContext } from 'react';
import { UserContext } from '../../context/UserContext.jsx';
import logo from '/icons/android-chrome-192x192.png';
import userDefault from '/user-img-default.png';
import { LoginButton, RegisterButton, LogoutButton } from './NavButtons.jsx';
function NavBar() {
    const { user } = useContext(UserContext);
    console.log(user);
    const [isUserMenuOpen, setIsUserMenuOpen] = useState(false);

    const toggleUserMenu = () => {
        setIsUserMenuOpen(!isUserMenuOpen);
    };
    return (
        <nav className="bg-gray-800">
            <div className="max-w-7xl mx-auto px-2 sm:px-6 lg:px-8">
                <div className="relative flex items-center justify-between h-16">
                    <div className="absolute inset-y-0 left-0 flex items-center sm:hidden">
                        <button type="button" className="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white" aria-controls="mobile-menu" aria-expanded="false">
                            <span className="sr-only">Open main menu</span>
                            <svg className="block h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                            </svg>
                            <svg className="hidden h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                            </svg>
                        </button>
                    </div>
                    <div className="flex-1 flex items-center justify-center sm:items-stretch sm:justify-start">
                        <div className="flex-shrink-0 flex items-center">
                            <img className="block lg:hidden h-8 w-auto" src={logo} alt="UNPet logo" />
                            <img className="hidden lg:block h-8 w-auto" src={logo} alt="UNPet logo" />
                            <h1 className="text-white font-bold ml-2">UNPet</h1>
                        </div>
                        <div className="hidden sm:block sm:ml-6">
                            <div className="flex space-x-4">
                                <a href="#" className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Inicio</a>
                                <a href="#" className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Mascotas</a>
                                <a href="#" className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Contacto</a>
                            </div>
                        </div>
                    </div>



                    <div className="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">
                        <div className="ml-3 relative">
                            <div>
                                <button
                                    type="button"
                                    className="bg-gray-800 flex text-sm rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white"
                                    id="user-menu-button"
                                    aria-expanded={isUserMenuOpen}
                                    aria-haspopup="true"
                                    onClick={toggleUserMenu}
                                >
                                    <span className="sr-only">Open user menu</span>
                                    <img className="h-8 w-8 rounded-full" src={user.urlfoto} alt="" />
                                    {user.isAuthenticated && <h3 className="text-white font-bold ml-2">{user.username}</h3>}
                                </button>
                            </div>

                            {isUserMenuOpen && (
                                <div
                                    className="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg py-1 bg-white ring-1 ring-black ring-opacity-5"
                                    role="menu"
                                    aria-orientation="vertical"
                                    aria-labelledby="user-menu-button"
                                    tabIndex={-1}
                                >
                                    <a href="#" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem" tabIndex={-1} id="user-menu-item-0">
                                        Perfil
                                    </a>
                                    <a href="#" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem" tabIndex={-1} id="user-menu-item-1">
                                        Configuración
                                    </a>
                                    <a href="#" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem" tabIndex={-1} id="user-menu-item-2">
                                        Cerrar sesión
                                    </a>
                                </div>
                            )}
                        </div>
                    </div>


                </div>
            </div>


        </nav>
    );
}

export default NavBar;



