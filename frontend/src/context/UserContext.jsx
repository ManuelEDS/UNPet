import { createContext, useState, useEffect } from "react";
import { UNPetAxios } from "../api/config";

export const UserContext = createContext();

export const UserContextProvider = ({ children }) => {
    const UserAxios = new UNPetAxios();
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [username, setUsername] = useState("Anonymous");
    const [urlfoto, setUrlfoto] = useState("/user-img-default.png");

    useEffect(() => {
        const checkAuth = async () => {
            try {
                const response = await UserAxios.get("/accounts/api/session/");
                console.log('tengo session?:-->',response, response.data);
                setIsAuthenticated(response.data.is_authenticated);
                setUsername(response.data.username?response.data.username:"Anonymous");
                setUrlfoto(response.data.urlfoto || "/user-img-default.png");
            } catch (error) {

            }
        };
        checkAuth();
    }, []);

    return (
        <UserContext.Provider value={{user:{ isAuthenticated, username, urlfoto }}}>
            {children}
        </UserContext.Provider>
    );
};

