from server.bo.eventBOs.EventBO import EventBO


class BreakBeginBO(EventBO):
    """
    Klasse BreakBegin.
    Ein BreakBeginBO stellt das Ereignis "Kommen" dar bzw. wenn ein Mitarbeiter sich einstempelt und enthält einen Zeitpunkt
    """

    def __init__(self):
        super().__init__()
        self._time = None
        self._type = 'breakbegin'

    def set_time(self, time):
        self._time = time

    def get_time(self):
        return self._time

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.

        Diese besteht aus der ID der Superklasse ergänzt durch den Zeitpunkt des
        des jeweiligen Events."""
        return "BreakBeginBO {}, {}, {}, {}".format(
                                               self.get_id(), self.get_date_of_last_change(),
                                               self.get_type(), self.get_time())

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein BreakBeginBO()."""
        obj = BreakBeginBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["date_of_last_change"])
        obj.set_time(dictionary["time"])
        return obj
