from server.bo import TimeIntervallBO as ti

"""
@author Ha Mi Duong (https://github.com/HamiDuong)
ProjectDurationBO ist eine Subklasse von TimeIntervallBO und stellt die Laufzeit eines Projekts da
Weil TimeIntervallBO bereits von BusinessObject erbt, muss diese Klasse nicht nochmal importiert werden
"""
class ProjectDurationBO (ti.TimeIntervallBO):
    """
    Konstruktor der Klasse TimeIntervallBO
    geerbte Attribute
        _id (BusinessObject -> TimeIntervallBO)
        _start: Startpunkt des Zeitintervalls (TimeIntervallBO)
        _end: Enpunkt des Zeitintervalls (TimeIntervallBO)
        _time_intervall_booking_id: Fremdschlüssel zum Objekt TimeIntervallBookingBO für die eindeutige
                                    Zuordnung zwischen Intervallbuchung und Zeitintervall (TimeIntervallBO)
    Attribute
        _project_id: Fremdschlüssel zum Object ProjectBO für die eindeutige Zuordnung zwischen Projektdauer und Projekt
    """
    def __init__(self):
        super().__init__()
        self._project_id = 0

    'Getter und Setter Methoden'
    def get_project_id(self):
        return self._project_id

    def set_project_id(self, id):
        self._project_id = id

    'Gibt die Werte eines Objekts der Klasse in Textform zurück'
    def __str__(self):
        return "ProjectDuration {}, von {} bist {}, von Projekt {}".format(self.get_id(), self.get_start(), self.get_end(), self.get_project_id())

    'wandelt ein Python dict() in ein ProjectDurationBO'
    def from_dict(dictionary=dict()):
        obj = ProjectDurationBO()
        obj.set_id(dictionary["id"])
        obj.set_start(dictionary["start"])
        obj.set_end(dictionary["end"])
        obj.set_time_intervall_booking_id(dictionary["time_intervall_booking_id"])
        obj.set_project_id(dictionary["project_id"])
        return obj