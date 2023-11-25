import React from 'react';
import { FaHeart, FaComment } from 'react-icons/fa';

export const Coment = ({ post }) => {
    const fecha = new Date(post.fechapublicacion).toLocaleDateString()
    const username = post.nombreorganizacion.match(/\(([^)]+)\)$/)[1]
    return (
        <div className="m-5 p-4">
            <div className="flex items-center mb-2">
                <a href={"/user/" + username}>
                    <img src={post.urlfoto_organizacion} alt={post.nombreorganizacion} className="w-10 h-10 rounded-full mr-2" />
                </a>
                <div>
                    <a href={"/user/" + username}>
                        <p className="text-sm font-medium">{post.nombreorganizacion}</p>
                    </a>
                    <p className="text-gray-500 text-xs">{fecha}</p>
                </div>
            </div>
            <p className="text-gray-800 text-sm mb-4">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Totam sit eos facere cum odit, voluptatum enim praesentium aspernatur numquam cupiditate, alias sapiente. Inventore perferendis quaerat quo officia adipisci quae quia!</p>
            <div className="flex items-center justify-between m-0">
                <div className="flex ">
                    <a className="flex items-center ml-0">
                        <FaHeart id={"heart" + post.id} className="w-5 h-5 text-gray-500 mr-1" />
                        <p className="text-gray-500 text-sm">{post.likes}</p>
                    </a>
                    <a href="/login" className="flex items-center ml-6">
                        <FaComment className="w-5 h-5 text-gray-500 mr-1" />
                        <span className="text-gray-500 text-sm mr-1">{post.comments}</span>
                    </a>
                </div>
            </div>
        </div>
    );
};
