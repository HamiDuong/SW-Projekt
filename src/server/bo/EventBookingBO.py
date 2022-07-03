from server.bo import BookingBO as book

"""
@author Mihriban Dogan (https://github.com/mihriban-dogan)
EventBookingBo ist eine Subklasse von BookingBO und erbt dessen Atributte und Methoden
Es speichert den User und das Zeitkonto, auf dem die Event Buchungen getätigt wurden
"""


class EventBookingBO (book.BookingBO):
    """
    Konstruktor der Klasse EventBookingBO
    geerbte Attribute
        _id (BusinessObject)
        _date_of_last_change
        _event_id: Fremdschlüssel zum EventBO
    """

    def __init__(self):
        super().__init__()
        self._event_id = None  # Fremdschlüsselbeziehung
    'Gibt die Werte eines Objekts der Klasse in Textform zurück'

    def get_event_id(self):
        """Auslesen der EventId."""
        return self._event_id

    def set_event_id(self, value):
        """Setzen der EventId."""
        self._event_id = value

    def __str__(self):
        return "EventBooking {}: Hat die EventId {}".format(self.get_id(), self.get_event_id())

    'wandelt ein Python dict() in ein EventBookingBO'
    def from_dict(dictionary=dict()):
        obj = EventBookingBO()
        obj.set_id(dictionary["id"])
        obj.set_date_of_last_change(dictionary["date_of_last_change"])
        obj.set_event_id(dictionary["event_id"])
        return obj
