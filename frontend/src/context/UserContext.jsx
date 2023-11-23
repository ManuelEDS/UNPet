import { createContext, useState, useEffect } from "react";
import { UNPetAxios } from "../api/config";
import { useMediaQuery } from 'react-responsive';
import PropTypes from 'prop-types';

export const UserContext = createContext();

export const UserContextProvider = ({ children }) => {
    const UserAxios = new UNPetAxios('/accounts');
    const [searchText, setSearchText] = useState("");
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [userType, setuserType] = useState("Anonymous");
    const [username, setUsername] = useState("Anonymous");
    const [urlfoto, setUrlfoto] = useState("/user-img-default.png");

    const checkAuth = async () => {
        try {
            const response = await UserAxios.get("/api/session/");
            const data = await response.json();
            if (data) {
                setIsAuthenticated(data.isAuthenticated);
                setUsername(data.username ? data.username : "Anonymous");
                setUrlfoto(data.urlfoto || "/user-img-default.png");
                setuserType(data.userType || "Anonymous");
            } else {
                console.log('La respuesta no tiene datos');
            }
        } catch (error) {
            console.log(error);
        }
    };

    useEffect(() => {
        checkAuth();
    }, []);

    return (
        <UserContext.Provider value={{ user: { isAuthenticated, username, urlfoto, userType, checkAuth }, search: { searchText, setSearchText } }}>
            {children}
        </UserContext.Provider>
    );
};

UserContextProvider.propTypes = {
    children: PropTypes.node.isRequired,
};

