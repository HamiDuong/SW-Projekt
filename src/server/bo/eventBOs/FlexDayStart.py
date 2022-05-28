from server.bo.eventBOs import EventBO


class FlexDayStartBO(EventBO.EventBO):
    """
    Klasse IllnessBegin.
    Ein IllnessBeginBO stellt das Ereignis "Gleittagbeginn" dar bzw. wenn ein MA seine Überstunden abbauen will.
    """

    def __init__(self):
        super().__init__()
        self._time = None
        self._type = 'flexdaystart'

    def set_time(self, time):
        self._time = time

    def get_time(self):
        return self._time

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein ComingBO()."""
        obj = FlexDayStartBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["date_of_last_change"])
        obj.set_time(dictionary["time"])
        return obj
