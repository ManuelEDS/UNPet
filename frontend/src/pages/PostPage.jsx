
import { useEffect, useState, useRef, useContext } from 'react';
import { useParams } from 'react-router-dom';
import { getPost, getComments } from '../api/posts.api';
import ImageSlider from '../components/imageslider';
import { FaHeart, FaComment, FaPaw, FaShareAlt, FaCopy } from 'react-icons/fa';
import { UserContext } from '../context/UserContext';
import { Coment } from '../components/Feed/Coments';
import { getPetById } from '../api/pets.api';
import { getUser } from '../api/accounts.api';
export const PostPage = () => {
    const { id } = useParams();
    const [post, setPost] = useState(null);
    const [username, setUsername] = useState(null);
    const [fecha, setFecha] = useState(null);
    const [showModal, setShowModal] = useState(false);
    const [showPetModal, setShowPetModal] = useState(false);
    const [copied, setCopied] = useState(false);
    const [coments, setComents] = useState(null); // [coment1, coment2, ...
    const [currentPetIndex, setCurrentPetIndex] = useState(null); // [coment1, coment2, ...
    const [currentPet, setCurrentPet] = useState(null); // [coment1, coment2, ...
    const [currentOrg, setCurrentOrg] = useState(null); // [coment1, coment2, ...
    const modalRef = useRef(null);
    const { user } = useContext(UserContext);
    const sortComents = (coments) => {
        return coments.sort((a, b) => new Date(b.fechapublicacion) - new Date(a.fechapublicacion));
    }
    useEffect(() => {
        const fetchPost = async () => {
            try {
                console.log('peticion a : ', 'http://localhost:8000/api/posts/api/posts/' + id);
                const data = await getPost(id)
                const dataComents = await getComments(id)
                setComents(sortComents(dataComents));

                console.log('data: ', data);
                setUsername(data.post.nombreorganizacion.match(/\(([^)]+)\)$/)[1])
                setFecha(new Date(data.post.fechapublicacion).toLocaleDateString());
                setPost(data.post);
                console.log('comentarios del state aqui-->: ', coments);
            } catch (error) {
                console.error('Error fetching user:', error);
            }
        };
        fetchPost();
        const handleClickOutside = (event) => {
            if (modalRef.current && !modalRef.current.contains(event.target)) {
                setShowModal(false);
            }
        };

        document.addEventListener('mousedown', handleClickOutside);
        return () => {
            document.removeEventListener('mousedown', handleClickOutside);
        };

    }, [id]);



    const handleCopyLink = () => {
        console.log('copiando link')
        const link = window.location.href;
        navigator.clipboard.writeText(link);
        setCopied(true);
    };

    const handleShowPet = async () => {
        console.log('antes de ejecutar handleShowPet: ', currentPetIndex, username);
        console.log('PRIMERO pet actual: ', currentPet);
        const pet = await getPetById(currentPetIndex.id);
        const org = await getUser(username);
        console.log('mascota actual: ', pet);
        setCurrentPet(pet)
        setCurrentOrg(org.user)
        setShowPetModal(true);
    }


    return (
        <>
            {post && (
                <div className="flex flex-wrap items-center justify-center content-between">
                    <div className="bg-white rounded-lg shadow-lg m-8  self-start ">
                        <div className="p-4 max-w-l">
                            <div className="flex items-center mb-4">
                                <a href={"/user/" + username}>
                                    <img src={post.urlfoto_organizacion} alt={post.nombreorganizacion} className="w-10 h-10 rounded-full mr-2" />
                                </a>
                                <div>
                                    <a href={"/user/" + username}>
                                        <p className="text-sm font-medium">{post.nombreorganizacion}</p>
                                    </a>
                                    <p className="text-gray-500 text-sm">{fecha}</p>
                                </div>
                            </div>
                            <h3 className="text-lg font-medium mb-2">{post.titulo}</h3>
                            <p className="text-gray-500 text-sm mb-4">{post.descripcion}</p>
                            <div className="w-full z-0">
                                {post.mascotas.length > 0 ? (
                                    <ImageSlider className="w-full z-0" images={post.mascotas} postid={post.id} setCurrentPet={setCurrentPetIndex} />
                                ) : (
                                    <a href="#">
                                        <img className="w-full z-0" src="../../../public/default-post-img.jpg" alt="" />
                                    </a>
                                )}
                            </div>
                            <div className="flex items-center justify-between m-3">
                                <div className="flex items-center justify-between w-full mt-3">
                                    <a className="flex items-center ml-4">
                                        <FaHeart id={"heart" + post.id} className="w-5 h-5 text-gray-500 mr-1" />
                                        <p className="text-gray-500 text-sm">{post.likes}</p>
                                    </a>
                                    <a href="/login" className="flex items-center">
                                        <FaComment className="w-5 h-5 text-gray-500 mr-1" />
                                        <span className="text-gray-500 text-sm mr-1">{post.comments}</span>
                                    </a>
                                    <div onClick={handleShowPet} className="flex items-center" >
                                        <FaPaw id={"paw" + post.id} className="w-5 h-5 text-gray-500 mr-2" />
                                        <span className="text-gray-500 text-sm mr-1" >Adoptar</span>
                                    </div>
                                    <button className="flex items-center  mr-4" onClick={() => setShowModal(true)}>
                                        <FaShareAlt className="w-5 h-5 text-gray-500 mr-1" />
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    {/* // COMENTARIOS */}
                    <div className="bg-white rounded-lg shadow-lg mt-8  self-start " id='seccion-comentarios'>
                        <div className="bg-white rounded-lg  max-w-lg">
                            {coments.map((coment, index) => (
                                <div key={index}>

                                    <Coment coment={coment} post={post} />
                                </div>
                            ))}
                            <button className='flex m-5' onClick={() => { console.log(coments) }}>Cargar comentarios</button>
                        </div>
                    </div>

                </div>
            )}

            {showModal &&

                <div className="fixed inset-0 flex items-center justify-center z-50" >
                    <div className="bg-white rounded-lg shadow-lg p-4">
                        <p className="text-center mb-4">Comparte este link con tus amigos:</p>
                        <div className="flex items-center justify-between">
                            <input type="text" value={window.location.href} readOnly className="w-full bg-gray-100 border border-gray-300 rounded p-2" />
                            <button className={`ml-2 bg-blue-500 text-white rounded p-2 ${copied ? 'text-green-500' : ''}`} onClick={handleCopyLink}>
                                <FaCopy className="ml-1" />
                            </button>
                            <button className='ml-2 bg-blue-500 rounded p-2   flex items-center ' onClick={() => { setShowModal(false); setCopied(false) }}>
                                Cerrar
                            </button>
                        </div>

                    </div>
                </div>


            }

            {showPetModal && currentPet && (
                <div className="fixed inset-0 flex items-center justify-center z-50">
  <div className="bg-white rounded-lg flex max-h-auto  overflow-hidden mr-5">

                    <div className="bg-white  p-4 m-7   flex items-center justify-center max-w-4xl">
                        <img src={currentPet.urlfoto} alt={currentPet.nombre} className="" />
                    </div>
                    <div className="bg-white rounded-lg flex-grow mr-8">
                        <div>
                            <p className="text-center m-4">Información de la mascota:</p>

                            <p className="mt-2">
                                <strong>Nombre:</strong> {currentPet.nombre}
                            </p>
                            <p>
                                <strong>Especie:</strong> {currentPet.especie}
                            </p>
                            <p>
                                <strong>Raza:</strong> {currentPet.raza}
                            </p>
                            <p>
                                <strong>Sexo:</strong> {currentPet.sexo}
                            </p>
                            <p>
                                <strong>Fecha de Nacimiento:</strong> {currentPet.fechanacimiento}
                            </p>
                            <p className='mb-6'>
                                <strong>Adoptada:</strong> {currentPet.adoptada ? 'Sí' : 'No'}
                            </p>
                            {currentPet.adoptada ? <strong className='mb-6'>Esta mascota ya fue adoptada, pero puedes seguir buscando a tu compañero ideal</strong> : <strong className='mb-6'>Contacta con nosotros si te gusta esta mascota!</strong>}

                            <div className="flex items-center mb-4 bg-yellow-300 p-3 rounded-lg mt-4">
                                <a href={"/user/" + username} className=''>
                                    <img src={post.urlfoto_organizacion} alt={post.nombreorganizacion} className="w-10 h-10 rounded-full mr-2" />
                                </a>
                                <div>
                                    <a href={"/user/" + username}>
                                        <p className="text-sm font-medium">{post.nombreorganizacion}</p>
                                    </a>
                                </div>


                            </div>
                            <div className=" mb-12 bg-yellow-200 p-3 rounded-lg mt-4">
                                <div >
                                    <strong>Email:</strong> {currentOrg.email}
                                </div>
                                <div>
                                    <strong>Direccion:</strong> {currentOrg.direccion}
                                </div>
                                <div>
                                    <strong>Localidad:</strong> {currentOrg.localidad}
                                </div>

                                <strong>Teléfono:</strong> {currentOrg.telefono}

                            </div>


                            <div className="flex items-end justify-between ">
                                <button
                                    className={`ml-2 ${currentPet.adoptada ? 'bg-gray-500' : 'bg-blue-500'} text-white rounded p-2 `}
                                    onClick={() => { console.log('le diste  a acptar, redirijir a adopciones'); }}
                                    disabled={currentPet.adoptada}
                                >
                                    Adoptar
                                </button>
                                <button
                                    className={`ml-2 bg-blue-500 text-white rounded p-2 `}
                                    onClick={() => {
                                        setShowPetModal(false);
                                    }}
                                >
                                    Cerrar
                                </button>
                            </div>

                        </div>

                    </div>


                    </div>
                   
                </div>
            )}
        </>
    );
};

