from server.bo import BusinessObject as bo


class UserBO (bo.BusinessObject):
    
    def __init__(self):
        super().__init__()
        self._first_name = ""  # Der Vorname des Benutzers.
        self._last_name = ""  # Der Nachname des Benutzers.
        self._mail_adresse = ""  # Die E-Mail-Adresse des Benutzers.
        self._user_name = ""  # Der Username des Benutzers. 

    def get_first_name(self):
        """Auslesen des Vornamens."""
        return self._first_name

    def set_first_name(self, value):
        """Setzen des Vornamens."""
        self._first_name = value

    def get_last_name(self):
        """Auslesen des Nachnamens."""
        return self._last_name

    def set_last_name(self, value):
        """Setzen des Nachnamens."""
        self._last_name = value

    def get_mail_adresse(self):
        """Auslesen der E-Mail-Adresse."""
        return self._mail_adresse

    def set_mail_adresse(self, value):
        """Setzen der E-Mail-Adresse."""
        self._mail_adresse = value

    def get_user_name(self):
        """Auslesen des Benutzernamens."""
        return self._user_name

    def set_user_name(self, value):
        """Setzen des Benutzernamens."""
        self._user_name = value        

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "UserBO: {}, {}, {}, {}, {}".format(self.get_id(), self._first_name, self._last_name, self._mail_adresse, self._user_name)

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen User()."""
        obj = UserBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_first_name(dictionary["first_name"])
        obj.set_last_name(dictionary["last_name"])
        obj.set_mail_adresse(dictionary["mail_adresse"])
        obj.set_user_name(dictionary["user_name"])        
        return obj
