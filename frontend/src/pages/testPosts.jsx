import React, { useState, useEffect } from 'react';
import InfiniteScroll from 'react-infinite-scroll-component';

const ScrollList = () => {
    const [items, setItems] = useState([]);
    const [hasMore, setHasMore] = useState(true);
    const [nextPageUrl, setNextPageUrl] = useState('http://localhost:8000/posts/api/posts/recent/');

    useEffect(() => {
        fetchItems();
    }, []);

    const fetchItems = async () => {
        if (nextPageUrl === null) {
            setHasMore(false);
            return;
        }

        try {
            const response = await fetch(nextPageUrl);
            const { count, next, previous, results } = await response.json();
            setItems(prevItems => [...prevItems, ...results]);
            setHasMore(next !== null);
            setNextPageUrl(next);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <InfiniteScroll
            dataLength={items.length}
            next={fetchItems}
            hasMore={hasMore}
            loader={<h4>Loading...</h4>}
            endMessage={<h4>No more items</h4>}
        >
            <div className="grid grid-cols-1 gap-4">
                {items.map((item, index) => (
                    <div key={index} className="bg-white rounded-lg shadow-md p-4">
                        <h2 className="text-lg font-bold mb-2">{item.titulo}</h2>
                        <p className="text-gray-700 text-base mb-2">{item.descripcion}</p>
                        <p className="text-gray-700 text-base mb-2">Estado: {item.estado}</p>
                        <p className="text-gray-700 text-base mb-2">Fecha de publicación: {item.fechapublicacion}</p>
                        <p className="text-gray-700 text-base mb-2">Likes: {item.likes}</p>
                        <p className="text-gray-700 text-base mb-2">Número de mascotas: {item.n_mascotas}</p>
                        <p className="text-gray-700 text-base mb-2">Número de mascotas adoptadas: {item.n_mascotas_adoptadas}</p>
                    </div>
                ))}
            </div>
        </InfiniteScroll>
    );
};

export default ScrollList;
