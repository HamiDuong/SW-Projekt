from server.bo.timeinterval import TimeIntervalBO as ti

"""
@author Ha Mi Duong (https://github.com/HamiDuong)

BreakBO ist eine Subklasse von TimeIntervallBO und stellt eine Arbeitspause eines Benutzers da
Weil TimeIntervalBO bereits von BusinessObject erbt, muss diese Klasse nicht nochmal importiert werden
"""
class BreakBO (ti.TimeIntervalBO):
    """
    Konstruktor der Klasse TimeIntervalBO
    geerbte Attribute
        _id (BusinessObject -> TimeIntervallBO)
        _start: Startpunkt des Zeitintervalls (TimeIntervallBO)
        _end: Enpunkt des Zeitintervalls (TimeIntervallBO)
        _time_interval_booking_id: Fremdschlüssel zum Objekt TimeIntervalBO für die eindeutige
                                    Zuordnung zwischen Intervallbuchung und Zeitintervall (TimeIntervaBO)
        _break_begin_id: Fremdschlüssel zum BreakBeginBO
        _break_end_id: Fremdschlüssel zum BreakEndBO
    """
    def __init__(self):
        super().__init__()
        self._break_begin_id = None
        self._break_end_id = None

    def get_break_begin_id(self):
        return self._break_begin_id
    
    def set_break_begin_id(self, id):
        self._break_begin_id = id

    def get_break_end_id(self):
        return self._break_end_id

    def set_break_end_id(self, id):
        self._break_end_id = id

    'Gibt die Werte eines Objekts der Klasse in Textform zurück'
    def __str__(self):
        return "Pause {}: von {} bis {}, gehört zur Intervall-Buchung mit der ID {}, Startevent: {}, Endevent: {}".format(self.get_id(), self.get_start(), self.get_end(), self.get_time_interval_booking_id(), self.get_break_begin_id(), self.get_break_end_id())

    'wandelt ein Python dict() in ein BreakBO'
    def from_dict(dictionary=dict()):
        obj = BreakBO()
        obj.set_id(dictionary["id"])
        obj.set_start(dictionary["start"])
        obj.set_end(dictionary["end"])
        obj.set_time_interval_booking_id(dictionary["time_intervall_booking_id"])
        obj.set_break_begin_id(dictionary["break_begin_id"])
        obj.set_break_end_id(dictionary["break_end_id"])
        return obj