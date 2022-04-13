from server.bo import TimeIntervallBO as ti

"""
@author Ha Mi Duong (https://github.com/HamiDuong)
ProjectWorkBO ist eine Subklasse von TimeIntervallBO und stellt die aktive Arbeitszeit an einem Task eines Projekts da
Weil TimeIntervallBO bereits von BusinessObject erbt, muss diese Klasse nicht nochmal importiert werden"""
class ProjectWorkBO (ti.TimeIntervallBO):
    """
    Konstruktor der Klasse TimeIntervallBO
    geerbte Attribute
        _id (BusinessObject -> TimeIntervallBO)
        _start: Startpunkt des Zeitintervalls (TimeIntervallBO)
        _end: Enpunkt des Zeitintervalls (TimeIntervallBO)
        _time_intervall_booking_id: Fremdschlüssel zum Objekt TimeIntervallBookingBO für die eindeutige
                                    Zuordnung zwischen Intervallbuchung und Zeitintervall (TimeIntervallBO)
    Attribute
        _activity_id: Fremdschlüssel zum Objekt ActivityBO für die eindeutige Zuordnung zwischen Projektarbeit und Aktivität
        _start_event: boolean, wenn True ist der Startpunkt ein Event
        _end_event: boolean, wenn True ist der Endpunkt ein Event

    """
    def __init__(self):
        super().__init__()
        self._activity_id = None
        self._start_event = False
        self._end_event = False

    'Getter und Setter Methoden'
    def get_activity_id(self):
        return self._activity_id
    
    def set_activity_id(self, id):
        self._activity_id = id

    def get_start_event(self):
        return self._start_event

    def set_start_event(self, bool):
        self._start_event = bool

    def get_end_event(self):
        return self._end_event

    def set_end_event(self, bool):
        self._end_event = bool

    'Gibt die Werte eines Objekts der Klasse in Textform zurück'
    def __str__(self):
        return "Projektarbeit {}: von {} bis {}, Ist Start ein Event? - {}, Ist Ende ein Event? - {}, gehört zur Aktivität {}".format(self.get_id(),self.get_start(), self.get_end(), self.get_start_event(), self.get_end_event(), self.get_activity_id())

    'wandelt ein Python dict() in ein ProjectWorkBO'
    def from_dict(dictionary=dict()):
        obj = ProjectWorkBO()
        obj.set_id(dictionary["id"])
        obj.set_start(dictionary["start"])
        obj.set_end(dictionary["end"])
        obj.set_time_intervall_booking_id(dictionary["time_intervall_booking_id"])
        obj.set_activity_id(dictionary["activity_id"])
        obj.set_start_event(dictionary["start_event"])
        obj.set_end_event(dictionary["end_event"])
        return obj