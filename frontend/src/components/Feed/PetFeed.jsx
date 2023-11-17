import { useState, useEffect } from 'react';
import InfiniteScroll from 'react-infinite-scroll-component';
import { FaHeart, FaComment, FaPaw, FaShareAlt } from 'react-icons/fa';
import { UNPetAxios } from '../../api/config';

const ScrollList = ({urlBase, onItemSelect = () => {} }) => {
    const unPetAxios = new UNPetAxios();
    const [items, setItems] = useState([]);
    const [hasMore, setHasMore] = useState(true);
    const [nextPageUrl, setNextPageUrl] = useState(removeAPIUrl(urlBase));

    useEffect(() => {
        fetchItems();

    }, []);

    function getRandomInt(max) {
        return Math.floor(Math.random() * max);
    }

    const imagenes = ["https://i.imgur.com/2CoV1nA.jpg", "https://i.imgur.com/8mtgT8C.png", "https://i.imgur.com/6TeLmcc.png"
    ]

    const fetchItems = async () => {
        if (nextPageUrl === null) {
            setHasMore(false);
            return;
        }

        try {
            const response = await unPetAxios.get(nextPageUrl);
            const { count, next, previous, results } = await response.json();
            setItems(prevItems => [...prevItems, ...results]);
            setHasMore(next !== null);
            setNextPageUrl(removeAPIUrl(next));
        } catch (error) {
            console.error(error);
        }
    };
    console.log(items)

    return (
        <InfiniteScroll
            dataLength={items.length}
            next={fetchItems}
            hasMore={hasMore}
            loader={<h4>😺🐶Encontrando los mejores compañeros... 😺🐶</h4>}
            endMessage={<h4>Todos los elementos han sido cargados</h4>}
        >
            <div className="">
                {items.map((item, index) => (
                    
                    <div key={index}>
                        {item.userType?<div>es un usuario</div>:<div>es un post</div>}
                        <div key={item.id} className="bg-white rounded-lg shadow-lg mb-8" onClick={onItemSelect}>
                            <div className="p-4">
                                <div className="flex items-center mb-4">
                                    <a href="#">
                                        <img src={"https://dummyimage.com/600x400/d1d1d1/5b62c7.jpg&text=Juan%20Perez"} alt={item.username} className="w-10 h-10 rounded-full mr-2" />
                                    </a>
                                    <div>
                                        <a href="#">
                                            <p className="text-sm font-medium">{"Juan Perez"}</p>
                                        </a>
                                        <p className="text-gray-500 text-sm">{item.fechapublicacion.slice(0, 10)}</p>
                                    </div>
                                </div>
                                <h3 className="text-lg font-medium mb-2">{item.titulo}</h3>
                                <p className="text-gray-500 text-sm mb-4">{item.descripcion}</p>
                                <img className="w-full" src={imagenes[(index % 3)]} alt={item.titulo} />
                                <div className="flex items-center justify-between m-3">
                                    <div className="flex items-center justify-between w-full mt-3">
                                        <a href="#" className="flex items-center ml-4">
                                            <FaHeart className="w-5 h-5 text-gray-500 mr-1" />
                                            <p className="text-gray-500 text-sm">{getRandomInt(10)}</p>
                                        </a >
                                        <a href="/login" className="flex items-center">
                                            <FaComment className="w-5 h-5 text-gray-500 mr-1" />
                                            <span className="text-gray-500 text-sm mr-1">{item.comments}</span>
                                        </a >
                                        <a href="#" className="flex items-center" >
                                            <FaPaw className="w-5 h-5 text-gray-500 mr-2" />
                                            <span className="text-gray-500 text-sm mr-1">Adoptar</span>
                                        </a>
                                        <a href="#" className="flex items-center  mr-4">
                                            <FaShareAlt className="w-5 h-5 text-gray-500 mr-1" />
                                        </a >
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </InfiniteScroll>
    );
};

function removeAPIUrl(url) {
    const patron = /https?:\/\/(?:unpet-api-rest\.onrender\.com|localhost:8000)\/api/g;

    // Reemplazar la parte que coincide con el patrón por una cadena vacía
    const nuevaUrl = url.replace(patron, '');

    return nuevaUrl;
}
export default ScrollList;
