import { useState } from "react";
import { registerUser } from "../services/authService";
import { useNavigate } from "react-router-dom";

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
        <form onSubmit={handleSubmit}>
            <h2>Registro</h2>

            <input 
              placeholder="Correo electrónico"
              value={email}
              onChange={e => setEmail(e.target.value)}
            />

            <input 
              placeholder="Número de teléfono"
              value={phone_number}
              onChange={e => setPhone(e.target.value)}
            />

            <input 
              placeholder="Nombre"
              value={first_name}
              onChange={e => setFirstName(e.target.value)}
            />

            <input 
              placeholder="Apellido"
              value={last_name}
              onChange={e => setLastName(e.target.value)}
            />

            <input 
              type="password"
              placeholder="Contraseña"
              value={password}
              onChange={e => setPassword(e.target.value)}
            />

            <button>Crear cuenta</button>
        </form>
    )

}