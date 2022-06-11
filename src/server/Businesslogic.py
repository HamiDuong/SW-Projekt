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
from .bo.eventBOs.FlexDayStart import FlexDayStartBO
from .db.eventMapper.FlexDayStartMapper import FlexDayStartMapper
from .bo.eventBOs.FlexDayEndBO import FlexDayEndBO
from .db.eventMapper.FlexDayEndMapper import FlexDayEndMapper

from .bo.BookingBO import BookingBO
from .db.BookingMapper import BookingMapper
from .bo.EventBookingBO import EventBookingBO
from .db.EventBookingMapper import EventBookingMapper
from .bo.TimeIntervalBookingBO import TimeIntervalBookingBO
from .db.TimeIntervalBookingMapper import TimeIntervalBookingMapper
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

    def create_event(self, type, coming_id, going_id, break_begin_id,  break_end_id,
                     illness_begin_id, illness_end_id, project_work_begin_id, project_work_end_id,
                     vacation_begin_id, vacation_end_id, flex_day_start_id, flex_day_end_id):
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
            return mapper.insert(coming)

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
            coming = mapper.update(coming)
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "coming_id", coming.get_id(), coming.get_type())
                mapper.update(event)
                self.save_event_booking(event)

    # Methode um ein ComingBO aus der Datenbank zu entfernen
    def delete_coming(self, coming):
        with ComingMapper() as mapper:
            mapper.delete(coming)

    # Erstellung eines GoingBOs, also wenn ein Mitarbeiter sich ausstempelt.
    def create_going(self, time):
        going = GoingBO()
        going.set_time(time)
        with GoingMapper() as mapper:
            return mapper.insert(going)

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
            going = mapper.update(going)
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "going_id", going.get_id(), going.get_type())
                mapper.update(event)
                self.save_event_booking(event)
    # Methode um ein GoingBO aus der Datenbank zu entfernen

    def delete_going(self, going):
        with GoingMapper() as mapper:
            mapper.delete(going)

    # Erstellung eines ProjectWorkBeginBOs, also wenn ein Mitarbeiter mit der Projektarbeit beginnt
    def create_project_work_begin(self, time):
        project_work_begin = ProjectWorkBeginBO()
        project_work_begin.set_time(time)
        with ProjectWorkBeginMapper() as mapper:
            return mapper.insert(project_work_begin)

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
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "project_work_begin_id", project_work_begin.get_id(), project_work_begin.get_type())
                mapper.update(event)
                self.save_event_booking(event)

    # Methode um ein ProjectWorkBeginBO aus der Datenbank zu entfernen
    def delete_project_work_begin(self, project_work_begin):
        with ProjectWorkBeginMapper() as mapper:
            mapper.delete(project_work_begin)

      # Erstellung eines ProjectWorkEndBOs, also wenn ein Mitarbeiter mit der Projektarbeit aufhört

    def create_project_work_end(self, time):
        project_work_end = ProjectWorkEndBO()
        project_work_end.set_time(time)
        with ProjectWorkEndMapper() as mapper:
            return mapper.insert(project_work_end)

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
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "project_work_end_id", project_work_end.get_id(), project_work_end.get_type())
                mapper.update(event)
                self.save_event_booking(event)

    # Methode um ein ProjectWorkEndBO aus der Datenbank zu entfernen
    def delete_project_work_end(self, project_work_end):
        with ProjectWorkEndMapper() as mapper:
            mapper.delete(project_work_end)

    # Erstellung eines VacationBeginBOs, also wenn ein Mitarbeiter seinen Urlaub antritt

    def create_vacation_begin(self, time):
        vacation_begin = VacationBeginBO()
        vacation_begin.set_time(time)
        with VacationBeginMapper() as mapper:
            return mapper.insert(vacation_begin)

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
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "vacation_begin_id", vacation_begin.get_id(), vacation_begin.get_type())
                mapper.update(event)
                self.save_event_booking(event)

    # Methode um ein VacationBeginBO aus der Datenbank zu entfernen
    def delete_vacation_begin(self, vacation_begin):
        with EventMapper() as mapper:
            startevent = mapper.find_by_foreign_key_and_type(
                "vacation_begin_id", vacation_begin.get_id(), vacation_begin.get_type())
        with EventBookingMapper() as mapper:
            starteventbooking = mapper.find_by_event_id(startevent.get_id())
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "eventBookingId", starteventbooking.get_id(), "E")

        with BookingMapper() as mapper:
            mapper.delete(booking)
        with EventBookingMapper() as mapper:
            mapper.delete(starteventbooking)
        with EventMapper() as mapper:
            mapper.delete(startevent)
        with VacationBeginMapper() as mapper:
            mapper.delete(vacation_begin)

    # Erstellung eines VacationEndBOs, also wenn ein Mitarbeiter aus dem Urlaub kommt
    def create_vacation_end(self, time):
        vacation_end = VacationEndBO()
        vacation_end.set_time(time)
        with VacationEndMapper() as mapper:
            return mapper.insert(vacation_end)

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
        with EventMapper() as mapper:
            startevent = mapper.find_by_foreign_key_and_type(
                "vacation_end_id", vacation_end.get_id(), vacation_end.get_type())
        with EventBookingMapper() as mapper:
            starteventbooking = mapper.find_by_event_id(startevent.get_id())
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "eventBookingId", starteventbooking.get_id(), "E")

        with BookingMapper() as mapper:
            mapper.delete(booking)
        with EventBookingMapper() as mapper:
            mapper.delete(starteventbooking)
        with EventMapper() as mapper:
            mapper.delete(startevent)
        with VacationEndMapper() as mapper:
            mapper.delete(vacation_end)

        # Erstellung eines IllnessBeginBOs, also der Beginn der Krankheit eines Mitarbeiters
    def create_illness_begin(self, time):
        illness_begin = IllnessBeginBO()
        illness_begin.set_time(time)
        with IllnessBeginMapper() as mapper:
            return mapper.insert(illness_begin)

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
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "illness_begin_id", illness_begin.get_id(), illness_begin.get_type())
                mapper.update(event)
                self.save_event_booking(event)

        # Methode um ein IllnessBeginBO aus der Datenbank zu entfernen
    def delete_illness_begin(self, illness_begin):
        with EventMapper() as mapper:
            startevent = mapper.find_by_foreign_key_and_type(
                "illness_begin_id", illness_begin.get_id(), illness_begin.get_type())
        with EventBookingMapper() as mapper:
            starteventbooking = mapper.find_by_event_id(startevent.get_id())
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "eventBookingId", starteventbooking.get_id(), "E")

        with BookingMapper() as mapper:
            mapper.delete(booking)
        with EventBookingMapper() as mapper:
            mapper.delete(starteventbooking)
        with EventMapper() as mapper:
            mapper.delete(startevent)
        with IllnessBeginMapper() as mapper:
            mapper.delete(illness_begin)

        # Erstellung eines IllnessEndBOs, also das Ende der Krankheit eines Mitarbeiters
    def create_illness_end(self, time):
        illness_end = IllnessEndBO()
        illness_end.set_time(time)
        with IllnessEndMapper() as mapper:
            return mapper.insert(illness_end)

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
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "illness_end_id", illness_end.get_id(), illness_end.get_type())
                mapper.update(event)
                self.save_event_booking(event)

    # Methode um ein IllnessEndBO aus der Datenbank zu entfernen
    def delete_illness_end(self, illness_end):
        with EventMapper() as mapper:
            startevent = mapper.find_by_foreign_key_and_type(
                "illness_end_id", illness_end.get_id(), illness_end.get_type())
        with EventBookingMapper() as mapper:
            starteventbooking = mapper.find_by_event_id(startevent.get_id())
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "eventBookingId", starteventbooking.get_id(), "E")

        with BookingMapper() as mapper:
            mapper.delete(booking)
        with EventBookingMapper() as mapper:
            mapper.delete(starteventbooking)
        with EventMapper() as mapper:
            mapper.delete(startevent)
        with IllnessEndMapper() as mapper:
            mapper.delete(illness_end)
        # Erstellung eines BreakEndBOs, also das Ende der Krankheit eines Mitarbeiters

    # Erstellung eines FlexDayStartBOs, also der Beginn der Gleittage eines Mitarbeiters

    def create_flex_day_start(self, time):
        flex_day_start = FlexDayStartBO()
        flex_day_start.set_time(time)
        with FlexDayStartMapper() as mapper:
            return mapper.insert(flex_day_start)

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
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "flex_day_start_id", flex_day_start.get_id(), flex_day_start.get_type())
                print(flex_day_start.get_id())
                mapper.update(event)
                self.save_event_booking(event)

    # Methode um ein FlexDayStartBO aus der Datenbank zu entfernen
    def delete_flex_day_start(self, flex_day_start):
        with FlexDayStartMapper() as mapper:
            mapper.delete(flex_day_start)

    # Erstellung eines FlexDayEndBOs, also das Ende der Gleittage eines Mitarbeiters
    def create_flex_day_end(self, time):
        flex_day_end = FlexDayEndBO()
        flex_day_end.set_time(time)
        with FlexDayEndMapper() as mapper:
            return mapper.insert(flex_day_end)

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
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "flex_day_end_id", flex_day_end.get_id(), flex_day_end.get_type())
                mapper.update(event)
                self.save_event_booking(event)

    # Methode um ein FlexDayEndBO aus der Datenbank zu entfernen
    def delete_flex_day_end(self, flex_day_end):
        with FlexDayEndMapper() as mapper:
            mapper.delete(flex_day_end)
        # Erstellung eines BreakEndBOs, also das Ende der Gleittage eines Mitarbeiters

    def create_break_begin(self, time):
        break_begin = BreakBeginBO()
        break_begin.set_time(time)
        with BreakBeginMapper() as mapper:
            return mapper.insert(break_begin)

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
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "break_begin_id", break_begin.get_id(), break_begin.get_type())
                mapper.update(event)
                self.save_event_booking(event)

        # Methode um ein BreakBeginBO aus der Datenbank zu entfernen

    def delete_break_begin(self, break_begin):
        with BreakBeginMapper() as mapper:
            mapper.delete(break_begin)

        # Erstellung eines BreakEndBOs, also das Ende der Krankheit eines Mitarbeiters

    def create_break_end(self, time):
        break_end = BreakEndBO()
        break_end.set_time(time)
        with BreakEndMapper() as mapper:
            return mapper.insert(break_end)

    # Methode um ein BreakEndBO mit bestimmter ID aus der Datenbank zu laden

    def get_break_end_by_id(self, number):
        with BreakEndMapper() as mapper:
            return mapper.find_by_key(number)

    # Methode um alle BreakEndBOs aus der Datenbank zu laden
    def get_all_break_ends(self):
        with BreakEndMapper() as mapper:
            return mapper.find_all()

    # Methode um ein BreakEndBO zu updaten
    def save_break_end(self, break_end):
        with BreakEndMapper() as mapper:
            mapper.update(break_end)
            with EventMapper() as mapper:
                event = mapper.find_by_foreign_key_and_type(
                    "break_end_id", break_end.get_id(), break_end.get_type())
                mapper.update(event)
                self.save_event_booking(event)

    # Methode um ein BreakEndBO aus der Datenbank zu entfernen
    def delete_breakEnd(self, breakEnd):
        with BreakEndMapper() as mapper:
            mapper.delete(breakEnd)

    '''Dieser Teil ist für die Filter-Funktion im Frontend'''

    # Support-Funktion
    def in_between_times(self, event, start, end):
        if event >= start and event <= end:
            return event
        else:  # over midnight e.g., 23:30-04:15
            pass

    # Support-Funktion
    def get_all_event_subclasses(self):
        events = [self.get_all_break_ends(), self.get_all_break_begins(), self.get_all_project_work_begins(),
                  self.get_all_project_work_ends(), self.get_all_vacation_begins(
        ), self.get_all_vacation_ends(),
            self.get_all_illnessBegins(), self.get_all_illnessEnds(),
            self.get_all_comings(), self.get_all_goings()]
        return events

    # Support-Funktion
    def get_all_events_in_between_times(self, start, end):
        events_in_between_times = []
        events = self.get_all_event_subclasses()
        for elem in events:
            events_in_between_times.append(
                self.in_between_times(elem, start, end))
        return events_in_between_times

    def get_all_events_by_timeperiod(self, start, end):
        enddate = datetime.now().fromisoformat(str(end))
        startdate = datetime.now().fromisoformat(str(start))
        events = self.get_all_event_subclasses()
        interval = []
        for elem in events:
            for x in elem:
                if x.get_time() >= startdate or x.get_time() <= enddate:
                    interval.append(x)
                else:
                    pass
        return interval

    def get_event_by_timeperiod_and_type(self, start, end, type):
        enddate = datetime.now().fromisoformat(str(end))
        startdate = datetime.now().fromisoformat(str(start))
        events = self.get_events_by_type(type)
        interval = []
        for elem in events:
            if elem.get_time() >= startdate or elem.get_time() <= enddate:
                interval.append(elem)
            else:
                pass
        return interval

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

    def create_timeinterval(self, type, break_id, illness_id, project_duration_id, project_work_id, vacation_id, flexday_id, work_id):
        timeinterval = TimeIntervalBO()
        # timeinterval.set_time_interval_booking_id(timeintervalbookingid)
        timeinterval.set_type(type)
        timeinterval.set_break_id(break_id)
        timeinterval.set_illness_id(illness_id)
        timeinterval.set_project_duration_id(project_duration_id)
        timeinterval.set_project_work_id(project_work_id)
        timeinterval.set_vacation_id(vacation_id)
        timeinterval.set_flex_day_id(flexday_id)
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
            with VacationMapper() as mapper:
                mapper.find_by_key()
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
        with BreakMapper() as mapper:
            mapper.update(break_obj)
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "breakId", break_obj.get_id(), break_obj.get_type())
                print(timeinterval)
                mapper.update(timeinterval)
                self.save_time_interval_booking(timeinterval)

    def delete_break(self, break_obj):

        with BreakBeginMapper() as mapper:
            break_begin = mapper.find_by_key(
                break_obj.get_start_event())
        with BreakEndMapper() as mapper:
            break_end = mapper.find_by_key(
                break_obj.get_end_event())
        with EventMapper() as mapper:
            startevent = mapper.find_by_foreign_key_and_type(
                "break_begin_id", break_begin.get_id(), break_begin.get_type())
        with EventMapper() as mapper:
            endevent = mapper.find_by_foreign_key_and_type(
                "break_end_id", break_end.get_id(), break_end.get_type())
        with EventBookingMapper() as mapper:
            starteventbooking = mapper.find_by_event_id(startevent.get_id())
        with EventBookingMapper() as mapper:
            endeventbooking = mapper.find_by_event_id(endevent.get_id())
        with TimeIntervalMapper() as mapper:
            timeinterval = mapper.find_by_foreign_key_and_type(
                "breakId", break_obj.get_id(), break_obj.get_type())
        with TimeIntervalBookingMapper() as mapper:
            timeintervalbooking = mapper.find_by_timeinterval_id(
                timeinterval.get_id())
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")

        with BookingMapper() as mapper:
            mapper.delete(booking)
        with TimeIntervalBookingMapper() as mapper:
            mapper.delete(timeintervalbooking)
        with TimeIntervalMapper() as mapper:
            mapper.delete(timeinterval)
        with BreakMapper() as mapper:
            mapper.delete(break_obj)
        with EventBookingMapper() as mapper:
            mapper.delete(starteventbooking)
        with EventBookingMapper() as mapper:
            mapper.delete(endeventbooking)
        with EventMapper() as mapper:
            mapper.delete(startevent)
        with EventMapper() as mapper:
            mapper.delete(endevent)
        with BreakBeginMapper() as mapper:
            mapper.delete(break_begin)
        with BreakEndMapper() as mapper:
            mapper.delete(break_end)

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
        with IllnessMapper() as mapper:
            mapper.update(illness)
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "illnessId", illness.get_id(), illness.get_type())
                print(timeinterval)
                mapper.update(timeinterval)
                self.save_time_interval_booking(timeinterval)

    def delete_illness(self, illness):
        if not ((illness.get_start_event() and illness.get_end_event()) == None):
            with IllnessBeginMapper() as mapper:
                illness_begin = mapper.find_by_key(
                    illness.get_start_event())
            with IllnessEndMapper() as mapper:
                illness_end = mapper.find_by_key(
                    illness.get_end_event())
            with EventMapper() as mapper:
                startevent = mapper.find_by_foreign_key_and_type(
                    "illness_begin_id", illness_begin.get_id(), illness_begin.get_type())
            with EventMapper() as mapper:
                endevent = mapper.find_by_foreign_key_and_type(
                    "illness_end_id", illness_end.get_id(), illness_end.get_type())
            with EventBookingMapper() as mapper:
                starteventbooking = mapper.find_by_event_id(
                    startevent.get_id())
            with EventBookingMapper() as mapper:
                endeventbooking = mapper.find_by_event_id(endevent.get_id())
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "illnessId", illness.get_id(), illness.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")

            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with IllnessMapper() as mapper:
                mapper.delete(illness)
            with EventBookingMapper() as mapper:
                mapper.delete(starteventbooking)
            with EventBookingMapper() as mapper:
                mapper.delete(endeventbooking)
            with EventMapper() as mapper:
                mapper.delete(startevent)
            with EventMapper() as mapper:
                mapper.delete(endevent)
            with IllnessBeginMapper() as mapper:
                mapper.delete(illness_begin)
            with IllnessEndMapper() as mapper:
                mapper.delete(illness_end)
        elif (illness.get_start_event() and illness.get_end_event()) == None:
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "illnessId", illness.get_id(), illness.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")
            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with IllnessMapper() as mapper:
                mapper.delete(illness)
        elif not (illness.get_start_event() == None):
            with IllnessBeginMapper() as mapper:
                illness_begin = mapper.find_by_key(
                    illness.get_start_event())
            with EventMapper() as mapper:
                startevent = mapper.find_by_foreign_key_and_type(
                    "illness_begin_id", illness_begin.get_id(), illness_begin.get_type())
            with EventBookingMapper() as mapper:
                starteventbooking = mapper.find_by_event_id(
                    startevent.get_id())
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "illnessId", illness.get_id(), illness.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")
            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with IllnessMapper() as mapper:
                mapper.delete(illness)
            with EventBookingMapper() as mapper:
                mapper.delete(starteventbooking)
            with EventMapper() as mapper:
                mapper.delete(startevent)
            with IllnessBeginMapper() as mapper:
                mapper.delete(illness_begin)
        elif not(illness.get_end_event() == None):
            with IllnessEndMapper() as mapper:
                illness_end = mapper.find_by_key(
                    illness.get_end_event())
            with EventMapper() as mapper:
                endevent = mapper.find_by_foreign_key_and_type(
                    "illness_end_id", illness_end.get_id(), illness_end.get_type())
            with EventBookingMapper() as mapper:
                endeventbooking = mapper.find_by_event_id(endevent.get_id())
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "illnessId", illness.get_id(), illness.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")
            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with IllnessMapper() as mapper:
                mapper.delete(illness)
            with EventBookingMapper() as mapper:
                mapper.delete(endeventbooking)
            with EventMapper() as mapper:
                mapper.delete(endevent)
            with IllnessEndMapper() as mapper:
                mapper.delete(illness_end)

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

    def create_vacation(self, start, end, startevent, endevent, type):
        vacation_obj = VacationBO()
        vacation_obj.set_start(start)
        vacation_obj.set_end(end)
        # vacation_obj.set_time_interval_id(time_interval_id)
        vacation_obj.set_start_event(startevent)
        vacation_obj.set_end_event(endevent)
        vacation_obj.set_type(type)

        with VacationMapper() as mapper:
            return mapper.insert(vacation_obj)

    def save_vacation(self, vacation_obj):
        with VacationMapper() as mapper:
            mapper.update(vacation_obj)
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "vacationId", vacation_obj.get_id(), vacation_obj.get_type())
                print(timeinterval)
                mapper.update(timeinterval)
                self.save_time_interval_booking(timeinterval)

    def delete_vacation(self, vacation_obj):
        if not ((vacation_obj.get_start_event() and vacation_obj.get_end_event()) == None):
            with VacationBeginMapper() as mapper:
                vacation_begin = mapper.find_by_key(
                    vacation_obj.get_start_event())
            with VacationEndMapper() as mapper:
                vacation_end = mapper.find_by_key(
                    vacation_obj.get_end_event())
            with EventMapper() as mapper:
                startevent = mapper.find_by_foreign_key_and_type(
                    "vacation_begin_id", vacation_begin.get_id(), vacation_begin.get_type())
            with EventMapper() as mapper:
                endevent = mapper.find_by_foreign_key_and_type(
                    "vacation_end_id", vacation_end.get_id(), vacation_end.get_type())
            with EventBookingMapper() as mapper:
                starteventbooking = mapper.find_by_event_id(
                    startevent.get_id())
            with EventBookingMapper() as mapper:
                endeventbooking = mapper.find_by_event_id(endevent.get_id())
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "vacationId", vacation_obj.get_id(), vacation_obj.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")

            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with VacationMapper() as mapper:
                mapper.delete(vacation_obj)
            with EventBookingMapper() as mapper:
                mapper.delete(starteventbooking)
            with EventBookingMapper() as mapper:
                mapper.delete(endeventbooking)
            with EventMapper() as mapper:
                mapper.delete(startevent)
            with EventMapper() as mapper:
                mapper.delete(endevent)
            with VacationBeginMapper() as mapper:
                mapper.delete(vacation_begin)
            with VacationEndMapper() as mapper:
                mapper.delete(vacation_end)
        elif (vacation_obj.get_start_event() and vacation_obj.get_end_event()) == None:
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "vacationId", vacation_obj.get_id(), vacation_obj.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")
            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with VacationMapper() as mapper:
                mapper.delete(vacation_obj)
        elif not (vacation_obj.get_start_event() == None):
            with VacationBeginMapper() as mapper:
                vacation_begin = mapper.find_by_key(
                    vacation_obj.get_start_event())
            with EventMapper() as mapper:
                startevent = mapper.find_by_foreign_key_and_type(
                    "vacation_begin_id", vacation_begin.get_id(), vacation_begin.get_type())
            with EventBookingMapper() as mapper:
                starteventbooking = mapper.find_by_event_id(
                    startevent.get_id())
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "vacationId", vacation_obj.get_id(), vacation_obj.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")
            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with VacationMapper() as mapper:
                mapper.delete(vacation_obj)
            with EventBookingMapper() as mapper:
                mapper.delete(starteventbooking)
            with EventMapper() as mapper:
                mapper.delete(startevent)
            with VacationBeginMapper() as mapper:
                mapper.delete(vacation_begin)
        elif not(vacation_obj.get_end_event() == None):
            with VacationEndMapper() as mapper:
                vacation_end = mapper.find_by_key(
                    vacation_obj.get_end_event())
            with EventMapper() as mapper:
                endevent = mapper.find_by_foreign_key_and_type(
                    "vacation_end_id", vacation_end.get_id(), vacation_end.get_type())
            with EventBookingMapper() as mapper:
                endeventbooking = mapper.find_by_event_id(endevent.get_id())
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "vacationId", vacation_obj.get_id(), vacation_obj.get_type())
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_timeinterval_id(
                    timeinterval.get_id())
            with BookingMapper() as mapper:
                booking = mapper.find_booking_by_booking_subclass(
                    "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")
            with BookingMapper() as mapper:
                mapper.delete(booking)
            with TimeIntervalBookingMapper() as mapper:
                mapper.delete(timeintervalbooking)
            with TimeIntervalMapper() as mapper:
                mapper.delete(timeinterval)
            with VacationMapper() as mapper:
                mapper.delete(vacation_obj)
            with EventBookingMapper() as mapper:
                mapper.delete(endeventbooking)
            with EventMapper() as mapper:
                mapper.delete(endevent)
            with VacationEndMapper() as mapper:
                mapper.delete(vacation_end)

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
        with WorkMapper() as mapper:
            work = mapper.update(work_obj)
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "workId", work.get_id(), work.get_type())
                mapper.update(timeinterval)
                self.save_time_interval_booking(timeinterval)

    def delete_work(self, work_obj):
        with ComingMapper() as mapper:
            coming = mapper.find_by_key(work_obj.get_start_event())
        with GoingMapper() as mapper:
            going = mapper.find_by_key(work_obj.get_end_event())
        with EventMapper() as mapper:
            startevent = mapper.find_by_foreign_key_and_type(
                "coming_id", coming.get_id(), coming.get_type())
        with EventMapper() as mapper:
            endevent = mapper.find_by_foreign_key_and_type(
                "going_id", going.get_id(), going.get_type())
        with EventBookingMapper() as mapper:
            starteventbooking = mapper.find_by_event_id(startevent.get_id())
        with EventBookingMapper() as mapper:
            endeventbooking = mapper.find_by_event_id(endevent.get_id())
        with TimeIntervalMapper() as mapper:
            timeinterval = mapper.find_by_foreign_key_and_type(
                "workId", work_obj.get_id(), work_obj.get_type())
        with TimeIntervalBookingMapper() as mapper:
            timeintervalbooking = mapper.find_by_timeinterval_id(
                timeinterval.get_id())
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")

        with BookingMapper() as mapper:
            mapper.delete(booking)
        with TimeIntervalBookingMapper() as mapper:
            mapper.delete(timeintervalbooking)
        with TimeIntervalMapper() as mapper:
            mapper.delete(timeinterval)
        with WorkMapper() as mapper:
            mapper.delete(work_obj)
        with EventBookingMapper() as mapper:
            mapper.delete(starteventbooking)
        with EventBookingMapper() as mapper:
            mapper.delete(endeventbooking)
        with EventMapper() as mapper:
            mapper.delete(startevent)
        with EventMapper() as mapper:
            mapper.delete(endevent)
        with ComingMapper() as mapper:
            mapper.delete(coming)
        with GoingMapper() as mapper:
            mapper.delete(going)

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
        work_obj.set_type("Flexday")

        with FlexDayMapper() as mapper:
            return mapper.insert(work_obj)

    def save_flex_day(self, flex_day_obj):
        with FlexDayMapper() as mapper:
            mapper.update(flex_day_obj)
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "flexDayId", flex_day_obj.get_id(), flex_day_obj.get_type())
                print(timeinterval)
                mapper.update(timeinterval)
                self.save_time_interval_booking(timeinterval)

    def delete_flex_day(self, flexday_obj):

        with FlexDayStartMapper() as mapper:
            flexday_begin = mapper.find_by_key(
                flexday_obj.get_start_event())
        with FlexDayEndMapper() as mapper:
            flexday_end = mapper.find_by_key(
                flexday_obj.get_end_event())
        with EventMapper() as mapper:
            startevent = mapper.find_by_foreign_key_and_type(
                "flex_day_start_id", flexday_begin.get_id(), flexday_begin.get_type())
        with EventMapper() as mapper:
            endevent = mapper.find_by_foreign_key_and_type(
                "flex_day_end_id", flexday_end.get_id(), flexday_end.get_type())
        with EventBookingMapper() as mapper:
            starteventbooking = mapper.find_by_event_id(startevent.get_id())
        with EventBookingMapper() as mapper:
            endeventbooking = mapper.find_by_event_id(endevent.get_id())
        with TimeIntervalMapper() as mapper:
            timeinterval = mapper.find_by_foreign_key_and_type(
                "flexDayId", flexday_obj.get_id(), flexday_obj.get_type())
        with TimeIntervalBookingMapper() as mapper:
            timeintervalbooking = mapper.find_by_timeinterval_id(
                timeinterval.get_id())
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")

        with BookingMapper() as mapper:
            mapper.delete(booking)
        with TimeIntervalBookingMapper() as mapper:
            mapper.delete(timeintervalbooking)
        with TimeIntervalMapper() as mapper:
            mapper.delete(timeinterval)
        with FlexDayMapper() as mapper:
            mapper.delete(flexday_obj)
        with EventBookingMapper() as mapper:
            mapper.delete(starteventbooking)
        with EventBookingMapper() as mapper:
            mapper.delete(endeventbooking)
        with EventMapper() as mapper:
            mapper.delete(startevent)
        with EventMapper() as mapper:
            mapper.delete(endevent)
        with FlexDayStartMapper() as mapper:
            mapper.delete(flexday_begin)
        with FlexDayEndMapper() as mapper:
            mapper.delete(flexday_end)

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
        with ProjectWorkMapper() as mapper:
            mapper.update(project_work_obj)
            with TimeIntervalMapper() as mapper:
                timeinterval = mapper.find_by_foreign_key_and_type(
                    "projectWorkId", project_work_obj.get_id(), project_work_obj.get_type())
                print(timeinterval)
                mapper.update(timeinterval)
                self.save_time_interval_booking(timeinterval)

    def delete_project_work(self, project_work_obj):
        with ProjectWorkBeginMapper() as mapper:
            project_work_begin = mapper.find_by_key(
                project_work_obj.get_start_event())
        with ProjectWorkEndMapper() as mapper:
            project_work_end = mapper.find_by_key(
                project_work_obj.get_end_event())
        with EventMapper() as mapper:
            startevent = mapper.find_by_foreign_key_and_type(
                "project_work_begin_id", project_work_begin.get_id(), project_work_begin.get_type())
        with EventMapper() as mapper:
            endevent = mapper.find_by_foreign_key_and_type(
                "project_work_end_id", project_work_end.get_id(), project_work_end.get_type())
        with EventBookingMapper() as mapper:
            starteventbooking = mapper.find_by_event_id(startevent.get_id())
        with EventBookingMapper() as mapper:
            endeventbooking = mapper.find_by_event_id(endevent.get_id())
        with TimeIntervalMapper() as mapper:
            timeinterval = mapper.find_by_foreign_key_and_type(
                "projectWorkId", project_work_obj.get_id(), project_work_obj.get_type())
        with TimeIntervalBookingMapper() as mapper:
            timeintervalbooking = mapper.find_by_timeinterval_id(
                timeinterval.get_id())
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "TimeIntervalBookingId", timeintervalbooking.get_id(), "T")

        with BookingMapper() as mapper:
            mapper.delete(booking)
        with TimeIntervalBookingMapper() as mapper:
            mapper.delete(timeintervalbooking)
        with TimeIntervalMapper() as mapper:
            mapper.delete(timeinterval)
        with ProjectWorkMapper() as mapper:
            mapper.delete(project_work_obj)
        with EventBookingMapper() as mapper:
            mapper.delete(starteventbooking)
        with EventBookingMapper() as mapper:
            mapper.delete(endeventbooking)
        with EventMapper() as mapper:
            mapper.delete(startevent)
        with EventMapper() as mapper:
            mapper.delete(endevent)
        with ProjectWorkBeginMapper() as mapper:
            mapper.delete(project_work_begin)
        with ProjectWorkEndMapper() as mapper:
            mapper.delete(project_work_end)

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

    def get_timeinterval_booking_by_id(self, id):
        with TimeIntervalBookingMapper as mapper:
            return mapper.find_by_key(id)

    def get_booking_by_id(self, id):
        with BookingMapper as mapper:
            return mapper.find_by_key(id)

    def get_event_booking_by_id(self, id):
        with EventBookingMapper as mapper:
            return mapper.find_by_key(id)

    def add_delta(self, tbooking):
        for elem in tbooking:
            timeintervalbooking = self.get_timeinterval_booking_for_delta(
                tbooking)

            booking = timeintervalbooking.get("timeintervals")

            for elem in booking:
                print("ELEM", elem)
                type = elem.get_type()
                if not ((elem.get_start_event() and elem.get_end_event) == None):
                    if type == 'Break':
                        with BreakBeginMapper() as mapper:
                            start_event = mapper.find_by_key(
                                elem.get_start_event())
                        with BreakEndMapper() as mapper:
                            end_event = mapper.find_by_key(
                                elem.get_end_event())

                        delta = end_event.get_time() - start_event.get_time()
                        delta_float = (delta.total_seconds()/60)/60
                        round(delta_float, 2)
                        self.calculate_delta(tbooking, delta_float)

                    if type == 'ProjectWork':
                        with ProjectWorkBeginMapper() as mapper:
                            start_event = mapper.find_by_key(
                                elem.get_start_event())
                        with ProjectWorkEndMapper() as mapper:
                            end_event = mapper.find_by_key(
                                elem.get_end_event())

                        delta = end_event.get_time() - start_event.get_time()
                        delta_float = (delta.total_seconds()/60)/60
                        round(delta_float, 2)
                        self.calculate_delta(tbooking, delta_float)
                    if type == 'Work':
                        with ComingMapper() as mapper:
                            start_event = mapper.find_by_key(
                                elem.get_start_event())
                        with GoingMapper() as mapper:
                            end_event = mapper.find_by_key(
                                elem.get_end_event())

                        delta = end_event.get_time() - start_event.get_time()
                        print("DELTA EVENT", delta)
                        delta_float = (delta.total_seconds()/60)/60
                        round(delta_float, 2)
                        self.calculate_delta(tbooking, delta_float)
                elif not (elem.get_start_event() is None):
                    if type == 'Break':
                        with BreakBeginMapper() as mapper:
                            start_event = mapper.find_by_key(
                                elem.get_start_event())

                        delta = elem.get_end() - start_event.get_time()
                        delta_float = (delta.total_seconds()/60)/60
                        round(delta_float, 2)
                        self.calculate_delta(tbooking, delta_float)
                    if type == 'ProjectWork':
                        with ProjectWorkBeginMapper() as mapper:
                            start_event = mapper.find_by_key(
                                elem.get_start_event())

                        delta = elem.get_end() - start_event.get_time()
                        delta_float = (delta.total_seconds()/60)/60
                        round(delta_float, 2)
                        self.calculate_delta(tbooking, delta_float)
                    if type == 'Work':
                        with ComingMapper() as mapper:
                            start_event = mapper.find_by_key(
                                elem.get_start_event())

                        delta = elem.get_end() - start_event.get_time()
                        delta_float = (delta.total_seconds()/60)/60
                        round(delta_float, 2)
                        self.calculate_delta(tbooking, delta_float)

                elif not (elem.get_end_event() is None):
                    if type == 'Break':
                        with BreakEndMapper() as mapper:
                            end_event = mapper.find_by_key(
                                elem.get_end_event())

                        delta = end_event.get_time() - elem.get_start()
                        delta_float = (delta.total_seconds()/60)/60
                        round(delta_float, 2)
                        self.calculate_delta(tbooking, delta_float)

                    if type == 'ProjectWork':
                        with ProjectWorkEndMapper() as mapper:
                            end_event = mapper.find_by_key(
                                elem.get_end_event())

                        delta = end_event.get_time() - elem.get_start()
                        delta_float = (delta.total_seconds()/60)/60
                        round(delta_float, 2)
                        self.calculate_delta(tbooking, delta_float)

                    if type == 'Work':
                        with GoingMapper() as mapper:
                            end_event = mapper.find_by_key(
                                elem.get_end_event())

                        delta = end_event.get_time() - elem.get_start()
                        delta_float = (delta.total_seconds()/60)/60
                        round(delta_float, 2)
                        self.calculate_delta(tbooking, delta_float)

                elif (elem.get_start_event() and elem.get_end_event) == None:
                    delta = elem.get_end() - elem.get_start()
                    delta_float = (delta.total_seconds()/60)/60
                    round(delta_float, 2)
                    print(delta_float)
                    self.calculate_delta(tbooking, delta_float)

    def add_delta_for_project_work(self, tbooking):
        for elem in tbooking:
            timeintervalbooking = self.get_timeinterval_booking_for_delta(
                tbooking)

            booking = timeintervalbooking.get("timeintervals")

            for elem in booking:
                print("ELEM", elem)
                with ProjectWorkBeginMapper() as mapper:
                    start_event = mapper.find_by_key(
                        elem.get_start_event())
                with ProjectWorkEndMapper() as mapper:
                    end_event = mapper.find_by_key(
                        elem.get_end_event())

                    delta = end_event.get_time() - start_event.get_time()
                    delta_float = (delta.total_seconds()/60)/60
                    activityid = elem.get_activity_id()
                    round(delta_float, 2)
                    self.calculate_delta_for_project_work(
                        tbooking, delta_float, activityid)

    def calculate_delta_for_project_work(self, tbooking, delta_float, activityid):
        for elem in tbooking:
            with ProjectUserMapper() as mapper:
                projectuser = mapper.find_by_key(elem.get_user_id())
                capacity = projectuser.get_capacity()

            if projectuser.get_current_capacity() == None or projectuser.get_current_capacity() == 0:
                current_capacity = capacity - delta_float
                projectuser.set_current_capacity(current_capacity)

            else:
                new_current_capacity = projectuser.get_current_capacity() - delta_float
                projectuser.set_current_capacity(new_current_capacity)

            with ActivityMapper() as mapper:
                activity = mapper.find_by_key(activityid)

            if activity.get_current_capacity() == None or activity.get_current_capacity() == 0:
                activity.set_current_capacity(delta_float)
            else:
                new_current_capacity_a = activity.get_current_capacity() + delta_float
                activity.set_current_capacity(new_current_capacity_a)
        return activity, projectuser

    def calculate_delta(self, tbooking, delta_float):
        for elem in tbooking:
            with WorkTimeAccountMapper() as mapper:
                account = mapper.find_by_key(elem.get_user_id())
                contracttime = account.get_contract_time()

            if delta_float < contracttime:
                deficit = delta_float - contracttime
                new_overtime = account.get_overtime() + deficit
                account.set_overtime(new_overtime)
                with WorkTimeAccountMapper() as mapper:
                    return mapper.update(account)
            elif delta_float > contracttime:
                overtime = delta_float - contracttime
                new_overtime = account.get_overtime() + overtime
                account.set_overtime(new_overtime)
                with WorkTimeAccountMapper() as mapper:
                    return mapper.update(account)
            elif delta_float == contracttime:
                pass
        return account

    def create_timeinterval_booking(self, timeintervalId):
        """Ein Timeinterval Booking anlegen"""

        timeintervalbooking = TimeIntervalBookingBO()
        timeintervalbooking.set_timeinterval_id(timeintervalId)

        with TimeIntervalBookingMapper() as mapper:
            return mapper.insert(timeintervalbooking)

    def create_booking_for_timeinterval(self, userId, worktimeAccountId, type, eventbookingId):
        with TimeIntervalBookingMapper() as mapper:
            last_entry = mapper.find_last_entry()
            id = last_entry.get_id()

        booking = BookingBO()
        booking.set_user_id(userId)
        booking.set_work_time_account_id(worktimeAccountId)
        booking.set_type(type)
        booking.set_event_booking_id(eventbookingId)
        booking.set_time_interval_booking_id(id)

        with BookingMapper() as mapper:
            return mapper.insert(booking)

    def create_event_booking(self, eventbookingId):
        """Ein Event Booking anlegen"""

        eventbooking = EventBookingBO()
        eventbooking.set_event_id(eventbookingId)

        with EventBookingMapper() as mapper:
            return mapper.insert(eventbooking)

    def create_booking_for_event(self, userId, worktimeAccountId, type, timeintervalbookingId):
        with EventBookingMapper() as mapper:
            last_entry = mapper.find_last_entry()
            id = last_entry.get_id()

        booking = BookingBO()
        booking.set_user_id(userId)
        booking.set_work_time_account_id(worktimeAccountId)
        booking.set_type(type)
        booking.set_event_booking_id(id)
        booking.set_time_interval_booking_id(timeintervalbookingId)

        with BookingMapper() as mapper:
            return mapper.insert(booking)

    def get_timeinterval_booking_for_delta(self, tbooking):
        booking_types = ["timeintervals", "events"]
        res_ti = []
        res_ti_e = []
        res_final = []

        for elem in tbooking:
            timeintervalbookingid = elem.get_time_interval_booking_id()
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_key(timeintervalbookingid)
                id = timeintervalbooking.get_timeinterval_id()
            with TimeIntervalMapper() as mapper:
                timeintervals = mapper.find_by_key(id)
                type = timeintervals.get_type()
                if type == 'break':
                    res = self.get_break_by_id(timeintervals.get_break_id())
                    if (res.get_start_event() and res.get_end_event) == None:
                        res_ti.append(res)
                    elif not ((res.get_start_event() and res.get_end_event()) == None):
                        with BreakBeginMapper() as mapper:
                            start_event = mapper.find_by_key(
                                res.get_start_event())
                        with BreakEndMapper() as mapper:
                            end_event = mapper.find_by_key(
                                res.get_start_event())
                        res_ti_e.append(start_event)
                        res_ti_e.append(end_event)
                        res_ti.append(res)
                    elif not (res.get_start_event() is None):
                        with BreakBeginMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                    elif not (res.get_end_event() is None):
                        with BreakEndMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)

                if type == 'projectWork':
                    res = self.get_project_work_by_id(
                        timeintervals.get_project_work_id())
                    if (res.get_start_event() and res.get_end_event) == None:
                        res_ti.append(res)
                    elif not ((res.get_start_event() and res.get_end_event()) == None):
                        with ProjectWorkBeginMapper() as mapper:
                            start_event = mapper.find_by_key(
                                res.get_start_event())
                        with ProjectWorkEndMapper() as mapper:
                            end_event = mapper.find_by_key(
                                res.get_start_event())
                        res_ti_e.append(start_event)
                        res_ti_e.append(end_event)
                        res_ti.append(res)
                    elif not (res.get_start_event() is None):
                        with ProjectWorkBeginMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                    elif not (res.get_end_event() is None):
                        with ProjectWorkEndMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)

                if type == 'work':
                    res = self.get_work_by_id(timeintervals.get_work_id())
                    if (res.get_start_event() and res.get_end_event) == None:
                        res_ti.append(res)
                    elif not ((res.get_start_event() and res.get_end_event()) == None):
                        with ComingMapper() as mapper:
                            start_event = mapper.find_by_key(
                                res.get_start_event())
                        with GoingMapper() as mapper:
                            end_event = mapper.find_by_key(
                                res.get_start_event())
                        res_ti_e.append(start_event)
                        res_ti_e.append(end_event)
                        res_ti.append(res)
                    elif not (res.get_start_event() is None):
                        with ComingMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                    elif not (res.get_end_event() is None):
                        with GoingMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
        res_final = [res_ti, res_ti_e]
        res_final_dict = dict(zip(booking_types, res_final))
        print(res_final_dict)
        return res_final_dict

    def get_all_timeinterval_bookings_for_user(self, user):
        booking_types = ["timeintervals", "events"]
        res_ti = []
        res_ti_e = []
        res_final = []

        with BookingMapper() as mapper:
            timeintervalbookings = mapper.find_timeinterval_bookings_by_user_id(
                user.get_id())

        for elem in timeintervalbookings:
            timeintervalbookingid = elem.get_time_interval_booking_id()
            with TimeIntervalBookingMapper() as mapper:
                timeintervalbooking = mapper.find_by_key(timeintervalbookingid)
                id = timeintervalbooking.get_timeinterval_id()
            with TimeIntervalMapper() as mapper:
                timeintervals = mapper.find_by_key(id)
                type = timeintervals.get_type()
                if type == 'break':
                    res = self.get_break_by_id(timeintervals.get_break_id())
                    if (res.get_start_event() and res.get_end_event) == None:
                        res_ti.append(res)
                    elif not ((res.get_start_event() and res.get_end_event()) == None):
                        with BreakBeginMapper() as mapper:
                            start_event = mapper.find_by_key(
                                res.get_start_event())
                        with BreakEndMapper() as mapper:
                            end_event = mapper.find_by_key(
                                res.get_start_event())
                        res_ti_e.append(start_event)
                        res_ti_e.append(end_event)
                        res_ti.append(res)
                    elif not (res.get_start_event() is None):
                        with BreakBeginMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                    elif not (res.get_end_event() is None):
                        with BreakEndMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                if type == 'illness':
                    res = self.get_illness_by_id(
                        timeintervals.get_illness_id())
                    if (res.get_start_event() and res.get_end_event) == None:
                        res_ti.append(res)
                    elif not ((res.get_start_event() and res.get_end_event()) == None):
                        with IllnessBeginMapper() as mapper:
                            start_event = mapper.find_by_key(
                                res.get_start_event())
                        with IllnessEndMapper() as mapper:
                            end_event = mapper.find_by_key(
                                res.get_start_event())
                        res_ti_e.append(start_event)
                        res_ti_e.append(end_event)
                        res_ti.append(res)
                    elif not (res.get_start_event() is None):
                        with IllnessBeginMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                    elif not (res.get_end_event() is None):
                        with IllnessEndMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                if type == 'projectDuration':
                    res = self.get_project_duration_by_id(
                        timeintervals.get_project_duration_id())
                    res_ti.append(res)
                if type == 'projectWork':
                    res = self.get_project_work_by_id(
                        timeintervals.get_project_work_id())
                    if (res.get_start_event() and res.get_end_event) == None:
                        res_ti.append(res)
                    elif not ((res.get_start_event() and res.get_end_event()) == None):
                        with ProjectWorkBeginMapper() as mapper:
                            start_event = mapper.find_by_key(
                                res.get_start_event())
                        with ProjectWorkEndMapper() as mapper:
                            end_event = mapper.find_by_key(
                                res.get_start_event())
                        res_ti_e.append(start_event)
                        res_ti_e.append(end_event)
                        res_ti.append(res)
                    elif not (res.get_start_event() is None):
                        with ProjectWorkBeginMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                    elif not (res.get_end_event() is None):
                        with ProjectWorkEndMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                if type == 'vacation':
                    res = self.get_vacation_by_id(
                        timeintervals.get_vacation_id())
                    if (res.get_start_event() and res.get_end_event) == None:
                        res_ti.append(res)
                    elif not ((res.get_start_event() and res.get_end_event()) == None):
                        with VacationBeginMapper() as mapper:
                            start_event = mapper.find_by_key(
                                res.get_start_event())
                        with VacationEndMapper() as mapper:
                            end_event = mapper.find_by_key(
                                res.get_start_event())
                        res_ti_e.append(start_event)
                        res_ti_e.append(end_event)
                        res_ti.append(res)
                    elif not (res.get_start_event() is None):
                        with VacationBeginMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                    elif not (res.get_end_event() is None):
                        with VacationEndMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                if type == 'work':
                    res = self.get_work_by_id(timeintervals.get_work_id())
                    if (res.get_start_event() and res.get_end_event) == None:
                        res_ti.append(res)
                    elif not ((res.get_start_event() and res.get_end_event()) == None):
                        with ComingMapper() as mapper:
                            start_event = mapper.find_by_key(
                                res.get_start_event())
                        with GoingMapper() as mapper:
                            end_event = mapper.find_by_key(
                                res.get_start_event())
                        res_ti_e.append(start_event)
                        res_ti_e.append(end_event)
                        res_ti.append(res)
                    elif not (res.get_start_event() is None):
                        with ComingMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
                    elif not (res.get_end_event() is None):
                        with GoingMapper() as mapper:
                            event = mapper.find_by_key(res.get_start_event())
                            res_ti_e.append(event)
                            res_ti.append(res)
        res_final = [res_ti, res_ti_e]
        res_final_dict = dict(zip(booking_types, res_final))
        print(res_final_dict)
        return res_final_dict

    def get_all_event_bookings_for_user(self, user):
        '''Als erstes werden die alle ids geholt, danach der Fremdschlüssel EventbookingId 
        und dieser wird dann in der Tabelle Eventbooking eingefügt 
        und dort wird dann nach dem FK Eventid gesucht'''

        res_e = []

        with BookingMapper() as mapper:
            eventbookings = mapper.find_event_bookings_by_user_id(
                user.get_id())

        for elem in eventbookings:
            eventbookingid = elem.get_event_booking_id()
            with EventBookingMapper() as mapper:
                eventbooking = mapper.find_by_key(eventbookingid)
                id = eventbooking.get_event_id()
            with EventMapper() as mapper:
                events = mapper.find_by_key(id)
                type = events.get_type()
            if type == 'breakBegin':
                res = self.get_break_begin_by_id(events.get_break_begin_id())
                res_e.append(res)
            if type == 'breakEnd':
                res = self.get_break_end_by_id(events.get_break_end_id())
                res_e.append(res)
            if type == 'illnessBegin':
                res = self.get_illness_begin_by_id(
                    events.get_illness_begin_id())
                res_e.append(res)
            if type == 'illnessEnd':
                res = self.get_illness_end_by_id(events.get_illness_end_id())
                res_e.append(res)
            if type == 'projectWorkBegin':
                res = self.get_project_work_begin_by_id(
                    events.get_project_work_begin_id())
                res_e.append(res)
            if type == 'projectWorkEnd':
                res = self.get_project_work_end_by_id(
                    events.get_project_work_end_id())
                res_e.append(res)
            if type == 'vacationBegin':
                res = self.get_vacation_begin_by_id(
                    events.get_vacation_begin_id())
                res_e.append(res)
            if type == 'vacationEnd':
                res = self.get_vacation_end_by_id(events.get_vacation_end_id())
                res_e.append(res)
            if type == 'coming':
                res = self.get_coming_by_id(events.get_coming_id())
                res_e.append(res)
            if type == 'going':
                res = self.get_going_by_id(events.get_going_id())
                res_e.append(res)
        print(res_e)
        return res_e

    def get_all_vacation_illness_event_bookings_for_user(self, user):
        '''Als erstes werden die alle ids geholt, danach der Fremdschlüssel EventbookingId 
        und dieser wird dann in der Tabelle Eventbooking eingefügt 
        und dort wird dann nach dem FK Eventid gesucht'''

        res_e = []

        with BookingMapper() as mapper:
            eventbookings = mapper.find_event_bookings_by_user_id(
                user.get_id())

        for elem in eventbookings:
            eventbookingid = elem.get_event_booking_id()
            with EventBookingMapper() as mapper:
                eventbooking = mapper.find_by_key(eventbookingid)
                id = eventbooking.get_event_id()
            with EventMapper() as mapper:
                events = mapper.find_by_key(id)
                type = events.get_type()
            if type == 'illnessBegin':
                res = self.get_illness_begin_by_id(
                    events.get_illness_begin_id())
                res_e.append(res)
            if type == 'illnessEnd':
                res = self.get_illness_end_by_id(events.get_illness_end_id())
                res_e.append(res)
            if type == 'vacationBegin':
                res = self.get_vacation_begin_by_id(
                    events.get_vacation_begin_id())
                res_e.append(res)
            if type == 'vacationEnd':
                res = self.get_vacation_end_by_id(events.get_vacation_end_id())
                res_e.append(res)
        print(res_e)
        return res_e

    def save_time_interval_booking(self, timeinterval):
        with TimeIntervalBookingMapper() as mapper:
            timeintervalbooking = mapper.find_by_key(timeinterval.get_id())
            mapper.update(timeintervalbooking)
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "timeIntervalBookingId", timeintervalbooking.get_id(), "T")
            mapper.update(booking)

    def delete_time_interval_booking(self, timeinterval):
        with TimeIntervalBookingMapper() as mapper:
            timeintervalbooking = mapper.find_by_key(timeinterval.get_id())
            mapper.delete(timeintervalbooking)
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "timeIntervalBookingId", timeintervalbooking.get_id(), "T")
            mapper.delete(booking)

    def save_event_booking(self, event):
        with EventBookingMapper() as mapper:
            eventbooking = mapper.find_by_key(event.get_id())
            mapper.update(eventbooking)
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "eventBookingId", eventbooking.get_id(), "E")
            if booking.get_type() == "E":
                mapper.update(booking)
            else:
                pass

    def delete_event_booking(self, event):
        with EventBookingMapper() as mapper:
            eventbooking = mapper.find_by_key(event.get_id())
            mapper.delete(eventbooking)
        with BookingMapper() as mapper:
            booking = mapper.find_booking_by_booking_subclass(
                "eventBookingId", eventbooking.get_id(), "E")
            if booking.get_type() == "E":
                mapper.update(booking)
            else:
                pass

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

    def create_user(self, first_name, last_name, mail_adress, googleId):
        user_obj = UserBO()
        user_obj.set_first_name(first_name)
        user_obj.set_last_name(last_name)
        user_obj.set_mail_adress(mail_adress)
        user_obj.set_google_user_id(googleId)

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
            return mapper.find_by_mail(mail_adress)

    def get_user_by_google_user_id(self, string):
        with UserMapper() as mapper:
            return mapper.find_by_googleuserid(string)

    # def get_user_by_user_name(self, user_name):
    #     with UserMapper() as mapper:
    #         return mapper.find_by_user_name(user_name)

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

    def create_worktimeaccount(self, userId, contractTime, overTime):
        worktimeaccount_obj = WorkTimeAccountBO()
        worktimeaccount_obj.set_user_id(userId)
        worktimeaccount_obj.set_contract_time(contractTime)
        worktimeaccount_obj.set_overtime(overTime)

        with WorkTimeAccountMapper() as mapper:
            return mapper.insert(worktimeaccount_obj)

    def get_worktimeaccount_by_user_id(self, user_id):
        with WorkTimeAccountMapper() as mapper:
            return mapper.find_by_user_id(user_id)

    def get_worktimeaccount_by_id(self, id):
        with WorkTimeAccountMapper() as mapper:
            return mapper.find_by_key(id)

    def get_all_worktimeaccounts(self):
        with WorkTimeAccountMapper() as mapper:
            return mapper.find_all()

    def save_worktimeaccount(self, worktimeaccount_obj):
        with WorkTimeAccountMapper() as mapper:
            mapper.update(worktimeaccount_obj)

    def delete_worktimeaccount(self, worktimeaccount_obj):
        with WorkTimeAccountMapper() as mapper:
            mapper.delete(worktimeaccount_obj)

    """
    Project
    """

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
            return mapper.find_projects_by_user_id(id)

    def get_by_project_name(self, name):
        with ProjectMapper() as mapper:
            mapper.find_by_project_name(name)

    # def get_project_duration_by_project_id(self, id):
    #     with ProjectMapper() as mapper:
    #         return mapper.find_by_project_id(id)

    """
    Projectuser
    """

    def create_projectuser(self, project_id, user_id, capacity, current):
        projectuser = ProjectUserBO()
        projectuser.set_project_id(project_id)
        projectuser.set_user_id(user_id)
        projectuser.set_capacity(capacity)
        projectuser.set_current_capacity(current)
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

    def get_project_by_name(self, name):
        projects = self.get_all_projects()
        for elem in projects:
            if elem.get_name() == name:
                return elem


# with EventMapper() as mapper:
#     event = mapper.find_by_key_and_type(1, "coming")
#     mapper.update(event)
