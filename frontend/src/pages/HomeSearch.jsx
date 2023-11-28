import LeftBar from '../components/LeftBar';
import { useMediaQuery } from 'react-responsive';
import ScrollList from '../components/Feed/Feed';
import { UserContext } from '../context/UserContext';
import { useState, useContext, useEffect } from 'react';
import { UNPetAxios } from '../api/config';
import CreatePostButton from '../components/NavBar/CreatePostButton';
import SearchPage from '../components/Feed/SearchPage';
import { useParams } from 'react-router-dom';
export const HomeSearch = () => {
    const { search } = useParams();
    const isDesktopOrLaptop = useMediaQuery({ minDeviceWidth: 800 });
    const { user } = useContext(UserContext);
    const { searchText, setSearchText } = search
    const unPetAxios = new UNPetAxios();
    const [dataItems, setDataItems] = useState(null);
    const { showBar, setShowBar } = useState(false);
    useEffect(() => {
        const fetchData = async () => {
            if (searchText !== "") {
                try {
                    const response = await unPetAxios.get('/search/api/general/?q=' + searchText);
                    const data = response
                    console.log('data: ', data);
                    setDataItems(data);
                } catch (error) {
                    console.error(error);
                }
            }
        };

        fetchData();
    }, [searchText, user.LeftBar]);
    return (
        <div className="flex justify-between  w-full overflow-y-auto">
            {user.leftBar && !isDesktopOrLaptop && <LeftBar />}

            <div className=''>
                {isDesktopOrLaptop && <LeftBar />}
            </div>
            {!user.leftBar &&
                <div className="max-w-2xl mx-auto ">
                    <h2 className="text-3xl font-bold text-center mb-4 py-4">¡Bienvenido a UNPet!</h2>
                    <p className="text-center mb-8">Entregando nuevas oportunidades</p>

                    {user.isAuthenticated && user.userType == 'Organizacion' && <CreatePostButton></CreatePostButton>}


                    <SearchPage search={search} dataItems={dataItems}></SearchPage>

                </div>
            }
        </div>
    );
};

export default HomeSearch;