from server.bo import BusinessObject as bo

"""
@author Ha Mi Duong (https://github.com/HamiDuong)
TimeIntervalBO bildet die Superklasse für Break, Vacation, ProjectWork und ProjectDuration
Es speichert 2 Zeitpunkte welche den Start und Endpunkt einer Zeitspanne bilden
"""
class TimeIntervalBO (bo.BusinessObject):
    """
    Konstruktor der Klasse TimeIntervalBO
    geerbte Attribute
        _id (BusinessObject)
        _date_of_last_change (BusinessObject)
    Attribute
        _start: Startpunkt des Zeitintervalls
        _end: Enpunkt des Zeitintervalls
        _time_interval_booking_id: Fremdschlüssel zum Objekt TimeIntervalBookingBO für die eindeutige Zuordnung zwischen Intervallbuchung und Zeitintervall
        _start_event: Id des Events welches als Start-Event dient
        _end_event: Id des Events welches als End-Event dient
        _type: Art des Timeintervalls (siehe Subklassen)
    """
    def __init__(self):
        super().__init__()
        self._type = None
        self._time_interval_booking_id = None
    
        #Attribute für die Subklassen, werden hier nicht benötigt
        self._start = None
        self._end = None
        self._time_interval_id = None
        self._start_event = None
        self._end_event = None

    'Getter und Setter Methoden zu den Attributen der Klasse'
    def get_type(self):
        return self._type

    def set_type(self, t):
        self._type = t

    def get_time_interval_booking_id(self):
        return self._time_interval_booking_id
    
    def set_time_interval_booking_id(self, time_interval_booking_id):
        self._time_interval_booking_id = time_interval_booking_id

    'Methoden für die Subklassen'
    def get_start(self):
        return self._start

    def set_start(self, start):
        self._start = start

    def get_end(self):
        return self._end

    def set_end(self, end):
        self._end = end

    def get_time_interval_id(self):
        return self._time_interval_id

    def set_time_interval_id(self, id):
        self._time_interval_id = id
    
    def get_start_event(self):
        return self._start_event

    def set_start_event(self, id):
        self._start_event = id
    
    def get_end_event(self):
        return self._end_event

    def set_end_event(self, id):
        self._end_event = id

    'Gibt die Werte eines Objekts der Klasse in Textform zurück'
    def __str__(self):
        return "Timeintervall {}: Intervall-Buchung mit der ID {}, Type: {}".format(self.get_id(),self.get_time_interval_booking_id(), self.get_type())

    'wandelt ein Python dict() in ein TimeIntervallBO'
    def from_dict(dictionary=dict()):
        obj = TimeIntervalBO()
        obj.set_id(dictionary["id"])
        obj.set_date_of_last_change(dictionary["date_of_last_change"])
        obj.set_time_interval_booking_id(dictionary["time_intervall_booking_id"])
        obj.set_type(dictionary["type"])
        return obj