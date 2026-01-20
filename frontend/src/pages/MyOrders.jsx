import { useEffect, useState } from "react";
import { getMyOrders } from "../services/orderService";
import { formatDateTime } from "../utils/date";
import "../styles/MyOrders.css";

export default function MyOrders() {
    const [orders, setOrders] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        getMyOrders()
          .then(res => setOrders(res.data))
          .finally(() => setLoading(false));
    },[]);

    if (loading) return <p className="orders-loading">Cargando compras...</p>;

    if (orders.length === 0) {
        return <p className="orders-empty">No tienes compras realizadas.</p>;
    }

    return (
        <div className="orders-container">
            <h1 className="orders-title">Mis compras</h1>

            {orders.map(order => (
                <div key={order.id} className="order-card">
                    <div className="order-header">
                        <h3>Orden #{order.id}</h3>
                        <span className={`order-status ${order.status.toLowerCase()}`}>
                            {order.status}
                        </span>
                    </div>
                    <p>Fecha: {formatDateTime(order.created_at)}</p>
                    <p>Película: {order.movie_name}</p>
                    <p>Precio unitario: ${order.ticket_unit_price}</p>
                    <p>Total: ${order.total_amount}</p>

                    <h4>Asientos</h4>
                    <ul className="seat-list">
                        {order.seats.map((seat, index) => (
                            <li key={index}>
                                {seat}
                            </li>
                        ))}
                    </ul>
                </div>
            ))}
        </div>
    )
}