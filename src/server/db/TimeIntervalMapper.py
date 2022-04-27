from abc import abstractmethod
from server.db import Mapper

"""
Mapper für TimeIntervalBO - Schnittstelle zur Datenbank
Dient als Superklasse für BreakMapper, ProjectDurationMapper, ProjectWorkMapper, Vacation
"""
class TimeIntervalMapper(Mapper):

    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def find_by_date(self, date):
        pass

    @abstractmethod
    def find_by_time_period(self, start_date, end_date):
        pass

    @abstractmethod
    def find_by_time_intervall_booking_id(self, bookingId):
        pass