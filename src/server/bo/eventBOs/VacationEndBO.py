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

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.

        Diese besteht aus der ID der Superklasse ergänzt durch den Zeitpunkt des
        des jeweiligen Events."""
        return "VacationEndBO {}, {}, {}, {}".format(
                                               self.get_id(), self.get_date_of_last_change(),
                                               self.get_type(), self.get_time())
    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein ComingBO()."""
        obj = VacationEndBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["dateOfLastChange"])
        obj.set_time(dictionary["time"])
        return obj
