from server.bo import BusinessObject as bo

class ProjectUserBO(bo.BusinessObject):
    """Klasse Projektmitarbeiter.
    Ein Projektmitarbeiter ist Teil eines oder mehreren Projekten
    """
    def __init__(self):
        super().__init__()
        self._project_id = None
        self._user_id = None
        self._capacity = None
        self._current_capacity = None

    def get_project_id(self):
        """Auslesen der Projekt ID"""
        return self._project_id

    def set_project_id(self, project_id):
        """Setzen der Projekt ID"""
        self._project_id = project_id

    def get_user_id(self):
        """Auslesen der User ID"""
        return self._user_id

    def set_user_id(self, user_id):
        """Setzen der User ID"""
        self._user_id = user_id

    def get_capacity(self):
        """Auslesen der Kapazitaet einer Aktivitaet"""
        return self._capacity

    def set_capacity(self, capacity):
        """Setzen der Kapazitaet einer Aktivitaet"""
        self._capacity = capacity

    def get_current_capacity(self):
        return self._current_capacity

    def set_current_capacity(self, cap):
        self._current_capacity = cap

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.
        
        Diese besteht aus der ID der Superklasse ergaenzt durch die Mitarbeiter an einem Projekt."""
        return "Customer: {}, {}, {}, {}, {}, {}".format(self.get_id(), self.get_date_of_last_change(),
                                                         self.get_project_id(), self.get_user_id(),
                                                         self.get_capacity(), self.get_current_capacity())

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen Customer()."""
        obj = ProjectUserBO()
        obj.set_id(dictionary["id"])
        obj.set_date_of_last_change(dictionary["dateOfLastChange"])
        obj.set_project_id(dictionary["projectId"])
        obj.set_user_id(dictionary["userId"])
        obj.set_capacity(dictionary["capacity"])
        obj.set_current_capacity(dictionary["currentCapacity"])
        return obj