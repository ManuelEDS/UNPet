// UserCard.jsx
export const UserCard = ({ user }) => (
  <div className="bg-white shadow overflow-hidden sm:rounded-lg">
    <div className="px-4 py-5 sm:px-6">
      <h3 className="text-lg leading-6 font-medium text-gray-900">{user.name}</h3>
      <p className="mt-1 max-w-2xl text-sm text-gray-500">{user.email}</p>
    </div>
    <div className="border-t border-gray-200 px-4 py-5 sm:p-0">
      {/* Aquí va el contenido del usuario */}
    </div>
  </div>
);
