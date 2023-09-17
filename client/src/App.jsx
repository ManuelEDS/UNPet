import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { FeedPage } from './pages/FeedPage'
import { PetFormPage } from './pages/PetFormPage'
import { Navigation } from './components/Navigation'

function App() {
  return (
    <BrowserRouter>
      <Navigation />
      <Routes>
        <Route path='/' element={<Navigate to="/pets" />} />
        <Route path='/pets' element={<FeedPage />} />
        <Route path='/pet-create' element={<PetFormPage />} />
        <Route path='/pets/:id' element={<PetFormPage />} />

      </Routes>
    </BrowserRouter>
  )
}

export default App