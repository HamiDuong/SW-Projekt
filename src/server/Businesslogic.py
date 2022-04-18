from bo.ComingBO import ComingBO
from db.ComingMapper import ComingMapper
from bo.GoingBO import GoingBO
from db.ComingMapper import ComingMapper
from db.GoingMapper import GoingMapper
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

    def get_all_comings(self):
        with GoingMapper() as mapper:
            return mapper.find_all()

    def save_coming(self, going):
        with GoingMapper() as mapper:
            mapper.update(going)

    def delete_coming(self, going):
        with GoingMapper() as mapper:
            mapper.delete(going)