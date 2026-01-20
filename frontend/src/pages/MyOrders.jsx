import { useEffect, useState } from "react";
import { getMyOrders } from "../services/orderService";
import { formatDateTime } from "../utils/date";

export default function MyOrders() {
    const [orders, setOrders] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        getMyOrders()
          .then(res => setOrders(res.data))
          .finally(() => setLoading(false));
    },[]);

    if (loading) return <p>Cargando compras...</p>;

    if (orders.length === 0) {
        return <p>No tienes compras realizadas.</p>;
    }

    return (
        <div>
            <h1>Mis compras</h1>

            {orders.map(order => (
                <div key={order.id} style={{ border: "1px solid #ccc", padding: 16, marginBottom: 16}}>
                    <h3>Orden #{order.id}</h3>
                    <p>Fecha: {formatDateTime(order.created_at)}</p>
                    <p>Precio unitario: ${order.ticket_unit_price}</p>
                    <p>Total: ${order.total_amount}</p>
                    <p>Estado: {order.status}</p>
                    <p>Película: {order.movie_name}</p>

                    <h4>Asientos</h4>
                    <ul>
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