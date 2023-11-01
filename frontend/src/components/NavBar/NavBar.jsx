import React from 'react';
import { AppBar, Toolbar, IconButton, Typography, InputBase, Button } from '@mui/material';
import { styled, alpha } from '@mui/material/styles';
import MenuIcon from '@mui/icons-material/Menu';
import { LoginButton, RegisterButton, LogoutButton } from './LoginButton.jsx';
import { useContext } from 'react';
import { UserContext } from '../../context/UserContext.jsx';
import logo from '../../public/icons/android-chrome-192x192.png';
import SearchIcon from '@mui/icons-material/Search';

const Search = styled('div')(({ theme }) => ({
    position: 'relative',
    borderRadius: theme.shape.borderRadius,
    backgroundColor: alpha(theme.palette.common.white, 0.15),
    '&:hover': {
        backgroundColor: alpha(theme.palette.common.white, 0.25),
    },
    marginLeft: 0,
    width: '100%',
    [theme.breakpoints.up('sm')]: {
        marginLeft: theme.spacing(1),
        width: 'auto',
    },
}));

const SearchInput = styled(InputBase)(({ theme }) => ({
    color: 'inherit',
    '& .MuiInputBase-input': {
        padding: theme.spacing(1, 1, 1, 0),
        paddingLeft: `calc(1em + ${theme.spacing(4)})`,
        transition: theme.transitions.create('width'),
        width: '100%',
        [theme.breakpoints.up('sm')]: {
            width: '12ch',
            '&:focus': {
                width: '20ch',
            },
        },
    },
}));



const SearchIconWrapper = styled(SearchIcon)(({ theme }) => ({
    color: theme.palette.common.white,
}));

function NavBar() {
    const { user } = useContext(UserContext);
    return (
        <AppBar position="static">
            <Toolbar>
                <IconButton edge="start" color="inherit" aria-label="menu">
                    <MenuIcon />
                </IconButton>
                <Typography variant="h6" noWrap>
                    <img src={logo} alt="UNPet logo" style={{ marginRight: '10px' }} />
                    UNPet
                </Typography>
                <Search>
                    <SearchInput
                        placeholder="Buscar…"
                        inputProps={{ 'aria-label': 'search' }}
                        endAdornment={
                            <InputAdornment position="end">
                                <SearchIconWrapper />
                            </InputAdornment>
                        }
                    />
                </Search>

                {user.isAuthenticated ? <LogoutButton /> :
                    <>
                        <LoginButton />
                        <RegisterButton />
                    </>
                }
            </Toolbar>
        </AppBar>
    );
}

export default NavBar;