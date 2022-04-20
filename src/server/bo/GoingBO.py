from multiprocessing import Event
from server.bo import EventBO


class GoingBO(EventBO.EventBO):
    """
    Klasse Going.
    Ein ComingBO stellt das Ereignis "Kommen" dar bzw. wenn ein Mitarbeiter sich ausstempelt und enthält einen Zeitpunkt.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein GoingBO()."""
        obj = GoingBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_first_name(dictionary["time"])
        obj.set_last_name(dictionary["event_booking_id"])
        return obj
