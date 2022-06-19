from server.bo import BusinessObject as bo

"""
@author Marco
@co-author Ha Mi Duong (https://github.com/HamiDuong)
"""


class UserBO (bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._first_name = ""  # Der Vorname des Benutzers.
        self._last_name = ""  # Der Nachname des Benutzers.
        self._mail_address = ""  # Die E-Mail-Adresse des Benutzers.
        self._google_user_id = ""

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

    def get_mail_adress(self):
        """Auslesen der E-Mail-Adresse."""
        return self._mail_adress

    def set_mail_adress(self, value):
        """Setzen der E-Mail-Adresse."""
        self._mail_adress = value

    def get_google_user_id(self):
        """Auslesen des Benutzernamens."""
        return self._google_user_id

    def set_google_user_id(self, value):
        """Setzen des Benutzernamens."""
        self._google_user_id = value

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "UserBO: Id {}, First Name {}, Last Name {}, Mail {}, GoogleId {}".format(self.get_id(), self.get_first_name(), self.get_last_name(), self.get_mail_adress(), self.get_google_user_id())

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in einen User()."""
        obj = UserBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_date_of_last_change(dictionary["dateOfLastChange"])
        obj.set_first_name(dictionary["firstName"])
        obj.set_last_name(dictionary["lastName"])
        obj.set_mail_adress(dictionary["mailAdress"])
        obj.set_google_user_id(dictionary["googleUserId"])
        return obj
