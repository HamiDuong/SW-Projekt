from server.bo.timeinterval import TimeIntervalBO as ti

"""
@author Ha Mi Duong (https://github.com/HamiDuong)
ProjectWorkBO ist eine Subklasse von TimeIntervalBO und stellt die aktive Arbeitszeit an einem Task eines Projekts da
Weil TimeIntervalBO bereits von BusinessObject erbt, muss diese Klasse nicht nochmal importiert werden"""
class ProjectWorkBO (ti.TimeIntervalBO):
    """
    Konstruktor der Klasse TimeIntervallBO
    geerbte Attribute
        _id (BusinessObject -> TimeIntervalBO)
        _date_of_last_change (BusinessObject -> TimeIntervalBO)
        _start: Startpunkt des Zeitintervalls (TimeIntervalBO)
        _end: Enpunkt des Zeitintervalls (TimeIntervalBO)
        _time_interval_booking_id: Fremdschlüssel zum Objekt TimeIntervalBO für die eindeutige
                                    Zuordnung zwischen Intervallbuchung und Zeitintervall (TimeIntervalBO)
        _start_event: Fremdschlüssel zum ProjectWorkBeginBO
        _end_event: Fremdschlüssel zum ProjectWorkEndBO
    Attribute
        _activity_id: Fremdschlüssel zum Objekt ActivityBO für die eindeutige Zuordnung zwischen Projektarbeit und Aktivität
    """
    def __init__(self):
        super().__init__()
        self._activity_id = None

    'Getter und Setter Methoden'
    def get_activity_id(self):
        return self._activity_id
    
    def set_activity_id(self, id):
        self._activity_id = id

    'Gibt die Werte eines Objekts der Klasse in Textform zurück'
    def __str__(self):
        return "Projektarbeit {}: von {} bis {}, gehört zur Intervall-Buchung mit der ID {}, Startevent: {}, Endevent: {}, Activity-Id: {}".format(self.get_id(), self.get_start(), self.get_end(), self.get_time_interval_booking_id(), self.get_start_event(), self.get_end_event(), self.get_activity_id())

    'wandelt ein Python dict() in ein BreakBO'
    def from_dict(dictionary=dict()):
        obj = ProjectWorkBO()
        obj.set_id(dictionary["id"])
        obj.set_date_of_last_change(dictionary["date_of_last_change"])
        obj.set_start(dictionary["start"])
        obj.set_end(dictionary["end"])
        obj.set_time_interval_booking_id(dictionary["time_intervall_booking_id"])
        obj.set_start_event(dictionary["start_event"])
        obj.set_end_event(dictionary["end_event"])
        obj.set_activity_id(dictionary["activity_id"])
        return obj