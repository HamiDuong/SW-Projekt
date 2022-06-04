from server.bo.eventBOs import EventBO


class IllnessEndBO(EventBO.EventBO):
    """
    Klasse IllnessEnd.
    Ein IllnessEndBO stellt das Ereignis "Krankheitsende" dar bzw. wenn ein Mitarbeiter sich wieder fit fühlt.
    """

    def __init__(self):
        super().__init__()
        self._time = None

    def set_time(self, time):
        self._time = time
        self._type = 'illnessend'

    def get_time(self):
        return self._time

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.

        Diese besteht aus der ID der Superklasse ergänzt durch den Zeitpunkt des
        des jeweiligen Events."""
        return "IllnessEndBO {}, {}, {}, {}".format(
                                               self.get_id(), self.get_date_of_last_change(),
                                               self.get_type(), self.get_time())
    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein ComingBO()."""
        obj = IllnessEndBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["dateOfLastChange"])
        obj.set_time(dictionary["time"])
        return obj
