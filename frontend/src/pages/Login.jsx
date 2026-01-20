import { useState } from "react";
import { loginUser } from "../services/authService";
import { useAuth } from "../context/AuthContext";
import { Link, useNavigate } from "react-router-dom";
import "./Auth.css";

export default function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const { login } = useAuth();
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const res = await loginUser({ email, password });
            login({ access: res.data.access, refresh: res.data.refresh });
            navigate("/");
        } catch (err) {
            console.error("Error al iniciar sesión:", err);
        }
    }

    return (
        <div className="auth-container">
            <div className="auth-card">
                <h1>Iniciar sesión</h1>
                
                <form onSubmit={handleSubmit}>
                    <input 
                        type="email" 
                        placeholder="Corre Electrónico" 
                        value={email} 
                        onChange={e => setEmail(e.target.value)}
                        required
                    />

                    <input 
                        type="password" 
                        placeholder="Contraseña" 
                        value={password} 
                        onChange={e => setPassword(e.target.value)}
                        required
                    />
                    
                    <button>Entrar</button>
                </form>

                <p className="auth-form-text">
                    ¿No tienes cuenta?{" "}
                    <Link to="/register">Regístrate aquí</Link>
                </p>
            </div>
        </div>
    )
}