import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { getMovieById, getMovieShows, getCities } from "../services/movieService";
import { useAuth } from "../context/AuthContext";
import { formatReadableDate } from "../utils/date";
import "./MovieDetail.css";

export default function MovieDetail() {
    const { tokens } = useAuth()
    const navigate = useNavigate()
    const { id } = useParams()
    const [movie, setMovie] = useState(null)
    const [loading, setLoading] = useState(true)
    const [shows, setShows] = useState([])
    const [selectedCity, setSelectedCity] = useState("")
    const [cities, setCities] = useState([])

    const handleShow = (showId) => {
        if(!tokens?.access) {
            navigate("/login")
        } else {
            navigate(`/buy/${showId}`)
        }
    }
    /** loading movie info */
    useEffect(() => {
        getMovieById(id)
          .then(res => setMovie(res.data))
          .catch(err => console.error(err))
    }, [id]);

    /**Loading Cities */
    useEffect(() => {
        getCities()
          .then(res => setCities(res.data))
          .catch(err => console.error(err))
    }, []);

    /**Loading movie shows by city */
    useEffect(() => {
        if (!selectedCity) return;

        setLoading(true);

        getMovieShows(id, selectedCity)
          .then(res => setShows(res.data))
          .catch(err => console.error(err))
          .finally(() => setLoading(false))
    }, [selectedCity, id])

    if(!movie) return <p>Cargando película...</p>

    return (
        <div className="movie-detail">
            <img className="movie-poster" src={movie.movie_poster} alt={movie.movie_name}/>

            <div className="movie-info">
                <h1>{movie.movie_name}</h1>

                <div className="movie-meta">
                    <p>{movie.synopsis}</p>
                    <p><b>Duración: </b> {movie.length_minutes} min</p>
                    <p><b>Fecha de estreno: </b> {formatReadableDate(movie.release_date)}</p>
                    <p><b>Género: </b> {movie.genres.map( genre => genre.genre_name).join(', ')}</p>
                </div>

                <h3>Selecciona una ciudad</h3>
                <select
                    value={selectedCity}
                    onChange={(e) => setSelectedCity(e.target.value)}
                >
                    <option value="">Selecciona una ciudad</option>
                    {cities.map(city => (
                        <option key={city.id} value={city.id}>
                            {city.city_name}
                        </option>
                    ))}
                </select>

                {loading && <p>Cargando funciones...</p>}

                {!loading && selectedCity && shows.length === 0 && (
                    <p>No hay funciones disponibles en esta ciudad</p>
                )}

                {!loading && shows.length > 0 && (
                    <div className="show-list">
                        {shows.map(show => (
                            <div className="show-card" key={show.id}>
                                <p className="show-card-text">
                                    {formatReadableDate(show.show_date)} |{" "} 
                                    {show.room.cinema.cinema_name}
                                </p>
                                <button onClick={() => handleShow(show.id)}>
                                    Comprar entrada
                                </button>
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
}