import { createContext, useState, useEffect } from "react";
import { UNPetAxios } from "../api/config";

export const UserContext = createContext();

export const UserContextProvider = ({ children }) => {
    const UserAxios = new UNPetAxios();
    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [username, setUsername] = useState("Anonymous");
    const [urlfoto, setUrlfoto] = useState("");

    useEffect(() => {
        const checkAuth = async () => {
            try {
                const response = await UserAxios.get("/accounts/api/session/");
                console.log('tengo session?:-->',response, response.data);
                setIsAuthenticated(true);
                setUsername(response.data.username);
                setUrlfoto(response.data.urlfoto || "/user-img-default.png");
            } catch (error) {
                setIsAuthenticated(false);
                setUsername("");
                setUrlfoto("/user-img-default.jpg");
            }
        };
        checkAuth();
    }, []);

    return (
        <UserContext.Provider value={{ isAuthenticated, username, urlfoto }}>
            {children}
        </UserContext.Provider>
    );
};

