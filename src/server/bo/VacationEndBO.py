from server.bo import EventBO


class VacationEndBO(EventBO.EventBO):
    """
    Klasse VacationEnd.
    Ein VacationEndBO stellt das Ereignis "Urlaubsende" dar.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein VacationEndBO()."""
        obj = VacationEndBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_time(dictionary["time"])
        obj.set_event_booking_id(dictionary["eventbooking_id"])
        return obj
