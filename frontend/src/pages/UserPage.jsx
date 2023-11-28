
import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getUser } from '../api/accounts.api';
import User from '../components/accounts/User';
export const UserPage = () => {
    const { username } = useParams();
    const [user, setUser] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const userData = await getUser(username);
                setUser(userData.user);
            } catch (error) {
                console.error('Error fetching user:', error);
            }
        };

        fetchData();
    }, [username]);

    return (
        <div>
            {user ? (
                <>

                    <User user={user} />

                </>
            ) : (
                <h1>🧐 Buscando datos de usuario... 🧐</h1>
            )}
        </div>
    );
};
