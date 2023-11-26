
import { FaHome, FaHashtag, FaQuestion, FaCog, FaUserCircle, FaChevronRight, FaChevronDown, FaExclamation, FaAddressBook  } from 'react-icons/fa';
import { VscLaw } from 'react-icons/vsc';
import { IconContext } from 'react-icons';
import { useNavigate } from 'react-router-dom';
import { UserContext } from '../context/UserContext';
import { useContext, useState } from 'react';

function LeftBar() {
    const navigate = useNavigate();
    const { user } = useContext(UserContext);
    const [showSubItems, setShowSubItems] = useState(false);

    const handleItemClick = () => {
        setShowSubItems(!showSubItems);
    };
    return (
        <div className="left-bar sticky top-0" style={{ height: "100%", width: '270px' }}>
            <ul className="space-y-5 py-5 pt-10" style={{ display: 'flex', flexDirection: 'column' }}>
                <li className="text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-md py-2 px-5 flex items-center justify-start">
                    <a href="#" className='py-2 px-3 flex items-center'>
                        <IconContext.Provider value={{ className: 'h-5 w-5 inline-block mr-2' }}>
                            <FaHome />
                        </IconContext.Provider>
                        Inicio
                    </a>
                </li>
                <li className="text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-md py-2 px-5 flex items-center justify-start">
                    <a href="#" className='py-2 px-3 flex items-center'>
                        <IconContext.Provider value={{ className: 'h-5 w-5 inline-block mr-2' }}>
                            <FaHashtag />
                        </IconContext.Provider>
                        Tendencias
                    </a>
                </li>

                <li className="text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-md py-2 px-5 flex items-center justify-start">
                    <button className='py-2 px-3 flex items-center' onClick={() => { user.isAuthenticated ? navigate('/profile') : navigate('/login') }}>
                        <IconContext.Provider value={{ className: 'h-5 w-5 inline-block mr-2' }}>
                            <FaCog />
                        </IconContext.Provider>
                        Mi perfil
                    </button>
                </li>
                <li className="text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-md py-2 px-5 flex items-center justify-start">
                    <a href="#" className='py-2 px-3 flex items-center' onClick={handleItemClick}>
                        <IconContext.Provider value={{ className: 'h-5 w-5 inline-block mr-2' }}>
                            <FaExclamation />
                        </IconContext.Provider>
                        Ayuda
                        <IconContext.Provider value={{ className: 'h-5 w-5 inline-block ml-2' }}>
                            {showSubItems ? <FaChevronDown /> : <FaChevronRight />}
                        </IconContext.Provider>
                    </a>

                </li>
                {showSubItems && (
                    <ul className="pt-0 mt-0" style={{ display: 'flex', flexDirection: 'column' }}>
                        <li className="text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-md py-2 px-5 flex items-center justify-start">
                            <a href="/quienes-somos" className='py-2 px-3 flex items-center'>
                                <IconContext.Provider value={{ className: 'h-5 w-5 inline-block mr-2' }}>
                                    <FaUserCircle />
                                </IconContext.Provider>
                                Sobre nosotros
                            </a>
                        </li>
                        <li className="text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-md py-2 px-5 flex items-center justify-start">
                            <a href="/legal/terms-and-conditions" className='py-2 px-3 flex items-center'>
                                <IconContext.Provider value={{ className: 'h-5 w-5 inline-block mr-2' }}>
                                    <VscLaw />
                                </IconContext.Provider>
                                Términos del servicio
                            </a>
                        </li>
                        <li className="text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-md py-2 px-5 flex items-center justify-start">
                            <a href="/legal/privacy-policies" className='py-2 px-3 flex items-center'>
                                <IconContext.Provider value={{ className: 'h-5 w-5 inline-block mr-2' }}>
                                    <FaAddressBook />
                                </IconContext.Provider>
                                Políticas de privacidad
                            </a>
                        </li>
                        <li className="text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-md py-2 px-5 flex items-center justify-start">
                            <a href="/legal/faq" className='py-2 px-3 flex items-center'>
                                <IconContext.Provider value={{ className: 'h-5 w-5 inline-block mr-2' }}>
                                    <FaQuestion />
                                </IconContext.Provider>
                                Preguntas frecuentes
                            </a>
                        </li>
                      
                    </ul>
                )}
            </ul>
        </div >
    );
}

export default LeftBar;
