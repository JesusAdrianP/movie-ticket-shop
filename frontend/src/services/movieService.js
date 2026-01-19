import { publicApi } from "../api/publicApi";

export const getMovies = () => publicApi.get("movies/list_movies")

export const getMovieById = (id) => {
    return publicApi.get(`movies/movie/${id}`)
}

export const getMovieShows = (movie_id, city_id) => {
    return publicApi.get(`movies/movie_shows/movie/${movie_id}?city=${city_id}`)
}

export const getCities = () => publicApi.get("movies/list_cities")