from server.bo import BusinessObject as bo

"""
@author Ha Mi Duong (https://github.com/HamiDuong)

TimeIntervalBO bildet die Superklasse für BreakBO, FlexDayBO, IllnessBO, ProjectDurationBO, ProjectWorkBO, VacationBO, WorkBO
"""
class TimeIntervalBO (bo.BusinessObject):
    """
    Konstruktor der Klasse TimeIntervalBO
    geerbte Attribute
        _id                     (BusinessObject)
        _date_of_last_change    (BusinessObject)
        _type: Art des Timeintervalls (siehe Subklassen)  
    Attribute
        _start: Startpunkt des Zeitintervalls
        _end: Enpunkt des Zeitintervalls
        _start_event: Id des Events welches als Start-Event dient
        _end_event: Id des Events welches als End-Event dient 
    Fremdschlüssel
        _break_id: zu BreakBO
        _flex_day_id: zu FlexDayBO
        _illness_id: zu IllnessBO
        _project_duration_id: zu ProjectDurationBO
        _project_work_id: zu ProjectWorkBO
        _vacation_id: zu VacationBO
        _work_id: zu WorkBO
    """
    def __init__(self):
        super().__init__()
        self._type = None
    
        #Attribute für die Subklassen, werden hier nicht benötigt
        self._start = None
        self._end = None
        self._start_event = None
        self._end_event = None

        #Fremschlüssel
        self._break_id = None
        self._flex_day_id = None
        self._illness_id = None
        self._project_duration_id = None
        self._project_work_id = None
        self._vacation_id = None
        self._work_id = None

    'Getter und Setter Methoden zu den Attributen der Klasse'
    def get_type(self):
        return self._type

    def set_type(self, t):
        self._type = t


    'Methoden für die Subklassen'
    def get_start(self):
        return self._start

    def set_start(self, start):
        self._start = start

    def get_end(self):
        return self._end

    def set_end(self, end):
        self._end = end
    
    def get_start_event(self):
        return self._start_event

    def set_start_event(self, id):
        self._start_event = id
    
    def get_end_event(self):
        return self._end_event

    def set_end_event(self, id):
        self._end_event = id

    'Methoden für Fremdschlüssel'
    def get_break_id(self):
        return self._break_id

    def set_break_id(self,id):
        self._break_id = id

    def get_illness_id(self):
        return self._illness_id

    def set_illness_id(self, id):
        self._illness_id = id

    def get_project_duration_id(self):
        return self._project_duration_id

    def set_project_duration_id(self, id):
        self._project_duration_id = id

    def get_project_work_id(self):
        return self._project_work_id

    def set_project_work_id(self, id):
        self._project_work_id = id

    def get_vacation_id(self):
        return self._vacation_id

    def set_vacation_id(self, id):
        self._vacation_id = id

    def get_work_id(self):
        return self._work_id

    def set_work_id(self, id):
        self._work_id = id

    def get_flex_day_id(self):
        return self._flex_day_id

    def set_flex_day_id(self, id):
        self._flex_day_id = id

    'Gibt die Werte eines Objekts der Klasse in Textform zurück'
    def __str__(self):
        return "Timeintervall {}: Type: {}".format(self.get_id(), self.get_type())

    'wandelt ein Python dict() in ein TimeIntervallBO'
    def from_dict(dictionary=dict()):
        obj = TimeIntervalBO()
        obj.set_id(dictionary["id"])
        obj.set_date_of_last_change(dictionary["date_of_last_change"])
        obj.set_type(dictionary["type"])
        obj.set_break_id(dictionary["break_id"])
        obj.set_flex_day_id(dictionary["flex_day_id"])
        obj.set_illness_id(dictionary["illness_id"])
        obj.set_project_duration_id(dictionary["project_duration_id"])
        obj.set_project_work_id(dictionary["project_work_id"])
        obj.set_vacation_id(dictionary["vacation_id"])
        obj.set_work_id(dictionary["work_id"])

        return obj