import { FaFacebook, FaInstagram, FaGithub } from 'react-icons/fa';
import { MdEmail } from 'react-icons/md';

const DevCard = ({ name, skills, photo, fb = '#', mail = '#', inst = '#', gh = '#' }) => {
    return (
        <div className="max-w-sm rounded overflow-hidden shadow-lg">
            <img className="w-full" src={photo} alt={name} />
            <div className="px-6 py-4">
                <div className="font-bold text-xl mb-2">{name}</div>
                <p className="text-gray-700 text-base">{skills}</p>
            </div>
            <div className="px-6 pt-4 pb-2">
                <a href={fb} target="_blank" rel="noopener" className="text-gray-700 mr-2">
                    <FaFacebook className="h-6 w-6 text-gray-500 hover:text-gray-700" />
                </a>
                <a href={'mailto:'+mail} target="_blank" rel="noopener" className="text-gray-700 mr-2">
                <MdEmail className="h-6 w-6 text-gray-500 hover:text-gray-700" />                </a>
                <a href={inst} target="_blank" rel="noopener" className="text-gray-700 mr-2">
                    <FaInstagram className="h-6 w-6 text-gray-500 hover:text-gray-700" />
                </a>
                <a href={gh} target="_blank" rel="noopener" className="text-gray-700 mr-2">
                    <FaGithub className="h-6 w-6 text-gray-500 hover:text-gray-700" />
                </a>
            </div>
        </div>
    );
};

export default DevCard;
