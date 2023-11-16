import { createContext, useState, useEffect } from "react";
import { UNPetAxios } from "../api/config";
// import { logout } from '../api/accounts.api';
import { useMediaQuery } from 'react-responsive';

// Tu componente...


export const UserContext = createContext();


import PropTypes from 'prop-types';

export const UserContextProvider = ({ children }) => {
    const UserAxios = new UNPetAxios('/accounts');
  
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [username, setUsername] = useState("Anonymous");
    const [urlfoto, setUrlfoto] = useState("/user-img-default.png");
    const isMobileQuery = useMediaQuery({ query: '(max-width: 600px)' });
    const [isMobile, setIsMobile] = useState(isMobileQuery); // Usar useMediaQuery para el valor inicial
    useEffect(() => {
        setIsMobile(isMobileQuery);
    }, [isMobileQuery]);

    useEffect(() => {
        const checkAuth = async () => {
            try {
                const response = await UserAxios.get("/api/session/");
                console.log('tengo session?:-->',response, response.data);
                let data = response.data.json();
                setIsAuthenticated(data.is_authenticated);

                setUsername(data.username ? data.username : "Anonymous");
                setUrlfoto(data.urlfoto || "/user-img-default.png");
            } catch (error) {
                console.log(error);
            }
        };
        checkAuth();
    }, []);

    return (
        <UserContext.Provider value={{ user: { isAuthenticated, username, urlfoto }, layout: { isMobile } }}>
            {children}
        </UserContext.Provider>
    );
};

UserContextProvider.propTypes = {
  children: PropTypes.node.isRequired,
};

