from multiprocessing import Event
from bo import EventBO

class GoingBO(EventBO):
    """Klasse Going.
    Ein Going ist ein Ereignis mit einem Zeitpunkt???
    """
    def __init__(self):
        super().__init__()

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen Customer()."""
        obj = GoingBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_first_name(dictionary["time"])
        obj.set_last_name(dictionary["event_booking_id"])
        return obj
