from bo.BreakBO import BreakBO
from bo.ProjectDurationBO import ProjectDurationBO
from bo.ProjectWorkBO import ProjectWorkBO
from bo.VacationBO import VacationBO

from db.BreakMapper import BreakMapper
from db.ProjectDurationMapper import ProjectDurationMapper
from db.ProjectWorkMapper import ProjectWorkMapper
from db.VacationMapper import VacationMapper

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
