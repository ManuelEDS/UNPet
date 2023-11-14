
import { FaPaw } from 'react-icons/fa';

function CreatePostButton() {

    return (
        <a href="/create-post" style={{ width: 160, padding: 10, cursor: "pointer" }}>
            <button

                type="button"
                className="group relative w-full flex justify-center py-2 px-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
                <span className="absolute left-0 flex items-center pl-3">
                    <FaPaw className="h-5 w-5 text-indigo-500 group-hover:text-indigo-400" aria-hidden="true" />
                </span>
                <p className="relative left-3">Crear Post</p>
            </button>
        </a>
    );
}

export default CreatePostButton;



