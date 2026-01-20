import "./Success.css";
import { useEffect, useState } from "react";
import { useNavigate, useParams, Link } from "react-router-dom";
import { formatDateTime } from "../utils/date";
import { getOrderById } from "../services/orderService";

export default function Success() {
    const { orderId } = useParams();
    const navigate = useNavigate();
    const [order, setOrder] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        getOrderById(orderId)
          .then(res => setOrder(res.data))
          .finally(() => setLoading(false));
    }, [orderId]);

    if(loading) return <p>Cargando compra...</p>;

    if (!order) {
        return (
            <div>
                <p>No se pudo cargar la orden.</p>
                <Link to="/my-orders">Ver mis compras</Link>
            </div>
        );
    }

    return (
        <div className="success-container">
            <h1 className="success-title">Compra realizada con éxito</h1>
            <p className="success-order"><strong>Orden:</strong> #{order.id}</p>
            <p className="success-text"><strong>Fecha de compra:</strong> {formatDateTime(order.created_at)}</p>
            <p className="success-text"><strong>Total:</strong> ${order.total_amount}</p>

            <h3>Entradas</h3>
            <p className="success-text"><strong>Película:</strong> {order.movie_name}</p>
            <p className="success-text"><strong>Fecha de la función:</strong> {formatDateTime(order.show_time)}</p>
            <h4>Asientos</h4>
            <ul>
                {order.seats.map((ticket, index) => (
                    <li key={index}>
                        {ticket}
                    </li>
                ))}
            </ul>

            <p className="success-text">Te enviamos un correo con la confirmación de tu compra.</p>

            <div>
                <button className="btn btn-primary" onClick={() => navigate("/")}>
                    Volver a la cartelera
                </button>
            </div>
        </div>
    )
}