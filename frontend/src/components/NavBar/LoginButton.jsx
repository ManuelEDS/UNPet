
import { UserContext } from '../../context/UserContext';
import { useContext } from 'react';
import { useHistory } from 'react-router-dom';
import { Button } from '@mui/material';
import { makeStyles } from '@mui/styles';

const loginButtonStyles = makeStyles({
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
    const history = useHistory();
    const classes = loginButtonStyles();

    const handleLogin = async () => {
        if (!user.isAuthenticated) {
            history.push('/login');
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

const registerButtonStyles = makeStyles({
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
    const history = useHistory();
    const classes = registerButtonStyles();

    const handleRegister = async () => {
        if (!user.isAuthenticated) {
            history.push('/register');
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

const logoutButtonStyles = makeStyles({
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
    const history = useHistory();
    const classes = logoutButtonStyles();

    const handleLogout = async () => {
        setUser({ isAuthenticated: false });
        history.push('/logout');
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
