from server.bo.eventBOs import EventBO


class IllnessBeginBO(EventBO.EventBO):
    """
    Klasse IllnessBegin.
    Ein IllnessBeginBO stellt das Ereignis "Krankheitsbeginn" dar bzw. wenn sich ein Mitarbeiter nicht wohl fühlt und der Krankheitsverlauf beginnt.
    """

    def __init__(self):
        super().__init__()
        self._time = None

    def set_time(self, time):
        self._time = time
        self._type = 'illnessbegin'

    def get_time(self):
        return self._time

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.

        Diese besteht aus der ID der Superklasse ergänzt durch den Zeitpunkt des
        des jeweiligen Events."""
        return "IllnessBeginBO {}, {}, {}, {}".format(
                                               self.get_id(), self.get_date_of_last_change(),
                                               self.get_type(), self.get_time())
    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein ComingBO()."""
        obj = IllnessBeginBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["dateOfLastChange"])
        obj.set_time(dictionary["time"])
        return obj
