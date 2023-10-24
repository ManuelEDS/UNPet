import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { FeedPage } from './pages/FeedPage'
import { PetFormPage } from './pages/PetFormPage'
import { SignIn } from './components/SignIn.jsx'
import { SignUp } from './components/SignUp.jsx'
import { OrgSingUp } from './components/OrgSingUp.jsx'
import { Password } from './components/Password'
import { Donations } from './components/Donations'

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
        <Route path='/donations' element={<Donations />} />
      </Routes>
    </BrowserRouter>

  )
}

export default App