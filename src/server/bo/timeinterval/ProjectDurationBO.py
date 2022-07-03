from server.bo.timeinterval import TimeIntervalBO as ti

"""
@author Ha Mi Duong (https://github.com/HamiDuong)

ProjectDurationBO ist eine Subklasse von TimeIntervallBO und stellt die Laufzeit eines Projekts da
Weil TimeIntervalBO bereits von BusinessObject erbt, muss diese Klasse nicht nochmal importiert werden
"""
class ProjectDurationBO (ti.TimeIntervalBO):

    """
    Konstruktor der Klasse ProjectDurationBO
    geerbte Attribute
        _id                                                 (BusinessObject -> TimeIntervalBO)
        _date_of_last_change                                (BusinessObject -> TimeIntervalBO)
        _start: Startpunkt des Zeitintervalls               (TimeIntervalBO)
        _end: Enpunkt des Zeitintervalls                    (TimeIntervalBO)
        _start_event: Fremdschlüssel zum ProjectBeginBO     (TimeIntervalBO)
        _end_event: Fremdschlüssel zum ProjectEndBO         (TimeIntervalBO)
        _type: Art der Subklasse, hier: "ProjectDuration"   (TimeIntervalBO)
    Attribute
        _project_id: Fremdschlüssel zum ProjectBO       
    """
    def __init__(self):
        super().__init__()
        self._project_id = None
        self.set_type("ProjectDuration")

    'Getter und Setter Methoden'
    def get_project_id(self):
        return self._project_id

    def set_project_id(self, id):
        self._project_id = id

    'Gibt die Werte eines Objekts der Klasse in Textform zurück'
    def __str__(self):
        return "Projektdauer {}: von {} bis {}, Startevent: {}, Endevent: {}, Projekt-Id: {}".format(self.get_id(), self.get_start(), self.get_end(), self.get_start_event(), self.get_end_event(), self.get_project_id())

    'wandelt ein Python dict() in ein BreakBO'
    def from_dict(dictionary=dict()):
        obj = ProjectDurationBO()
        obj.set_id(dictionary["id"])
        obj.set_date_of_last_change(dictionary["dateOfLastChange"])
        obj.set_start(dictionary["start"])
        obj.set_end(dictionary["end"])
        obj.set_start_event(dictionary["startEvent"])
        obj.set_end_event(dictionary["endEvent"])
        obj.set_type(dictionary["type"])
        obj.set_project_id(dictionary["projectId"])
        return obj
