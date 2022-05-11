from xmlrpc.client import DateTime
from bo.eventBOs.ComingBO import ComingBO
from db.eventMapper.ComingMapper import ComingMapper
from bo.eventBOs.GoingBO import GoingBO
from db.eventMapper.GoingMapper import GoingMapper
from bo.eventBOs.VacationBeginBO import VacationBeginBO
from db.eventMapper.VacationBeginMapper import VacationBeginMapper
from bo.eventBOs.VacationEndBO import VacationEndBO
from db.eventMapper.VacationEndMapper import VacationEndMapper
from bo.BookingBO import BookingBO
from db.BookingMapper import BookingMapper
from bo.EventBookingBO import EventBookingBO
from db.EventBookingMapper import EventBookingMapper
from bo.TimeIntervalBookingBO import TimeIntervalBookingBO
from db.TimeIntervalBookingMapper import TimeIntervalBookingMapper
'''from bo.BreakBO import BreakBO
from bo.ProjectDurationBO import ProjectDurationBO'''
#from bo.ProjectWorkBO import ProjectWorkBO
#from bo.VacationBO import VacationBO
from datetime import datetime


class Businesslogic():

    def __init__(self):
        pass

    def create_coming(self, time, event_id):
        coming = ComingBO()
        coming.set_time(time)
        coming.set_event_id(event_id)
        with ComingMapper() as mapper:
            return mapper.insert(coming)

    def get_coming_by_id(self, number):
        with ComingMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_comings(self):
        with ComingMapper() as mapper:
            return mapper.find_all()

    def save_coming(self, coming):
        with ComingMapper() as mapper:
            mapper.update(coming)

    def delete_coming(self, coming):
        with ComingMapper() as mapper:
            mapper.delete(coming)

    def create_going(self, time, event_booking_id):
        going = GoingBO()
        going.set_time(time)
        going.set_event_booking_id(event_booking_id)
        with GoingMapper() as mapper:
            return mapper.insert(going)

    def get_going_by_id(self, number):
        with GoingMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_goings(self):
        with GoingMapper() as mapper:
            return mapper.find_all()

    def save_going(self, going):
        with GoingMapper() as mapper:
            mapper.update(going)

    def delete_going(self, going):
        with GoingMapper() as mapper:
            mapper.delete(going)

    def create_vacation_begin(self, time, event_booking_id):
        vacation_begin = VacationBeginBO()
        vacation_begin.set_time(time)
        vacation_begin.set_event_booking_id(event_booking_id)
        with VacationBeginMapper() as mapper:
            return mapper.insert(vacation_begin)

    def get_vacation_begin_by_id(self, number):
        with VacationBeginMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_vacation_begins(self):
        with VacationBeginMapper() as mapper:
            return mapper.find_all()

    def save_vacation_begin(self, vacation_begin):
        with VacationBeginMapper() as mapper:
            mapper.update(vacation_begin)

    def delete_vacation_begin(self, vacation_begin):
        with VacationBeginMapper() as mapper:
            mapper.delete(vacation_begin)

    def create_vacation_end(self, time, event_booking_id):
        vacation_end = VacationEndBO()
        vacation_end.set_time(time)
        vacation_end.set_event_booking_id(event_booking_id)
        with VacationEndMapper() as mapper:
            return mapper.insert(vacation_end)

    def get_vacation_end_by_id(self, number):
        with VacationEndMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_vacation_ends(self):
        with VacationEndMapper() as mapper:
            return mapper.find_all()

    def save_vacation_end(self, vacation_end):
        with VacationEndMapper() as mapper:
            mapper.update(vacation_end)

    def delete_vacation_end(self, vacation_end):
        with VacationEndMapper() as mapper:
            mapper.delete(vacation_end)

    """
    Booking Methoden
    """

    def create_timeinterval_booking(self, userId, worktimeAccountId, timeintervalId, type):
        """Ein Timeinterval Booking anlegen"""
        # Zunächst wird das Booking erstellt
        booking = BookingBO()
        booking.set_user_id(userId)
        booking.set_work_time_account_id(worktimeAccountId)
        booking.set_type(type)
        booking.set_id(1)

        # Das Booking Objekt wird in die Datenbank eingefügt
        # Die Id des gerade erstellten Objektes wird als "bookingid" gespeichert, das wird später für
        # die Fremdschlüsselbeziehung zu Timeintervalbooking benötigt
        with BookingMapper() as mapper:
            mapper.insert(booking)
            bookingid = booking.get_id()

        # Jetzt wird das Timeintervalbooking Objekt erstellt
        # Die zueben gespeicherte bookingid wird hier gesetzt
        timeintervalbooking = TimeIntervalBookingBO()
        timeintervalbooking.set_id(1)
        # Die Timeintervalid als Fremdschlüssel muss noch mit der Erstellung von Timeintervallen verknüpft werden
        timeintervalbooking.set_timeinterval_id(timeintervalId)
        timeintervalbooking.set_booking_id(bookingid)

        # Das TimeintervalBookingObjekt wird in die Datenbank eingefügt
        with TimeIntervalBookingMapper() as mapper:
            return mapper.insert(timeintervalbooking)

        # Hinzufügen der der Delta Zeitrechnung des Zeitintervalls, damit man die overtime und worktime berechnen
        # Hinzufügen der TimeintervalId von Hami nach Absprache
    def create_event_booking(self, userId, worktimeAccountId, eventId, type):
        """Ein Timeinterval Booking anlegen"""
        # Zunächst wird das Booking erstellt
        booking = BookingBO()
        booking.set_user_id(userId)
        booking.set_work_time_account_id(worktimeAccountId)
        booking.set_type(type)
        booking.set_id(1)

        # Das Booking Objekt wird in die Datenbank eingefügt
        # Die Id des gerade erstellten Objektes wird als "bookingid" gespeichert, das wird später für
        # die Fremdschlüsselbeziehung zu Eventbooking benötigt
        with BookingMapper() as mapper:
            mapper.insert(booking)
            bookingid = booking.get_id()

        # Jetzt wird das Eventbooking Objekt erstellt
        # Die zueben gespeicherte bookingid wird hier gesetzt
        eventbooking = EventBookingBO()
        eventbooking.set_id(1)
        # Die eventid als Fremdschlüssel muss noch mit der Erstellung von Timeintervallen verknüpft werden
        eventbooking.set_event_id(eventId)
        eventbooking.set_booking_id(bookingid)

        # Das EventBookingObjekt wird in die Datenbank eingefügt
        with EventBookingMapper() as mapper:
            return mapper.insert(eventbooking)
        # Hinzufügen der EventId von Khadi nach Absprache

    def get_all_bookings_for_worktime_account(self, account):

        # Zunächst werden alle Timeintervalbookings aus der Tabelle Bookings geholt
        with BookingMapper() as mapper:
            timeintervalbookings = mapper.find_timeinterval_bookings_by_work_time_account_id(
                account)

        # Jetzt werden die Ids der Timeintervallbookings aus der Tabelle Bookingsgeholt
            for timeintervalbooking in timeintervalbookings:
                bookingid = timeintervalbooking.get_id()
        # Die Bookings aus der Tabelle Timeintervallbookings werden mithilfe der Bookingids aus der Tabelle Bookings ausgelesen (Fremdschlüssel)
                with TimeIntervalBookingMapper() as mapper:
                    timeintervalbookingids = mapper.find_by_booking_id(
                        bookingid)
        # Der Fremdschlüssel Timeintervalid wird aus der Tabelle Timeintervalbookings ausgelesen, damit wir ihn in die Tabelle Timeinterval einfügen können
                    for timeintervalid in timeintervalbookingids:
                        timeintervalids = timeintervalid.get_timeinterval_id()
                        print("Timeintervalids", timeintervalids)

                    # Hinzufügen der Timeintervalle nach Absprache mit Hami

                    # with TimeintervalMapper() as mapper:
                    #     mapper.find_by_id()

        # Jetzt werden auch die EventBookings geholt
        with BookingMapper() as mapper:
            eventbookings = mapper.find_event_bookings_by_work_time_account_id(
                account)

        # Jetzt werden die Ids der eventbookings aus der Tabelle Bookings geholt
            for eventbooking in eventbookings:
                bookingid = eventbooking.get_id()
        # Die Bookings aus der Tabelle Eventbookings werden mithilfe der Bookingids aus der Tabelle Bookings ausgelesen (Fremdschlüssel)
                with EventBookingMapper() as mapper:
                    eventbookingids = mapper.find_by_booking_id(bookingid)
        # Der Fremdschlüssel Eventid wird aus der Tabelle Eventbookings ausgelesen, damit wir ihn in die Tabelle Event einfügen können
                    for eventids in eventbookingids:
                        eventids = eventids.get_event_id()
                        print("EventIds", eventids)

                    # Hinzufügen der Events nach Absprache mit Khadi

    def delete_timeinterval_booking(self, bookingid):
        # Die Timeintervallbookings werden aus der Tabelle Timeintervalbookings, mithilfe der BookingId als Fremdschlüssel, gelöscht
        with TimeIntervalBookingMapper() as mapper:
            booking = mapper.find_by_booking_id(bookingid)
        # Hier wird der Fremdschlüssel TimeintervalId geholt, damit wir später die Zeitintervalle aus der Tabelle Timeintervals löschen können
            for timeintervalbooking in booking:
                timeintervalid = timeintervalbooking.get_timeinterval_id()
            mapper.delete(bookingid)
        # Die Bookings werden aus der Tabelle Bookings gelöscht
        with BookingMapper() as mapper:
            mapper.delete(bookingid)
        # Nach Absprache mit Hami auskommentieren
        # with TimeintervalMapper() as mapper:
            # mapper.delete(timeintervalid)

    def delete_event_booking(self, bookingid):
        # Die Eventbookings werden aus der Tabelle Eventbookings, mithilfe der BookingId als Fremdschlüssel, gelöscht
        with EventBookingMapper() as mapper:
            booking = mapper.find_by_booking_id(bookingid)
        # Hier wird der Fremdschlüssel EventId geholt, damit wir später die Events aus der Tabelle Events löschen können
            for eventbooking in booking:
                eventid = eventbooking.get_event_id()
            mapper.delete(bookingid)

        # Die Bookings werden aus der Tabelle Bookings gelöscht
        with BookingMapper() as mapper:
            mapper.delete(bookingid)
        # Nach Absprache mit Khadi auskommentieren
        # with EventMapper() as mapper:
            # mapper.delete(eventid)

    def update_timeinterval_booking(self, booking):
        # Dateoflastchange wird in der Tabelle Timeintervalbookings geändert
        with TimeIntervalBookingMapper() as mapper:
            mapper.update(booking)
    # Dateoflastchange wird in der Tabelle Bookings geändert
        with BookingMapper() as mapper:
            return mapper.update(booking)

    def update_event_booking(self, booking):
        # Dateoflastchange wird in der Tabelle Eventbookings geändert
        with EventBookingMapper() as mapper:
            mapper.update(booking)
    # Dateoflastchange wird in der Tabelle Bookings geändert
        with BookingMapper() as mapper:
            return mapper.update(booking)


"""
Break Methoden
"""

'''def get_all_breaks(self):
    with BreakMapper() as mapper:
        return mapper.find_all()


def get_break_by_id(self, id):
    with BreakMapper() as mapper:
        return mapper.find_by_key(id)


def create_break(self, start, end, time_interval_booking_id):
    break_obj = BreakBO()
    break_obj.set_start(start)
    break_obj.set_end(end)
    break_obj.set_time_interval_booking_id(time_interval_booking_id)
    break_obj.set_id(1)

    with BreakMapper() as mapper:
        return mapper.insert(break_obj)


def save_break(self, break_obj):
    with BreakMapper as mapper:
        mapper.update(break_obj)


def delete_break(self, break_obj):
    with BreakMapper as mapper:
        mapper.delete(break_obj)


def get_break_by_date(self, date):
    with BreakMapper() as mapper:
        return mapper.find_by_date(date)


def get_break_by_time_period(self, startdate, enddate):
    with BreakMapper() as mapper:
        return mapper.find_by_time_period(startdate, enddate)


def get_break_by_timeinterval_booking_id(self, id):
    with BreakMapper() as mapper:
        return mapper.find_by_time_interval_booking(id)


"""
ProjectDuration Methoden
"""


def get_all_project_durations(self):
    with ProjectDurationMapper() as mapper:
        return mapper.find_all()


def get_project_duration_by_id(self, id):
    with ProjectDurationMapper() as mapper:
        return mapper.find_by_key(id)


def create_project_duration(self, start, end, time_interval_booking_id, project_id):
    project_duration_obj = ProjectDurationBO()
    project_duration_obj.set_start(start)
    project_duration_obj.set_end(end)
    project_duration_obj.set_time_interval_booking_id(time_interval_booking_id)
    project_duration_obj.set_project_id(project_id)
    project_duration_obj.set_id(1)

    with ProjectDurationMapper() as mapper:
        return mapper.insert(project_duration_obj)


def save_project_duration(self, project_duration_obj):
    with ProjectDurationMapper as mapper:
        mapper.update(project_duration_obj)


def delete_project_duration(self, project_duration_obj):
    with ProjectDurationMapper as mapper:
        mapper.delete(project_duration_obj)


def get_project_duration_by_date(self, date):
    with ProjectDurationMapper() as mapper:
        return mapper.find_by_date(date)


def get_project_duration_by_time_period(self, startdate, enddate):
    with ProjectDurationMapper() as mapper:
        return mapper.find_by_time_period(startdate, enddate)


def get_project_duration_by_time_interval_booking_id(self, id):
    with ProjectDurationMapper() as mapper:
        return mapper.find_by_time_interval_booking_id(id)


def get_project_duration_by_project_id(self, id):
    with ProjectDurationMapper() as mapper:
        return mapper.find_by_project_id(id)

'''
"""
ProjectWork Methoden
"""

"""
Vacation Methoden
"""


'''def get_all_vacations(self):
    with VacationMapper() as mapper:
        return mapper.find_all()


def get_vacation_by_id(self, id):
    with VacationMapper() as mapper:
        return mapper.find_by_key(id)


def create_vacation(self, start, end, time_interval_booking_id):
    vacation_obj = VacationBO()
    vacation_obj.set_start(start)
    vacation_obj.set_end(end)
    vacation_obj.set_time_interval_booking_id(time_interval_booking_id)
    vacation_obj.set_id(1)

    with VacationMapper() as mapper:
        return mapper.insert(vacation_obj)


def save_vacation(self, break_obj):
    with VacationMapper as mapper:
        mapper.update(break_obj)


def delete_vacation(self, break_obj):
    with VacationMapper as mapper:
        mapper.delete(break_obj)


def get_vacation_by_date(self, date):
    with VacationMapper() as mapper:
        return mapper.find_by_date(date)


def get_vacation_by_time_period(self, startdate, enddate):
    with VacationMapper() as mapper:
        return mapper.find_by_time_period(startdate, enddate)


def get_vacation_by_timeinterval_booking_id(self, id):
    with VacationMapper() as mapper:
        return mapper.find_by_time_interval_booking(id)
'''
