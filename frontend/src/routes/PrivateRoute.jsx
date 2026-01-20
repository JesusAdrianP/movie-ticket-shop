import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export const PrivateRoute = () => {
    const { tokens } = useAuth();
    return tokens?.access ? <Outlet /> : <Navigate to={"/login"} />;
}