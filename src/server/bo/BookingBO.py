from server.bo import BusinessObject as bo

"""
@author Mihriban Dogan (https://github.com/mihriban-dogan)
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
        _event_booking_id: Fremdschlüssel zum Objekt EventBookingBO
        _time_interval_booking_id: Fremdschlüssel zum Objekt TimeIntervalBookingBOs
    """

    def __init__(self):
        super().__init__()
        self._work_time_account_id = None  # Fremdschlüsselbeziehung
        self._user_id = None  # Fremdschlüsselbeziehung
        self._type = ""  # Typ der Buchung
        self._event_booking_id = None  # Fremdschlüsselbeziehung
        self._time_interval_booking_id = None  # Fremdschlüsselbeziehung

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

    def get_time_interval_booking_id(self):
        """Auslesen des Fremdschlüssels TimeintervalBookingId."""
        return self._time_interval_booking_id

    def set_time_interval_booking_id(self, value):
        """Setzen des Fremdschlüssels TimeintervalBookingId."""
        self._time_interval_booking_id = value

    def get_event_booking_id(self):
        """Auslesen des Fremdschlüssels EventBookingId."""
        return self._event_booking_id

    def set_event_booking_id(self, value):
        """Setzen des Fremdschlüssels EventBookingId."""
        self._event_booking_id = value

    'Gibt die Werte eines Objekts der Klasse in Textform zurück'

    def __str__(self):
        return "Booking: Hat die Id {}, den Typ{}, gehört zum User mit der ID {} und dem Zeitkonto mit der ID {}, hat die timeintervalbookingid {} und eventbookingid {}".format(self.get_id(), self.get_type(), self.get_user_id(), self.get_work_time_account_id(), self.get_time_interval_booking_id(), self.get_event_booking_id())

    'wandelt ein Python dict() in ein BookingBO'
    def from_dict(dictionary=dict()):
        obj = BookingBO()
        obj.set_id(dictionary["id"])
        obj.set_date_of_last_change(dictionary["dateOfLastChange"])
        obj.set_work_time_account_id(dictionary["workTimeAccountId"])
        obj.set_user_id(dictionary["userId"])
        obj.set_type(dictionary["type"])
        obj.set_event_booking_id(dictionary["eventBookingId"])
        obj.set_time_interval_booking_id(
            dictionary["timeIntervalBookingId"])
        return obj
