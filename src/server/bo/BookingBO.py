from server.bo import BusinessObject as bo

"""
@author Mihriban Dogan 
BookingBO bildet die Superklasse für TimeIntervalBookingBO und EventBookingBO
Es speichert den User und das Zeitkonto, auf dem die Buchungen getätigt wurden
"""


class BookingBO (bo.BusinessObject):
    """
    Konstruktor der Klasse BookingBO
    geerbte Attribute
        _id (BusinessObject)
        _date_of_last_change
    Attribute
        _work_time_account_id: Fremdschlüssel zum Objekt WorkTimeAccountBO für die eindeutige Zuordnung zwischen Buchung und Zeitkonto
        _user_id: Fremdschlüssel zum Objekt UserBO für die eindeutige Zuordnung zwischen Buchung und Benutzer
        _type: Stellt den Typ der Buchung dar (Zeitintervall oder Ereignis)
    """

    def __init__(self):
        super().__init__()
        self._work_time_account_id = None  # Fremdschlüsselbeziehung
        self._user_id = None  # Fremdschlüsselbeziehung
        self._type = ""  # Typ der Buchung

    'Getter und Setter Methoden zu den Attributen der Klasse'

    def get_work_time_account_id(self):
        """Auslesen des Fremdschlüssels zum Zeitkonto."""
        return self._work_time_account_id

    def set_work_time_account_id(self, account):
        """Setzen des Fremdschlüssels zum Zeitkonto."""
        self._work_time_account_id = account

    def get_user_id(self):
        """Auslesen des Fremdschlüssels zum Benutzer."""
        return self._user_id

    def set_user_id(self, user):
        """Setzen des Fremdschlüssels zum Benutzer."""
        self._user_id = user

    def get_type(self):
        """Auslesen des Buchungstyp."""
        return self._type

    def set_type(self, value):
        """Setzen des Buchungstyp."""
        self._type = value

    'Gibt die Werte eines Objekts der Klasse in Textform zurück'

    def __str__(self):
        return "Booking {}: Hat die Id {}, den Typ{}, gehört zum User mit der ID {} und dem Zeitkonto mit der ID {}".format(self.get_id(), self.get_type(), self.get_user_id(), self.get_work_time_account_id())

    'wandelt ein Python dict() in ein BookingBO'
    def from_dict(dictionary=dict()):
        obj = BookingBO()
        obj.set_id(dictionary["id"])
        obj.set_work_time_account_id(dictionary["work_time_account_id"])
        obj.set_user_id(dictionary["user_id"])
        obj.set_type(dictionary["type"])
        return obj
