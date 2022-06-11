from server.bo.eventBOs import EventBO


class ProjectWorkEndBO(EventBO.EventBO):
    """
    Klasse ProjectWorkEnd.
    Ein ProjectWorkEndBO stellt das Ereignis "Ende der Projektarbeit" dar bzw. wenn ein Mitarbeiter die tatsächliche Projektarbeit beendet.
    """

    def __init__(self):
        super().__init__()
        self._time = None
        self._type = 'projectworkend'

    def set_time(self, time):
        self._time = time

    def get_time(self):
        return self._time

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.

        Diese besteht aus der ID der Superklasse ergänzt durch den Zeitpunkt des
        des jeweiligen Events."""
        return "ProjectWorkEndBO {}, {}, {}, {}".format(
            self.get_id(), self.get_date_of_last_change(),
            self.get_type(), self.get_time())

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein ComingBO()."""
        obj = ProjectWorkEndBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["dateOfLastChange"])
        obj.set_time(dictionary["time"])
        return obj

    @staticmethod
    def from_dict_timeinterval(dictionary=dict()):
        obj = ProjectWorkEndBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["dateOfLastChange"])
        obj.set_time(dictionary["end"])
        return obj
