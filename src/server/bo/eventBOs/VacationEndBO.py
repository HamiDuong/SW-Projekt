from server.bo.eventBOs import EventBO


class VacationEndBO(EventBO.EventBO):
    """
    Klasse VacationEnd.
    Ein VacationEndBO stellt das Ereignis "Urlaubsende" dar.
    """

    def __init__(self):
        super().__init__()
        self._time = None
        self._type = 'vacationend'

    def set_time(self, time):
        self._time = time

    def get_time(self):
        return self._time

    def get_type(self):
        return self._type

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein ComingBO()."""
        obj = VacationEndBO
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["date_of_last_change"])
        obj.set_time(dictionary["time"])
        return obj
