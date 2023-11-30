import ScrollList from '../Feed/Feed';



const OrganizacionCard = ({ user }) => {
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
    <div className="bg-white rounded-lg shadow-lg p-4 my-10 justify-center max-w-2xl mx-auto "> {/* Added 'justify-center' class */}
      <div className='flex justify-center mt-6 space-x-10'>
        <img src={user.urlfoto} alt="Foto de perfil" className="w-32 h-32 rounded-full" />
        <div>
          <p className="text-2xl font-bold mb-2">{user.name}</p>
          <h1 className="text-xl font-bold mb-2">@{user.username}</h1>
          <p>Email: {user.email}</p>
          <p>{user.is_superuser && <div><p>Super Usuario</p></div>}</p>
          <p>{user.is_staff && <div><p>STAFF</p></div>}</p>
          <p style={{ color: user.is_active ? 'black' : 'red' }}>{user.is_active ? 'Activo' : 'Baneado'}</p>
          <p>Tipo: {user.userType}</p>
          <p>Teléfono: {user.telefono}</p>
          <p>Localidad: {user.localidad}</p>
          <p>Dirección: {user.direccion}</p>
          <p>Fecha de registro: {getDaysSinceJoining(user.date_joined) <= 2 ? `Se unió hace ${getDaysSinceJoining(user.date_joined)} días` : `Se unió el ${formatDate(user.date_joined)}`}</p>
        </div>
      </div>
      <div className='flex justify-between' id='posts'> {/* Added 'justify-center' class */}
        <div className="max-w-2xl mx-auto mt-10 ">
          <h2 className="text-2xl font-bold text-center mb-4 py-4">Publicaciones de la organización</h2>

          <ScrollList urlBase={'/posts/api/posts/' + user.username + '/posts/'} org={true}></ScrollList>
        </div>
      </div>


    </div>
  );
};

export default OrganizacionCard;
