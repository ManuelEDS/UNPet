import  { useState } from 'react';
import TextField from '@mui/material/TextField';
import IconButton from '@mui/material/IconButton';
import SearchIcon from '@mui/icons-material/Search';

function SearchBar({ onSearch }) {
  const [searchText, setSearchText] = useState('');

  const handleSearch = () => {
    onSearch(searchText);
  };

  return (
    <div style={{ display: 'flex', alignItems: 'center' }}>
      <TextField
        label="Buscar"
        variant="outlined"
        size="small"
        fullWidth
        value={searchText}
        onChange={(e) => setSearchText(e.target.value)}
      />
      <IconButton
        color="primary"
        onClick={handleSearch}
        style={{ marginLeft: '8px' }}
      >
        <SearchIcon />
      </IconButton>
    </div>
  );
}

export default SearchBar;
