import "../styles/Movies.css";
import { useEffect, useState } from "react";
import { getMovies } from "../services/movieService";
import MovieCard from "../components/MovieCard";

export default function Movies() {
    const [movies, setMovies] = useState([]);
    const [loading, setLoading] = useState(true);

    //filters
    const [movieName, setMovieName] = useState("");

    useEffect(() => {
        setLoading(true);

        getMovies({
            movie_name: movieName
        })
          .then(res => setMovies(res.data))
          .finally(() => setLoading(false))
    }, [movieName]);

    return (
        <div className="movies-container">
            <h1>Cartelera</h1>

            <div className="movies-search">
                <input
                    type="text"
                    placeholder="Buscar película.."                  
                    value={movieName}
                    onChange={e => setMovieName(e.target.value)}
                />
            </div>

            {loading && <p>Cargando películas...</p>}

            {!loading && movies.length === 0 && (
                <p className="no-results">No se encontraron películas</p>
            )}

            <div className="movies-grid">
                {movies.map(movie => (<MovieCard key={movie.id} movie={movie}/>))}
            </div>
        </div>
    );
};