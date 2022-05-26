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

    # Erstellung eines ComingBOs, also wenn ein Mitarbeiter sich einstempelt.
    def create_coming(self, time, event_id):
        coming = ComingBO()
        coming.set_time(time)
        coming.set_event_id(event_id)
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
            mapper.update(coming)

    # Methode um ein ComingBO aus der Datenbank zu entfernen
    def delete_coming(self, coming):
        with ComingMapper() as mapper:
            mapper.delete(coming)

    # Erstellung eines GoingBOs, also wenn ein Mitarbeiter sich ausstempelt.
    def create_going(self, time, event_booking_id):
        going = GoingBO()
        going.set_time(time)
        going.set_event_booking_id(event_booking_id)
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
            mapper.update(going)

    # Methode um ein GoingBO aus der Datenbank zu entfernen
    def delete_going(self, going):
        with GoingMapper() as mapper:
            mapper.delete(going)

    # Erstellung eines ProjectWorkBeginBOs, also wenn ein Mitarbeiter mit der Projektarbeit beginnt
    def create_project_work_begin(self, time, event_id):
        project_work_begin = ProjectWorkBeginBO()
        project_work_begin.set_time(time)
        project_work_begin.set_event_id(event_id)
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

    # Methode um ein ProjectWorkBeginBO aus der Datenbank zu entfernen
    def delete_project_work_begin(self, project_work_begin):
        with ProjectWorkBeginMapper() as mapper:
            mapper.delete(project_work_begin)

      # Erstellung eines ProjectWorkEndBOs, also wenn ein Mitarbeiter mit der Projektarbeit aufhört

    def create_project_work_end(self, time, event_id):
        project_work_end = ProjectWorkEndBO()
        project_work_end.set_time(time)
        project_work_end.set_event_id(event_id)
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

    # Methode um ein ProjectWorkEndBO aus der Datenbank zu entfernen
    def delete_project_work_end(self, project_work_end):
        with ProjectWorkEndMapper() as mapper:
            mapper.delete(project_work_end)

    # Erstellung eines VacationBeginBOs, also wenn ein Mitarbeiter seinen Urlaub antritt

    def create_vacation_begin(self, time, event_booking_id):
        vacation_begin = VacationBeginBO()
        vacation_begin.set_time(time)
        vacation_begin.set_event_booking_id(event_booking_id)
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

    # Methode um ein VacationBeginBO aus der Datenbank zu entfernen
    def delete_vacation_begin(self, vacation_begin):
        with VacationBeginMapper() as mapper:
            mapper.delete(vacation_begin)

    # Erstellung eines VacationEndBOs, also wenn ein Mitarbeiter aus dem Urlaub kommt
    def create_vacation_end(self, time, event_booking_id):
        vacation_end = VacationEndBO()
        vacation_end.set_time(time)
        vacation_end.set_event_booking_id(event_booking_id)
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
        with VacationEndMapper() as mapper:
            mapper.delete(vacation_end)

        # Erstellung eines IllnessBeginBOs, also der Beginn der Krankheit eines Mitarbeiters
    def create_illnessBegin(self, time, event_id):
        illnessBegin = IllnessBeginBO()
        illnessBegin.set_time(time)
        illnessBegin.set_event_id(event_id)
        with IllnessBeginMapper() as mapper:
            return mapper.insert(illnessBegin)

    # Methode um ein IllnessBeginBO mit bestimmter ID aus der Datenbank zu laden
    def get_illnessBegin_by_id(self, number):
        with IllnessBeginMapper() as mapper:
            return mapper.find_by_key(number)
        # Methode um alle IllnessBeginBOs aus der Datenbank zu laden

    def get_all_illnessBegins(self):
        with IllnessBeginMapper() as mapper:
            return mapper.find_all()

        # Methode um ein IllnessBeginBO zu updaten
    def save_illnessBegin(self, illnessBegin):
        with IllnessBeginMapper() as mapper:
            mapper.update(illnessBegin)

        # Methode um ein IllnessBeginBO aus der Datenbank zu entfernen
    def delete_illnessBegin(self, illnessBegin):
        with IllnessBeginMapper() as mapper:
            mapper.delete(illnessBegin)

        # Erstellung eines IllnessEndBOs, also das Ende der Krankheit eines Mitarbeiters
    def create_illnessEnd(self, time, event_id):
        illnessEnd = IllnessEndBO()
        illnessEnd.set_time(time)
        illnessEnd.set_event_id(event_id)
        with IllnessEndMapper() as mapper:
            return mapper.insert(illnessEnd)

    # Methode um ein IllnessEndBO mit bestimmter ID aus der Datenbank zu laden
    def get_illnessEnd_by_id(self, number):
        with IllnessEndMapper() as mapper:
            return mapper.find_by_key(number)

    # Methode um alle IllnessEndBOs aus der Datenbank zu laden
    def get_all_illnessEnds(self):
        with IllnessEndMapper() as mapper:
            return mapper.find_all()

    # Methode um ein IllnessEndBO zu updaten
    def save_illnessEnd(self, illnessEnd):
        with IllnessEndMapper() as mapper:
            mapper.update(illnessEnd)

    # Methode um ein IllnessEndBO aus der Datenbank zu entfernen
    def delete_illnessEnd(self, illnessEnd):
        with IllnessEndMapper() as mapper:
            mapper.delete(illnessEnd)

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

    def get_timeinterval_booking_by_id(self, id):
        with TimeIntervalBookingMapper as mapper:
            return mapper.find_by_key(id)

    def get_booking_by_id(self, id):
        with BookingMapper as mapper:
            return mapper.find_by_key(id)

    def get_event_booking_by_id(self, id):
        with EventBookingMapper as mapper:
            return mapper.find_by_key(id)

    # def create_timeinterval_booking(self, userId, worktimeAccountId, timeintervalId, type):
    #     """Ein Timeinterval Booking anlegen"""

    #     '''Als erstes wird das TimeintervalBooking Objekt erstellt und dessen Id wird in der variable timeintervalbookingid gespeichert'''

    #     timeintervalbooking = TimeIntervalBookingBO()
    #     timeintervalbooking.set_id(1)
    #     timeintervalbooking.set_timeinterval_id(timeintervalId)

    #     with TimeIntervalBookingMapper() as mapper:
    #         mapper.insert(timeintervalbooking)
    #         timeintervalbookingid = timeintervalbooking.get_id()

    #     '''Jetzt wird das Booking Objekt gespeichert und die vorher gespeicherte id wird nun als Fremdschlüssel eingefügt'''

    #     booking = BookingBO()
    #     booking.set_user_id(userId)
    #     booking.set_work_time_account_id(worktimeAccountId)
    #     booking.set_type(type)
    #     booking.set_time_interval_booking_id(timeintervalbookingid)
    #     booking.set_id(1)

    #     with BookingMapper() as mapper:
    #         return mapper.insert(booking)

    #     # Hinzufügen der der Delta Zeitrechnung des Zeitintervalls, damit man die overtime und worktime berechnen
    #     # Hinzufügen der TimeintervalId von Hami nach Absprache

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

    def get_vacation_by_timeinterval_booking_id(self, id):
        with VacationMapper() as mapper:
            return mapper.find_by_time_interval_booking(id)

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
