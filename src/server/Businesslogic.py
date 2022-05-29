from .bo.eventBOs.EventBO import EventBO
from .db.eventMapper.EventMapper import EventMapper
from .bo.eventBOs.ComingBO import ComingBO
from .db.eventMapper.ComingMapper import ComingMapper
from .bo.eventBOs.GoingBO import GoingBO
from .db.eventMapper.GoingMapper import GoingMapper
from .bo.eventBOs.VacationBeginBO import VacationBeginBO
from .db.eventMapper.VacationBeginMapper import VacationBeginMapper
from .bo.eventBOs.VacationEndBO import VacationEndBO
from .db.eventMapper.VacationEndMapper import VacationEndMapper
from .bo.eventBOs.IllnessBeginBO import IllnessBeginBO
from .db.eventMapper.IllnessBeginMapper import IllnessBeginMapper
from .bo.eventBOs.IllnessEndBO import IllnessEndBO
from .db.eventMapper.IllnessEndMapper import IllnessEndMapper
from .bo.eventBOs.ProjectWorkBegin import ProjectWorkBeginBO
from .db.eventMapper.ProjectWorkBeginMapper import ProjectWorkBeginMapper
from .bo.eventBOs.ProjectWorkEnd import ProjectWorkEndBO
from .db.eventMapper.ProjectWorkEndMapper import ProjectWorkEndMapper
from .bo.eventBOs.BreakBeginBO import BreakBeginBO
from .db.eventMapper.BreakBeginMapper import BreakBeginMapper
from .bo.eventBOs.BreakEndBO import BreakEndBO
from .db.eventMapper.BreakEndMapper import BreakEndMapper

from bo.eventBOs.EventBO import EventBO
from db.eventMapper.EventMapper import EventMapper
from bo.eventBOs.ComingBO import ComingBO
from db.eventMapper.ComingMapper import ComingMapper
from bo.eventBOs.GoingBO import GoingBO
from db.eventMapper.GoingMapper import GoingMapper
from bo.eventBOs.VacationBeginBO import VacationBeginBO
from db.eventMapper.VacationBeginMapper import VacationBeginMapper
from bo.eventBOs.VacationEndBO import VacationEndBO
from db.eventMapper.VacationEndMapper import VacationEndMapper
from bo.eventBOs.IllnessBeginBO import IllnessBeginBO
from db.eventMapper.IllnessBeginMapper import IllnessBeginMapper
from bo.eventBOs.IllnessEndBO import IllnessEndBO
from db.eventMapper.IllnessEndMapper import IllnessEndMapper
from bo.eventBOs.ProjectWorkBegin import ProjectWorkBeginBO
from db.eventMapper.ProjectWorkBeginMapper import ProjectWorkBeginMapper
from bo.eventBOs.ProjectWorkEnd import ProjectWorkEndBO
from db.eventMapper.ProjectWorkEndMapper import ProjectWorkEndMapper
from bo.eventBOs.BreakBeginBO import BreakBeginBO
from db.eventMapper.BreakBeginMapper import BreakBeginMapper
from bo.eventBOs.BreakEndBO import BreakEndBO
from db.eventMapper.BreakEndMapper import BreakEndMapper
from bo.eventBOs.FlexDayStart import FlexDayStartBO
from db.eventMapper.FlexDayStartMapper import FlexDayStartMapper
from bo.eventBOs.FlexDayEndBO import FlexDayEndBO
from db.eventMapper.FlexDayEndMapper import FlexDayEndMapper

from .bo.BookingBO import BookingBO
from .db.BookingMapper import BookingMapper
from .bo.EventBookingBO import EventBookingBO
from .db.EventBookingMapper import EventBookingMapper
from .bo.TimeIntervalBookingBO import TimeIntervalBookingBO
from .db.TimeIntervalBookingMapper import TimeIntervalBookingMapper

from asyncio.windows_events import NULL

from .bo.timeinterval.TimeIntervalBO import TimeIntervalBO
from .db.timeinterval.TimeIntervalMapper import TimeIntervalMapper
from .bo.timeinterval.BreakBO import BreakBO
from .db.timeinterval.BreakMapper import BreakMapper
from .bo.timeinterval.IllnessBO import IllnessBO
from .db.timeinterval.IllnessMapper import IllnessMapper
from .bo.timeinterval.ProjectDurationBO import ProjectDurationBO
from .db.timeinterval.ProjectDurationMapper import ProjectDurationMapper
from .bo.timeinterval.ProjectWorkBO import ProjectWorkBO
from .db.timeinterval.ProjectWorkMapper import ProjectWorkMapper
from .bo.timeinterval.VacationBO import VacationBO
from .db.timeinterval.VacationMapper import VacationMapper
from .bo.timeinterval.WorkBO import WorkBO
from .db.timeinterval.WorkMapper import WorkMapper
from .bo.timeinterval.FlexDayBO import FlexDayBO
from .db.timeinterval.FlexDayMapper import FlexDayMapper

from datetime import datetime
from .bo.UserBO import UserBO
from .db.UserMapper import UserMapper
from .bo.WorkTimeAccountBO import WorkTimeAccountBO
from .db.WorkTimeAccountMapper import WorkTimeAccountMapper
from .bo.ProjectBO import ProjectBO
from .db.ProjectMapper import ProjectMapper
from .bo.ProjectUserBO import ProjectUserBO
from .db.ProjectUserMapper import ProjectUserMapper
from .bo.ActivityBO import ActivityBO
from .db.ActivityMapper import ActivityMapper


class Businesslogic():

    def __init__(self):
        pass

    '''Beginn der Event-& und Evensubklassenmethoden'''
    '''Author: Khadidja Kebaili'''

    def create_event(self, type, coming_id= None, going_id= None, break_begin_id= None,  break_end_id= None,
                     illness_begin_id= None, illness_end_id= None, project_work_begin_id= None, project_work_end_id= None,
                     vacation_begin_id= None, vacation_end_id = None, flex_day_start_id = None, flex_day_end_id = None):
        event = EventBO()
        event.set_type(type),
        event.set_coming_id(coming_id),
        event.set_going_id(going_id),
        event.set_break_begin_id(break_begin_id),
        event.set_break_end_id(break_end_id),
        event.set_illness_begin_id(illness_begin_id),
        event.set_illness_end_id(illness_end_id),
        event.set_project_work_begin_id(project_work_begin_id),
        event.set_project_work_end_id(project_work_end_id),
        event.set_vacation_begin_id(vacation_begin_id),
        event.set_vacation_end_id(vacation_end_id)
        event.set_flex_day_start_id(flex_day_start_id)
        event.set_flex_day_end_id(flex_day_end_id)
        with EventMapper() as mapper:
            return mapper.insert(event)

    # Methode um ein EventBO mit bestimmter ID aus der Datenbank zu laden
    def get_event_by_id(self, number):
        with EventMapper() as mapper:
            return mapper.find_by_key(number)

    # Methode um alle EventBOs aus der Datenbank zu laden
    def get_all_events(self):
        with EventMapper() as mapper:
            return mapper.find_all()

    def get_all_events_by_type(self, type):
        events = self.get_all_events()
        events_of_type = []
        for elem in events:
            if elem.get_type == type:
                events_of_type.append(elem)
        return events_of_type

    # Methode um ein EventBOs zu updaten
    def save_event(self, event):
        with EventMapper() as mapper:
            mapper.update(event)

    # Methode um ein EventBO aus der Datenbank zu entfernen
    def delete_event(self, event):
        with EventMapper() as mapper:
            mapper.delete(event)
    # Erstellung eines ComingBOs, also wenn ein Mitarbeiter sich einstempelt.

    def create_coming(self, time):
        coming = ComingBO()
        coming.set_time(time)
        with ComingMapper() as mapper:
            mapper.insert(coming)
        co_id = coming.get_id()
        self.create_event(type='coming', coming_id=co_id)
        return coming


    # Methode um ein ComingBO mit bestimmter ID aus der Datenbank zu laden

    def get_coming_by_id(self, number):
        with ComingMapper() as mapper:
            return mapper.find_by_key(number)

    # Methode um alle ComingBOs aus der Datenbank zu laden
    def get_all_comings(self):
        with ComingMapper() as mapper:
            return mapper.find_all()

    # Methode um ein ComingBOs zu updaten
    def save_coming(self, coming):
        with ComingMapper() as mapper:
            mapper.update(coming)

    # Methode um ein ComingBO aus der Datenbank zu entfernen
    def delete_coming(self, coming):
        with ComingMapper() as mapper:
            mapper.delete(coming)

    # Erstellung eines GoingBOs, also wenn ein Mitarbeiter sich ausstempelt.
    def create_going(self, time):
        going = GoingBO()
        going.set_time(time)
        with GoingMapper() as mapper:
            mapper.insert(going)
        go_id = going.get_id()
        self.create_event(type='going', going_id=go_id)
        return going

    # Methode um ein GoingBO mit bestimmter ID aus der Datenbank zu laden
    def get_going_by_id(self, number):
        with GoingMapper() as mapper:
            return mapper.find_by_key(number)

    # Methode um alle GoingBOs aus der Datenbank zu laden
    def get_all_goings(self):
        with GoingMapper() as mapper:
            return mapper.find_all()

    # Methode um ein GoingBO zu updaten
    def save_going(self, going):
        with GoingMapper() as mapper:
            mapper.update(going)

    # Methode um ein GoingBO aus der Datenbank zu entfernen
    def delete_going(self, going):
        with GoingMapper() as mapper:
            mapper.delete(going)

    # Erstellung eines ProjectWorkBeginBOs, also wenn ein Mitarbeiter mit der Projektarbeit beginnt
    def create_project_work_begin(self, time):
        project_work_begin = ProjectWorkBeginBO()
        project_work_begin.set_time(time)
        with ProjectWorkBeginMapper() as mapper:
            mapper.insert(project_work_begin)
        prjwrk = project_work_begin.get_id()
        self.create_event(type='projectworkbegin', project_work_begin_id=prjwrk)
        return project_work_begin

    # Methode um ein ProjectWorkBeginBO mit bestimmter ID aus der Datenbank zu laden
    def get_project_work_begin_by_id(self, number):
        with ProjectWorkBeginMapper() as mapper:
            return mapper.find_by_key(number)

    # Methode um alle ProjectWorkBeginBOs aus der Datenbank zu laden
    def get_all_project_work_begins(self):
        with ProjectWorkBeginMapper() as mapper:
            return mapper.find_all()

    # Methode um ein ProjectWorkBeginBOs zu updaten
    def save_project_work_begin(self, project_work_begin):
        with ProjectWorkBeginMapper() as mapper:
            mapper.update(project_work_begin)

    # Methode um ein ProjectWorkBeginBO aus der Datenbank zu entfernen
    def delete_project_work_begin(self, project_work_begin):
        with ProjectWorkBeginMapper() as mapper:
            mapper.delete(project_work_begin)

      # Erstellung eines ProjectWorkEndBOs, also wenn ein Mitarbeiter mit der Projektarbeit aufhört

    def create_project_work_end(self, time):
        project_work_end = ProjectWorkEndBO()
        project_work_end.set_time(time)
        with ProjectWorkEndMapper() as mapper:
            mapper.insert(project_work_end)
        prjwrk = project_work_end.get_id()
        self.create_event(type='projectworkend', project_work_end_id=prjwrk)
        return project_work_end

    # Methode um ein ProjectWorkEndBO mit bestimmter ID aus der Datenbank zu laden
    def get_project_work_end_by_id(self, number):
        with ProjectWorkEndMapper() as mapper:
            return mapper.find_by_key(number)

    # Methode um alle ProjectWorkEndBOs aus der Datenbank zu laden
    def get_all_project_work_ends(self):
        with ProjectWorkEndMapper() as mapper:
            return mapper.find_all()

    # Methode um ein ProjectWorkEndBOs zu updaten
    def save_project_work_end(self, project_work_end):
        with ProjectWorkEndMapper() as mapper:
            mapper.update(project_work_end)

    # Methode um ein ProjectWorkEndBO aus der Datenbank zu entfernen
    def delete_project_work_end(self, project_work_end):
        with ProjectWorkEndMapper() as mapper:
            mapper.delete(project_work_end)

    # Erstellung eines VacationBeginBOs, also wenn ein Mitarbeiter seinen Urlaub antritt

    def create_vacation_begin(self, time):
        vacation_begin = VacationBeginBO()
        vacation_begin.set_time(time)
        with VacationBeginMapper() as mapper:
            mapper.insert(vacation_begin)
        vac_begin = vacation_begin.get_id()
        self.create_event(type='vacationbegin', vacation_begin_id=vac_begin)
        return vacation_begin

    # Methode um ein VacationBeginBO mit bestimmter ID aus der Datenbank zu laden
    def get_vacation_begin_by_id(self, number):
        with VacationBeginMapper() as mapper:
            return mapper.find_by_key(number)

    # Methode um alle VacationBeginBOs aus der Datenbank zu laden
    def get_all_vacation_begins(self):
        with VacationBeginMapper() as mapper:
            return mapper.find_all()

    # Methode um ein VacationBeginBO zu updaten
    def save_vacation_begin(self, vacation_begin):
        with VacationBeginMapper() as mapper:
            mapper.update(vacation_begin)

    # Methode um ein VacationBeginBO aus der Datenbank zu entfernen
    def delete_vacation_begin(self, vacation_begin):
        with VacationBeginMapper() as mapper:
            mapper.delete(vacation_begin)

    # Erstellung eines VacationEndBOs, also wenn ein Mitarbeiter aus dem Urlaub kommt
    def create_vacation_end(self, time):
        vacation_end = VacationEndBO()
        vacation_end.set_time(time)
        with VacationEndMapper() as mapper:
            mapper.insert(vacation_end)
        vac_end = vacation_end.get_id()
        self.create_event(type='vacationend', vacation_begin_id=vac_end)
        return vacation_end

    # Methode um ein VacationEndBO mit bestimmter ID aus der Datenbank zu laden
    def get_vacation_end_by_id(self, number):
        with VacationEndMapper() as mapper:
            return mapper.find_by_key(number)

    # Methode um alle VacationEndBOs aus der Datenbank zu laden
    def get_all_vacation_ends(self):
        with VacationEndMapper() as mapper:
            return mapper.find_all()

    # Methode um ein VacationEndBO zu updaten
    def save_vacation_end(self, vacation_end):
        with VacationEndMapper() as mapper:
            mapper.update(vacation_end)

    # Methode um ein VacationEndBO aus der Datenbank zu entfernen
    def delete_vacation_end(self, vacation_end):
        with VacationEndMapper() as mapper:
            mapper.delete(vacation_end)

        # Erstellung eines IllnessBeginBOs, also der Beginn der Krankheit eines Mitarbeiters
    def create_illness_begin(self, time):
        illness_begin = IllnessBeginBO()
        illness_begin.set_time(time)
        with IllnessBeginMapper() as mapper:
            mapper.insert(illness_begin)
        ill_begin = illness_begin.get_id()
        self.create_event(type='illnessbegin', illness_begin_id=ill_begin)
        return illness_begin

    # Methode um ein IllnessBeginBO mit bestimmter ID aus der Datenbank zu laden
    def get_illness_begin_by_id(self, number):
        with IllnessBeginMapper() as mapper:
            return mapper.find_by_key(number)
        # Methode um alle IllnessBeginBOs aus der Datenbank zu laden

    def get_all_illness_begins(self):
        with IllnessBeginMapper() as mapper:
            return mapper.find_all()

        # Methode um ein IllnessBeginBO zu updaten
    def save_illness_begin(self, illness_begin):
        with IllnessBeginMapper() as mapper:
            mapper.update(illness_begin)

        # Methode um ein IllnessBeginBO aus der Datenbank zu entfernen
    def delete_illness_begin(self, illness_begin):
        with IllnessBeginMapper() as mapper:
            mapper.delete(illness_begin)

        # Erstellung eines IllnessEndBOs, also das Ende der Krankheit eines Mitarbeiters
    def create_illness_end(self, time):
        illness_end = IllnessEndBO()
        illness_end.set_time(time)
        with IllnessEndMapper() as mapper:
            mapper.insert(illness_end)
        ill_end = illness_end.get_id()
        self.create_event(type='illnessend', illness_end_id=ill_end)
        return illness_end

    # Methode um ein IllnessEndBO mit bestimmter ID aus der Datenbank zu laden
    def get_illness_end_by_id(self, number):
        with IllnessEndMapper() as mapper:
            return mapper.find_by_key(number)

    # Methode um alle IllnessEndBOs aus der Datenbank zu laden
    def get_all_illness_end(self):
        with IllnessEndMapper() as mapper:
            return mapper.find_all()

    # Methode um ein IllnessEndBO zu updaten
    def save_illness_end(self, illness_end):
        with IllnessEndMapper() as mapper:
            mapper.update(illness_end)

    # Methode um ein IllnessEndBO aus der Datenbank zu entfernen
    def delete_illness_end(self, illness_end):
        with IllnessEndMapper() as mapper:
            mapper.delete(illness_end)
        # Erstellung eines BreakEndBOs, also das Ende der Krankheit eines Mitarbeiters

    # Erstellung eines FlexDayStartBOs, also der Beginn der Gleittage eines Mitarbeiters

    def create_flex_day_start(self, time):
        flex_day_start = FlexDayStartBO()
        flex_day_start.set_time(time)
        with FlexDayStartMapper() as mapper:
            mapper.insert(flex_day_start)
        flex_begin = flex_day_start.get_id()
        self.create_event(type='flexdaystart', flex_day_start_id = flex_begin)
        return flex_day_start

    # Methode um ein FlexDayStartBO mit bestimmter ID aus der Datenbank zu laden
    def get_flex_day_start_by_id(self, number):
        with FlexDayStartMapper() as mapper:
            return mapper.find_by_key(number)

    # Methode um alle FlexDayStartBOs aus der Datenbank zu laden
    def get_all_flex_day_starts(self):
        with FlexDayStartMapper() as mapper:
            return mapper.find_all()

    # Methode um ein FlexDayStartBO zu updaten
    def save_flex_day_start(self, flex_day_start):
        with FlexDayStartMapper() as mapper:
            mapper.update(flex_day_start)

    # Methode um ein FlexDayStartBO aus der Datenbank zu entfernen
    def delete_flex_day_start(self, flex_day_start):
        with FlexDayStartMapper() as mapper:
            mapper.delete(flex_day_start)

    # Erstellung eines FlexDayEndBOs, also das Ende der Gleittage eines Mitarbeiters
    def create_flex_day_end(self, time):
        flex_day_end = FlexDayEndBO()
        flex_day_end.set_time(time)
        with FlexDayEndMapper() as mapper:
            mapper.insert(flex_day_end)
        flex_end = flex_day_end.get_id()
        self.create_event(type='flexdayend', flex_day_end_id=flex_end)
        return flex_day_end

    # Methode um ein FlexDayEndBO mit bestimmter ID aus der Datenbank zu laden
    def get_flex_day_end_by_id(self, number):
        with FlexDayEndMapper() as mapper:
            return mapper.find_by_key(number)

    # Methode um alle FlexDayEndBOs aus der Datenbank zu laden
    def get_all_flex_day_end(self):
        with FlexDayEndMapper() as mapper:
            return mapper.find_all()

    # Methode um ein FlexDayEndBO zu updaten
    def save_flex_day_end(self, flex_day_end):
        with FlexDayEndMapper() as mapper:
            mapper.update(flex_day_end)

    # Methode um ein FlexDayEndBO aus der Datenbank zu entfernen
    def delete_flex_day_end(self, flex_day_end):
        with FlexDayEndMapper() as mapper:
            mapper.delete(flex_day_end)
        # Erstellung eines BreakEndBOs, also das Ende der Gleittage eines Mitarbeiters

    def create_break_begin(self, time):
        break_begin = BreakBeginBO()
        break_begin.set_time(time)
        with BreakBeginMapper() as mapper:
            mapper.insert(break_begin)
        brk_begin = break_begin.get_id()
        self.create_event(type='breakbegin', break_begin_id=brk_begin)
        return break_begin

    # Methode um ein BreakBeginBO mit bestimmter ID aus der Datenbank zu laden
    def get_break_begin_by_id(self, number):
        with BreakBeginMapper() as mapper:
            return mapper.find_by_key(number)
        # Methode um alle BreakBeginBOs aus der Datenbank zu laden

    def get_all_break_begins(self):
        with BreakBeginMapper() as mapper:
            return mapper.find_all()

        # Methode um ein BreakBeginBO zu updaten

    def save_break_begin(self, break_begin):
        with BreakBeginMapper() as mapper:
            mapper.update(break_begin)

        # Methode um ein BreakBeginBO aus der Datenbank zu entfernen

    def delete_break_begin(self, break_begin):
        with BreakBeginMapper() as mapper:
            mapper.delete(break_begin)

        # Erstellung eines BreakEndBOs, also das Ende der Krankheit eines Mitarbeiters

    def create_break_end(self, time):
        break_end = BreakEndBO()
        break_end.set_time(time)
        with BreakEndMapper() as mapper:
            mapper.insert(break_end)
        brk_end = break_end.get_id()
        self.create_event(type='breakend', break_end_id=brk_end)
        return break_end

    # Methode um ein BreakEndBO mit bestimmter ID aus der Datenbank zu laden
    def get_break_end_by_id(self, number):
        with BreakEndMapper() as mapper:
            return mapper.find_by_key(number)

    # Methode um alle BreakEndBOs aus der Datenbank zu laden
    def get_all_break_ends(self):
        with BreakEndMapper() as mapper:
            return mapper.find_all()

    def get_break_end_by_timeinterval(self, start, end):
        enddate = datetime.now().fromisoformat(str(end))
        startend = datetime.now().fromisoformat(str(end))
        events = self.get_all_break_ends()
        interval = []
        for elem in events:
            if elem.get_time() >= start or elem.get_time() <= end:
                interval.append(elem)
            else:
                pass
        return interval

    # Methode um ein BreakEndBO zu updaten
    def save_break_end(self, break_end):
        with BreakEndMapper() as mapper:
            mapper.update(break_end)

    # Methode um ein BreakEndBO aus der Datenbank zu entfernen
    def delete_breakEnd(self, breakEnd):
        with BreakEndMapper() as mapper:
            mapper.delete(breakEnd)

    '''Dieser Teil ist für die Filter-Funktion im Frontend'''

    def in_between_times(self, event, start, end):
        if event >= start and event <= end:
            return event
        else:  # over midnight e.g., 23:30-04:15
            pass

    def get_all_event_subclasses(self):
        events = [self.get_all_break_ends(), self.get_all_break_begins(), self.get_all_project_work_begins(),
                  self.get_all_project_work_ends(), self.get_all_vacation_begins(
        ), self.get_all_vacation_ends(),
            self.get_all_illnessBegins(), self.get_all_illnessEnds(),
            self.get_all_comings(), self.get_all_goings()]
        return events

    def get_all_events_in_between_times(self, start, end):
        events_in_between_times = []
        events = self.get_all_event_subclasses()
        for elem in events:
            events_in_between_times.append(
                self.in_between_times(elem, start, end))

    """
    Timeinterval Methoden
    @author Ha Mi Duong (https://github.com/HamiDuong)
    """

    def get_all_timeintervals(self):
        with TimeIntervalMapper() as mapper:
            return mapper.find_all()

    def get_timeinterval_by_id(self, id):
        with TimeIntervalMapper() as mapper:
            return mapper.find_by_key(id)

    def create_timeinterval(self, type, break_id, illness_id, project_duration_id, project_work_id, vacation_id, work_id):
        timeinterval = TimeIntervalBO()
        # timeinterval.set_time_interval_booking_id(timeintervalbookingid)
        timeinterval.set_type(type)
        timeinterval.set_break_id(break_id)
        timeinterval.set_illness_id(illness_id)
        timeinterval.set_project_duration_id(project_duration_id)
        timeinterval.set_project_work_id(project_work_id)
        timeinterval.set_vacation_id(vacation_id)
        timeinterval.set_work_id(work_id)

        with TimeIntervalMapper() as mapper:
            return mapper.insert(timeinterval)

    def save_timeinterval(self, timeinterval):
        with TimeIntervalMapper() as mapper:
            return mapper.update(timeinterval)

    def delete_timeinterval(self, timeinterval):
        with TimeIntervalMapper() as mapper:
            mapper.delete(timeinterval)

    def get_timeinterval_by_type(self, type):
        with TimeIntervalMapper() as mapper:
            mapper.find_by_type(type)

    # def get_timeinterval_by_user(self, userid):
        # workaccount des aktuellen Users holen
        #workaccount = self.get_worktimeaccount_by_user_id(userid)
        # id des Workaccounts
        #id = workaccount.get_id()

        # alle TimeintervalBooking holen

        # alle Timeintervals holen

        # Subklassen holen

    def get_subclass_timeinterval_by_timeinterval(self, timeinterval):
        type = timeinterval.get_type()
        if type == 'Break':
            res = self.get_break_by_id(timeinterval.get_break_id())
        if type == 'Illness':
            res = self.get_illness_by_id(timeinterval.get_illness_id())
        if type == 'ProjectDuration':
            res = self.get_project_duration_by_id(
                timeinterval.get_project_duration_id())
        if type == 'ProjectWork':
            res = self.get_project_work_by_id(
                timeinterval.get_project_work_id())
        if type == 'Vacation':
            res = self.get_vacation_by_id(timeinterval.get_vacation_id())
        if type == 'Work':
            res = self.get_work_by_id(timeinterval.get_work_id())
        return res

    """
    Break Methoden
    @author Ha Mi Duong (https://github.com/HamiDuong)
    """

    def get_all_breaks(self):
        with BreakMapper() as mapper:
            return mapper.find_all()

    def get_break_by_id(self, id):
        with BreakMapper() as mapper:
            return mapper.find_by_key(id)

    def create_break(self, start, end, s_event, e_event):
        break_obj = BreakBO()
        break_obj.set_start(start)
        break_obj.set_end(end)
        # break_obj.set_time_interval_id(time_interval_id)
        break_obj.set_start_event(s_event)
        break_obj.set_end_event(e_event)
        break_obj.set_type("Break")

        with BreakMapper() as mapper:
            return mapper.insert(break_obj)

    def create_break_with_interval(self, start, end, s_event, e_event):
        break_obj = BreakBO()
        break_obj.set_start(start)
        break_obj.set_end(end)
        # break_obj.set_time_interval_id(time_interval_id)
        break_obj.set_start_event(s_event)
        break_obj.set_end_event(e_event)
        break_obj.set_type("Break")

        with BreakMapper() as mapper:
            return mapper.insert(break_obj)

    def save_break(self, break_obj):
        with BreakMapper as mapper:
            mapper.update(break_obj)

    def delete_break(self, break_obj):
        with BreakMapper as mapper:
            mapper.delete(break_obj)

    def get_breaks_by_date(self, date):
        with BreakMapper() as mapper:
            return mapper.find_by_date(date)

    def get_breaks_by_time_period(self, startdate, enddate):
        with BreakMapper() as mapper:
            return mapper.find_by_time_period(startdate, enddate)

    # def get_break_by_timeinterval_id(self, id):
    #     with BreakMapper() as mapper:
    #         return mapper.find_by_time_interval_id(id)

    """
    Illness Methoden
    @author Ha Mi Duong (https://github.com/HamiDuong)
    """

    def get_all_illnesses(self):
        with IllnessMapper() as mapper:
            return mapper.find_all()

    def get_illness_by_id(self, id):
        with IllnessMapper() as mapper:
            return mapper.find_by_key(id)

    def create_illness(self, start, end, startevent, endevent):
        illness = IllnessBO()
        illness.set_start(start)
        illness.set_end(end)
        # illness.set_time_interval_id(time_interval_id)
        illness.set_start_event(startevent)
        illness.set_end_event(endevent)
        illness.set_type("Illness")

        with IllnessMapper() as mapper:
            return mapper.insert(illness)

    def save_illness(self, illness):
        with IllnessMapper as mapper:
            mapper.update(illness)

    def delete_illness(self, illness):
        with IllnessMapper as mapper:
            mapper.delete(illness)

    def get_illnesses_by_date(self, date):
        with IllnessMapper() as mapper:
            return mapper.find_by_date(date)

    def get_illnesses_by_time_period(self, startdate, enddate):
        with IllnessMapper() as mapper:
            return mapper.find_by_time_period(startdate, enddate)

    # def get_vacation_by_timeinterval_id(self, id):
    #     with IllnessMapper() as mapper:
    #         return mapper.find_by_time_interval_id(id)

    """
    Vacation Methoden
    @author Ha Mi Duong (https://github.com/HamiDuong)
    """

    def get_all_vacations(self):
        with VacationMapper() as mapper:
            return mapper.find_all()

    def get_vacation_by_id(self, id):
        with VacationMapper() as mapper:
            return mapper.find_by_key(id)

    def create_vacation(self, start, end, startevent, endevent):
        vacation_obj = VacationBO()
        vacation_obj.set_start(start)
        vacation_obj.set_end(end)
        # vacation_obj.set_time_interval_id(time_interval_id)
        vacation_obj.set_start_event(startevent)
        vacation_obj.set_end_event(endevent)
        vacation_obj.set_type("Vacation")

        with VacationMapper() as mapper:
            return mapper.insert(vacation_obj)

    def save_vacation(self, vacation_obj):
        with VacationMapper as mapper:
            mapper.update(vacation_obj)

    def delete_vacation(self, vacation_obj):
        with VacationMapper as mapper:
            mapper.delete(vacation_obj)

    def get_vacations_by_date(self, date):
        with VacationMapper() as mapper:
            return mapper.find_by_date(date)

    def get_vacations_by_time_period(self, startdate, enddate):
        with VacationMapper() as mapper:
            return mapper.find_by_time_period(startdate, enddate)

    # def get_vacation_by_timeinterval_id(self, id):
    #     with VacationMapper() as mapper:
    #         return mapper.find_by_time_interval_id(id)

    """
    Work Methoden
    @author Ha Mi Duong (https://github.com/HamiDuong)
    """

    def get_all_works(self):
        with WorkMapper() as mapper:
            return mapper.find_all()

    def get_work_by_id(self, id):
        with WorkMapper() as mapper:
            return mapper.find_by_key(id)

    def create_work(self, start, end, startevent, endevent):
        work_obj = WorkBO()
        work_obj.set_start(start)
        work_obj.set_end(end)
        # work_obj.set_time_interval_id(time_interval_id)
        work_obj.set_start_event(startevent)
        work_obj.set_end_event(endevent)
        work_obj.set_type("Work")

        with WorkMapper() as mapper:
            return mapper.insert(work_obj)

    def save_work(self, work_obj):
        with WorkMapper as mapper:
            mapper.update(work_obj)

    def delete_work(self, work_obj):
        with WorkMapper as mapper:
            mapper.delete(work_obj)

    def get_works_by_date(self, date):
        with WorkMapper() as mapper:
            return mapper.find_by_date(date)

    def get_works_by_time_period(self, startdate, enddate):
        with WorkMapper() as mapper:
            return mapper.find_by_time_period(startdate, enddate)

    # def get_work_by_timeinterval_id(self, id):
    #     with WorkMapper() as mapper:
    #         return mapper.find_by_time_interval_id(id)

    """
    FlexDay Methoden
    @author Ha Mi Duong (https://github.com/HamiDuong)
    """

    def get_all_flex_days(self):
        with FlexDayMapper() as mapper:
            return mapper.find_all()

    def get_flex_day_by_id(self, id):
        with FlexDayMapper() as mapper:
            return mapper.find_by_key(id)

    def create_flex_day(self, start, end, startevent, endevent):
        work_obj = FlexDayBO()
        work_obj.set_start(start)
        work_obj.set_end(end)
        # work_obj.set_time_interval_id(time_interval_id)
        work_obj.set_start_event(startevent)
        work_obj.set_end_event(endevent)
        work_obj.set_type("Work")

        with FlexDayMapper() as mapper:
            return mapper.insert(work_obj)

    def save_flex_day(self, work_obj):
        with FlexDayMapper as mapper:
            mapper.update(work_obj)

    def delete_flex_day(self, work_obj):
        with FlexDayMapper as mapper:
            mapper.delete(work_obj)

    def get_flex_days_by_date(self, date):
        with FlexDayMapper() as mapper:
            return mapper.find_by_date(date)

    def get_flex_days_by_time_period(self, startdate, enddate):
        with FlexDayMapper() as mapper:
            return mapper.find_by_time_period(startdate, enddate)

    # def get_work_by_timeinterval_id(self, id):
    #     with WorkMapper() as mapper:
    #         return mapper.find_by_time_interval_id(id)

    """
    ProjectDuration Methoden
    @author Ha Mi Duong (https://github.com/HamiDuong)
    """

    def get_all_project_durations(self):
        with ProjectDurationMapper() as mapper:
            return mapper.find_all()

    def get_project_duration_by_id(self, id):
        with ProjectDurationMapper() as mapper:
            return mapper.find_by_key(id)

    def create_project_duration(self, start, end, startevent, endevent, project_id):
        project_duration_obj = ProjectDurationBO()
        project_duration_obj.set_start(start)
        project_duration_obj.set_end(end)
        # project_duration_obj.set_time_interval_id(time_interval_id)
        project_duration_obj.set_start_event(startevent)
        project_duration_obj.set_end_event(endevent)
        project_duration_obj.set_type("ProjectDuration")
        project_duration_obj.set_project_id(project_id)

        with ProjectDurationMapper() as mapper:
            return mapper.insert(project_duration_obj)

    def save_project_duration(self, project_duration_obj):
        with ProjectDurationMapper as mapper:
            mapper.update(project_duration_obj)

    def delete_project_duration(self, project_duration_obj):
        with ProjectDurationMapper as mapper:
            mapper.delete(project_duration_obj)

    def get_project_durations_by_date(self, date):
        with ProjectDurationMapper() as mapper:
            return mapper.find_by_date(date)

    def get_project_durations_by_time_period(self, startdate, enddate):
        with ProjectDurationMapper() as mapper:
            return mapper.find_by_time_period(startdate, enddate)

    # def get_project_duration_by_time_interval_id(self, id):
    #     with ProjectDurationMapper() as mapper:
    #         return mapper.find_by_time_interval_id(id)

    def get_project_duration_by_project_id(self, id):
        with ProjectDurationMapper() as mapper:
            return mapper.find_by_project_id(id)

    """
    ProjectWork Methoden
    @author Ha Mi Duong (https://github.com/HamiDuong)
    """

    def get_all_project_works(self):
        with ProjectWorkMapper() as mapper:
            return mapper.find_all()

    def get_project_work_by_id(self, id):
        with ProjectWorkMapper() as mapper:
            return mapper.find_by_key(id)

    def create_project_work(self, start, end, startevent, endevent, activity_id):
        project_work_obj = ProjectWorkBO()
        project_work_obj.set_start(start)
        project_work_obj.set_end(end)
        # project_work_obj.set_time_interval_id(time_interval_id)
        project_work_obj.set_start_event(startevent)
        project_work_obj.set_end_event(endevent)
        project_work_obj.set_type("ProjectWork")
        project_work_obj.set_activity_id(activity_id)

        with ProjectWorkMapper() as mapper:
            return mapper.insert(project_work_obj)

    def save_project_work(self, project_work_obj):
        with ProjectWorkMapper as mapper:
            mapper.update(project_work_obj)

    def delete_project_work(self, project_work_obj):
        with ProjectWorkMapper as mapper:
            mapper.delete(project_work_obj)

    def get_project_works_by_date(self, date):
        with ProjectWorkMapper() as mapper:
            return mapper.find_by_date(date)

    def get_project_works_by_time_period(self, startdate, enddate):
        with ProjectWorkMapper() as mapper:
            return mapper.find_by_time_period(startdate, enddate)

    # def get_project_duration_by_time_interval_id(self, id):
    #     with ProjectWorkMapper() as mapper:
    #         return mapper.find_by_time_interval_id(id)

    def get_project_works_by_activity_id(self, id):
        with ProjectWorkMapper() as mapper:
            return mapper.find_all_by_activity_id(id)

    """
    Booking Methoden @author Mihriban Dogan (https://github.com/mihriban-dogan)
    """

    def create_timeinterval_booking(self, userId, worktimeAccountId, timeintervalId, type):
        """Ein Timeinterval Booking anlegen"""

        '''Als erstes wird das TimeintervalBooking Objekt erstellt und dessen Id wird in der variable timeintervalbookingid gespeichert'''

        timeintervalbooking = TimeIntervalBookingBO()
        timeintervalbooking.set_id(1)
        timeintervalbooking.set_timeinterval_id(timeintervalId)

        with TimeIntervalBookingMapper() as mapper:
            mapper.insert(timeintervalbooking)
            timeintervalbookingid = timeintervalbooking.get_id()

        '''Jetzt wird das Booking Objekt gespeichert und die vorher gespeicherte id wird nun als Fremdschlüssel eingefügt'''

        booking = BookingBO()
        booking.set_user_id(userId)
        booking.set_work_time_account_id(worktimeAccountId)
        booking.set_type(type)
        booking.set_time_interval_booking_id(timeintervalbookingid)
        booking.set_id(1)

        with BookingMapper() as mapper:
            return mapper.insert(booking)

        # Hinzufügen der der Delta Zeitrechnung des Zeitintervalls, damit man die overtime und worktime berechnen
        # Hinzufügen der TimeintervalId von Hami nach Absprache

    def create_event_booking(self, userId, worktimeAccountId, eventId, type):
        """Ein Event Booking anlegen"""

        '''Als erstes wird das EventBooking Objekt erstellt und dessen Id wird in der variable eventbookingid gespeichert'''

        eventbooking = EventBookingBO()
        eventbooking.set_id(1)
        eventbooking.set_event_id(eventId)

        with EventBookingMapper() as mapper:
            mapper.insert(eventbooking)
            eventbookingid = eventbooking.get_id()

        '''Jetzt wird das Booking Objekt gespeichert und die vorher gespeicherte id wird nun als Fremdschlüssel eingefügt'''

        booking = BookingBO()
        booking.set_user_id(userId)
        booking.set_work_time_account_id(worktimeAccountId)
        booking.set_type(type)
        booking.set_event_booking_id(eventbookingid)
        booking.set_id(1)

        with BookingMapper() as mapper:
            return mapper.insert(booking)

        # Hinzufügen der EventId von Khadi nach Absprache

    def get_all_bookings_for_worktime_account(self, account):
        '''Als erstes werden die alle ids geholt, danach der Fremdschlüssel TimeintervalbookingId 
        und dieser wird dann in der Tabelle Timeintervalbooking eingefügt 
        und dort wird dann nach dem FK Timeintervalid gesucht'''
        with BookingMapper() as mapper:
            timeintervalbookings = mapper.find_timeinterval_bookings_by_work_time_account_id(
                account)
            print("TIMEINTERVALBOOKINGS", timeintervalbookings)

        for elem in timeintervalbookings:
            timeintervalbookingid = elem.get_time_interval_booking_id()
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_key(timeintervalbookingid)
                id = timeintervalbooking.get_timeinterval_id()
                print(id)

        '''Als erstes werden die alle ids geholt, danach der Fremdschlüssel EventbookingId 
        und dieser wird dann in der Tabelle Eventbooking eingefügt 
        und dort wird dann nach dem FK Eventid gesucht'''

        with BookingMapper() as mapper:
            eventbookings = mapper.find_event_bookings_by_work_time_account_id(
                account)
            print("Eventbookings", eventbookings)

        for elem in eventbookings:
            eventbookingid = elem.get_event_booking_id()
            with EventBookingMapper() as mapper:
                eventbooking = mapper.find_by_key(eventbookingid)
                id = eventbooking.get_event_id()
                print(id)

    def delete_timeinterval_booking(self, bookingid):

        with BookingMapper() as mapper:
            booking = mapper.find_by_key(bookingid)
            timeintervalbookingid = booking.get_time_interval_booking_id()
            mapper.delete(booking)

        with TimeIntervalBookingMapper() as mapper:
            timeintervalbooking = mapper.find_by_key(timeintervalbookingid)
            mapper.delete(timeintervalbooking)

        # # Nach Absprache mit Hami fertig machen
        # # with TimeintervalMapper() as mapper:
        #     # mapper.delete(timeintervalid)

    def delete_event_booking(self, bookingid):

        with BookingMapper() as mapper:
            booking = mapper.find_by_key(bookingid)
            eventbookingid = booking.get_event_booking_id()
            mapper.delete(booking)

        with EventBookingMapper() as mapper:
            eventbooking = mapper.find_by_key(eventbookingid)
            mapper.delete(eventbooking)

        # Nach Absprache mit Khadi auskommentieren
        # with EventMapper() as mapper:
            # mapper.delete(eventid)

    def update_timeinterval_booking(self, booking):
       # Dateoflastchange wird in der Tabelle Bookings geändert
        with BookingMapper() as mapper:
            mapper.update(booking)

        # Dateoflastchange wird in der Tabelle Timeintervalbookings geändert
        with TimeIntervalBookingMapper() as mapper:
            return mapper.update(booking)

    def update_event_booking(self, booking):
        # Dateoflastchange wird in der Tabelle Bookings geändert
        with BookingMapper() as mapper:
            mapper.update(booking)

        # Dateoflastchange wird in der Tabelle Eventbookings geändert
        with EventBookingMapper() as mapper:
            return mapper.update(booking)

    """
    User Methoden
    """

    def create_user(self, first_name, last_name, mail_adress, user_name):
        user_obj = UserBO()
        user_obj.set_first_name(first_name)
        user_obj.set_last_name(last_name)
        user_obj.set_mail_adress(mail_adress)
        user_obj.set_user_name(user_name)

        with UserMapper() as mapper:
            return mapper.insert(user_obj)

    '''def get_user_by_first_name(self, first_name):
        with UserMapper() as mapper:
            return mapper.find_by_first_name(first_name)

    def get_user_by_last_name(self, last_name):
        with UserMapper() as mapper:
            return mapper.find_by_last_name(last_name)'''

    def get_user_by_mail_adress(self, mail_adress):
        with UserMapper() as mapper:
            return mapper.find_by_mail_adress(mail_adress)

    def get_user_by_user_name(self, user_name):
        with UserMapper() as mapper:
            return mapper.find_by_user_name(user_name)

    def get_user_by_id(self, number):
        with UserMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_users(self):
        with UserMapper() as mapper:
            return mapper.find_all()

    def save_user(self, user_obj):
        with UserMapper() as mapper:
            mapper.update(user_obj)

    def delete_user(self, user_obj):
        with UserMapper() as mapper:
            mapper.delete(user_obj)

    """
    WorkTimeAccount Methoden
    """

    def create_worktimeaccount(self, user_id):
        worktimeaccount_obj = WorkTimeAccountBO()
        worktimeaccount_obj.set_user_id(user_id)
        worktimeaccount_obj.set_id(1)

        with WorkTimeAccountMapper() as mapper:
            return mapper.insert(worktimeaccount_obj)

    def get_worktimeaccount_by_user_id(self, user_id):
        with WorkTimeAccountMapper() as mapper:
            return mapper.find_by_user_id(user_id)

    def get_all_worktimeaccounts(self):
        with WorkTimeAccountMapper() as mapper:
            return mapper.find_all()

    def save_user(self, worktimeaccount_obj):
        with WorkTimeAccountMapper() as mapper:
            mapper.update(worktimeaccount_obj)

    def delete_user(self, worktimeaccount_obj):
        with WorkTimeAccountMapper() as mapper:
            mapper.delete(worktimeaccount_obj)

    # Project

    def create_project(self, name, commissioner, user_id, duration):
        project = ProjectBO()
        project.set_name(name)
        project.set_commissioner(commissioner)
        project.set_user_id(user_id)
        project.set_duration(duration)
        with ProjectMapper() as mapper:
            return mapper.insert(project)

    def get_project_by_id(self, id):
        with ProjectMapper() as mapper:
            return mapper.find_by_key(id)

    def get_all_projects(self):
        with ProjectMapper() as mapper:
            return mapper.find_all()

    def save_project(self, project):
        with ProjectMapper() as mapper:
            mapper.update(project)

    def delete_project(self, project):
        with ProjectMapper() as mapper:
            mapper.delete(project)

    def get_projects_by_user_id(self, id):
        with ProjectMapper() as mapper:
            mapper.find_projects_by_user_id(id)

    def get_by_project_name(self, name):
        with ProjectMapper() as mapper:
            mapper.find_by_project_name(name)

    def get_project_duration_by_project_id(self, id):
        with ProjectMapper() as mapper:
            return mapper.find_by_project_id(id)

    # Projectuser

    def create_projectuser(self, project_id, user_id, capacity):
        projectuser = ProjectUserBO()
        projectuser.set_project_id(project_id)
        projectuser.set_user_id(user_id)
        projectuser.set_capacity(capacity)
        with ProjectUserMapper() as mapper:
            return mapper.insert(projectuser)

    def get_projectuser_by_id(self, id):
        with ProjectUserMapper() as mapper:
            return mapper.find_by_key(id)

    def get_all_projectusers(self):
        with ProjectUserMapper() as mapper:
            return mapper.find_all()

    def save_projectuser(self, projectuser):
        with ProjectUserMapper() as mapper:
            mapper.update(projectuser)

    def delete_projectuser(self, projectuser):
        with ProjectUserMapper() as mapper:
            mapper.delete(projectuser)

    def get_all_project_members(self, project_id):
        with ProjectUserMapper() as mapper:
            mapper.find_all_project_members(project_id)

    # Activity

    def create_activity(self, name, capacity, project_id):
        activity = ActivityBO()
        activity.set_name(name)
        activity.set_capacity(capacity)
        activity.set_project_id(project_id)
        with ActivityMapper() as mapper:
            return mapper.insert(activity)

    def get_activity_by_id(self, id):
        with ActivityMapper() as mapper:
            return mapper.find_by_key(id)

    def get_all_activities(self):
        with ActivityMapper() as mapper:
            return mapper.find_all()

    def save_activity(self, activity):
        with ActivityMapper() as mapper:
            mapper.update(activity)

    def delete_activity(self, activity):
        with ActivityMapper() as mapper:
            mapper.delete(activity)

    def get_by_name(self, name):
        with ActivityMapper() as mapper:
            return mapper.find_by_name(name)

    def get_all_by_project_id(self, project_id):
        with ActivityMapper() as mapper:
            return mapper.find_all_by_project_id(project_id)


#adm = Businesslogic()
'''coming = adm.get_all_comings()
going = adm.get_all_goings()
projectworkstart = adm.get_all_project_work_begins()
projectworkend = adm.get_all_project_work_ends()
vacationbegin = adm.get_all_vacation_begins()
vacationends = adm.get_all_vacation_ends()
illnessbegin = adm.get_all_vacation_begins()
illnessend = adm.get_all_vacation_ends()
flexdaystart = adm.get_all_flex_day_starts()
flexdayend = adm.get_all_flex_day_end()
breakstart = adm.get_all_break_begins()
breakend = adm.get_all_break_ends()
events = adm.get_all_events()

print(len(events))
print(len(coming))
print(len(going))
print(len(breakstart))
print(len(breakend))
print(len(flexdayend))
print(len(flexdaystart))
print(len(illnessbegin))
print(len(illnessend))
print(len(vacationbegin))
print(len(vacationends))
print(len(projectworkend))
print(len(projectworkstart))'''

'''a = adm.get_coming_by_id(1)
b = adm.get_break_end_by_id(1)
c = adm.get_break_begin_by_id(1)
d = adm.get_illness_begin_by_id(1)
e = adm.get_illness_end_by_id(1)
f = adm.get_vacation_begin_by_id(1)
g = adm.get_vacation_end_by_id(1)
h = adm.get_project_work_begin_by_id(1)
i = adm.get_project_work_end_by_id(1)
j = adm.get_going_by_id(1)
k = adm.get_flex_day_end_by_id(1)
l = adm.get_flex_day_start_by_id(1)
print(a,b,c,d,e,f,g,h,i,j)'''