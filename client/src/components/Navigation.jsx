import {Link} from 'react-router-dom'
export function Navigation() {
  return (
    <div>
        <Link to="/pets">
            <h1>UNPet</h1>
        </Link>        
        <Link to="/pet-create">Crear Mascota</Link>

    </div>
  )
}