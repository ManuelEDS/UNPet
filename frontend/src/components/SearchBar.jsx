import { useState } from "react";




function SearchBar({ onSearch }) {
  const [searchText, setSearchText] = useState('');

  const handleSearch = () => {
    // Elimina los espacios al principio y al final del texto y reemplaza cualquier secuencia de espacios en blanco con un solo espacio
    const cleanedText = searchText.trim().replace(/\s+/g, ' ');

    // Divide el texto en palabras
    const words = cleanedText.split(' ');

    // Separa las palabras que comienzan con '@' y las que no
    const atWords = words.filter(word => word.startsWith('@'));
    const otherWords = words.filter(word => !word.startsWith('@'));

    // Ordena las palabras que comienzan con '@' en orden alfabético
    atWords.sort();

    // Combina las palabras que comienzan con '@' y las que no
    const searchTextFormated = [...atWords, ...otherWords].join(' ');

    onSearch(searchTextFormated);
  };

  const highlightTags = (text) => {
    const regex = /@(\w+)(?!\S)/g;
    return text.replace(regex, '<span class="tag">@$1</span>');
  };

  return (
    <div className="flex items-center">
      <input
        type="text"
        placeholder="Buscar.."
        className="border border-gray-300 rounded-md py-2 px-4 w-full"
        value={searchText}
        onChange={(e) => setSearchText(e.target.value)}
        dangerouslySetInnerHTML={{ __html: highlightTags(searchText) }}
      />
      <button
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded ml-2"
        onClick={handleSearch}
      >
        <SearchIcon className="h-5 w-5" />
      </button>
    </div>
  );
}
