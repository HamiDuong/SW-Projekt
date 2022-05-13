from server.bo.eventBOs import EventBO


class VacationBeginBO(EventBO.EventBO):
    """
    Klasse VacationBegin.
    Ein VacationBeginBO stellt das Ereignis "Urlaubsbeginn" dar.
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
        """Umwandeln eines Python dict() in ein VacationBeginBO()."""
        obj = VacationBeginBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_time(dictionary["time"])
        obj.set_event_id(dictionary["eventid"])
        return obj
