import { useEffect } from "react";
import { getMovies } from "../services/movieService";

function Home() {
    useEffect(() => {
        getMovies().then( res => console.log(res.data));
    }, []);

    return <h1>Películas disponibles</h1>
}

export default Home;