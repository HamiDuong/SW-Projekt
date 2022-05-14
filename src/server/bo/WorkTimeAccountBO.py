from server.bo import BusinessObject as bo


class WorkTimeAccountBO (bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._user_id = None


    def get_user_id(self):
        """Auslesen der User ID ."""
        return self._user_id

    def set_user_id(self, user):
        """Setzen der User ID."""
        self._user_id = user



    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "WorkTimeAccountBO: {}, {}".format(self.get_id(), self._user_id)

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen User()."""
        obj = WorkTimeAccountBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_user_id(dictionary["user_id"])
        return obj
