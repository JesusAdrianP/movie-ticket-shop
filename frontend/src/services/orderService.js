import privateApi from "../api/privateApi";

export const createOrder = (data) => {
    return privateApi.post("orders/buy/tickets", data);
}

export const getMyOrders = () => {
    return privateApi.get("/orders/my-orders");
}

export const getOrderById = (orderId) => {
    return privateApi.get(`/orders/my-order/${orderId}`)
}