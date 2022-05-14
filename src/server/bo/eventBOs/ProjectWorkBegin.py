from server.bo.eventBOs import EventBO


class ProjectWorkBeginBO(EventBO.EventBO):
    """
    Klasse ProjectWorkEnd.
    Ein ProjectWorkEndBO stellt das Ereignis "Beginn der Projektarbeit" dar, also wenn ein Mitarbeiter mit der Projektarbeit beginnt.
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
        """Umwandeln eines Python dict() in ein ProjectWorkBeginBO()."""
        obj = ProjectWorkBeginBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_time(dictionary["time"])
        obj.set_event_id(dictionary["eventid"])
        return obj
