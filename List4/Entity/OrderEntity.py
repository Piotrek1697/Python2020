"""
Class that represents Order entity
"""


class OrderEntity:
    ID = None
    receiver = ''

    def __init__(self, order_id, receiver_name):
        """
        Initialize OrderEntity class

        Parameters
        ----------
        order_id : int
        receiver_name : str
        """
        self.ID = order_id
        self.receiver = receiver_name

    def __str__(self) -> str:
        return f"Order ID: {self.ID}\n" \
               f"Receiver: {self.receiver}"
