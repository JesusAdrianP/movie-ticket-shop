import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import Movies from "../pages/Movies";
import MovieDetail from "../pages/MovieDetail";
import Login from "../pages/Login";
import Register from "../pages/Register";
import Buy from "../pages/Buy";
import Success from "../pages/Success";

export default function AppRouter() {
    return (
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Movies/>} />
            <Route path="/movies/:id" element={<MovieDetail/>} />
            <Route path="/login" element={<Login/>} />
            <Route path="/register" element={<Register/>} />
            <Route path="/buy/:movieShowId" element={<Buy/>} />
            <Route path="/success" element={<Success/>} />
          </Routes>
        </BrowserRouter>
    )
}