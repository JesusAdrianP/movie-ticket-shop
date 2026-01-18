from django.db import transaction
from .models import Order, Ticket, Payment
from movies.models import MovieShow

@transaction.atomic
def create_order_with_tickets(user, order_date, tickets_data, payment_data):
    #creating order
    order = Order.objects.create(
        user_id= user,
        order_date = order_date,
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
    movie_show_id = tickets_data[0]['movie_show_id']
    tickets_quantity = len(tickets_data)
    movie_show = MovieShow.objects.get(pk=movie_show_id)
    movie_show.available_seats = movie_show.available_seats - tickets_quantity
    movie_show.save()
    
    return order