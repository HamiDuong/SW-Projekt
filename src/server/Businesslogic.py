from bo.ComingBO import ComingBO
from db.ComingMapper import ComingMapper
from bo.GoingBO import GoingBO
from db.GoingMapper import GoingMapper
from bo.VacationBeginBO import VacationBeginBO
from db.VacationBeginMapper import VacationBeginMapper
from bo.VacationEndBO import VacationEndBO
from db.VacationEndMapper import VacationEndMapper
from bo.BreakBO import BreakBO
from bo.ProjectDurationBO import ProjectDurationBO
#from bo.ProjectWorkBO import ProjectWorkBO
from bo.VacationBO import VacationBO
from datetime import datetime


class Businesslogic (object):

    def __init__(self):
        pass

    def create_coming(self, time, event_booking_id):
        coming = ComingBO()
        coming.set_time(time)
        coming.set_event_booking_id(event_booking_id)
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


class Businesslogic (object):
    def __init__(self):
        pass


"""
Break Methoden
"""


def get_all_breaks(self):
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


"""
ProjectWork Methoden
"""

"""
Vacation Methoden
"""


def get_all_vacations(self):
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
