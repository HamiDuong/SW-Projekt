from server.bo.timeinterval import TimeIntervalBO as ti

class WorkBO (ti.TimeIntervalBO):
    """
    Konstruktor der Klasse WorkBO
    geerbte Attribute
        _id (BusinessObject -> TimeIntervalBO)
        _date_of_last_change (BusinessObject -> TimeIntervalBO)
        _start: Startpunkt des Zeitintervalls (TimeIntervalBO)
        _end: Enpunkt des Zeitintervalls (TimeIntervalBO)
        #_time_interval_id: Fremdschlüssel zu TimeIntervalBO
        _start_event: Fremdschlüssel zum ComingBO
        _end_event: Fremdschlüssel zum GoingBO
        _type: Art der Subklasse, hier: Work
    """
    def __init__(self):
        super().__init__()
        self.set_type("Work")

    'Gibt die Werte eines Objekts der Klasse in Textform zurück'
    def __str__(self):
        return "Arbeit {}: von {} bis {}, Startevent: {}, Endevent: {}".format(self.get_id(), self.get_start(), self.get_end(), self.get_start_event(), self.get_end_event())

    'wandelt ein Python dict() in ein WorkBO'
    def from_dict(dictionary=dict()):
        obj = WorkBO()
        obj.set_id(dictionary["id"])
        obj.set_date_of_last_change(dictionary["date_of_last_change"])
        obj.set_start(dictionary["start"])
        obj.set_end(dictionary["end"])
        #obj.set_time_interval_id(dictionary["time_intervall_id"])
        obj.set_start_event(dictionary["start_event"])
        obj.set_end_event(dictionary["end_event"])
        obj.set_type(dictionary["type"])
        return obj