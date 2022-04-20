from server.bo.timeinterval import TimeIntervalBO as ti

"""
@author Ha Mi Duong (https://github.com/HamiDuong)
VacationBO ist eine Subklasse von TimeIntervalBO und stellt den Urlaub eines Mitarbeiters da
Weil TimeIntervalBO bereits von BusinessObject erbt, muss diese Klasse nicht nochmal importiert werden
"""
class VacationBO (ti.TimeIntervalBO):
    """
    Konstruktor der Klasse TimeIntervallBO
    geerbte Attribute
        _id (BusinessObject -> TimeIntervallBO)
        _start: Startpunkt des Zeitintervalls (TimeIntervallBO)
        _end: Enpunkt des Zeitintervalls (TimeIntervallBO)
        _time_interval_booking_id: Fremdschlüssel zum Objekt TimeIntervalBO für die eindeutige
                                    Zuordnung zwischen Intervallbuchung und Zeitintervall (TimeIntervallBO)
    """
    def __init__(self):
        super().__init__()

    'Gibt die Werte eines Objekts der Klasse in Textform zurück'
    def __str__(self):
         return "Urlaub {}: von {} bis {}, gehört zur Intervall-Buchung mit der ID {}".format(self.get_id(), self.get_start(), self.get_end(), self.get_time_interval_booking_id())

    'wandelt ein Python dict() in ein VacationBO'
    def from_dict(dictionary=dict()):
        obj = VacationBO()
        obj.set_id(dictionary["id"])
        obj.set_start(dictionary["start"])
        obj.set_end(dictionary["end"])
        obj.set_time_interval_booking_id(dictionary["time_intervall_booking_id"])
        return obj