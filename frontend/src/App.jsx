import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { FeedPage } from './pages/FeedPage'
import { PetFormPage } from './pages/PetFormPage'
import { Login } from './pages/LoginPage'
import { Register } from './pages/RegisterPage.jsx'
import { RegisterOrg } from './pages/RegisterOrg.jsx'
import { Password } from './pages/Password'
import { HomePage } from './pages/HomePage'
import { TermsCond } from './pages/TermsCond'
import { PoliticsPriv } from './pages/Politicspriv'
import { Donations } from './components/Donations'
import WhoAreWePage from './pages/WhoAreWePage'
import TestPosts from './pages/testPosts'
import { UserContextProvider } from './context/UserContext'
import NavBar from './components/NavBar/NavBar'
import Footer from './components/Footer'
function App() {


  return (
    <UserContextProvider>
      <BrowserRouter>
        <NavBar />
        <Routes>
          <Route path='/pets' element={<FeedPage />} />
          <Route path='/' element={<Navigate to="/pets" />} />
          <Route path='/pet-create' element={<PetFormPage />} />
          <Route path='/pets/:id' element={<PetFormPage />} />
          <Route path='/login' element={<Login />} />
          <Route path='/register' element={<Register />} />
          <Route path='/register-org' element={<RegisterOrg />} />
          <Route path='/password' element={<Password />} />
          <Route path='/home' element={<HomePage />} />
          <Route path='/legal/terms-and-conditions' element={<TermsCond />} />
          <Route path='/legal/privacy-policies' element={<PoliticsPriv />} />
          <Route path='/donations' element={<Donations />} />
          <Route path='/quienes-somos' element={<WhoAreWePage />} />
          <Route path='/posttest' element={<TestPosts />} />
        </Routes>
        <Footer />
      </BrowserRouter>
    </UserContextProvider>

  )
}

export default App