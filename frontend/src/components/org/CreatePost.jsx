// eslint-disable-next-line no-unused-vars
import { Link } from 'react-router-dom'
import { useNavigate } from "react-router-dom";
import { createPost } from '../../api/posts.api';
import { useEffect, useState, useRef, useContext } from 'react';
import { useParams } from 'react-router-dom';
import { getPost } from '../../api/posts.api';
import ImageSlider from '../imageslider';
import { FaHeart, FaComment, FaPaw, FaShareAlt, FaCopy } from 'react-icons/fa';
import { UserContext } from '../../context/UserContext';
import { Coment } from '../Feed/Coments';

export const CreatePost = () => {
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
                const data = await getPost(1)
                
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

        
        </>
    );
};







// <p className="mt-2 text-center text-sm text-gray-600">
//                     Recuerda nuestros{' '}
//                     <Link
//                         to="/legal/terms-and-conditions"
//                         className="font-medium text-indigo-600 hover:text-indigo-500"
//                     >
//                         Términos del servicio
//                     </Link>
//                 </p>