import { useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function PasswordResetConfirm() {
    const { uidb64, token } = useParams();
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [error, setError] = useState(null);
    const [success, setSuccess] = useState(false);
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();
        if (password !== confirmPassword) {
            setError('Las contraseñas no coinciden');
            return;
        }
        try {
            const response = await axios.post(`https://unpet-api-rest.onrender.com/api/accounts/password-reset-confirm/${uidb64}/${token}/`, {
                new_password: password
            });
            if (response.status === 200) {
                setSuccess(true);
            }
        } catch (error) {
            setError('Hubo un error al restablecer la contraseña');
        }
    };

    if (success) {
        navigate('/home');
    }

    return (
        <form onSubmit={handleSubmit} className="flex flex-col space-y-4">
            <input type="password" placeholder="Nueva contraseña" value={password} onChange={(e) => setPassword(e.target.value)} required className="border border-gray-300 rounded-md px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent" />
            <input type="password" placeholder="Confirmar nueva contraseña" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} required className="border border-gray-300 rounded-md px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent" />
            {error && <p className="text-red-500">{error}</p>}
            <button type="submit" className="bg-blue-500 text-white rounded-md px-4 py-2 hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50">Restablecer contraseña</button>
        </form>
    );
}

export default PasswordResetConfirm;