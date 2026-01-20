import { publicApi } from "../api/publicApi";

export const loginUser = (data) => {
    return publicApi.post("users/login", data)
}

export const registerUser = (data) => {
    return publicApi.post("users/create", data)
}