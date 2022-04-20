from server.bo import EventBO


class ComingBO(EventBO.EventBO):
    """
    Klasse Coming.
    Ein ComingBO stellt das Ereignis "Kommen" dar bzw. wenn ein Mitarbeiter sich einstempelt und enthält einen Zeitpunkt
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein ComingBO()."""
        obj = ComingBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_time(dictionary["time"])
        obj.set_event_booking_id(dictionary["eventbooking_id"])
        return obj
