import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { FeedPage } from './pages/FeedPage'
import { PetFormPage } from './pages/PetFormPage'
import { SignIn } from './pages/SignIn.jsx'
import { SignUp } from './pages/SignUp.jsx'
import { OrgSingUp } from './pages/OrgSingUp.jsx'
import { Password } from './pages/Password'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Navigate to="/pets" />} />
        <Route path='/pets' element={<FeedPage />} />
        <Route path='/pet-create' element={<PetFormPage />} />
        <Route path='/pets/:id' element={<PetFormPage />} />
        <Route path='/sign-in' element={<SignIn />} />
        <Route path='/sign-up' element={<SignUp />} />
        <Route path='/sign-up-org' element={<OrgSingUp />} />
        <Route path='/password' element={<Password />} />
      </Routes>
    </BrowserRouter>

  )
}

export default App