import { useEffect, useState, useContext } from 'react';
import { UserContext } from '../context/UserContext.jsx';
import { getOrganizationPets, updatePet, deletePet, createPet } from '../api/pets.api.js';
import { Modal } from '../components/Modal.jsx';
import { MdEdit, MdCancel, MdDelete } from "react-icons/md";
import { createPost } from '../api/posts.api.js';
import { BASE_URL } from '../api/config.js';
import axios from 'axios';
export const PetList = () => {
    const [pets, setPets] = useState([]);
    const [selectedPets, setSelectedPets] = useState([]);;
    const [showEdit, setShowEdit] = useState(false);
    const [loading, setLoading] = useState(false);
    const [editedPet, setEditedPet] = useState(null)
    const [showCreate, setShowCreate] = useState(false);
    const { user } = useContext(UserContext)
    const request = axios.create({
        baseURL: BASE_URL,
        headers: {
            "Content-Type": 'application/json',
           "X-CSRFToken": user.csrfToken,
        },
        withCredentials: true,
    });
    useEffect(() => {
        const fetchPets = async () => {
            console.log('EL FETCH CON FNCION: ');
            const data = await request.get('/pets/api/pets/organization').then((response) => setPets(response.data))
            console.log('EL DATA con unpetaxios: ', data)
            
        }
        fetchPets();
        setShowEdit(false);
    }, []);
    useEffect(() => {
        console.log('selectedPets en useffect: ', selectedPets);
    }, [selectedPets]);
    useEffect(() => {
        console.log('editedPet en useffect: ', editedPet);
    }, [editedPet]);

    const handleSelectPet = (petIndex) => {
        const selectedPet = pets[petIndex];
        if (!selectedPets.includes(selectedPet)) {
            setSelectedPets([...selectedPets, selectedPet]);
        }
    }
    const handleDeselectPet = (petIndex) => {
        console.log('petIndex: ', petIndex, ' pets: ', pets);
        const deselectedPet = selectedPets[petIndex];
        console.log('selectedPets antes: ', selectedPets);
        setSelectedPets(selectedPets.filter(pet => pet !== deselectedPet));
        console.log('deseleccionado: ', deselectedPet);
        console.log('selectedPets: ', selectedPets);

    }
    const handleStartEditPet = (petIndex, petsList) => {
        const selectedPet = petsList[petIndex];
        setEditedPet(selectedPet);
        setShowEdit(true);
    }
    const handleSaveEditPet = async (petID, petsList) => {
        const pet = petsList.find(pet => pet.id === petID);
        console.log('find pet: ', pet)
        const selectedPet = pet
        const valid = validateData(editedPet);

        if (!valid) {
            console.log('no valido');

            return;
        }
        else {
            setLoading(true);
            console.log('valido, aqui se ejecuta el updatePet()');
            //await new Promise(resolve => setTimeout(resolve, 500));
            request.defaults.headers.put['X-CSRFToken'] = user.csrfToken;
            request.defaults.headers.put['csrftoken'] = user.csrfToken;
            document.cookie = `csrftoken=${user.csrfToken}`;
            console.log('justo antes de enviar el request: ', editedPet, user.csrfToken, request.defaults.headers, 'document.cookie: ',document.cookie);
            request.put('/pets/api/pets/'+editedPet.id+'/update/', editedPet, {
                headers: {
                    "Content-Type": 'application/json',
                     "X-CSRFToken": user.csrfToken,
                     'csrftoken': user.csrfToken
                    
                },
            })
            .then((response) => {
                // Maneja la respuesta aquí
                console.log('uodate pet: Response: ', response);
            })
            .catch((error) => console.error(error));
            
            
            //Response = await updatePet(editedPet.id, editedPet);
            console.log('Response: ', Response);
            setLoading(false);
            // window.location.reload();
        }
        setShowEdit(false);

    }
    const handleDeletePet = async (petID) => {
        setLoading(true);
        console.log('valido, aqui se ejecuta el deletePet()');
        //await new Promise(resolve => setTimeout(resolve, 500));
        Response = await deletePet(petID);
        console.log('Response: ', Response);
        setLoading(false);
        window.location.reload();

    }
    const handleCreatePet = async (event) => {
        event.preventDefault();
        console.log('CREAR PET INICIANDO...');
        const data = new FormData(event.currentTarget);
        const valid = validateData(data);
        if (!valid) {
            console.log('no valido');
        }
        else {
            setLoading(true);
            console.log('valido, aqui se ejecuta el createPet()');
            //await new Promise(resolve => setTimeout(resolve, 500));
            Response = await createPet(data);
            console.log('Response: ', Response);
            setLoading(false);
            window.location.reload();
        }
    }











    const handleCheckboxChange = (event) => {
        console.log('event.target.name: ', event.target.name, ' event.target.checked: ', event.target.checked);
        const newPet = {
            ...editedPet,
            "adoptada": event.target.checked
        };
        setEditedPet(newPet);
    }
    const handleChange = (event) => {
        console.log('event.target.name: ', event.target.name, ' event.target.value: ', event.target.value);
        const name = event.target.name;
        const newPet = {
            ...editedPet,
            [name]: event.target.value
        };
        setEditedPet(newPet);
        console.log('editedPet modificado: ', editedPet);
    }
    function validateData(data) {
        console.log('pet antes de ser validado: ', data);
        const formData = new FormData();
        let object = {};
        for (let key in data) {
            let value = data[key];
            if (key === 'adoptada') {
                value = value === 'true';
            }
            formData.append(key, value);
        }
        formData.forEach((value, key) => object[key] = value);
        console.log('formData: ', object);
        //console.log('formData: ', formData);
        for (let [key, value] of formData) {
            console.log('key: ', key, ' value: ', value);
            if (!value || value === '') {
                return false;
            }
        }
        return true;
    }

    const handleCreatePost = async (event) => {
        event.preventDefault();
        console.log('CREAR POST INICIANDO...');
    
        const dataPost = new FormData(event.currentTarget);
        const data = new FormData();
        const valid = true //validateData(dataPost);
    
        if (!valid || selectedPets.length === 0) {
            console.log('no valido');
        }
        else {
            addDataToForm(dataPost, "n_mascotas", selectedPets.length);
            addDataToForm(dataPost, "n_mascotas_adoptadas", 0);
            addDataToForm(dataPost, "idorganizacion", user.id);
           
            // Añade los valores para 'mascotas'
            let mascotas = selectedPets.map(pet => JSON.stringify(pet));
            dataPost.append("mascotas", JSON.stringify(mascotas));
            data.append("post", JSON.stringify(Object.fromEntries(dataPost.entries())));
    
            setLoading(true);
            console.log('valido, aqui se ejecuta el createPost()');
            //await new Promise(resolve => setTimeout(resolve, 500));
            console.log('data justo antes del create post: ');
            for (let [key, value] of data.entries()) {
                console.log(`${key}: ${value}`);
            }
            const response = await createPost(data);
            console.log('Response: ', response);
            setLoading(false);
            window.location.reload();
        }
    }

    function handleImageUpload(e) {
        const file = e.target.files[0];
        const reader = new FileReader();
        console.log('se cargó algo de imagen', file, reader);
        reader.onloadend = () => {
            document.getElementById('image_preview').src = reader.result;
        }

        if (file) {
            reader.readAsDataURL(file);
        } else {
            document.getElementById('image_preview').src = '';
        }
    }
    function addDataToForm(formData, key, value) {
        formData.append(key, value);
        return formData;
    }
    return (
        <>
            {loading && <div className="fixed top-0 left-0 z-50 w-screen h-screen flex items-center justify-center bg-black bg-opacity-50">
                <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-white"></div>
            </div>}
            <div className="flex flex-wrap items-start justify-center content-between ">

                <div className='bg-white rounded-lg shadow-lg m-8 p-5 self-start w-full h-full sm:w-6/12 '>

                    <form className="flex flex-col" method="POST" encType="multipart/form-data" onSubmit={handleCreatePost}>
                        <label className="mb-2">
                            Estado:
                            <select name="estado" className="w-full p-2 mt-1 border rounded">
                                <option value="Disponibles">Disponibles</option>
                                {/* Agrega aquí las otras opciones si las hay */}
                            </select>
                        </label>
                        <label className="mb-2">
                            Título:
                            <input type="text" name="titulo" className="w-full p-2 mt-1 border rounded" />
                        </label>
                        <label className="mb-2">
                            Descripción:
                            <textarea name="descripcion" className="w-full p-2 mt-1 border rounded"></textarea>
                        </label>
                        <img src="../../public/default-post-img.jpg" alt="Default Post" className="w-full " />
                        <button type="submit" className="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-green-600 text-base font-medium text-white hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 sm:ml-3 sm:w-auto sm:text-sm mb-4">
                            Crear
                        </button>
                    </form>

                    {selectedPets && selectedPets.map((pet, index) => (
                        <div key={index} className="flex items-center mb-4 w-full rounded-md border-2  bg-white shadow-lg" >
                            <img src={pet.urlfoto} alt={pet.nombre} className="m-2 w-28 " />
                            <div className='my-2  w-44'>
                                <p className="text-sm font-bold">{pet.nombre}</p>
                                <p className="mt-2">
                                    {pet.especie}
                                </p>
                                <p className="mt-2">
                                    <strong>Nació el:</strong> {pet.fechanacimiento}
                                </p>
                                {/* {pet.adoptada ? <p className="mt-2 text-red-500">Adoptada</p> : <p className="mt-2 text-green-500">En adopción</p>} */}



                            </div>
                            <div>
                                <button className="mt-2 text-green-500 mx-2 bg-gray-300 hover:bg-gray-200 p-2 rounded-md shadow-lg" onClick={() => { handleStartEditPet(index, selectedPets) }}>
                                    <MdEdit className='w-6 h-6'></MdEdit>
                                </button>
                                <button className="mt-2 text-red-500 mx-2 p-2 bg-gray-300 hover:bg-gray-200 rounded-md shadow-lg" onClick={() => { handleDeselectPet(index) }}>
                                    <MdCancel className='w-6 h-6'></MdCancel>
                                </button>
                            </div>
                        </div>
                    ))}

                </div>
                <div className=" rounded-lg  m-8 self-start bg-gray-200 w-full sm:w-96 ">  {/* //w-full  para moviles*/}
                    <div className="flex items-center justify-center bg-green-400 hover:bg-green-300 text-white font-bold rounded-md h-12 mb-4 cursor-pointer" onClick={() => { setShowCreate(true) }}>Crear mascota</div>
                    {pets.map((pet, index) => (
                        <div key={index} className={`flex items-center mb-4 w-full rounded-md border-2 pt-2  ${pet.adoptada ? 'bg-gray-300' : 'bg-white'} shadow-lg`} >

                            <img src={pet.urlfoto} alt={pet.nombre} className="m-2 w-28 cursor-pointer" onClick={() => { !pet.adoptada && handleSelectPet(index) }} />
                            <div className='my-2  w-full'>
                                <p className="text-sm font-bold bg-yellow-400 text-white text-center mr-2 ">{pet.nombre}</p>
                                <p className="mt-2">
                                    <strong>Especie:</strong> {pet.especie}
                                </p>
                                <p className="mt-2">
                                    <strong>Raza:</strong> {pet.raza || 'No especificada'}
                                </p>
                                <p className="mt-2">
                                    <strong>Sexo:</strong> {pet.sexo}
                                </p>
                                <p className="mt-2">
                                    <strong>Nació el:</strong> {pet.fechanacimiento}
                                </p>
                                {pet.adoptada ? <p className="mt-2 text-red-500">Adoptada</p> : <p className="mt-2 text-green-500">En adopción</p>}




                            </div>
                            <div>
                                <button className="mt-2 text-green-500 mx-2 bg-gray-300 hover:bg-gray-200 p-2 rounded-md shadow-lg" onClick={() => { handleStartEditPet(index, pets) }}>
                                    <MdEdit className='w-6 h-6'></MdEdit>
                                </button>
                                <button className="mt-2 text-red-500 mx-2 p-2  bg-gray-300 hover:bg-gray-200 rounded-md shadow-lg" onClick={() => { handleDeletePet(pet.id) }}>
                                    <MdDelete className='w-6 h-6'></MdDelete>
                                </button>
                            </div>
                        </div>
                    ))}
                </div>

            </div>

            {editedPet && showEdit && <Modal open={showEdit} title='' type='' onClose={setShowEdit} onAccept={() => { handleSaveEditPet(editedPet.id, pets) }} acceptText='Guardar cambios' cancelText='No guardar'>
                <form className="flex flex-col" method="POST" encType="multipart/form-data" onSubmit={handleSaveEditPet}>
                    <label className="mb-2">
                        Nombre:
                        <input type="text" name="nombre" value={editedPet.nombre} onChange={handleChange} className="w-full p-2 mt-1 border rounded" />
                    </label>
                    <label className="mb-2">
                        Especie:
                        <select name="especie" value={editedPet.especie} onChange={handleChange} className="w-full p-2 mt-1 border rounded">
                            <option value="Gato">Gato</option>
                            <option value="Perro">Perro</option>
                        </select>
                    </label>
                    <label className="mb-2">
                        Raza:
                        <input type="text" name="raza" value={editedPet.raza} onChange={handleChange} className="w-full p-2 mt-1 border rounded" />
                    </label>
                    <label className="mb-2">
                        Sexo:
                        <select name="sexo" value={editedPet.sexo} onChange={handleChange} className="w-full p-2 mt-1 border rounded">
                            <option value="Macho">Macho</option>
                            <option value="Hembra">Hembra</option>
                        </select>
                    </label>

                    <label className="mb-2">
                        Fecha de nacimiento:
                        <input type="date" name="fechanacimiento" value={editedPet.fechanacimiento} onChange={handleChange} className="w-full p-2 mt-1 border rounded" />
                    </label>
                    <label className="mb-2">
                        URL de la foto:
                        <input type="text" name="urlfoto" value={editedPet.urlfoto} onChange={handleChange} className="w-full p-2 mt-1 border rounded" />
                    </label>
                    <label className="mb-2">
                        Adoptada:
                        <input type="checkbox" name="adoptada" checked={editedPet.adoptada} onChange={handleCheckboxChange} className="m-2 b-2" />
                    </label>
                </form>


            </Modal>}

            {showCreate &&
                <Modal open={true} title='' type='' showButtons={false}>
                    <form className="flex flex-col" method="POST" encType="multipart/form-data" onSubmit={handleCreatePet}>
                        <label className="mb-2">
                            Nombre:
                            <input type="text" name="nombre" className="w-full p-2 mt-1 border rounded" />
                        </label>
                        <label className="mb-2">
                            Especie:
                            <select name="especie" className="w-full p-2 mt-1 border rounded">
                                <option value="Gato">Gato</option>
                                <option value="Perro">Perro</option>
                            </select>
                        </label>
                        <label className="mb-2">
                            Raza:
                            <input type="text" name="raza" className="w-full p-2 mt-1 border rounded" />
                        </label>
                        <label className="mb-2">
                            Sexo:
                            <select name="sexo" className="w-full p-2 mt-1 border rounded">
                                <option value="Macho">Macho</option>
                                <option value="Hembra">Hembra</option>
                            </select>
                        </label>
                        <label className="mb-2">
                            Fecha de nacimiento:
                            <input type="date" name="fechanacimiento" className="w-full p-2 mt-1 border rounded" />
                        </label>

                        <label htmlFor="photo_file" className="block text-sm font-medium text-gray-700 py-2">
                            Foto de perfil
                            <input
                                id="photo_file"
                                name="photo_file"
                                type="file"
                                accept="image/*"
                                className="appearance-none block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                                onChange={handleImageUpload}
                            ></input>
                            <img id="image_preview" className="mt-2 rounded-xl" width="50" />
                        </label>



                        {/* <label className="mb-2">
                            Adoptada:
                            <input type="checkbox" name="adoptada" checked={false} className="m-2 b-2" />
                        </label> */}

                        <div className="sm:flex sm:items-start">
                            <button type="submit" className="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-green-600 text-base font-medium text-white hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 sm:ml-3 sm:w-auto sm:text-sm mb-4">
                                Crear
                            </button>
                            <button className="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-red-600 text-base font-medium text-white hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 mb-4 focus:ring-red-500 sm:ml-3 sm:w-auto sm:text-sm" onClick={() => { setShowCreate(false) }}>
                                Cancelar
                            </button>
                        </div>
                    </form>
                </Modal>


            }

        </>
    );
};
