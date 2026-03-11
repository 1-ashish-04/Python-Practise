from orders.Orders import OrderService
from payments.Payments import PaymentService

class Runner:

    def run(self):
        order = OrderService()
        order.place_order("Admin")

        payment = PaymentService()
        payment.make_payment("Admin", 1000)

r = Runner()
r.run()