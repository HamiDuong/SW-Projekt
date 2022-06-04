from server.bo import BusinessObject as bo

"""
@author Marco
@co-author Ha Mi Duong (https://github.com/HamiDuong)
"""
class WorkTimeAccountBO (bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._user_id = None
        self._overtime = None
        self._contract_time = None


    def get_user_id(self):
        """Auslesen der User ID ."""
        return self._user_id

    def set_user_id(self, user):
        """Setzen der User ID."""
        self._user_id = user

    def get_overtime(self):
        return self._overtime

    def set_overtime(self, value):
        self._overtime = value

    def get_contract_time(self):
        return self._contract_time

    def set_contract_time(self, value):
        self._contract_time = value

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "WorkTimeAccountBO: Id {}, User {}, Overtime {}, Contract time{}".format(self.get_id(), self.get_user_id(), self.get_overtime(), self.get_contract_time())

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen User()."""
        obj = WorkTimeAccountBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["date_of_last_change"])
        obj.set_user_id(dictionary["user_id"])
        obj.set_overtime(dictionary["overtime"])
        obj.set_contract_time(dictionary["contract_time"])
        return obj
