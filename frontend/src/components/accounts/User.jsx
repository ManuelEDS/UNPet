import { MdAccountCircle } from 'react-icons/md';
import PersonaCard from './PersonaCard';
import OrganizacionCard from './OrganizacionCard';

const User = ({ user }) => {
    console.log(user, user.username);
    return (
        <>
            {user.userType === 'Persona' ? (
                <PersonaCard user={user} />
            ) : (
                <OrganizacionCard user={user} />
            )
            }
        </>

    );

};

export default User;
