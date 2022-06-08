from server.bo import BusinessObject as bo

class ProjectBO(bo.BusinessObject):
    """Klasse Projekt.
    Ein Projekt besteht aus Projektleiter und Mitarbeiter
    """
    def __init__(self):
        super().__init__()
        self._name = None
        self._commissioner = None
        self._user_id = None

    def get_name(self):
        """Auslesen des Namen"""
        return self._name

    def set_name(self, name):
        """Setzen des Namen"""
        self._name = name

    def get_commissioner(self):
        """Auslesen des Projektleiter"""
        return self._commissioner

    def set_commissioner(self, commissioner):
        """Setzen des Projektleiter"""
        self._commissioner = commissioner

    def get_user_id(self):
        """Auslesen der User ID"""
        return self._user_id

    def set_user_id(self, user_id):
        """Setzen der User ID"""
        self._user_id = user_id

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.
        
        Diese besteht aus der ID der Superklasse ergaenzt durch die Mitarbeiter an einem Projekt."""
        return "Customer: {}, {}, {}, {}, {}, {}".format(self.get_id(), self.get_date_of_last_change(), self.get_name(), self.get_commissioner(), self.get_user_id)

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen Customer()."""
        obj = ProjectBO()
        obj.set_id(dictionary["id"])
        obj.set_date_of_last_change(dictionary["date_of_last_change"])
        obj.set_name(dictionary["name"])  
        obj.set_commissioner(dictionary["commissioner"])
        obj.set_user_id(dictionary["user_id"])
        return obj

