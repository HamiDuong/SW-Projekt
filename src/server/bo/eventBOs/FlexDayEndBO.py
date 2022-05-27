from server.bo.eventBOs import EventBO


class FlexDayEndBO(EventBO.EventBO):
    """
    Klasse IllnessBegin.
    Ein IllnessBeginBO stellt das Ereignis "Gleittagende" dar bzw. der Tag des Abbaus beendet wird.
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
        """Umwandeln eines Python dict() in ein ComingBO()."""
        obj = FlexDayEndBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["date_of_last_change"])
        obj.set_time(dictionary["time"])
        return obj
