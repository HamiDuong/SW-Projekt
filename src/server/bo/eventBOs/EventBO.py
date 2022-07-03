from server.bo import BusinessObject as bo


class EventBO(bo.BusinessObject):
    """
    @author Khadidja Kebaili (https://github.com/KhadidjaKebaili)

    Klasse Event.
    Ein Event ist ein Ereignis mit einem Zeitpunkt
    """

    def __init__(self):
        super().__init__()
        self._type = None
        self._coming_ID = None
        self._going_ID = None
        self._vacation_begin_ID = None
        self._vacation_end_ID = None
        self._illness_begin_ID = None
        self._illness_end_ID = None
        self._project_work_begin_ID = None
        self._project_work_end_ID = None
        self._break_begin_ID = None
        self._break_end_ID = None
        self._flex_day_end_ID = None
        self._flex_day_start_ID = None

    def set_type(self, type):
        """Methode um den Eventtyp zu setzen."""
        self._type = type

    def get_type(self):
        """Methode um den Eventtyp zurückzubekommen."""
        return self._type

    def set_coming_id(self, coming_id):
        """Setzen der Ereignisbuchung-ID für ein Kommen-Event."""
        self._coming_ID = coming_id

    def get_coming_id(self):
        """Auslesen der Ereignisbuchung-ID für ein Kommen-Event."""
        return self._coming_ID

    def set_going_id(self, going_id):
        """Setzen der Ereignisbuchung-ID für ein Gehen-Event."""
        self._going_ID = going_id

    def get_going_id(self):
        """Auslesen der Ereignisbuchung-ID für ein Gehen-Event."""
        return self._going_ID

    def set_illness_begin_id(self, illness_begin_id):
        """Setzen der Ereignisbuchung-ID für ein Krankheitsbegin-Event."""
        self._illness_begin_ID = illness_begin_id

    def get_illness_begin_id(self):
        """Auslesen der Ereignisbuchung-ID für ein Krankheitsbegin-Event."""
        return self._illness_begin_ID

    def set_illness_end_id(self, illness_end_id):
        """Setzen der Ereignisbuchung-ID für ein Krankheitsende-Event."""
        self._illness_end_ID = illness_end_id

    def get_illness_end_id(self):
        """Auslesen der Ereignisbuchung-ID für ein Krankheitsende-Event."""
        return self._illness_end_ID

    def set_vacation_begin_id(self, vacation_begin_id):
        """Setzen der Ereignisbuchung-ID für ein Urlaubsbegin-Event."""
        self._vacation_begin_ID = vacation_begin_id

    def get_vacation_begin_id(self):
        """Auslesen der Ereignisbuchung-ID für ein Urlaubsbegin-Event."""
        return self._vacation_begin_ID

    def set_vacation_end_id(self, vacation_end_id):
        """Setzen der Ereignisbuchung-ID für ein Urlaubsende-Event."""
        self._vacation_end_ID = vacation_end_id

    def get_vacation_end_id(self):
        """Auslesen der Ereignisbuchung-ID für ein Urlaubsende-Event."""
        return self._vacation_end_ID

    def set_project_work_begin_id(self, project_work_begin_id):
        """Setzen der Ereignisbuchung-ID für ein Projektarbeitsbegin-Event."""
        self._project_work_begin_ID = project_work_begin_id

    def get_project_work_begin_id(self):
        """Auslesen der Ereignisbuchung-ID für ein Projektarbeitsbegin-Event."""
        return self._project_work_begin_ID

    def set_project_work_end_id(self, project_work_end_id):
        """Setzen der Ereignisbuchung-ID für ein Projektarbeitsende-Event.."""
        self._project_work_end_ID = project_work_end_id

    def get_project_work_end_id(self):
        """Auslesen der Ereignisbuchung-ID für ein Projektarbeitsende-Event.."""
        return self._project_work_end_ID

    def set_break_begin_id(self, break_begin_begin_id):
        """Setzen der Ereignisbuchung-ID für ein Pausenbegin-Event.."""
        self._break_begin_ID = break_begin_begin_id

    def get_break_begin_id(self):
        """Auslesen der Ereignisbuchung-ID für ein Pausenbegin-Event.."""
        return self._break_begin_ID

    def set_break_end_id(self, break_begin_end_id):
        """Setzen der Ereignisbuchung-ID für ein Pausenende-Event.."""
        self._break_end_ID = break_begin_end_id

    def get_break_end_id(self):
        """Auslesen der Ereignisbuchung-ID für ein Pausenende-Event.."""
        return self._break_end_ID

    def set_flex_day_start_id(self, flex_day_start_begin_id):
        """Setzen der Ereignisbuchung-ID für ein Uberstundenabbaubegin-Event."""
        self._flex_day_start_ID = flex_day_start_begin_id

    def get_flex_day_start_id(self):
        """Auslesen der Ereignisbuchung-ID für ein Uberstundenabbaubegin-Event."""
        return self._flex_day_start_ID

    def set_flex_day_end_id(self, flex_day_start_end_id):
        """Setzen der Ereignisbuchung-ID für ein Uberstundenabbauende-Event."""
        self._flex_day_end_ID = flex_day_start_end_id

    def get_flex_day_end_id(self):
        """Auslesen der Ereignisbuchung-ID für ein Uberstundenabbauende-Event."""
        return self._flex_day_end_ID

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz.
        Diese besteht aus der ID der Superklasse ergänzt durch den Zeitpunkt des
        des jeweiligen Events."""
        return (
            "EventBO {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(
                self.get_id(),
                self.get_date_of_last_change(),
                self.get_type(),
                self.get_coming_id(),
                self.get_going_id(),
                self.get_break_begin_id(),
                self.get_break_end_id(),
                self.get_illness_begin_id(),
                self.get_illness_end_id(),
                self.get_project_work_begin_id(),
                self.get_project_work_end_id(),
                self.get_vacation_begin_id(),
                self.get_vacation_end_id(),
                self.get_flex_day_start_id(),
                self.get_flex_day_end_id(),
            )
        )

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
