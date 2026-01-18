export default function MovieCard({ movie }) {
    return (
        <div style={{ border: "1px solid #add", padding: "1rem"}}>
            <img 
              src={movie.movie_poster} 
              alt={movie.movie_name}
              style={{ width: "100%", height: "250px", objectFit: "cover" }}
            />

            <h3>{movie.movie_name}</h3>
        </div>
    )
}