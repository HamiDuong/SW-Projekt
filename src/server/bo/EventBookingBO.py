from server.bo import BookingBO as book

"""
@author Mihriban Dogan 
EventBookingBo ist eine Subklasse von BookingBO und erbt dessen Atributte und Methoden
Es speichert den User und das Zeitkonto, auf dem die Event Buchungen getätigt wurden
"""


class EventBookingBO (book.BookingBO):
    """
    Konstruktor der Klasse EventBookingBO
    geerbte Attribute
        _id (BusinessObject)
        _date_of_last_change
        _work_time_account_id: Fremdschlüssel zum Objekt WorkTimeAccountBO für die eindeutige Zuordnung zwischen Buchung und Zeitkonto
        _user_id: Fremdschlüssel zum Objekt UserBO für die eindeutige Zuordnung zwischen Buchung und Benutzer
        _type: Stellt den Typ der Buchung dar (Ereignis)
    """

    def __init__(self):
        super().__init__()

    'Gibt die Werte eines Objekts der Klasse in Textform zurück'

    def __str__(self):
        return "EventBooking {}: Hat die Id {}, den Typ{}, gehört zum User mit der ID {} und dem Zeitkonto mit der ID {}".format(self.get_id(), self.get_type(), self.get_user_id(), self.get_work_time_account_id())

    'wandelt ein Python dict() in ein EventBookingBO'
    def from_dict(dictionary=dict()):
        obj = EventBookingBO()
        obj.set_id(dictionary["id"])
        obj.set_work_time_account_id(dictionary["work_time_account_id"])
        obj.set_user_id(dictionary["user_id"])
        obj.set_type(dictionary["type"])
        return obj
