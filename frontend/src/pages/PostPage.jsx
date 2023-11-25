
import { useEffect, useState, useRef, useContext } from 'react';
import { useParams } from 'react-router-dom';
import { getPost } from '../api/posts.api';
import ImageSlider from '../components/imageslider';
import { FaHeart, FaComment, FaPaw, FaShareAlt, FaCopy } from 'react-icons/fa';
import { UserContext } from '../context/UserContext';
import { Coment } from '../components/Feed/Coments';
export const PostPage = () => {
    const { id } = useParams();
    const [post, setPost] = useState(null);
    const [username, setUsername] = useState(null);
    const [fecha, setFecha] = useState(null);
    const [showModal, setShowModal] = useState(false);
    const [copied, setCopied] = useState(false);
    const modalRef = useRef(null);
    const { user } = useContext(UserContext);
    useEffect(() => {
        const fetchData = async () => {
            try {
                console.log('peticion a : ', 'http://localhost:8000/api/posts/api/posts/' + id);
                const data = await getPost(id)
                
                console.log('data: ', data);
                setUsername(data.post.nombreorganizacion.match(/\(([^)]+)\)$/)[1])
                setFecha(new Date(data.post.fechapublicacion).toLocaleDateString());
                setPost(data.post);
            } catch (error) {
                console.error('Error fetching user:', error);
            }
        };
        fetchData();
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
                                    <ImageSlider className="w-full z-0" images={post.mascotas} postid={post.id}/>
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
                                    <a href='#' className="flex items-center" >
                                        <FaPaw id={"paw" + post.id} className="w-5 h-5 text-gray-500 mr-2" />
                                        <span className="text-gray-500 text-sm mr-1">Adoptar</span>
                                    </a>
                                    <button className="flex items-center  mr-4" onClick={()=>setShowModal(true)}>
                                        <FaShareAlt className="w-5 h-5 text-gray-500 mr-1" />
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    {/* // COMENTARIOS */}
                    <div className="bg-white rounded-lg shadow-lg mt-8  self-start " id='seccion-comentarios'>
                    <div className="bg-white rounded-lg  max-w-lg">
                        <Coment post={post}  />
                        <Coment post={post}  />
                        <Coment post={post}  />
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
                                <button className='ml-2 bg-blue-500 rounded p-2   flex items-center ' onClick={()=>{setShowModal(false); setCopied(false)}}>
                                    Cerrar
                                </button>
                            </div>
                            
                        </div>
                    </div>
                
                
            }
        </>
    );
};

