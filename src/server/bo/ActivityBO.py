from server.bo import BusinessObject as bo

"""
@author [Vi Nam Le] (https://github.com/vinamle)
Klasse Aktivitaet.
Eine Aktivitaet gehoert zu einem Projekt und gibt an was und wie lange am Projekt gearbeitet wird
"""
class ActivityBO(bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._name = None
        self._capacity = None
        self._project_id = None
        # self._duration = None
        self._current_capacity = None

    def get_name(self):
        """Auslesen des Namen"""
        return self._name

    def set_name(self, name):
        """Setzen des Namen"""
        self._name = name

    def get_capacity(self):
        """Auslesen der Kapazitaet einer Aktivitaet"""
        return self._capacity

    def set_capacity(self, capacity):
        """Setzen der Kapazitaet einer Aktivitaet"""
        self._capacity = capacity

    def get_project_id(self):
        """Auslesen der Projekt ID"""
        return self._project_id

    def set_project_id(self, project_id):
        """Setzen der Projekt ID"""
        self._project_id = project_id

    # def get_duration(self):
    #     return self._duration

    # def set_duration(self, value):
    #     self._duration = value

    def get_current_capacity(self):
        return self._current_capacity

    def set_current_capacity(self, value):
        self._current_capacity = value

    """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz"""
    def __str__(self):
        return "Aktivität: {}, {}, {}, {}, {}, {}, {}".format(self.get_id(), self.get_date_of_last_change(), self.get_name(), self.get_capacity(), self.get_project_id(), self.get_current_capacity())
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz
        Diese besteht aus der ID der Superklasse ergänzt durch die Aktivitaeten eines Projekts."""


    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen ActivityBO()."""
        obj = ActivityBO()
        obj.set_id(dictionary["id"])
        obj.set_date_of_last_change(dictionary["dateOfLastChange"])
        obj.set_name(dictionary["name"])
        obj.set_capacity(dictionary["capacity"])
        obj.set_project_id(dictionary["projectId"])
        # obj.set_duration(dictionary["duration"])
        obj.set_current_capacity(dictionary["currentCapacity"])
        return obj