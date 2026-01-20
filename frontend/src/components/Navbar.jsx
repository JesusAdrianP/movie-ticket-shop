import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import "../styles/Navbar.css"

export default function Navbar() {
    const {tokens, logout} = useAuth();

    return (
        <nav className="navbar">
            <Link to="/" className="navbar__logo">CineApp</Link>

            <div className="navbar__links">
                <Link to="/">Películas</Link>

                {!tokens && (
                    <>
                        <Link to="/login">Login</Link>
                        <Link to="/register">Registro</Link>
                    </>
                )}

                {tokens && (
                    <>
                        <Link to="/my-orders">Mis compras</Link>
                        <button className="navbar__logout" onClick={logout}>Salir</button>
                    </>
                )}
            </div>
        </nav>
    )
}