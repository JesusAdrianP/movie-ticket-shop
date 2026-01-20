import { createContext, useContext, useState } from "react";

const AuthContext = createContext();

export function AuthProvider({ children }) {
    const [tokens, setTokens] = useState(() => {
        const stored = localStorage.getItem("authTokens");
        return stored ? JSON.parse(stored) : null;
    });

    const login =  (newTokens) => {
        localStorage.setItem("authTokens", JSON.stringify(newTokens));
        setTokens(newTokens);
    }

    const logout = () => {
        localStorage.removeItem("authTokens");
        setTokens(null);
    }

    return (
        <AuthContext.Provider value={{ tokens, login, logout}}>
            {children}
        </AuthContext.Provider>
    )
}

export const useAuth = () => useContext(AuthContext);