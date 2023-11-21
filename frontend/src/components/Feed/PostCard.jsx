// PostCard.jsimport { Fragment } from 'react';
import ImageSlider from '../../components/imageslider';
import { FaHeart, FaComment, FaPaw, FaShareAlt } from 'react-icons/fa';
import Modal from '../Modal';
import { useEffect } from 'react';

const PostCard = ({ post, onItemSelect = () => { } }) => {
  // Formatear la fecha
  const fecha = new Date(post.fechapublicacion).toLocaleDateString();
  function getRandomInt(max) {
    return Math.floor(Math.random() * max);
  }

  var heart = document.getElementById("heart" + post.id);
  var paw = document.getElementById("paw" + post.id);
  var open = false;

  if (heart != null) {
    heart.addEventListener("click", function () {
      heart.style.color = "#f34747";
    });
  }

  if (paw != null) {
    paw.addEventListener("click", function () {
      console.log(open)
      open = true;
    });
  }

  return (
    <div className="bg-white rounded-lg shadow-lg mb-8" onClick={onItemSelect}>
      <Modal open={open} />
      <div className="p-4">
        <div className="flex items-center mb-4">
          <a href="#">
            <img src={post.urlfoto_organizacion} alt={post.nombreorganizacion} className="w-10 h-10 rounded-full mr-2" />
          </a>
          <div>
            <a href="#">
              <p className="text-sm font-medium">{post.nombreorganizacion}</p>
            </a>
            <p className="text-gray-500 text-sm">{fecha}</p>
          </div>
        </div>
        <h3 className="text-lg font-medium mb-2">{post.titulo}</h3>
        <p className="text-gray-500 text-sm mb-4">{post.descripcion}</p>
        <ImageSlider className="w-full" images={post.mascotas} />
        <div className="flex items-center justify-between m-3">
          <div className="flex items-center justify-between w-full mt-3">
            <a className="flex items-center ml-4">
              <FaHeart id={"heart" + post.id} className="w-5 h-5 text-gray-500 mr-1" />
              <p className="text-gray-500 text-sm">{getRandomInt(10)}</p>
            </a >
            <a href="/login" className="flex items-center">
              <FaComment className="w-5 h-5 text-gray-500 mr-1" />
              <span className="text-gray-500 text-sm mr-1">{post.comments}</span>
            </a >
            <a className="flex items-center" >
              <FaPaw id={"paw" + post.id} className="w-5 h-5 text-gray-500 mr-2" />
              <span className="text-gray-500 text-sm mr-1">Adoptar</span>
            </a>
            <a className="flex items-center  mr-4">
              <FaShareAlt className="w-5 h-5 text-gray-500 mr-1" />
            </a >
          </div>
        </div>
      </div>
    </div>

  );
};

export default PostCard;