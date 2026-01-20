import { useState } from "react";
import { registerUser } from "../services/authService";
import { Link, useNavigate } from "react-router-dom";

export default function Register() {
    const [email, setEmail] = useState("");
    const [phone_number, setPhone] = useState("");
    const [first_name, setFirstName] = useState("");
    const [last_name, setLastName] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();

    const handleSubmit = (e) => {
        e.preventDefault();

        registerUser({email, phone_number, first_name, last_name, password})
          .then(() => navigate("/login"))
    }

    return (
        <div className="auth-container">
            <div className="auth-card">
                <h1>Registro</h1>

                <form onSubmit={handleSubmit}>
                    <input
                        type="email"
                        placeholder="Correo electrónico"
                        value={email}
                        onChange={e => setEmail(e.target.value)}
                        required
                    />
                    
                    <input 
                        placeholder="Número de teléfono"
                        value={phone_number}
                        onChange={e => setPhone(e.target.value)}
                        required
                    />
                    
                    <input 
                        placeholder="Nombre"
                        value={first_name}
                        onChange={e => setFirstName(e.target.value)}
                        required
                    />
                    
                    <input 
                        placeholder="Apellido"
                        value={last_name}
                        onChange={e => setLastName(e.target.value)}
                        required
                    />
                    
                    <input 
                        type="password"
                        placeholder="Contraseña"
                        value={password}
                        onChange={e => setPassword(e.target.value)}
                        required
                    />
                    
                    <button type="submit">Crear cuenta</button>
                </form>

                <p className="auth-form-text">
                    ¿Ya tienes una cuenta?{" "}
                    <Link to="/login">Inicia sesión aquí</Link>
                </p>
            </div>
        </div>
    )

}