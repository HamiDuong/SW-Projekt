from server.bo.eventBOs import EventBO


class IllnessBeginBO(EventBO.EventBO):
    """
    @author Khadidja Kebaili (https://github.com/KhadidjaKebaili)

    Klasse IllnessBegin.
    Ein IllnessBeginBO stellt das Ereignis "Krankheitsbeginn" dar bzw. wenn sich ein Mitarbeiter nicht wohl fühlt und der Krankheitsverlauf beginnt.
    """

    def __init__(self):
        super().__init__()
        self._time = None

    def set_time(self, time):
        """Methode um die Zeit des Krankheitsbeginn einzustellen."""
        self._time = time
        self._type = 'illnessbegin'

    def get_time(self):
        """Methode um die Zeit des Krankheitsbeginn zurückzubekommen."""
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

    @staticmethod
    def from_dict_timeinterval(dictionary=dict()):
        '''@author Mihriban Dogan (https://github.com/mihriban-dogan)'''
        obj = IllnessBeginBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["dateOfLastChange"])
        obj.set_time(dictionary["start"])
        return obj
