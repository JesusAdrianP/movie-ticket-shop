from django.db import transaction
from .models import Order, Ticket, Payment
from movies.models import MovieShow
from django.core.mail import send_mail
from rest_framework.exceptions import ValidationError
from .serializers import OrderSerializer
from django.utils import timezone

@transaction.atomic
def create_order_with_tickets(user, tickets_data, payment_data):
    #Obtaining movie show instance
    movie_show = MovieShow.objects.select_for_update().get(id=tickets_data[0]['movie_show_id'])
    
    #obtaining the seats selected by the user
    requested_seats = [ticket['seat_number'] for ticket in tickets_data]
    
    #Searching seats selected in occupied seats
    occupied_seats = set(
        Ticket.objects.filter(movie_show_id = movie_show, seat_number__in=requested_seats).values_list('seat_number', flat=True)
    )
    
    #if seats selected by the user is ocuppied raise error
    if occupied_seats:
        raise ValidationError({"detail": f"Asientos ocupados: {', '.join(occupied_seats)}"})
    
    #creating order
    order = Order.objects.create(
        user_id= user,
        total_amount = 0
    )
    
    total_amount = 0
    
    #creating tickets
    for ticket_data in tickets_data:
        ticket = Ticket.objects.create(
            order_id = order,
            movie_show_id_id = ticket_data['movie_show_id'],
            seat_number = ticket_data['seat_number'],
            unit_price = ticket_data['unit_price']
        )
        total_amount += ticket.unit_price
    
    #creating payment
    Payment.objects.create(
        order_id = order,
        payment_method = payment_data['payment_method'],
        card_holder_name = payment_data['card_holder_name'],
        card_last_four_digits = payment_data['card_last_four_digits'],
        status = "APPROVED"
    )
    
    #Finishing order
    order.total_amount = total_amount
    order.save()
    
    return order

def send_order_confirmation_email(order):
    """
    Function to send purchase confirmation to user email
    Serialize order data to obtain info from tickets and movie show
    """
    serializer = OrderSerializer(order)
    order_data = serializer.data
    
    purchase_date = timezone.localtime(order.created_at).strftime("%d/%m/%Y %H:%M")
    show_date = timezone.localtime(order_data['show_time']).strftime("%d/%m/%Y %H:%M")
    
    message = (
        f"Hola {order.user_id.first_name},\n\n"
        "¡Gracias por tu compra! 🎉\n\n"
        f"Estado de la orden: {order_data['status']}\n"
        f"Número de orden: #{order.id}\n"
        f"Fecha de compra: {purchase_date}\n"
        f"Película: {order_data['movie_name']}\n"
        f"Cine: {order_data['cinema_name']} - {order_data['city_name']}\n"
        f"Sala: {order_data['room_name']}\n"
        f"Función: {show_date}\n"
        f"Asientos: {', '.join(order_data['seats'])}\n"
        f"Total pagado: ${order.total_amount}\n\n"
        "\n\nSi tienes alguna inquietud, puedes consultar tus órdenes desde la aplicación.\n\n"
        "Gracias por confiar en CineApp 🎬"
    )
    
    send_mail(
        subject="Confirmación de compra",
        message=message,
        from_email=None,
        recipient_list=[order.user_id.email],
    )