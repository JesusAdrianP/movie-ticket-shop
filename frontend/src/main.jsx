import { createRoot } from 'react-dom/client'
import "./styles/variables.css"
import "./styles/global.css"
import "./styles/buttons.css"
import App from './App.jsx'
import { AuthProvider } from './context/AuthContext.jsx'

createRoot(document.getElementById('root')).render(
  <AuthProvider>
    <App />
  </AuthProvider>,
)
