import { publicApi } from "../api/publicApi";

export const getMovies = (filters = {}) => {
    const params = new URLSearchParams(filters).toString();
    return publicApi.get(`movies/list_movies?${params}`);
} 

export const getMovieById = (id) => {
    return publicApi.get(`movies/movie/${id}`)
}

export const getMovieShows = (movie_id, city_id) => {
    return publicApi.get(`movies/movie_shows/movie/${movie_id}?city=${city_id}`)
}

export const getMovieShowById = (movieShowId) => {
    return publicApi.get(`movies/movie_show/${movieShowId}`)
}

export const getCities = () => publicApi.get("movies/list_cities")