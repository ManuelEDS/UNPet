import { useState, useEffect } from 'react';
import InfiniteScroll from 'react-infinite-scroll-component';
import { UNPetAxios } from '../../api/config';
import PostCard from './PostCard';
import { getCSRF } from '../../api/config';
import { BASE_URL } from '../../api/config';
import axios from 'axios';
const ScrollList = ({ urlBase, onItemSelect = () => { }, forceUpdate = () => { } }) => {
    const unPetAxios = new UNPetAxios();
    const [items, setItems] = useState([]);
    const [hasMore, setHasMore] = useState(true);
    const [nextPageUrl, setNextPageUrl] = useState(removeAPIUrl(urlBase));

    useEffect(() => {
        fetchItems();

    }, []);


    const fetchItems = async () => {
        if (nextPageUrl === null) {
            setHasMore(false);
            return;
        }

        try {
            fetch(BASE_URL + "/accounts/api/csrf/", {
                credentials: 'include'
            })
                .then(response => response.headers.get('X-CSRFToken'))
                .then(csrfToken => {
                    fetch(BASE_URL + urlBase, {

                        method: 'GET',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': csrfToken
                        },
                        credentials: 'include'

                    })
                        .then(response => response.json())
                        .then(data => {

                            const { count, next, previous, results } = data
                            setItems(prevItems => [...prevItems, ...results]);
                            setHasMore(next !== null);
                            setNextPageUrl(removeAPIUrl(next));

                        });


                })

        } catch (error) {
            console.error(error);
        }
    };
    return (
        <InfiniteScroll
            dataLength={items.length}
            next={fetchItems}
            hasMore={hasMore}
            loader={<h4>😺🐶Encontrando los mejores compañeros... 😺🐶</h4>}
            endMessage={<h4>Todos los elementos han sido cargados</h4>}
        >
            <div >
                {items.map((item, index) => (
                    <div key={index} onClick={() => onItemSelect(item.id)} >
                        {item.userType ? <div>es un usuario</div> : item.raza ? <div>es una mascota</div> : <PostCard post={item} onItemSelect={() => onItemSelect(item.id)} />}
                    </div>
                ))}
            </div>
        </InfiniteScroll>
    );
};

function removeAPIUrl(url) {
    if (url === null) {
        return null;
    }
    const patron = /https?:\/\/(?:unpet-api-rest\.onrender\.com|localhost:8000)\/api/g;

    // Reemplazar la parte que coincide con el patrón por una cadena vacía
    const nuevaUrl = url.replace(patron, '');

    return nuevaUrl;
}
export default ScrollList;
