from server.bo.eventBOs.EventBO import EventBO


class BreakEndBO(EventBO):
    """
    Klasse BreakBegin.
    Ein BreakBeginBO stellt das Ereignis "Kommen" dar bzw. wenn ein Mitarbeiter sich einstempelt und enthält einen Zeitpunkt
    """

    def __init__(self):
        super().__init__()
        self._time = None

    def set_time(self, time):
        self._time = time

    def get_time(self):
        return self._time

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein BreakBeginBO()."""
        obj = BreakEndBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["dateOfLastChange"])
        obj.set_time(dictionary["time"])
        return obj
