from server.bo.eventBOs import EventBO


class VacationBeginBO(EventBO.EventBO):
    """
    Klasse VacationBegin.
    Ein VacationBeginBO stellt das Ereignis "Urlaubsbeginn" dar.
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
        obj = VacationBeginBO
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["dateOfLastChange"])
        obj.set_time(dictionary["time"])
        return obj
