from server.bo import EventBO
from datetime import datetime


class GoingBO(EventBO.EventBO):
    """
    Klasse Going.
    Ein GoingBO stellt das Ereignis "Gehen" dar bzw. wenn ein Mitarbeiter sich ausstempelt und enthält einen Zeitpunkt.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein GoingBO()."""
        obj = GoingBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_time(dictionary["time"])
        obj.set_event_booking_id(dictionary["event_booking_id"])
        return obj
