from server.bo import BusinessObject as bo

"""
@author Ha Mi Duong (https://github.com/HamiDuong)
TimeIntervallBO bildet die Superklasse für Break, Vacation, ProjectWork und ProjectDuration
Es speichert 2 Zeitpunkte welche den Start und Endpunkt einer Zeitspanne bilden
"""
class TimeIntervallBO (bo.BusinessObject):
    """
    Konstruktor der Klasse TimeIntervallBO
    geerbte Attribute
        _id (BusinessObject)
    Attribute
        _start: Startpunkt des Zeitintervalls
        _end: Enpunkt des Zeitintervalls
        _time_intervall_booking_id: Fremdschlüssel zum Objekt TimeIntervallBookingBO für die eindeutige Zuordnung zwischen Intervallbuchung und Zeitintervall
    """
    def __init__(self):
        super().__init__()
        self._start = None
        self._end = None
        self._time_intervall_booking_id = None

    'Getter und Setter Methoden zu den Attributen der Klasse'
    def get_start(self):
        return self._start

    def set_start(self, start):
        self._start = start

    def get_end(self):
        return self._end

    def set_end(self, end):
        self._end = end

    def get_time_intervall_booking_id(self):
        return self._time_intervall_booking_id
    
    def set_time_intervall_booking_id(self, time_intervall_booking_id):
        self._time_intervall_booking_id = time_intervall_booking_id

    'Gibt die Werte eines Objekts der Klasse in Textform zurück'
    def __str__(self):
        return "Timeintervall {}: Startpunkt {}, Endpunkt {}, gehört zur Intervall-Buchung mit der ID {}".format(self.get_id(), self.get_start(), self.get_end(), self.get_time_intervall_booking_id())

    'wandelt ein Python dict() in ein TimeIntervallBO'
    def from_dict(dictionary=dict()):
        obj = TimeIntervallBO()
        obj.set_id(dictionary["id"])
        obj.set_start(dictionary["start"])
        obj.set_end(dictionary["end"])
        obj.set_time_intervall_booking_id(dictionary["time_intervall_booking_id"])
        return obj