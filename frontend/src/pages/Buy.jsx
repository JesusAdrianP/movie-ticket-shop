import { useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { createOrder } from "../services/orderService";

export default function Buy() {
    const { movieShowId } = useParams();
    const navigate = useNavigate();

    //Tickets
    const [seats, setSeats] = useState(["A1"]);
    const ticketPrice = 15000

    //payment
    const [paymentMethod, setPaymentMethod] = useState("CREDIT_CARD");
    const [cardHolderName, setCardHolderName] = useState("");
    const [cardLastFour, setCardLastFour] = useState("");

    const addSeat = () => {
        setSeats([...seats, `A${seats.length + 1}`])
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        
        const payload = {
            order_date: new Date().toISOString().split("T")[0],
            tickets: seats.map(seat => ({
                movie_show_id: movieShowId,
                seat_number: seat,
                unit_price: ticketPrice
            })),
            payment: {
                payment_method: paymentMethod,
                card_holder_name: cardHolderName,
                card_last_four_digits: cardLastFour
            }
        }

        createOrder(payload).then(() => {
            navigate("/success")
        })
    }

    return (
        <form onSubmit={handleSubmit}>
            <h2>Comprar entradas</h2>

            <h3>Entradas</h3>
            {seats.map((seat, index) => (
                <p key={index}>Asiento {seat}</p>
            ))}

            <button type="button" onClick={addSeat}>
                Agregar asiento
            </button>

            <p>Total: ${seats.length * ticketPrice}</p>

            <h3>Pago</h3>
            <label>Método de pago</label>
            <select 
                value={paymentMethod}
                onChange={e => setPaymentMethod(e.target.value)}
            >
                <option value="CREDIT_CARD">Tarjeta de crédito</option>
                <option value="DEBIT_CARD">Tarjeta débito</option>
                <option value="PSE">PSE</option>
            </select>

            <input
              placeholder="Nombre del titular"
              value={cardHolderName}
              onChange={e => setCardHolderName(e.target.value)}
              required 
            />

            <input
              placeholder="Últimos 4 dígitos"
              maxLength="4"
              value={cardLastFour}
              onChange={e => setCardLastFour(e.target.value)}
              required
            />
            <button>Confirmar compra</button>
        </form>
    )
}