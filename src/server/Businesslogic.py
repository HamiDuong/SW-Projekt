from bo.ComingBO import ComingBO
from db.ComingMapper import ComingMapper
from bo.GoingBO import GoingBO
from db.GoingMapper import GoingMapper
from bo.VacationBeginBO import VacationBeginBO
from db.VacationBeginMapper import VacationBeginMapper
from bo.VacationEndBO import VacationEndBO
from db.VacationEndMapper import VacationEndMapper
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
