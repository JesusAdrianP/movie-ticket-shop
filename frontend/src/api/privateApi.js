import axios from "axios";

const privateApi = axios.create({
    baseURL: "http://localhost:8000/",
    headers: {
        "Content-Type": "application/json",
    },
});

privateApi.interceptors.request.use((config) => {
    const stored_tokens = localStorage.getItem("authTokens");
    const access_token = stored_tokens ? JSON.parse(stored_tokens).access : null;
    if (access_token) {
        config.headers.Authorization = `Bearer ${access_token}`;
    }
    return config;
});

export default privateApi;