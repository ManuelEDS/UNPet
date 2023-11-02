
import { UserContext } from '../../context/UserContext';
import { useContext } from 'react';
import { Button } from '@mui/material';
import { styled } from '@mui/material/styles'; // Updated import statement
import { useNavigate } from "react-router-dom";

const loginButtonStyles = styled({
    button: {
        color: 'white',
        backgroundColor: '#3f51b5',
        '&:hover': {
            backgroundColor: '#2c387e',
        },
    },
});

export function LoginButton() {
    const { user } = useContext(UserContext);
    const navigate = useNavigate();
    const classes = loginButtonStyles();

    const handleLogin = async () => {
        if (!user.isAuthenticated) {
            navigate('/login');
        }
    };

    return (
        <Button
            onClick={handleLogin}
            disabled={user.isAuthenticated}
            className={classes.button}
        >
            Iniciar sesión
        </Button>
    );
}

const registerButtonStyles = styled({
    button: {
        color: '#3f51b5',
        backgroundColor: 'white',
        '&:hover': {
            backgroundColor: '#f5f5f5',
        },
    },
});

export function RegisterButton() {
    const { user } = useContext(UserContext);
    const navigate = useNavigate();

    const classes = registerButtonStyles();

    const handleRegister = async () => {
        if (!user.isAuthenticated) {
            navigate('/register');
        }
    };

    return (
        <Button
            onClick={handleRegister}
            disabled={user.isAuthenticated}
            className={classes.button}
        >
            Registrarse
        </Button>
    );
}

const logoutButtonStyles = styled({
    button: {
        color: '#3f51b5',
        backgroundColor: 'white',
        '&:hover': {
            backgroundColor: '#f5f5f5',
        },
    },
});

export function LogoutButton() {
    const { user, setUser } = useContext(UserContext);
    const navigate = useNavigate();
    const classes = logoutButtonStyles();

    const handleLogout = async () => {
        setUser({ isAuthenticated: false });
        navigate('/logout');
    };

    return (
        <Button
            onClick={handleLogout}
            disabled={!user.isAuthenticated}
            className={classes.button}
        >
            Cerrar sesión
        </Button>
    );
}
