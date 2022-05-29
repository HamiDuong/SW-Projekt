from server.bo.eventBOs import EventBO
from datetime import datetime


class GoingBO(EventBO.EventBO):
    """
    Klasse Going.
    Ein GoingBO stellt das Ereignis "Gehen" dar bzw. wenn ein Mitarbeiter sich ausstempelt und enthält einen Zeitpunkt.
    """

    def __init__(self):
        super().__init__()
        self._time = None
        self._type = 'going'

    def set_time(self, time):
        self._time = time

    def get_time(self):
        return self._time

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.

        Diese besteht aus der ID der Superklasse ergänzt durch den Zeitpunkt des
        des jeweiligen Events."""
        return "GoingBO {}, {}, {}, {}".format(
                                               self.get_id(), self.get_date_of_last_change(),
                                               self.get_type(), self.get_time())

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein ComingBO()."""
        obj = GoingBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["date_of_last_change"])
        obj.set_time(dictionary["time"])
        return obj
