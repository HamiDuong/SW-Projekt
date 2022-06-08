from server.bo.eventBOs import EventBO


class FlexDayStartBO(EventBO.EventBO):
    """
    Klasse IllnessBegin.
    Ein IllnessBeginBO stellt das Ereignis "Gleittagbeginn" dar bzw. wenn ein MA seine Überstunden abbauen will.
    """

    def __init__(self):
        super().__init__()
        self._time = None
        self._type = 'flexdaystart'

    def set_time(self, time):
        self._time = time

    def get_time(self):
        return self._time

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.

        Diese besteht aus der ID der Superklasse ergänzt durch den Zeitpunkt des
        des jeweiligen Events."""
        return "FlexDayStartBO {}, {}, {}, {}".format(
            self.get_id(), self.get_date_of_last_change(),
            self.get_type(), self.get_time())

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein ComingBO()."""
        obj = FlexDayStartBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["dateOfLastChange"])
        obj.set_time(dictionary["time"])
        return obj

    @staticmethod
    def from_dict_timeinterval(dictionary=dict()):
        obj = FlexDayStartBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["dateOfLastChange"])
        obj.set_time(dictionary["start"])
        return obj
