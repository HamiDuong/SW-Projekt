from server.bo import EventBO


class VacationBeginBO(EventBO.EventBO):
    """
    Klasse VacationBegin.
    Ein VacationBeginBO stellt das Ereignis "Urlaubsbeginn" dar.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein VacationBeginBO()."""
        obj = VacationBeginBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_time(dictionary["time"])
        obj.set_event_booking_id(dictionary["eventbooking_id"])
        return obj
