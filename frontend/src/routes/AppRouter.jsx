import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "../pages/Home";
import Movies from "../pages/Movies";

export default function AppRouter() {
    return (
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Movies/>} />
          </Routes>
        </BrowserRouter>
    )
}