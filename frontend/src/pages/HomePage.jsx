import LeftBar from '../components/LeftBar';
import { useMediaQuery } from 'react-responsive';
import ScrollList from '../components/Feed/Feed';
import { UserContext } from '../context/UserContext';
import { useState, useContext, useEffect } from 'react';
import { UNPetAxios } from '../api/config';

export const HomePage = () => {
    const isDesktopOrLaptop = useMediaQuery({ minDeviceWidth: 800 });
    const { user, search } = useContext(UserContext);
    const { searchText, setSearchText } = search
    const unPetAxios = new UNPetAxios();
    const [dataItems, setDataItems] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            if (searchText !== "") {
                try {
                    const response = await unPetAxios.get('/search/api/general/?q=' + searchText);
                    const data = response
                    setDataItems(data);
                } catch (error) {
                    console.error(error);
                }
            }
        };

        fetchData();
    }, [searchText]);
    return (
        <div className="flex justify-between  w-full overflow-y-auto">
            <div className=''>
                {isDesktopOrLaptop && <LeftBar />}
            </div>
            <div className="max-w-2xl mx-auto ">
                <h2 className="text-3xl font-bold text-center mb-4 py-4">¡Bienvenido a UNPet!</h2>
                <p className="text-center mb-8">Entregando nuevas oportunidades</p>
                <ScrollList urlBase={'/posts/api/posts/trend/'} dataItems={dataItems}></ScrollList> 
            </div>
        </div>
    );
};

export default HomePage;