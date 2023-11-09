
import { FaHome, FaHashtag, FaStar, FaCog, FaUserCircle } from 'react-icons/fa';
import { IconContext } from 'react-icons';

function LeftBar() {
    return (
        <div className="left-bar" style={{ height: "100%", width: '270px' }}>
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
                    <a href="#" className='py-2 px-3 flex items-center'>
                        <IconContext.Provider value={{ className: 'h-5 w-5 inline-block mr-2' }}>
                            <FaStar />
                        </IconContext.Provider>
                        Favoritos
                    </a>
                </li>
                <li className="text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-md py-2 px-5 flex items-center justify-start">
                    <a href="#" className='py-2 px-3 flex items-center'>
                        <IconContext.Provider value={{ className: 'h-5 w-5 inline-block mr-2' }}>
                            <FaCog />
                        </IconContext.Provider>
                        COnfiguración
                    </a>
                </li>
            </ul>
        </div>
    );
}

export default LeftBar;
