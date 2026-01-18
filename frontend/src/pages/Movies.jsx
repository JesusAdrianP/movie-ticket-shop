import { useEffect, useState } from "react";
import { getMovies } from "../services/movieService";
import MovieCard from "../components/MovieCard";

export default function Movies() {
    const [movies, setMovies] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        getMovies()
          .then(res => setMovies(res.data))
          .finally(() => setLoading(false))
    }, []);

    if (loading) return <p>Cargando películas...</p>

    return (
        <div>
            <h1>Cartelera</h1>

            <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(200px, 1fr))", gap:"1rem"}}>
                {movies.map(movie => (<MovieCard key={movie.id} movie={movie}/>))}
            </div>
        </div>
    );
};