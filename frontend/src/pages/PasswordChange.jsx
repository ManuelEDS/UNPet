import React, { useState } from 'react';
import axios from 'axios';

function PasswordChange() {
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [error, setError] = useState(null);
    const [success, setSuccess] = useState(false);

    const handleSubmit = async (event) => {
        event.preventDefault();
        if (password !== confirmPassword) {
            setError('Las contraseñas no coinciden');
            return;
        }
        try {
            const response = await axios.post('https://unpet-api-rest.onrender.com/api/change-password/', {
                new_password: password,
                confirm_password: confirmPassword
            });
            if (response.status === 200) {
                setSuccess(true);
            }
        } catch (error) {
            setError('Hubo un error al cambiar la contraseña');
        }
    };

    if (success) {
        return <p>¡Contraseña cambiada con éxito!</p>;
    }

    return (
        <form onSubmit={handleSubmit} className="flex flex-col space-y-4">
            <input type="password" placeholder="Nueva contraseña" value={password} onChange={(e) => setPassword(e.target.value)} required className="border border-gray-300 rounded-md px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent" />
            <input type="password" placeholder="Confirmar nueva contraseña" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} required className="border border-gray-300 rounded-md px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent" />
            {error && <p className="text-red-500">{error}</p>}
            <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline">Cambiar contraseña</button>
        </form>
    );
}

export default PasswordChange;