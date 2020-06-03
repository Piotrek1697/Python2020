class ProductEntity:
    ID = None
    name = ''
    magazine_quantity = None
    price = None

    def __init__(self, product_id, product_name, product_quantity, product_price):
        self.ID = product_id
        self.name = product_name
        self.magazine_quantity = product_quantity
        self.price = product_price

    def __str__(self) -> str:
        return f"Product ID: {self.ID}\n" \
               f"Name: : {self.name}\n" \
               f"Magazine Quantity {self.magazine_quantity}\n" \
               f"Price: {self.price}"
