"""
Class that represents Parcel entity
"""

from datetime import date


class ParcelEntity:
    ID = None
    sender = ''
    receiver = ''
    delivery_city = ''
    sent_date = None
    delivery_date = None

    def __init__(self, id_parcel, sender, receiver, delivery_city, sent_date, delivery_date):
        """
        Initialize ParcelEntity class

        Parameters
        -----------
        id_parcel : int
        sender : str
        receiver : str
        delivery_city : str
        sent_date : date
        delivery_date : date
        """
        self.ID = id_parcel
        self.sender = sender
        self.receiver = receiver
        self.delivery_city = delivery_city
        self.sent_date = sent_date
        self.delivery_date = delivery_date

    @staticmethod
    def parse_parcel_sent(parcel_str):
        """
        Parse string that is like: Sender,Receiver,Delivery City. To object, send date added (date.now)

        Parameters
        -----------
        parcel_str : str

        Returns
        --------
        parcel : ParcelEntity
        """
        parc = parcel_str.split(',')
        if len(parc) != 3:
            raise Exception('Input must have 3 elements separated with comma')
        return ParcelEntity(None, parc[0], parc[1], parc[2], date.today(), None)

    def __str__(self) -> str:
        return f"Parcel ID: {self.ID}\n" \
               f"Sender: {self.sender}\n" \
               f"Receiver: {self.receiver}\n" \
               f"Deliver City: {self.delivery_city}\n" \
               f"Parcel sent date: {self.sent_date}\n" \
               f"Parcel delivery: {self.delivery_date}"
