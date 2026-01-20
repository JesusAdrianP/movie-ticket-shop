import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { createOrder } from "../services/orderService";
import { getMovieShowById } from "../services/movieService";
import SeatGrid from "../components/SeatGrid";
import { useAuth } from "../context/AuthContext";
import "../styles/Buy.css";

export default function Buy() {
    const { movieShowId } = useParams();
    const { tokens, logout } = useAuth();
    const navigate = useNavigate();
    const [submitting, setSubmitting] = useState(false);

    //Tickets
    const [movieShow, setMovieshow] = useState(null);
    const [selectedSeats, setSelectedSeats] = useState([]);
    const [loading, setLoading] = useState(true);

    //payment
    const [paymentMethod, setPaymentMethod] = useState("CREDIT_CARD");
    const [cardHolderName, setCardHolderName] = useState("");
    const [cardLastFour, setCardLastFour] = useState("");

    useEffect(() => {
        if(!tokens?.access) {
            navigate("/login");
        }
    }, [tokens, navigate])

    useEffect(() => {
        setLoading(true);
        getMovieShowById(movieShowId)
          .then(res => setMovieshow(res.data))
          .catch(() => navigate("/"))
          .finally(() => setLoading(false));
    }, [movieShowId, navigate]);

    const handleSubmit = (e) => {
        e.preventDefault();

        if (selectedSeats.length === 0) {
            alert("Debes seleccionar al menos un asiento");
            return;
        }
        
        const payload = {
            tickets: selectedSeats.map(seat => ({
                movie_show_id: movieShowId,
                seat_number: seat,
                unit_price: movieShow.price
            })),
            payment: {
                payment_method: paymentMethod,
                card_holder_name: cardHolderName,
                card_last_four_digits: cardLastFour
            }
        }

        setSubmitting(true);

        createOrder(payload)
          .then(res => navigate(`/success/${res.data.order_id}`))
          .catch( err => {
            if (err.response?.status === 401) {
                logout();
                navigate("/login");
                return;
            }
            const msg = err.response?.data?.detail || "Error al procesar la compra";
            alert(msg);
           })
           .finally(() => setSubmitting(false));
    }

    return (
        <form className="buy-container" onSubmit={handleSubmit}>
            <h2>Comprar entradas</h2>

            {loading && <p>Cargando función...</p>}

            {movieShow && (
                <div className="buy-section">
                    <h3>Selecciona tus asientos</h3>
                    <SeatGrid
                        rows={movieShow.room.rows}
                        seatsPerRow={movieShow.room.seats_per_row}
                        occupiedSeats={movieShow.occupied_seats}
                        selectedSeats={selectedSeats}
                        setSelectedSeats={setSelectedSeats}
                    />
                    
                    <p className="seat-info">Asientos seleccionados: {selectedSeats.join(", ")}</p>
                    <p className="total">Total: ${selectedSeats.length * movieShow.price}</p>
                </div>
            )}

            <div className="buy-section">
                <div className="payment-group">
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
                </div>
                <button className="confirm-btn" disabled={selectedSeats.length === 0 || submitting}>
                    {submitting ? "Procesando...":"Confirmar compra"}
                </button>
            </div> 
        </form>
    )
}