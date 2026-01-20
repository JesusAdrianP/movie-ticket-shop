import "../styles/SeatGrid.css";

export default function SeatGrid({
    rows,
    seatsPerRow,
    occupiedSeats,
    selectedSeats,
    setSelectedSeats
}) {
    const toggleSeat = (seat) => {
        if (occupiedSeats.includes(seat)) return;

        setSelectedSeats( prev => 
            prev.includes(seat)
              ? prev.filter(s => s !== seat)
              : [...prev, seat]
        );
    };

    return (
        <div className="seat-grid">
            <div className="screen">PANTALLA</div>

            {rows.map(row => (
                <div className="seat-row" key={row}>
                    {Array.from({ length: seatsPerRow }).map((_, i) => {
                        const seat = `${row}${i + 1}`;
                        const isSelected = selectedSeats.includes(seat);
                        const isOccupied =  occupiedSeats.includes(seat);

                        return(
                            <button key={seat} type="button" disabled={isOccupied} onClick={() => toggleSeat(seat)}
                              className={`seat 
                                  ${isSelected ? "selected": ""}
                                  ${isOccupied ? "occupied": ""}`}>
                                {seat}
                            </button>
                        )
                    })}
                </div>
            ))}
        </div>
    )
}