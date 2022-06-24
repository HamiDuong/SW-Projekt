from server.bo.eventBOs import EventBO


class IllnessEndBO(EventBO.EventBO):
    """
    @author Khadidja Kebaili (https://github.com/KhadidjaKebaili)

    Klasse IllnessEnd.
    Ein IllnessEndBO stellt das Ereignis "Krankheitsende" dar bzw. wenn ein Mitarbeiter sich wieder fit fühlt.
    """

    def __init__(self):
        super().__init__()
        self._time = None

    def set_time(self, time):
        """Methode um die Zeit der Krankheitsendung einzustellen."""
        self._time = time
        self._type = 'illnessend'

    def get_time(self):
        """Methode um die Zeit der Krankheitsendung zurückzubekommen."""
        return self._time

    def set_type(self, type):
        """Methode um den Eventtyp zu setzen."""
        self._type = type

    def get_type(self):
        """Methode um den Eventtyp zurückzubekommen."""
        return self._type

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

    @staticmethod
    def from_dict_timeinterval(dictionary=dict()):
        '''@author Mihriban Dogan (https://github.com/mihriban-dogan)'''
        obj = IllnessEndBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["dateOfLastChange"])
        obj.set_time(dictionary["end"])
        return obj
