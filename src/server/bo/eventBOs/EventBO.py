from server.bo import BusinessObject as bo


class EventBO(bo.BusinessObject):
    """Klasse Event.
    Ein Event ist ein Ereignis mit einem Zeitpunkt
    """

    def __init__(self):
        super().__init__()
        self._type = None
        self._coming_ID = 0
        self._going_ID = 0
        self._vacation_begin_ID = 0
        self._vacation_end_ID = 0
        self._illness_begin_ID = 0
        self._illness_end_ID = 0
        self._project_work_begin_ID = 0
        self._project_work_end_ID = 0
        self._break_begin_ID = 0
        self._break_end_ID = 0
        self._flex_day_end_ID = 0
        self._flex_day_start_ID = 0

    def set_type(self, type):
        """Setzen des Typs des Ereignisses"""
        self._type = type

    def get_type(self):
        return self._type

    def set_coming_id(self, coming_id):
        """Setzen der Ereignisbuchung-ID."""
        self._coming_ID = coming_id

    def get_coming_id(self):
        """Auslesen der Ereignisbuchung-ID."""
        return self._coming_ID

    def set_going_id(self, going_id):
        """Setzen der Ereignisbuchung-ID."""
        self._going_ID = going_id

    def get_going_id(self):
        """Auslesen der Ereignisbuchung-ID."""
        return self._going_ID

    def set_illness_begin_id(self, illness_begin_id):
        """Setzen der Ereignisbuchung-ID."""
        self._illness_begin_ID = illness_begin_id

    def get_illness_begin_id(self):
        """Auslesen der Ereignisbuchung-ID."""
        return self._illness_begin_ID

    def set_illness_end_id(self, illness_end_id):
        """Setzen der Ereignisbuchung-ID."""
        self._illness_end_ID = illness_end_id

    def get_illness_end_id(self):
        """Auslesen der Ereignisbuchung-ID."""
        return self._illness_end_ID

    def set_vacation_begin_id(self, vacation_begin_id):
        """Setzen der Ereignisbuchung-ID."""
        self._vacation_begin_ID = vacation_begin_id

    def get_vacation_begin_id(self):
        """Auslesen der Ereignisbuchung-ID."""
        return self._vacation_begin_ID

    def set_vacation_end_id(self, vacation_end_id):
        """Setzen der Ereignisbuchung-ID."""
        self._vacation_end_ID = vacation_end_id

    def get_vacation_end_id(self):
        """Auslesen der Ereignisbuchung-ID."""
        return self._vacation_end_ID

    def set_project_work_begin_id(self, project_work_begin_id):
        """Setzen der Ereignisbuchung-ID."""
        self._project_work_begin_ID = project_work_begin_id

    def get_project_work_begin_id(self):
        """Auslesen der Ereignisbuchung-ID."""
        return self._project_work_begin_ID

    def set_project_work_end_id(self, project_work_end_id):
        """Setzen der Ereignisbuchung-ID."""
        self._project_work_end_ID= project_work_end_id

    def get_project_work_end_id(self):
        """Auslesen der Ereignisbuchung-ID."""
        return self._project_work_end_ID

    def set_break_begin_id(self, break_begin_begin_id):
        """Setzen der Ereignisbuchung-ID."""
        self._break_begin_ID = break_begin_begin_id

    def get_break_begin_id(self):
        """Auslesen der Ereignisbuchung-ID."""
        return self._break_begin_ID

    def set_break_end_id(self, break_begin_end_id):
        """Setzen der Ereignisbuchung-ID."""
        self._break_end_ID = break_begin_end_id

    def get_break_end_id(self):
        """Auslesen der Ereignisbuchung-ID."""
        return self._break_end_ID

    def set_flex_day_start_id(self, flex_day_start_begin_id):
        """Setzen der Ereignisbuchung-ID."""
        self._flex_day_start_ID = flex_day_start_begin_id

    def get_flex_day_start_id(self):
        """Auslesen der Ereignisbuchung-ID."""
        return self._flex_day_start_ID

    def set_flex_day_end_id(self, flex_day_start_end_id):
        """Setzen der Ereignisbuchung-ID."""
        self._flex_day_end_ID = flex_day_start_end_id

    def get_flex_day_end_id(self):
        """Auslesen der Ereignisbuchung-ID."""
        return self._flex_day_end_ID

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.

        Diese besteht aus der ID der Superklasse ergänzt durch den Zeitpunkt des
        des jeweiligen Events."""
        return "EventBO {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(
                                               self.get_id(), self.get_date_of_last_change(),
                                               self.get_type(),
                                               self.get_coming_id(), self.get_going_id(),
                                               self.get_break_begin_id(),  self.get_break_end_id(),
                                               self.get_illness_begin_id(), self.get_illness_end_id(),
                                               self.get_project_work_begin_id(), self.get_project_work_end_id(),
                                               self.get_vacation_begin_id(), self.get_vacation_end_id(),
                                               self.get_flex_day_start_id(), self.get_flex_day_end_id())

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein EventBO()."""
        obj = EventBO()
        obj.set_id(dictionary["id"])  # eigentlich Teil von BusinessObject !
        obj.set_coming_id(dictionary["ComingID"])
        obj.set_going_id(dictionary["GoingID"])
        obj.set_break_begin_id(dictionary["BreakBeginID"])
        obj.set_break_end_id(dictionary["BreakEndID"])
        obj.set_illness_begin_id(dictionary["IllnessBeginID"])
        obj.set_illness_end_id(dictionary["IllnessEndID"])
        obj.set_project_work_begin_id(dictionary["ProjectWorkBeginID"])
        obj.set_project_work_end_id(dictionary["ProjectWorkEndID"])
        obj.set_vacation_begin_id(dictionary["VacationBeginID"])
        obj.set_vacation_end_id(dictionary["VacationEndID"])
        obj.set_flex_day_start_id(dictionary["FlexDayStartID"])
        obj.set_flex_day_end_id(dictionary["FlexDayEndID"])
        return obj
