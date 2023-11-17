import { Link } from 'react-router-dom'
import { useNavigate } from "react-router-dom";
import { useState } from 'react';
import { createPost } from '../api/posts.api';
import ScrollList from '../components/Feed/Feed';

export function CreatePost() {
    const navigate = useNavigate();
    const [selectedItems, setSelectedItems] = useState([]); // Nuevo estado para almacenar los IDs de los elementos seleccionados

    const handleSubmit = async (event) => {
        event.preventDefault();
        const data = new FormData(event.currentTarget);
        console.log(data)
        console.log(selectedItems) // Imprime los IDs de los elementos seleccionados cuando se envía el formulario
    };

    return (
        <div className="max-h-screen bg-gray-50 flex flex-col justify-left py-36 sm:px-6 lg:px-8 h-full">
            <form className="space-y-6" onSubmit={handleSubmit}>
                <label>
                    contenido de tu publicación
                </label>
                
                <input
                    id="title"
                    name="title"
                    type="text"
                    required
                />
                <div>
                    <button type="submit">
                        Crear Post
                    </button>
                </div>
            </form>
            <ScrollList 
                urlBase={'/pets/api/posts/recent/'} 
                onItemSelect={id => setSelectedItems(prevItems => [...prevItems, id])} // Pasa una función que actualiza el estado de selectedItems
            />
        </div>
    );
}