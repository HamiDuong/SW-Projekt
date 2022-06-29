from server.bo import BookingBO as book

"""
@author Mihriban Dogan (https://github.com/mihriban-dogan)
TimeIntervalBookingBo ist eine Subklasse von BookingBO und erbt dessen Atributte und Methoden
Es speichert den User und das Zeitkonto, auf dem die Zeitintervall Buchungen getätigt wurden
"""


class TimeIntervalBookingBO (book.BookingBO):
    """
    Konstruktor der Klasse TimeIntervalBookingBO
    geerbte Attribute
        _id (BusinessObject)
        _date_of_last_change
        _time_interval_id: Fremdschlüssel zum TimeintervalBO
    """

    def __init__(self):
        super().__init__()
        self._timeinterval_id = None  # Fremdschlüsselbeziehung

    def get_timeinterval_id(self):
        """Auslesen der TimeintervalId."""
        return self._timeinterval_id

    def set_timeinterval_id(self, value):
        """Setzen der TimeintervalId."""
        self._timeinterval_id = value

    'Gibt die Werte eines Objekts der Klasse in Textform zurück'

    def __str__(self):
        return "Das TimeIntervalBooking mit der ID {}: Hat die timeintervalid {}".format(self._id, self._timeinterval_id)

    'wandelt ein Python dict() in ein TimeIntervalBookingBO'
    def from_dict(dictionary=dict()):
        obj = TimeIntervalBookingBO()
        obj.set_id(dictionary["id"])
        obj.set_date_of_last_change(dictionary["date_of_last_change"])
        obj.set_timeinterval_id(dictionary["timeinterval_id"])
        return obj
