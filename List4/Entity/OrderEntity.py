class OrderEntity:
    ID = None
    receiver = ''

    def __init__(self, order_id, receiver_name):
        self.ID = order_id
        self.receiver = receiver_name

    def __str__(self) -> str:
        return f"Order ID: {self.ID}\n" \
               f"Receiver: {self.receiver}"
