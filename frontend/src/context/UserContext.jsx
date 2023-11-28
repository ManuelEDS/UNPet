import { createContext, useState, useEffect } from "react";
import { UNPetAxios } from "../api/config";
import PropTypes from 'prop-types';
import { getCSRF } from "../api/config";
export const UserContext = createContext();

export const UserContextProvider = ({ children, isDesktop }) => {
    const UserAxios = new UNPetAxios('/accounts');
    const [searchText, setSearchText] = useState("");
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [userType, setuserType] = useState("Anonymous");
    const [username, setUsername] = useState("Anonymous");
    const [urlfoto, setUrlfoto] = useState("/user-img-default.png");
    const [isDesktopOrLaptop, setIsDesktopOrLaptop] = useState(isDesktop);
    const [leftBar, setLeftBar] = useState(false);
    const [csrfToken, setCsrfToken] = useState(null);

    const checkAuth = async () => {
        try {
            const response = await UserAxios.get("/api/session/");
            const data = response.data
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
        setIsDesktopOrLaptop(isDesktop);
        setLeftBar(false);
    }, [isDesktop]);


    useEffect(() => {
        const fetchCSRFToken = async () => {
            const tk = await getCSRF();
            setCsrfToken(tk);
        };

        fetchCSRFToken();
    }, []);

    useEffect(() => {
        console.log('csrfToken en el user CONTEXT: ', csrfToken);
    }, [csrfToken]);

    return (
        <UserContext.Provider value={{ user: { isAuthenticated, username, urlfoto, userType, checkAuth, isDesktopOrLaptop , leftBar, setLeftBar, csrfToken}, search: { searchText, setSearchText } }}>
            {children}
        </UserContext.Provider>
    );
};

UserContextProvider.propTypes = {
    children: PropTypes.node.isRequired,
};

