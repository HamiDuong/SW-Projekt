from server.bo.timeinterval import TimeIntervalBO as ti

"""
@author Ha Mi Duong (https://github.com/HamiDuong)

FlexDayBO ist eine Subklasse von TimeIntervallBO und stellt eine Arbeitspause eines Benutzers da
Weil TimeIntervalBO bereits von BusinessObject erbt, muss diese Klasse nicht nochmal importiert werden
"""
class FlexDayBO (ti.TimeIntervalBO):

    """
    Konstruktor der Klasse IllnessBO
    geerbte Attribute                                   geerbt von
        _id                                             (BusinessObject -> TimeIntervalBO)
        _date_of_last_change                            (BusinessObject -> TimeIntervalBO)
        _start: Startpunkt des Zeitintervalls           (TimeIntervalBO)
        _end: Enpunkt des Zeitintervalls                (TimeIntervalBO)
        _start_event: Fremdschlüssel zum FlexDayBeginBO (TimeIntervalBO)
        _end_event: Fremdschlüssel zum FlexDayEndBO     (TimeIntervalBO)
        _type: Art des Intervalls - hier: "FlexDay"     (TimeIntervalBO)
    """
    def __init__(self):
        super().__init__()
        self.set_type("FlexDay")

    'Gibt die Werte eines Objekts der Klasse in Textform zurück'
    def __str__(self):
        return "FlexDay {}: von {} bis {}, Startevent: {}, Endevent: {}".format(self.get_id(), self.get_start(), self.get_end(), self.get_start_event(), self.get_end_event())

    'wandelt ein Python dict() in ein FlexDayBO'
    def from_dict(dictionary=dict()):
        obj = FlexDayBO()
        obj.set_id(dictionary["id"])
        obj.set_date_of_last_change(dictionary["dateOfLastChange"])
        obj.set_start(dictionary["start"])
        obj.set_end(dictionary["end"])
        obj.set_start_event(dictionary["startEvent"])
        obj.set_end_event(dictionary["endEvent"])
        obj.set_type(dictionary["type"])
        return obj
