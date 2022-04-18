from server.bo import TimeIntervallBO as ti

"""
@author Ha Mi Duong (https://github.com/HamiDuong)
BreakBO ist eine Subklasse von TimeIntervallBO und stellt eine Arbeitspause eines Benutzers da
Weil TimeIntervallBO bereits von BusinessObject erbt, muss diese Klasse nicht nochmal importiert werden
"""
class BreakBO (ti.TimeIntervallBO):
    """
    Konstruktor der Klasse TimeIntervallBO
    geerbte Attribute
        _id (BusinessObject -> TimeIntervallBO)
        _start: Startpunkt des Zeitintervalls (TimeIntervallBO)
        _end: Enpunkt des Zeitintervalls (TimeIntervallBO)
        _time_intervall_booking_id: Fremdschlüssel zum Objekt TimeIntervallBookingBO für die eindeutige
                                    Zuordnung zwischen Intervallbuchung und Zeitintervall (TimeIntervallBO)
    """
    def __init__(self):
        super().__init__()

    'Gibt die Werte eines Objekts der Klasse in Textform zurück'
    def __str__(self):
        return "Pause {}: von {} bis {}, gehört zur Intervall-Buchung mit der ID {}".format(self.get_id(), self.get_start(), self.get_end(), self.get_time_intervall_booking_id())

    'wandelt ein Python dict() in ein BreakBO'
    def from_dict(dictionary=dict()):
        obj = BreakBO()
        obj.set_id(dictionary["id"])
        obj.set_start(dictionary["start"])
        obj.set_end(dictionary["end"])
        obj.set_time_intervall_booking_id(dictionary["time_intervall_booking_id"])
        return obj