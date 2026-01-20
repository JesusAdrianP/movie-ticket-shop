import { BrowserRouter, Routes, Route } from "react-router-dom";
import Movies from "../pages/Movies";
import MovieDetail from "../pages/MovieDetail";
import Login from "../pages/Login";
import Register from "../pages/Register";
import Buy from "../pages/Buy";
import Success from "../pages/Success";
import { PrivateRoute } from "./PrivateRoute";
import MyOrders from "../pages/MyOrders";
import Navbar from "../components/Navbar";

export default function AppRouter() {
    return (
        <BrowserRouter>
          <Navbar/>
          <Routes>
            <Route path="/" element={<Movies/>} />
            <Route path="/movies/:id" element={<MovieDetail/>} />
            <Route path="/login" element={<Login/>} />
            <Route path="/register" element={<Register/>} />
            <Route element={<PrivateRoute/>}>
              <Route path="/buy/:movieShowId" element={<Buy/>} />
            </Route>
            <Route element={<PrivateRoute/>}>
              <Route path="/my-orders" element={<MyOrders/>} />
            </Route>
            <Route element={<PrivateRoute/>}>
              <Route path="/success/:orderId" element={<Success/>} />
            </Route>
          </Routes>
        </BrowserRouter>
    )
}