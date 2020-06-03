class OrdersProductsEntity:
    ID = None
    order = None
    product = None
    order_quantity = None

    def __init__(self, id, order, product, quantity):
        self.ID = id
        self.order = order
        self.product = product
        self.order_quantity = quantity

    def __str__(self) -> str:
        return f"ID: {self.ID}\n" \
               f"Order: {self.order}\n" \
               f"Product: {self.product}\n" \
               f"Order quantity: {self.order_quantity}"
