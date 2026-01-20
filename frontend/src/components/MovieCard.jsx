import { useNavigate } from "react-router-dom";
import "./MovieCard.css";

export default function MovieCard({ movie }) {
    const navigate = useNavigate();

    return (
        <div 
          className="movie-card"
          onClick={() => navigate(`/movies/${movie.id}`)}
        >
            <img 
              src={movie.movie_poster} 
              alt={movie.movie_name}
              className="movie-card__image"
            />

            <div className="movie-card__content">
              <h3>{movie.movie_name}</h3>
            </div>
        </div>
    )
}