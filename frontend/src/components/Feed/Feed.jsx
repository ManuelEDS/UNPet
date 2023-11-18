import { useState, useEffect } from 'react';
import InfiniteScroll from 'react-infinite-scroll-component';
import { UNPetAxios } from '../../api/config';
import { UserContext } from '../../context/UserContext.jsx';
import { useContext } from 'react';
import PostCard from './PostCard';
const ScrollList = ({ urlBase, onItemSelect = () => { } }) => {
    const { search } = useContext(UserContext);
    const unPetAxios = new UNPetAxios();
    const [items, setItems] = useState([]);
    const [hasMore, setHasMore] = useState(true);
    const [nextPageUrl, setNextPageUrl] = useState(removeAPIUrl(urlBase));

    if (search.searchText != "") {
        setNextPageUrl("/search/api/general/?q=" + search.searchText)
    }

    const fetchItems = async () => {
        if (nextPageUrl === null) {
            setHasMore(false);
            return;
        }

        try {
            const response = await unPetAxios.get(nextPageUrl);
            const { next, results } = await response.json();
            setItems(prevItems => [...prevItems, ...results]);
            setHasMore(next !== null);
            setNextPageUrl(removeAPIUrl(next));
        } catch (error) {
            console.error(error);
        }
    };

    useEffect(() => {
        fetchItems();
    }, []);

    console.log(nextPageUrl)
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

                    <div key={index} onClick={() => onItemSelect(item.id)}>
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
