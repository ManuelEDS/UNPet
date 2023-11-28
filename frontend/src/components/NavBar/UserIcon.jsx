import { useState, useRef, useEffect } from 'react';
import { UserContext } from '../../context/UserContext';
import { useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { logout } from '../../api/accounts.api'
import { FaPaw } from 'react-icons/fa'
function UserIcon({ user: userdata }) {
    const navigate = useNavigate();
    const [isUserMenuOpen, setIsUserMenuOpen] = useState(false);
    const { user } = useContext(UserContext);
    const userMenuRef = useRef(null);

    const handleLogout = async () => {
        setIsUserMenuOpen(false);

        const response = await logout();

        if (response.isAuthenticated === false) {
            console.log('logout exitoso');
            window.location.reload(); // Refresh the page
        } else {
            console.log('error en logout:', response.data, response.data.error);
        }
    };
    
    const handleClickOutside = (event) => {
        if (userMenuRef.current && !userMenuRef.current.contains(event.target)) {
            setIsUserMenuOpen(false);
        }
    };

    useEffect(() => {
        document.addEventListener('mousedown', handleClickOutside);
        return () => {
            document.removeEventListener('mousedown', handleClickOutside);
        };
    }, []);

    return (


        <div className='mr-12'>
            
            

            <div className="flex-shrink-0 flex items-center relative">
            {user.isAuthenticated && <div className="font-bold text-white bg-green p-2 rounded-lg mr-3 "><p>{user.username}</p></div>}
                <button onClick={() => { setIsUserMenuOpen(!isUserMenuOpen); }} className="flex-shrink-0 flex items-center focus:outline-none" >
                    <img className="h-10 w-10 rounded-full" src={userdata.urlfoto} alt="user_photo" />
                </button>
                
            </div>
            {isUserMenuOpen && (
                <ul ref={userMenuRef} className="absolute right-0 mt-2 py-2 w-48 bg-white rounded-md shadow-lg">
                    
                    {user.isAuthenticated ?
                        <>
                            <li className="px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900 cursor-pointer" onClick={ handleLogout}>
                                Cerrar sesión
                            </li>
                            <li className="px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900 cursor-pointer" onClick={ ()=>{navigate('/user/'+ user.username)}}>
                                Mi perfil
                            </li>
                            {userdata.usertype == 'Organizacion' && <li className="px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900 cursor-pointer" onClick={() => { setIsUserMenuOpen(false); navigate('/create-post') }}>

                                <button
                                    type="button"
                                    className="group relative w-full flex justify-center py-2 px-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                                >
                                    <span className="absolute left-0 flex items-center pl-3">
                                        <FaPaw className="h-5 w-5 text-indigo-500 group-hover:text-indigo-400" aria-hidden="true" />
                                    </span>
                                    <p className="relative left-3">Crear publicación</p>
                                </button>

                            </li>}

                        </>

                        :

                        <>
                            <li className="px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900 cursor-pointer" onClick={() => { setIsUserMenuOpen(false); navigate('/login'); }}>
                                Iniciar sesión
                            </li>
                            <li className="px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900 cursor-pointer" onClick={() => { setIsUserMenuOpen(false); navigate('/register'); }}>
                                Registrarse
                            </li>
                            <li className="px-4 py-2 text-sm text-gray-700 hover:bg-gray-200 hover:text-gray-900 cursor-pointer " onClick={() => { setIsUserMenuOpen(false); navigate('/register-org'); }}>
                                Registrarse como organización
                            </li>
                        </>

                    }

                </ul>
            )}
        </div>


    );
}

export default UserIcon;



