
import { FaHome, FaHashtag, FaStar, FaCog } from 'react-icons/fa';
import { IconContext } from 'react-icons';

function LeftBar() {
    return (
        <div className="left-bar">
            <ul className="space-y-2">
                <li className="text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-md py-2 px-4">
                    <IconContext.Provider value={{ className: 'h-5 w-5 inline-block mr-2' }}>
                        <FaHome />
                    </IconContext.Provider>
                    Home
                </li>
                <li className="text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-md py-2 px-4">
                    <IconContext.Provider value={{ className: 'h-5 w-5 inline-block mr-2' }}>
                        <FaHashtag />
                    </IconContext.Provider>
                    Trends
                </li>
                <li className="text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-md py-2 px-4">
                    <IconContext.Provider value={{ className: 'h-5 w-5 inline-block mr-2' }}>
                        <FaStar />
                    </IconContext.Provider>
                    Favorites
                </li>
                <li className="text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-md py-2 px-4">
                    <IconContext.Provider value={{ className: 'h-5 w-5 inline-block mr-2' }}>
                        <FaCog />
                    </IconContext.Provider>
                    Config
                </li>
            </ul>
            <div className="user-section flex items-center space-x-2 mt-4">
                <IconContext.Provider value={{ className: 'h-8 w-8 text-gray-600' }}>
                    <div>
                        <FaUserCircle />
                    </div>
                </IconContext.Provider>
                <span className="text-gray-600 font-medium">User Name</span>
            </div>
        </div>
    );
}

export default LeftBar;
