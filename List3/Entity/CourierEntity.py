from List3.Entity.ParcelEntity import ParcelEntity


class CourierEntity:
    ID = None
    city = ''
    isAvailable = ''
    parcel = None

    def __init__(self, courier_id, city, available, parcel):
        self.ID = courier_id
        self.city = city
        self.isAvailable = available
        self.parcel = parcel

    def __str__(self) -> str:
        return f"Courier ID: {self.ID}\n" \
               f"City: {self.city}\n" \
               f"isAvailable: {self.isAvailable}\n" \
               f"Parcel: [{self.parcel}]"
