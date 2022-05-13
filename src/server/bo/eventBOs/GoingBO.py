from server.bo.eventBOs import EventBO
from datetime import datetime


class GoingBO(EventBO.EventBO):
    """
    Klasse Going.
    Ein GoingBO stellt das Ereignis "Gehen" dar bzw. wenn ein Mitarbeiter sich ausstempelt und enthält einen Zeitpunkt.
    """

    def __init__(self):
        super().__init__()
        self._event_id = None

    def set_event_id(self, event_id):
        self._event_id = event_id

    def get_event_id(self):
        return self._event_id

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein GoingBO()."""
        obj = GoingBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_time(dictionary["time"])
        obj.set_event_id(dictionary["eventid"])
        return obj
