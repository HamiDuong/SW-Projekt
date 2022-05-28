from server.bo.eventBOs import EventBO


class ProjectWorkBeginBO(EventBO.EventBO):
    """
    Klasse ProjectWorkEnd.
    Ein ProjectWorkEndBO stellt das Ereignis "Beginn der Projektarbeit" dar, also wenn ein Mitarbeiter mit der Projektarbeit beginnt.
    """


    def __init__(self):
        super().__init__()
        self._time = None

    def set_time(self, time):
        self._time = time
        self._type = 'projectworkbegin'

    def get_time(self):
        return self._time

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein ComingBO()."""
        obj = ProjectWorkBeginBO
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["date_of_last_change"])
        obj.set_time(dictionary["time"])
        return obj
