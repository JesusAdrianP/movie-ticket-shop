import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { getMovieById, getMovieShows, getCities } from "../services/movieService";
import { useAuth } from "../context/AuthContext";
import { parseISO } from "date-fns";
import { formatInTimeZone } from "date-fns-tz";
import { es } from "date-fns/locale";

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

    if(!movie) return <p>Cargando película</p>

    return (
        <div>
            <img src={movie.movie_poster} alt={movie.movie_name} style={{width: "300px"}} />

            <h1>{movie.movie_name}</h1>
            <p>{movie.synopsis}</p>
            <p><b>Duración: </b> {movie.length_minutes} min</p>
            <p><b>Fecha de estreno: </b> {movie.release_date}</p>
            <p><b>Género: </b> {movie.genres.map( genre => genre.genre_name).join(', ')}</p>

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
                <>
                  <h3>Funciones disponibles</h3>
                  {shows.map(show => (
                    <div key={show.id}>
                        <p>
                            {formatInTimeZone(show.show_date, "UTC", "EEEE, dd 'de' MMMM yyyy, HH:mm", {locale: es} )} | {show.cinema_id.cinema_name}
                        </p>
                        <button onClick={() => handleShow(show.id)}>Comprar entrada</button>
                    </div>
                   ))}
                </>
            )}
        </div>
    )
}