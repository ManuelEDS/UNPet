import React from 'react';
import { FaHeart, FaComment } from 'react-icons/fa';

export const Coment = ({ coment, post , parent={}}) => {
    const fecha = new Date(coment.fechapublicacion).toLocaleDateString()
    const username = coment.autor
    const useranme_post = post.nombreorganizacion.match(/\(([^)]+)\)$/)[1]
    return (
        <>
        <div className="m-5 p-4">
            <div className="flex items-center mb-2">
                <a href={"/user/" + username}>
                    <img src={coment.urlfoto_autor} alt={username} className="w-10 h-10 rounded-full mr-2" />
                </a>
                <div>
                    <a href={"/user/" + username}>
                        <p className="text-sm font-bold">@{username}</p>
                    </a>
                    <p className="text-gray-500 text-xs">{fecha}</p>
                </div>
            </div>
            <div className="text-gray-800 text-sm mb-4">
                
                {parent?<><div>
                    <a href={"/user/" + username}><p className="text-sm font-bold">@{coment.autor}</p></a>
                
                <p>{coment.contenido}</p>
                </div>
                
                </>
                     : coment.contenido}
                     
                     
                     </div>
            <div className="flex items-center justify-between m-0">
                <div className="flex ">
                    <a className="flex items-center ml-0">
                        <FaHeart id={"heart" + coment.id} className="w-5 h-5 text-gray-500 mr-1" />
                        <p className="text-gray-500 text-sm">45</p>
                    </a>
                    <a href="/login" className="flex items-center ml-6">
                        <FaComment className="w-5 h-5 text-gray-500 mr-1" />
                        
                    </a>
                </div>
                
            </div>
            
        </div>
        <div className=" ml-12 border-l border-gray-500 border-solid">
            {coment.respuestas && coment.respuestas.map((resp, index) => (
                <div className=' ' key={index}>
                    <Coment coment={resp} post={post} parent ={coment}/>
                </div>
            ))}

            
        </div>
        
        </>
    );
};
