
const PersonaCard = ({ user, detailed = false }) => {
    const formatDate = (dateString) => {
        const date = new Date(dateString);
        const options = { year: 'numeric', month: 'numeric', day: 'numeric' };
        return date.toLocaleDateString(undefined, options);
    };

    const getDaysSinceJoining = (dateString) => {
        const today = new Date();
        const joinDate = new Date(dateString);
        const timeDiff = Math.abs(today.getTime() - joinDate.getTime());
        const daysDiff = Math.ceil(timeDiff / (1000 * 3600 * 24));
        return daysDiff;
    };

    return (
        <div className="bg-white rounded-lg shadow-lg p-4 my-10 justify-center max-w-2xl mx-auto mt7 "> {/* Added 'justify-center' class */}
            <div className='flex justify-center m-6'>
                <img src={user.urlfoto} alt="Foto de perfil" className="w-32 h-32 rounded-full mr-4" />
                <div>
                    <p className="text-xl font-bold mb-2"> {user.first_name + ' ' + user.last_name}</p>
                    <h1 className="text-2xl font-bold mb-2">@{user.username}</h1>
                    <p>Email: {user.email}</p>

                    <p>{user.is_superuser && <div><p>Super Usuario</p></div>}</p>
                    <p>{user.is_staff && <div><p>STAFF</p></div>}</p>
                    <p style={{ color: user.is_active ? 'black' : 'red' }}>{user.is_active ? 'Activo' : 'Baneado'}</p>
                    <p>Tipo: {user.userType}</p>
                    {detailed &&
                        <>
                            <p>Teléfono: {user.telefono}</p>
                            <p>Localidad: {user.localidad}</p>
                        </>
                    }
                    <p>Fecha de registro: {getDaysSinceJoining(user.date_joined) <= 2 ? `Se unió hace ${getDaysSinceJoining(user.date_joined)} días` : `Se unió el ${formatDate(user.date_joined)}`}</p>
                </div>
            </div>
            <div className='flex justify-between m-6' id='posts'> {/* Added 'justify-center' class */}
                <div>hola</div>
                <div>hola</div>
                <div>hola</div>
                <div>hola</div><div>hola</div><div>hola</div><div>hola</div><div>hola</div>
            </div>


        </div>
    );
};

export default PersonaCard;
