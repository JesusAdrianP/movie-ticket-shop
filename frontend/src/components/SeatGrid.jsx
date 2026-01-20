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
        <div>
            {rows.map(row => (
                <div key={row} style={{ display: "flex"}}>
                    {Array.from({ length: seatsPerRow }).map((_, i) => {
                        const seat = `${row}${i + 1}`;
                        const isSelected = selectedSeats.includes(seat);
                        const isOccupied =  occupiedSeats.includes(seat);

                        return(
                            <button key={seat} type="button" disabled={isOccupied} onClick={() => toggleSeat(seat)}
                              style={{
                                margin:4, 
                                width:35, 
                                height:35, 
                                backgroundColor: isOccupied
                                  ? "#aaa"
                                  :isSelected
                                  ? "#4caf50"
                                  :"#eee"}}>
                                {seat}
                            </button>
                        )
                    })}
                </div>
            ))}
        </div>
    )
}