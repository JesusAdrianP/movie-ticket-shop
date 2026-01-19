import { useState } from "react";
import { loginUser } from "../services/authService";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

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
        <form onSubmit={handleSubmit}>
            <h2>Iniciar sesión</h2>

            <input placeholder="Corre Electrónico" value={email} onChange={e => setEmail(e.target.value)}/>
            <input type="password" placeholder="Contraseña" value={password} onChange={e => setPassword(e.target.value)}/>

            <button>Entrar</button>
        </form>
    )
}