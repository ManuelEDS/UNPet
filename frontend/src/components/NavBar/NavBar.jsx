import { useContext } from 'react';
import { UserContext } from '../../context/UserContext.jsx';
import logo from '/icons/android-chrome-192x192.png';
import SearchBar from '../SearchBar.jsx';
import UNPetMark from './UNPetMark.jsx';
import UserIcon from './UserIcon.jsx';
import CreatePostButton from './CreatePostButton.jsx';
import { searchGeneral } from '../../api/search.api';
import { GiHamburgerMenu } from "react-icons/gi";
import { useMediaQuery } from 'react-responsive';

function NavBar() {
  const { user, search } = useContext(UserContext);
  //console.log('user: ', user
  // );
  const handleShowLeftBar = async () => {
    console.log('leftbar 0: ', user.leftBar);
    await user.setLeftBar(user.leftBar ? false : true)
    console.log('leftbar: ', user.leftBar);
  }

  const searchHandler = (searchText) => {
    const trimmedSearchText = searchText.trim();
    const singleSpacedText = trimmedSearchText.replace(/\s+/g, ' ');
    const formattedSearchText = encodeURIComponent(singleSpacedText);
    search.setSearchText(formattedSearchText);
    console.log('este es el texto a buscar: ', formattedSearchText);
    console.log('resultados: ', searchGeneral(formattedSearchText));
    window.location.href = "/search";
  }
  return (
    <nav className="bg-gray-800">

      <div className="mx-auto px-0">

        <div className="flex items-center justify-between h-16">
          {!user.isDesktopOrLaptop && <div className='bg-white px-3 py-2 mx-2  rounded-lg cursor-pointer'>
            <button onClick={handleShowLeftBar}>
              <GiHamburgerMenu />
            </button>
          </div>}
          <UNPetMark logo={logo}></UNPetMark>
          <SearchBar onSearch={searchHandler} />
          <UserIcon user={user}></UserIcon>
        </div>
      </div>
    </nav>
  );
}
export default NavBar;

