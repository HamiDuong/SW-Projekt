from bo import BusinessObject

class EventBO(BusinessObject):
    """Klasse Event.
    Ein Event ist ein Ereignis mit einem Zeitpunkt???
    """
    def __init__(self):
        super().__init__()
        self._time = None
        self._event_booking_id = None

    def get_time(self):
        """Auslesen der ID."""
        return self._time

    def set_time(self, datetime):
        """Setzen der ID."""
        self._time = datetime

    def get_booking_id(self):
        """Auslesen der Ereignisbuchung-ID."""
        return self._event_booking_id

    def set_booking_id(self, booking_id):
        """Setzen der Ereignisbuchung-ID."""
        self._event_booking_id = booking_id

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.
        
        Diese besteht aus der ID der Superklasse ergänzt durch den Zeitpunkt des
        des jeweiligen Events."""
        return "Customer: {}, {}, {}, {}".format(self.get_id(), self.get_date_of_last_change(), self._time, self._event_booking_id)

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen Customer()."""
        obj = EventBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_first_name(dictionary["time"])
        obj.set_last_name(dictionary["eventbooking_id"])
        return obj
