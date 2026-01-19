import privateApi from "../api/privateApi";

export const createOrder = (data) => {
    return privateApi.post("orders/buy/tickets", data)
}