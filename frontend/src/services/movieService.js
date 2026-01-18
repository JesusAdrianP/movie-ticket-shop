import { publicApi } from "../api/publicApi";

export const getMovies = () => publicApi.get("movies/list_movies")