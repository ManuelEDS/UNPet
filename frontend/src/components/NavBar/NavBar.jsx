import { useContext } from 'react';
import { UserContext } from '../../context/UserContext.jsx';
import logo from '/icons/android-chrome-192x192.png';
import SearchBar from '../SearchBar.jsx';
import UNPetMark from './UNPetMark.jsx';
import UserIcon from './UserIcon.jsx';
import CreatePostButton from './CreatePostButton.jsx';
import { searchGeneral } from '../../api/search.api';
function NavBar() {
  const { user, search } = useContext(UserContext);


  const searchHandler = (searchText) => {
    const trimmedSearchText = searchText.trim();
    const singleSpacedText = trimmedSearchText.replace(/\s+/g, ' ');
    const formattedSearchText = encodeURIComponent(singleSpacedText);
    search.setSearchText(formattedSearchText);
    console.log('este es el texto a buscar: ', formattedSearchText);
    console.log('resultados: ', searchGeneral(formattedSearchText));
}
  return (
    <nav className="bg-gray-800">
      <div className="mx-auto px-8">
        <div className="flex items-center justify-between h-16">
          <UNPetMark logo={logo}></UNPetMark>
          <SearchBar onSearch={searchHandler} />
          <CreatePostButton />
          <UserIcon user={user}></UserIcon>
        </div>
      </div>
    </nav>
  );
}
export default NavBar;

